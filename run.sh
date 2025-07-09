#!/bin/bash

# Run generate.py with GPT-4o model
echo "Running generate.py with GPT-4o model..."
OPENAI_API_KEY=$(cat ~/.openai/key) \
./generate.py conversation_samples.yaml gpt-4o --output golden.jsonl


# Run generate.py with Llama-4-Maverick model
echo "Running generate.py with Llama-4-Maverick model..."
OPENAI_API_KEY=$(cat ~/.llama/api/key) \
BASE_URL=https://api.llama.com/compat/v1 \
./generate.py conversation_samples.yaml Llama-4-Maverick-17B-128E-Instruct-FP8 --output maverick.jsonl

# Run score.py with the two output files
echo "Running score.py with the generated files..."
./score.py golden.jsonl maverick.jsonl

echo "All tasks completed!"
