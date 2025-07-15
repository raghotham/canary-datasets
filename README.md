# Canary Datasets

A tool to create canary datasets with simple yaml-based conversations. Use 'generate' to use OpenAI APIs (responses and chat completions) to generate full conversation logs by writing dialogs and tools in a simple yaml file. The conversation logs capture all tool calls and tool outputs in addition to assistant and user messages. Can compare tool calls made by different models by running 'score'.

## Setup

```bash
chmod +x generate.py score.py
```

## Generate

Generate conversation logs by running models on conversation samples.

### Basic Usage

```bash
# Run all conversations with default settings
OPENAI_API_KEY=`cat ~/.openai/key` \
./generate.py sample_conversations.yaml gpt-4o

# Run with specific mode
OPENAI_API_KEY=`cat ~/.openai/key` \
./generate.py sample_conversations.yaml gpt-4o --mode chat_tools

# Run with custom output file
OPENAI_API_KEY=`cat ~/.openai/key` \
./generate.py sample_conversations.yaml gpt-4o --output my_results.jsonl

# Run specific samples only
OPENAI_API_KEY=`cat ~/.openai/key` \
./generate.py sample_conversations.yaml gpt-4o --samples 1,3,5

# Run with debug mode (shows API requests/responses)
OPENAI_API_KEY=`cat ~/.openai/key` \
./generate.py sample_conversations.yaml gpt-4o --debug

# Combine multiple options
OPENAI_API_KEY=`cat ~/.openai/key` \
./generate.py sample_conversations.yaml gpt-4o --mode chat_tools --samples 1,3,5 --output test_results.jsonl --debug
```

### API Modes

- `chat_tools`: Uses chat completions with tools parameter (default)
- `responses`: Uses OpenAI's responses API
- `system_prompt`: Uses chat completions with tools defined in system prompt (legacy)

### Different Models/Providers

```bash
# OpenAI
OPENAI_API_KEY=`cat ~/.openai/key` \
./generate.py sample_conversations.yaml gpt-4o --output gpt4o.jsonl

# Llama
OPENAI_API_KEY=`cat ~/.llama/api/key` \
BASE_URL=https://api.llama.com/compat/v1 \
./generate.py sample_conversations.yaml Llama-4-Maverick-17B-128E-Instruct-FP8 --output maverick.jsonl

# Local Llama Stack
ollama run llama3.2 --keepalive 60m # terminal 1
uv run --with llama-stack llama stack build --template ollama --run # terminal 2

# terminal 3
OPENAI_API_KEY=`cat ~/.llama/stack/key` \
BASE_URL=http://localhost:8321/v1/openai/v1 \
./generate.py sample_conversations.yaml llama3.2 --output llama32.jsonl

### Arguments

- `conversations_file`: YAML file containing conversation samples
- `model`: Model name to use for evaluation
- `--mode`: API mode to use (default: chat_tools)
- `--samples`: Comma-separated list of sample IDs to run (e.g., "1,3,5,6,10")
- `--output`: Output log file name (auto-adds .jsonl if needed)
- `--debug`: Enable debug mode to print API requests and responses

## Score

Compare tool calls between two conversation log files.

### Basic Usage

```bash
# Compare two log files
./score.py conversation_logs_gpt-4o_20250709111847.jsonl conversation_logs_llama_20250709111748.jsonl

# Compare with custom output files
./score.py gpt4o.jsonl llama32.jsonl

# Compare files in different directories
./score.py generate_samples/gpt4o.jsonl generate_samples/llama32.jsonl
```

### Comparison Types

The script identifies several types of differences:

- **match**: Tool calls are identical
- **diff**: Tool calls differ in content
- **typediff**: Tool calls are the same, but argument types differ (e.g., string vs integer)
- **missing1**: Entry only exists in second file
- **missing2**: Entry only exists in first file
- **file1_only**: First file has tool calls, second file is empty
- **file2_only**: Second file has tool calls, first file is empty

### Output

The script provides:
- Summary statistics (total comparisons, matches, differences, etc.)
- Detailed comparison table showing each sample/turn
- Legend explaining the difference types

## Conversation Samples

Conversations are defined in `sample_conversations.yaml` with:

- `name`: Human-readable description
- `tools`: List of available tools for this conversation
- `messages`: List of user messages (multi-turn conversations)

### Example

```yaml
conversations:
  - name: "Weather queries with unit conversion"
    tools:
      - get_weather
      - convert_units
    messages:
      - "What's the weather in Boston?"
      - "Convert that temperature to Celsius for me"
```

## Tools

Tools are defined in `sample_tools.py`. The system automatically:

- Discovers all functions in the module
- Extracts type hints for argument validation
- Applies type coercion during comparison
- Supports adding new tools without code changes

## Workflow

1. **Add tools**: Define new functions in `sample_tools.py`
2. **Add conversations**: Create new conversation samples in `sample_conversations.yaml`
3. **Generate golden dataset**: Run on a reference model (e.g., GPT-4)
4. **Test other models**: Run on models you want to evaluate
5. **Compare results**: Use `score.py` to compare against the golden dataset

## Examples

```bash
# Generate golden dataset
OPENAI_API_KEY=`cat ~/.openai/key` \
./generate.py sample_conversations.yaml gpt-4o --output golden_dataset.jsonl

# Test a new model with debug mode
OPENAI_API_KEY=`cat ~/.llama/api/key` \
BASE_URL=https://api.llama.com/compat/v1 \
./generate.py sample_conversations.yaml Llama-4-Maverick-17B-128E-Instruct-FP8 --output llama_results.jsonl --debug

# Compare results
./score.py golden_dataset.jsonl llama_results.jsonl

# Run specific samples for quick testing
OPENAI_API_KEY=`cat ~/.openai/key` \
./generate.py sample_conversations.yaml gpt-4o --samples 1,3 --output quick_test.jsonl

# Debug API issues
OPENAI_API_KEY=`cat ~/.llama/stack/key` \
BASE_URL=http://localhost:8321/v1/openai/v1 \
./generate.py sample_conversations.yaml llama3.2:3b --samples 1 --debug
```

## Debug Mode

Use `--debug` to troubleshoot API issues:

- **Shows API requests**: See exactly what's being sent to the model
- **Shows API responses**: See the complete response from the model
- **No turn entry clutter**: Clean output focused on API communication
- **Useful for**: Debugging API format issues, understanding model behavior, troubleshooting tool call problems

## File Structure

```
.
├── generate.py              # Main generation script
├── score.py                 # Comparison script
├── sample_conversations.yaml # Conversation definitions
├── sample_tools.py          # Tool function definitions
├── README.md               # This file
└── generate_samples/       # Output directory (auto-created)
    ├── gpt4o.jsonl
    ├── llama32.jsonl
    └── ...
```
