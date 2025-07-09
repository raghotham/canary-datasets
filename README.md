# evals

```
chmod +x generate.py
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

```
OPENAI_API_KEY=`cat ~/.openai/key` \
./generate.py conversation_samples.yaml gpt-4o
```

# Make changes

1. Add more functions to [tools_samples.py](tools_samples.py)
2. Add more conversations to [conversation_samples.yaml](conversation_samples.yaml)
3. Run it on openai. Manually verify. 
4. Run it on llama api
