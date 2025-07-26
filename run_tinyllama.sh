#!/bin/bash

# TinyLLAMA Runner Shell Script
# This script provides a convenient way to run the TinyLLAMA runner

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if requirements are installed
if ! python3 -c "import requests" &> /dev/null; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
fi

# Check if Ollama is running
if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo "❌ Error: Ollama is not running"
    echo "Please start Ollama first by running: ollama serve"
    exit 1
fi

# Run the TinyLLAMA runner with all provided arguments
python3 tinyllama_runner.py "$@" 