# Scratch Evals

## Generate

```
chmod +x generate.py
```

Usage:
```
./generate.py [-h] [--mode {responses,chat_tools,system_prompt}] conversations_file model

Run conversation evaluations with different API modes

positional arguments:
  conversations_file    YAML file containing conversation samples
  model                 Model name to use for evaluation

options:
  -h, --help            show this help message and exit
  --mode {responses,chat_tools,system_prompt}
                        API mode to use (default: chat_tools)```
```

Run on OpenAI
```
OPENAI_API_KEY=`cat ~/.openai/key` \
./generate.py conversation_samples.yaml gpt-4o
```

Run on Llama API:
```
OPENAI_API_KEY=`cat ~/.llama/api/key` \
BASE_URL=https://api.llama.com/compat/v1 \
./generate.py conversation_samples.yaml Llama-4-Maverick-17B-128E-Instruct-FP8
```

Run on Llama Stack:

```bash
# run ollama in one terminal
ollama run llama3.2 --keepalive 60m

# run llama stack in another terminal
INFERENCE_MODEL=llama3.2 llama stack build --template ollama --run

# run generate in third terminal
OPENAI_API_KEY=`cat ~/.openai/key` \
BASE_URL=http://localhost:8321/v1/openai/v1 \
./generate.py conversation_samples.yaml llama3.2
```

## Score

```
chmod +x score.py
```

Usage:
```
./score.py [-h] file1 file2

Compare tool calls between two conversation log files

positional arguments:
  file1       First conversation log file
  file2       Second conversation log file

options:
  -h, --help  show this help message and exit```
```

Run it to compare two runs 
```
./score.py conversation_logs_gpt-4o_20250709111847.jsonl conversation_logs_Llama-4-Maverick-17B-128E-Instruct-FP8_20250709111748.jsonl
```


## Make changes

1. Add more functions to [tools_samples.py](tools_samples.py)
2. Add more conversations to [conversation_samples.yaml](conversation_samples.yaml)
3. Run it on openai to generate golden dataset
4. Run on other models and score against
