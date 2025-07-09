#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.8"
# dependencies = [
#   "argparse",
#   "rich"
# ]
# ///

import json
import sys
import argparse
from typing import Dict, List, Any, Tuple
from rich.console import Console
from rich.table import Table

def load_conversation_logs(filename: str) -> Dict[Tuple[int, int], List[Dict[str, Any]]]:
    """
    Load conversation logs from a JSONL file.

    Args:
        filename: Path to the JSONL file

    Returns:
        Dictionary mapping (sample_id, turn_id) tuples to tool_calls lists
    """
    logs = {}

    with open(filename, 'r') as f:
        for line_num, line in enumerate(f, 1):
            try:
                data = json.loads(line.strip())
                sample_id = data.get('sample_id')
                turn_id = data.get('turn_id')
                tool_calls = data.get('tool_calls', [])

                if sample_id is not None and turn_id is not None:
                    logs[(sample_id, turn_id)] = tool_calls
                else:
                    print(f"Warning: Line {line_num} missing sample_id or turn_id")

            except json.JSONDecodeError as e:
                print(f"Error parsing JSON on line {line_num}: {e}")
                continue

    return logs

def normalize_tool_calls(tool_calls: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    Normalize tool calls for comparison by sorting and removing call_id.

    Args:
        tool_calls: List of tool call dictionaries

    Returns:
        Normalized list of tool calls
    """
    normalized = []

    for tool_call in tool_calls:
        # Create a copy without call_id for comparison
        normalized_call = {
            'name': tool_call.get('name'),
            'arguments': tool_call.get('arguments')
        }
        normalized.append(normalized_call)

    # Sort by name and arguments for consistent comparison
    return sorted(normalized, key=lambda x: (x['name'], x['arguments']))

def compare_tool_calls(file1_logs: Dict[Tuple[int, int], List[Dict[str, Any]]],
                      file2_logs: Dict[Tuple[int, int], List[Dict[str, Any]]]) -> Dict[str, Any]:
    """
    Compare tool calls between two conversation log files.

    Args:
        file1_logs: Tool calls from first file
        file2_logs: Tool calls from second file

    Returns:
        Dictionary with comparison results
    """
    all_keys = set(file1_logs.keys()) | set(file2_logs.keys())

    results = {
        'total_comparisons': 0,
        'matching': 0,
        'different': 0,
        'missing_in_file1': 0,
        'missing_in_file2': 0,
        'file1_has_tools_file2_empty': 0,
        'file2_has_tools_file1_empty': 0,
        'differences': []
    }

    for sample_id, turn_id in sorted(all_keys):
        tool_calls1 = file1_logs.get((sample_id, turn_id), [])
        tool_calls2 = file2_logs.get((sample_id, turn_id), [])

        results['total_comparisons'] += 1

        # Check if entry exists in both files
        exists_in_file1 = (sample_id, turn_id) in file1_logs
        exists_in_file2 = (sample_id, turn_id) in file2_logs

        if not exists_in_file1:
            results['missing_in_file1'] += 1
            results['differences'].append({
                'sample_id': sample_id,
                'turn_id': turn_id,
                'status': 'missing1',
                'file1_tool_calls': [],
                'file2_tool_calls': tool_calls2
            })
        elif not exists_in_file2:
            results['missing_in_file2'] += 1
            results['differences'].append({
                'sample_id': sample_id,
                'turn_id': turn_id,
                'status': 'missing2',
                'file1_tool_calls': tool_calls1,
                'file2_tool_calls': []
            })
        else:
            # Both entries exist, compare tool calls
            has_tools1 = len(tool_calls1) > 0
            has_tools2 = len(tool_calls2) > 0

            # Check for cases where one has tools and the other is empty
            if has_tools1 and not has_tools2:
                results['file1_has_tools_file2_empty'] += 1
                results['differences'].append({
                    'sample_id': sample_id,
                    'turn_id': turn_id,
                    'status': 'file1_only',
                    'file1_tool_calls': tool_calls1,
                    'file2_tool_calls': tool_calls2
                })
            elif has_tools2 and not has_tools1:
                results['file2_has_tools_file1_empty'] += 1
                results['differences'].append({
                    'sample_id': sample_id,
                    'turn_id': turn_id,
                    'status': 'file2_only',
                    'file1_tool_calls': tool_calls1,
                    'file2_tool_calls': tool_calls2
                })
            else:
                # Both have tools or both are empty, compare normally
                normalized1 = normalize_tool_calls(tool_calls1)
                normalized2 = normalize_tool_calls(tool_calls2)

                if normalized1 == normalized2:
                    results['matching'] += 1
                    results['differences'].append({
                        'sample_id': sample_id,
                        'turn_id': turn_id,
                        'status': 'match',
                        'file1_tool_calls': tool_calls1,
                        'file2_tool_calls': tool_calls2
                    })
                else:
                    results['different'] += 1
                    results['differences'].append({
                        'sample_id': sample_id,
                        'turn_id': turn_id,
                        'status': 'diff',
                        'file1_tool_calls': tool_calls1,
                        'file2_tool_calls': tool_calls2,
                        'normalized1': normalized1,
                        'normalized2': normalized2
                    })

    return results

def print_comparison_results(results: Dict[str, Any], file1_name: str, file2_name: str):
    """
    Print formatted comparison results in a side-by-side table format.

    Args:
        results: Comparison results dictionary
        file1_name: Name of first file
        file2_name: Name of second file
    """
    console = Console()

    print(f"\n=== Tool Calls Comparison: {file1_name} vs {file2_name} ===\n")

    print(f"Total comparisons: {results['total_comparisons']}")
    print(f"Matching tool calls: {results['matching']}")
    print(f"Different tool calls: {results['different']}")
    print(f"Missing in {file1_name}: {results['missing_in_file1']}")
    print(f"Missing in {file2_name}: {results['missing_in_file2']}")
    print(f"{file1_name} has tools, {file2_name} empty: {results['file1_has_tools_file2_empty']}")
    print(f"{file2_name} has tools, {file1_name} empty: {results['file2_has_tools_file1_empty']}")

    if results['differences']:
        print(f"\n=== Detailed Comparison Table ===\n")

        # Create rich table
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("Sample", style="cyan", width=8)
        table.add_column("Turn", style="cyan", width=6)
        table.add_column("Status", style="yellow", width=12)
        table.add_column(file1_name, style="green", width=40)
        table.add_column(file2_name, style="blue", width=40)

        for diff in results['differences']:
            sample_id = diff['sample_id']
            turn_id = diff['turn_id']
            status = diff['status']
            file1_tools = format_tool_calls(diff['file1_tool_calls'])
            file2_tools = format_tool_calls(diff['file2_tool_calls'])

            table.add_row(str(sample_id), str(turn_id), status, file1_tools, file2_tools)

        console.print(table)

        print(f"\nLegend:")
        print(f"  match: Tool calls are identical")
        print(f"  diff: Tool calls differ in content")
        print(f"  missing1: Entry only exists in {file2_name}")
        print(f"  missing2: Entry only exists in {file1_name}")
        print(f"  file1_only: {file1_name} has tool calls, {file2_name} is empty")
        print(f"  file2_only: {file2_name} has tool calls, {file1_name} is empty")

def format_tool_calls(tool_calls: List[Dict[str, Any]]) -> str:
    """
    Format tool calls for display in a readable way.

    Args:
        tool_calls: List of tool call dictionaries

    Returns:
        Formatted string representation
    """
    if not tool_calls:
        return "[]"

    formatted = []
    for tool_call in tool_calls:
        name = tool_call.get('name', 'unknown')
        args = tool_call.get('arguments', '{}')

        # Try to parse arguments for better display
        try:
            import json
            parsed_args = json.loads(args)
            # Show key arguments
            if isinstance(parsed_args, dict):
                key_args = []
                for key, value in parsed_args.items():
                    if key in ['location', 'amount', 'from_currency', 'to_currency', 'value', 'from_unit', 'to_unit']:
                        key_args.append(f"{key}={value}")
                if key_args:
                    args_display = f"({', '.join(key_args)})"
                else:
                    args_display = f"({args})"
            else:
                args_display = f"({args})"
        except:
            args_display = f"({args})"

        formatted.append(f"{name}{args_display}")

    return ", ".join(formatted)

def main():
    parser = argparse.ArgumentParser(description='Compare tool calls between two conversation log files')
    parser.add_argument('file1', help='First conversation log file')
    parser.add_argument('file2', help='Second conversation log file')

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()

    # Load both files
    print(f"Loading {args.file1}...")
    file1_logs = load_conversation_logs(args.file1)
    print(f"Loaded {len(file1_logs)} entries from {args.file1}")

    print(f"Loading {args.file2}...")
    file2_logs = load_conversation_logs(args.file2)
    print(f"Loaded {len(file2_logs)} entries from {args.file2}")

    # Compare tool calls
    results = compare_tool_calls(file1_logs, file2_logs)

    # Print results
    print_comparison_results(results, args.file1, args.file2)

if __name__ == "__main__":
    main()