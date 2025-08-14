#!/usr/bin/env -S uv run --script
#
# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "openai>=1.0.0",
#   "rich",
#   "pyyaml"
# ]
# ///

import datetime
import inspect
import json
import os
import sys
import yaml
import argparse
from rich.pretty import pprint
from typing import (
    Any,
    Boolean,
    Dict,
    List,
    Literal,
    Type,
    Union,
    get_args,
    get_type_hints,
)
import openai
import copy

# Import sample tools and create executor
import sample_tools


class ToolExecutor:
    """Executes tool calls by mapping function names to registered functions."""

    def __init__(self, *functions):
        self._registered_tools = {}
        for func in functions:
            self.register(func.__name__, func)

    def register(self, name: str, func: callable):
        """Register a function with a name.

        Args:
            name: Name to register the function under
            func: The function to register
        """
        self._registered_tools[name] = func

    def create_filtered_executor(self, tool_names: List[str]) -> "ToolExecutor":
        """Create a new executor with only the specified tools.

        Args:
            tool_names: List of tool names to include

        Returns:
            New ToolExecutor instance with only the specified tools
        """
        filtered_tools = []
        for name in tool_names:
            if name in self._registered_tools:
                filtered_tools.append(self._registered_tools[name])
            else:
                raise ValueError(f"Tool '{name}' not found")

        return ToolExecutor(*filtered_tools)

    def execute(self, tool_calls: List) -> List[Dict]:
        """Execute a list of tool calls and return their responses.

        Args:
            tool_calls: List of tool call objects from responses API or chat completions API

        Returns:
            List of tool response dictionaries with results
        """
        tool_responses = []

        for tool_call in tool_calls:
            # Support both dict and Pydantic object for chat completions
            function_name = getattr(tool_call, "name", None)
            if function_name is None and hasattr(tool_call, "function"):
                function_name = getattr(tool_call.function, "name", None)
            arguments = getattr(tool_call, "arguments", None)
            if arguments is None and hasattr(tool_call, "function"):
                arguments = getattr(tool_call.function, "arguments", None)
            if isinstance(arguments, str):
                try:
                    arguments = json.loads(arguments)
                except Exception:
                    pass
            if function_name in self._registered_tools:
                try:
                    # Convert arguments to expected types
                    converted_args = self._convert_arguments(function_name, arguments)
                    result = self._registered_tools[function_name](**converted_args)
                    tool_responses.append(
                        {
                            "type": "function_call_output",
                            "call_id": getattr(
                                tool_call, "call_id", getattr(tool_call, "id", None)
                            ),
                            "output": json.dumps(result),
                        }
                    )
                except Exception as e:
                    tool_responses.append(
                        {
                            "type": "function_call_output",
                            "call_id": getattr(
                                tool_call, "call_id", getattr(tool_call, "id", None)
                            ),
                            "output": json.dumps(
                                f"Error executing {function_name}: {str(e)}"
                            ),
                        }
                    )
            else:
                tool_responses.append(
                    {
                        "type": "function_call_output",
                        "call_id": getattr(
                            tool_call, "call_id", getattr(tool_call, "id", None)
                        ),
                        "output": json.dumps(f"Unknown function: {function_name}"),
                    }
                )

        return tool_responses

    def get_tool_schemas(self) -> List[Dict[str, Any]]:
        """Generate OpenAI tool schema for the responses API."""
        tool_schemas = []
        for func in self._registered_tools.values():
            tool_schemas.append(self._generate_tool_schema(func, chat_format=False))
        return tool_schemas

    def get_chat_tool_schemas(self) -> List[Dict[str, Any]]:
        """Generate OpenAI tool schema for the chat completions API."""
        tool_schemas = []
        for func in self._registered_tools.values():
            tool_schemas.append(self._generate_tool_schema(func, chat_format=True))
        return tool_schemas

    def get_system_prompt(self, py: Boolean = False) -> str:
        """Generate system prompt with tool definitions in JSON format."""
        system_prompt = """You are a helpful assistant and an expert in function composition. You can answer general questions using your internal knowledge OR invoke functions when necessary. Follow these strict guidelines:

1. FUNCTION CALLS:
- ONLY use functions that are EXPLICITLY listed in the function list below
- If NO functions are listed (empty function list []), respond ONLY with internal knowledge or "I don't have access to [Unavailable service] information"
- If a function is not in the list, respond ONLY with internal knowledge or "I don't have access to [Unavailable service] information"
- If ALL required parameters are present AND the query EXACTLY matches a listed function's purpose: output ONLY the function call(s)
- Use exact format: [{"name":"func_name1","arguments":{"param1":"value1","param2":"value2"}}, {"name":"func_name2","arguments":{...}}]
Examples:
CORRECT: [{"name":"get_weather","arguments":{"location":"Vancouver"}}, {"name":"calculate_route","arguments":{"start":"Boston","end":"New York"}}] <- Only if get_weather and calculate_route are in function list
INCORRECT: {"name":"get_weather","arguments":{"location":"New York"}}
INCORRECT: Let me check the weather: [{"name":"get_weather","arguments":{"location":"New York"}}]
INCORRECT: [{"name":"get_events","arguments":{"location":"Singapore"}}] <- If function not in list

2. RESPONSE RULES:
- For pure function requests matching a listed function: ONLY output the function call(s)
- For knowledge questions: ONLY output text
- For missing parameters: ONLY request the specific missing parameters
- For unavailable services (not in function list): output ONLY with internal knowledge or "I don't have access to [Unavailable service] information". Do NOT execute a function call.
- If the query asks for information beyond what a listed function provides: output ONLY with internal knowledge about your limitations
- NEVER combine text and function calls in the same response
- NEVER suggest alternative functions when the requested service is unavailable
- NEVER create or invent new functions not listed below

3. STRICT BOUNDARIES:
- ONLY use functions from the list below - no exceptions
- NEVER use a function as an alternative to unavailable information
- NEVER call functions not present in the function list
- NEVER add explanatory text to function calls
- NEVER respond with empty brackets
- Use proper JSON syntax for function calls
- Check the function list carefully before responding

4. TOOL RESPONSE HANDLING:
- When receiving tool responses: provide concise, natural language responses
- Don't repeat tool response verbatim
- Don't add supplementary information

Here is a list of functions in JSON format that you can invoke:\n\n"""

        if py:
            system_prompt = """You are a helpful assistant and an expert in function composition. You can answer general questions using your internal knowledge OR invoke functions when necessary. Follow these strict guidelines:

1. FUNCTION CALLS:
- ONLY use functions that are EXPLICITLY listed in the function list below
- If NO functions are listed (empty function list []), respond ONLY with internal knowledge or "I don't have access to [Unavailable service] information"
- If a function is not in the list, respond ONLY with internal knowledge or "I don't have access to [Unavailable service] information"
- If ALL required parameters are present AND the query EXACTLY matches a listed function's purpose: output ONLY the function call(s)
- Use exact format: [{"name":"func_name1","arguments":{"param1":"value1","param2":"value2"}}, {"name":"func_name2","arguments":{...}}]
Examples:
CORRECT: [{"name":"get_weather","arguments":{"location":"Vancouver"}}, {"name":"calculate_route","arguments":{"start":"Boston","end":"New York"}}] <- Only if get_weather and calculate_route are in function list
INCORRECT: {"name":"get_weather","arguments":{"location":"New York"}}
INCORRECT: Let me check the weather: [{"name":"get_weather","arguments":{"location":"New York"}}]
INCORRECT: [{"name":"get_events","arguments":{"location":"Singapore"}}] <- If function not in list

2. RESPONSE RULES:
- For pure function requests matching a listed function: ONLY output the function call(s)
- For knowledge questions: ONLY output text
- For missing parameters: ONLY request the specific missing parameters
- For unavailable services (not in function list): output ONLY with internal knowledge or "I don't have access to [Unavailable service] information". Do NOT execute a function call.
- If the query asks for information beyond what a listed function provides: output ONLY with internal knowledge about your limitations
- NEVER combine text and function calls in the same response
- NEVER suggest alternative functions when the requested service is unavailable
- NEVER create or invent new functions not listed below

3. STRICT BOUNDARIES:
- ONLY use functions from the list below - no exceptions
- NEVER use a function as an alternative to unavailable information
- NEVER call functions not present in the function list
- NEVER add explanatory text to function calls
- NEVER respond with empty brackets
- Use proper JSON syntax for function calls
- Check the function list carefully before responding

4. TOOL RESPONSE HANDLING:
- When receiving tool responses: provide concise, natural language responses
- Don't repeat tool response verbatim
- Don't add supplementary information

Here is a list of functions in JSON format that you can invoke:\n\n"""

        system_prompt += json.dumps(self.get_tool_schemas(), indent=2)
        return system_prompt

    def _generate_tool_schema(self, func, chat_format=False) -> Dict[str, Any]:
        """Generate OpenAI tool schema from a Python function's type hints and docstring."""
        hints = get_type_hints(func)
        sig = inspect.signature(func)
        doc = inspect.getdoc(func)

        # Parse docstring to get parameter descriptions
        param_desc = {}
        if doc:
            for line in doc.split("\n"):
                if ":" in line and "Args:" in doc:
                    param = line.split(":")[0].strip()
                    desc = line.split(":")[1].strip()
                    param_desc[param] = desc

        # Build parameters object
        properties = {}
        required = []

        for param_name, param in sig.parameters.items():
            param_type = hints[param_name]

            # Handle Literal types
            if hasattr(param_type, "__origin__") and param_type.__origin__ is Literal:
                properties[param_name] = {
                    "type": "string",
                    "enum": list(get_args(param_type)),
                    "description": param_desc.get(param_name, ""),
                }
            # Handle basic types
            else:
                type_map = {
                    str: "string",
                    int: "number",
                    float: "number",
                    bool: "boolean",
                }
                properties[param_name] = {
                    "type": type_map.get(param_type, "string"),
                    "description": param_desc.get(param_name, ""),
                }

            # Check if parameter is required
            if param.default == inspect.Parameter.empty:
                required.append(param_name)
            elif param.default is not None:
                properties[param_name]["default"] = param.default

        if chat_format:
            return {
                "type": "function",
                "function": {
                    "name": func.__name__,
                    "description": doc.split("\n")[0] if doc else "",
                    "parameters": {
                        "type": "object",
                        "properties": properties,
                        "required": required,
                    },
                },
            }
        else:
            return {
                "type": "function",
                "name": func.__name__,
                "description": doc.split("\n")[0] if doc else "",
                "parameters": {
                    "type": "object",
                    "properties": properties,
                    "required": required,
                },
            }

    def _convert_arguments(self, function_name: str, arguments: Dict) -> Dict:
        """Convert arguments to the expected types based on function type hints."""
        func = self._registered_tools[function_name]
        type_hints = get_type_hints(func)
        converted_args = {}

        for param_name, value in arguments.items():
            if param_name in type_hints:
                expected_type = type_hints[param_name]
                try:
                    converted_args[param_name] = self._convert_value(
                        value, expected_type
                    )
                except (ValueError, TypeError) as e:
                    raise ValueError(
                        f"Failed to convert parameter '{param_name}' with value '{value}' to type {expected_type}: {e}"
                    )
            else:
                # If no type hint, use the value as-is
                converted_args[param_name] = value

        return converted_args

    def _convert_value(self, value: Any, target_type: Type) -> Any:
        """Convert a value to the target type."""
        # Handle None values
        if value is None:
            return None

        # Handle Union types (e.g., Union[str, int])
        if hasattr(target_type, "__origin__") and target_type.__origin__ is Union:
            # Try each type in the union
            for union_type in get_args(target_type):
                if union_type is type(None):  # Skip NoneType
                    continue
                try:
                    return self._convert_value(value, union_type)
                except (ValueError, TypeError):
                    continue
            raise ValueError(f"Cannot convert '{value}' to any type in {target_type}")

        # Handle Literal types
        if hasattr(target_type, "__origin__") and target_type.__origin__ is Literal:
            if value in get_args(target_type):
                return value
            else:
                raise ValueError(
                    f"Value '{value}' not in allowed values {get_args(target_type)}"
                )

        # Handle basic types
        if target_type is str:
            return str(value)
        elif target_type is int:
            return int(value)
        elif target_type is float:
            return float(value)
        elif target_type is bool:
            if isinstance(value, str):
                return value.lower() in ("true", "1", "yes", "on")
            return bool(value)
        elif target_type is list:
            if isinstance(value, str):
                # Try to parse as JSON if it's a string
                try:
                    return json.loads(value)
                except json.JSONDecodeError:
                    # If not JSON, split by comma
                    return [item.strip() for item in value.split(",")]
            return list(value)
        elif target_type is dict:
            if isinstance(value, str):
                try:
                    return json.loads(value)
                except json.JSONDecodeError:
                    raise ValueError(f"Cannot convert string '{value}' to dict")
            return dict(value)

        # For other types, try to construct them directly
        try:
            return target_type(value)
        except (ValueError, TypeError):
            raise ValueError(f"Cannot convert '{value}' to {target_type}")


def log_turn(
    sample_id,
    turn_id,
    user_message,
    tool_calls,
    tool_outputs,
    assistant_message,
    messages=[],
    model_name=None,
    log_filename=None,
):
    """Log a complete turn with all its data."""
    # Convert messages to serializable format
    serializable_messages = []
    for msg in messages:
        message_dict = {}
        # Handle both dicts and objects
        if isinstance(msg, dict):
            role = msg.get("role")
            if role is not None:
                message_dict["role"] = role
            content = msg.get("content")
            if content is not None:
                message_dict["content"] = content
            tool_calls_val = msg.get("tool_calls")
            if tool_calls_val:
                message_dict["tool_calls"] = [
                    tc.model_dump() if hasattr(tc, "model_dump") else tc
                    for tc in tool_calls_val
                ]
            tool_call_id = msg.get("tool_call_id")
            if tool_call_id is not None:
                message_dict["tool_call_id"] = tool_call_id
        else:
            role = getattr(msg, "role", None)
            if role is not None:
                message_dict["role"] = role
            content = getattr(msg, "content", None)
            if content is not None:
                message_dict["content"] = content
            tool_calls_val = getattr(msg, "tool_calls", None)
            if tool_calls_val:
                message_dict["tool_calls"] = [
                    tc.model_dump() if hasattr(tc, "model_dump") else tc
                    for tc in tool_calls_val
                ]
            tool_call_id = getattr(msg, "tool_call_id", None)
            if tool_call_id is not None:
                message_dict["tool_call_id"] = tool_call_id
        if message_dict:  # Only append if we have any non-null fields
            serializable_messages.append(message_dict)
    # Create turn entry
    turn_entry = {
        "sample_id": sample_id,
        "turn_id": turn_id,
        "messages": serializable_messages,
        "user_message": user_message,
        "tool_calls": tool_calls,
        "tool_outputs": tool_outputs,
        "assistant_message": assistant_message,
    }

    try:
        with open(log_filename, "a") as f:
            f.write(json.dumps(turn_entry) + "\n")
    except Exception as e:
        print(f"Error writing to log file {log_filename}: {e}")
        sys.exit(1)


def execute_response_turn(
    client, model, executor, previous_id, user_message, sample_id, turn_id
):
    inputs = [
        {
            "type": "message",
            "role": "user",
            "content": [{"type": "input_text", "text": user_message}],
        }
    ]

    all_tool_calls = []
    all_tool_outputs = []

    while True:
        # Only include previous_response_id if it's not None
        request_params = {
            "model": model,
            "input": inputs,
            "tools": executor.get_tool_schemas(),
            "stream": False,
        }
        if previous_id is not None:
            request_params["previous_response_id"] = previous_id

        resp = client.responses.create(**request_params)
        # pprint(resp)

        # If model gives text, output and finish
        if all(item.type != "function_call" for item in resp.output):
            # Handle different output types
            for item in resp.output:
                if hasattr(item, "content"):  # Regular message
                    content_blocks = item.content
                    text = next(
                        block.text
                        for block in content_blocks
                        if block.type == "output_text"
                    )
                    return text, resp.id, all_tool_calls, all_tool_outputs
                elif hasattr(item, "text"):  # Reasoning item
                    return item.text, resp.id, all_tool_calls, all_tool_outputs
                elif hasattr(item, "output_text"):  # Direct text output
                    return item.output_text, resp.id, all_tool_calls, all_tool_outputs

            # Fallback: try to get any text from the response
            for item in resp.output:
                if hasattr(item, "text"):
                    return item.text, resp.id, all_tool_calls, all_tool_outputs

            return "No text response found", resp.id, all_tool_calls, all_tool_outputs

        # Otherwise run tools, feed outputs back
        tool_calls = [item for item in resp.output if item.type == "function_call"]
        for tool_call in tool_calls:
            all_tool_calls.append(
                {
                    "call_id": tool_call.call_id,
                    "name": tool_call.name,
                    "arguments": tool_call.arguments,
                }
            )
        tool_outputs = executor.execute(tool_calls)
        for tool_output in tool_outputs:
            all_tool_outputs.append(
                {"call_id": tool_output["call_id"], "output": tool_output["output"]}
            )
            # Add tool output as a message to inputs
            inputs.append(
                {
                    "type": "message",
                    "role": "tool",
                    "tool_call_id": tool_output["call_id"],
                    "content": [
                        {"type": "output_text", "text": str(tool_output["output"])}
                    ],
                }
            )
        previous_id = resp.id


def assistant_response_conversation(
    client, model, executor, user_messages, sample_id, log_filename
):
    previous_id = None
    messages = []  # Track full conversation history
    for turn_id, user_message in enumerate(user_messages, 1):
        response, previous_id, tool_calls, tool_outputs = execute_response_turn(
            client, model, executor, previous_id, user_message, sample_id, turn_id
        )

        # Add user message
        messages.append({"role": "user", "content": user_message})

        if tool_calls:
            # Add assistant message with tool calls
            messages.append(
                {"role": "assistant", "content": None, "tool_calls": tool_calls}
            )
            # Add tool response messages
            for tool_output in tool_outputs:
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_output["call_id"],
                        "content": str(tool_output["output"]),
                    }
                )

        # Add final assistant response
        messages.append({"role": "assistant", "content": response})

        log_turn(
            sample_id,
            turn_id,
            user_message,
            tool_calls,
            tool_outputs,
            response,
            messages,
            model,
            log_filename,
        )


def execute_chat_turn(
    client, model, executor, messages, user_message, use_system_prompt, debug=False
):
    # Add new user message to conversation
    messages.append({"role": "user", "content": user_message})

    all_tool_calls = []
    all_tool_outputs = []

    while True:
        # Prepare request parameters
        request_params = {"model": model, "messages": messages, "stream": False}

        if use_system_prompt:
            # Add system prompt with tool schemas instead of tools parameter
            system_prompt = executor.get_system_prompt()

            # Add system message at the beginning if not already present
            if not messages or messages[0]["role"] != "system":
                messages.insert(0, {"role": "system", "content": system_prompt})
        else:
            # Use tools parameter as before
            request_params["tools"] = executor.get_chat_tool_schemas()

        # Make chat completion request
        if debug:
            pprint(request_params)
        resp = client.chat.completions.create(**request_params)
        if debug:
            pprint(resp)
        assistant_message = resp.choices[0].message
        messages.append(assistant_message)

        # If no tool calls, return the response
        if not assistant_message.tool_calls:
            return assistant_message.content, messages, all_tool_calls, all_tool_outputs

        # Handle tool calls
        tool_calls = assistant_message.tool_calls
        for tool_call in tool_calls:
            # Check if we need to use the older format for local APIs
            if hasattr(tool_call, "call_id"):
                # Older format
                all_tool_calls.append(
                    {
                        "call_id": tool_call.call_id,
                        "name": tool_call.tool_name,
                        "arguments": tool_call.arguments,
                    }
                )
            else:
                # Standard OpenAI format
                all_tool_calls.append(
                    {
                        "call_id": tool_call.id,
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments,
                    }
                )

        tool_outputs = executor.execute(tool_calls)
        for tool_output in tool_outputs:
            all_tool_outputs.append(
                {"call_id": tool_output["call_id"], "output": tool_output["output"]}
            )
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_output["call_id"],
                    "content": str(tool_output["output"]),
                }
            )


def assistant_chat_conversation(
    client,
    model,
    executor,
    user_messages,
    sample_id,
    use_system_prompt,
    log_filename,
    debug=False,
):
    messages = []  # Track full conversation history
    for turn_id, user_message in enumerate(user_messages, 1):
        response, updated_messages, tool_calls, tool_outputs = execute_chat_turn(
            client, model, executor, messages, user_message, use_system_prompt, debug
        )

        # Update our messages list with the returned messages
        messages = updated_messages

        # Debug: print the messages to see what we have
        print(f"\nDEBUG: Turn {turn_id} has {len(messages)} messages")
        for i, msg in enumerate(messages):
            if hasattr(msg, "model_dump"):
                msg_dict = msg.model_dump()
            else:
                msg_dict = msg
            role = msg_dict.get("role", "unknown")
            if "content" in msg_dict and msg_dict.get("content"):
                print(
                    f"  {i}: {role} - {str(msg_dict.get('content', 'no content'))[:50]}..."
                )
            elif "tool_calls" in msg_dict and msg_dict.get("tool_calls"):
                tool_calls = [
                    fn.get("function", {}) for fn in msg_dict.get("tool_calls", [])
                ]
                tool_calls_str = ",".join(
                    [
                        f"{tc.get('name', 'unknown')}({tc.get('arguments', {})})"
                        for tc in tool_calls
                    ]
                )
                print(f"  {i}: {role} - git {tool_calls_str}")
            else:
                print(f"  {i}: {role} - no content")

        # Convert all messages to dicts for logging (handle Pydantic objects)
        messages_for_log = []
        for msg in messages:
            if hasattr(msg, "model_dump"):
                messages_for_log.append(msg.model_dump())
            else:
                messages_for_log.append(copy.deepcopy(msg))

        # Ensure tool responses are in the messages array for logging
        if tool_outputs:
            tool_response_ids = set()
            for msg in messages_for_log:
                if msg.get("role") == "tool":
                    tool_response_ids.add(msg.get("tool_call_id"))
            for tool_output in tool_outputs:
                if tool_output["call_id"] not in tool_response_ids:
                    messages_for_log.append(
                        {
                            "role": "tool",
                            "tool_call_id": tool_output["call_id"],
                            "content": str(tool_output["output"]),
                        }
                    )

        log_turn(
            sample_id,
            turn_id,
            user_message,
            tool_calls,
            tool_outputs,
            response,
            messages_for_log,
            model,
            log_filename,
        )


def load_conversations_from_yaml(filename):
    """Load conversation samples from YAML file."""
    with open(filename, "r") as f:
        data = yaml.safe_load(f)
    return data["conversations"]


# Get all functions from sample_tools module
tools = [
    obj for name, obj in inspect.getmembers(sample_tools) if inspect.isfunction(obj)
]
executor = ToolExecutor(*tools)

# Set up argument parser
parser = argparse.ArgumentParser(
    description="Run conversation evaluations with different API modes"
)
parser.add_argument(
    "conversations_file", help="YAML file containing conversation samples"
)
parser.add_argument("model", help="Model name to use for evaluation")
parser.add_argument(
    "--mode",
    choices=["responses", "chat_tools", "system_prompt"],
    default="chat_tools",
    help="API mode to use (default: chat_tools)",
)
parser.add_argument(
    "--samples",
    help='Comma-separated list of sample IDs to run (e.g., "1,3,5,6,10"). If not specified, runs all samples.',
)
parser.add_argument(
    "--output",
    help="Output log file name. If not specified, auto-generates with timestamp.",
)
parser.add_argument(
    "--debug",
    action="store_true",
    help="Enable debug mode to print requests and responses",
)

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print(
        "Error: The OPENAI_API_KEY environment variable is not set. Please set it to your OpenAI (or any other endpoint's API key) as shown in the README."
    )
    sys.exit(1)
base_url = os.getenv("BASE_URL", "https://api.openai.com/v1")
try:
    client = openai.OpenAI(api_key=api_key, base_url=base_url)
except Exception as e:
    print(f"Error initializing OpenAI client: {e}")
    sys.exit(1)

conversations_file = args.conversations_file

model = args.model
# Check if the specified model is available
try:
    available_models = [model.id for model in client.models.list()]
    if model not in available_models:
        print(f"Error: Model '{model}' is not available. Available models are:")
        print("\n".join(available_models))
        sys.exit(1)
except Exception as e:
    print(f"Error: Could not verify model availability: {e}")
    sys.exit(1)

use_system_prompt = args.mode == "system_prompt"
debug = args.debug

print(f"Loading conversations from {conversations_file}")
conversations = load_conversations_from_yaml(conversations_file)

# Parse samples argument if provided
selected_samples = set()
if args.samples:
    try:
        selected_samples = {int(x.strip()) for x in args.samples.split(",")}
        print(f"Running only samples: {sorted(selected_samples)}")
    except ValueError as e:
        print(f"Error parsing samples argument: {e}")
        print("Samples should be comma-separated integers (e.g., '1,3,5,6,10')")
        sys.exit(1)

# Determine output filename
if args.output:
    log_filename = args.output
    if not log_filename.endswith(".jsonl"):
        log_filename += ".jsonl"
else:
    # Auto-generate filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    log_filename = f"conversation_logs_{model}_{timestamp}.jsonl"

sample_id = 0
conversations_run = 0
for conversation in conversations:
    sample_id += 1

    # Skip if samples are specified and this sample is not in the list
    if selected_samples and sample_id not in selected_samples:
        continue

    conversations_run += 1
    print(
        f"\n=== Running conversation: {conversation['name']} (sample_id={sample_id}) ===\n"
    )

    # Get tools for this conversation, default to all tools if not specified
    conversation_tools = conversation.get("tools", [])
    if conversation_tools:
        # Create a filtered executor with only the specified tools
        conversation_executor = executor.create_filtered_executor(conversation_tools)
        print(f"Using tools: {conversation_tools}")
    else:
        # Use all available tools
        conversation_executor = executor
        print("Using all available tools")

    if args.mode == "responses":
        assistant_response_conversation(
            client,
            model,
            conversation_executor,
            conversation["messages"],
            sample_id,
            log_filename,
        )
    else:
        assistant_chat_conversation(
            client,
            model,
            conversation_executor,
            conversation["messages"],
            sample_id,
            use_system_prompt,
            log_filename,
            debug,
        )

print(f"Logged {conversations_run} conversations to {log_filename}")
