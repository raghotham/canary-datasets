# evals

```
chmod +x harness.py
```

```
OPENAI_API_KEY=`cat ~/.llama/api/key` \
BASE_URL=https://api.llama.com/compat/v1 \
./harness.py conversation_samples.yaml Llama-4-Maverick-17B-128E-Instruct-FP8
```

```
OPENAI_API_KEY=`cat ~/.openai/key` \
./harness.py conversation_samples.yaml gpt-4o
```
