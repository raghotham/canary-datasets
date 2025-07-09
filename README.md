# Scratch Evals

## Generate

```
chmod +x generate.py
```

Usage:
```
./generate.py [-h] [--mode {responses,chat_tools,system_prompt}] conversations_file model
```

```
OPENAI_API_KEY=`cat ~/.openai/key` \
./generate.py conversation_samples.yaml gpt-4o
```

```
OPENAI_API_KEY=`cat ~/.llama/api/key` \
BASE_URL=https://api.llama.com/compat/v1 \
./generate.py conversation_samples.yaml Llama-4-Maverick-17B-128E-Instruct-FP8
```

## Score

```
chmod +x score.py
```

Usage:
```
./score.py [-h] file1 file2
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
