#!/bin/bash

# Run generate.py with GPT-4o model
echo "Running generate.py with GPT-4o model..."
OPENAI_API_KEY=$(cat ~/.openai/key) \
./generate.py conversation_samples.yaml gpt-4o

# Store the output filename for GPT-4o
GPT4O_OUTPUT=$(ls -t conversation_logs_gpt-4o_*.jsonl | head -n 1)
echo "GPT-4o output: $GPT4O_OUTPUT"

# Run generate.py with Llama-4-Maverick model
echo "Running generate.py with Llama-4-Maverick model..."
OPENAI_API_KEY=$(cat ~/.llama/api/key) \
BASE_URL=https://api.llama.com/compat/v1 \
./generate.py conversation_samples.yaml Llama-4-Maverick-17B-128E-Instruct-FP8

# Store the output filename for Llama-4-Maverick
LLAMA_OUTPUT=$(ls -t conversation_logs_Llama-4-Maverick-17B-128E-Instruct-FP8_*.jsonl | head -n 1)
echo "Llama-4-Maverick output: $LLAMA_OUTPUT"

# Run score.py with the two output files
echo "Running score.py with the generated files..."
./score.py "$GPT4O_OUTPUT" "$LLAMA_OUTPUT"

echo "All tasks completed!"
