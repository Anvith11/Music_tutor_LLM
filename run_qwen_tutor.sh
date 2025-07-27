#!/bin/bash

# Qwen2-Audio Music Tutor Shell Script
# This script provides a convenient way to run the Qwen2-Audio music tutor

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if requirements are installed
if ! python3 -c "import torch, transformers, librosa" &> /dev/null; then
    echo "📦 Installing dependencies..."
    echo "This may take a while as it includes PyTorch and other large packages..."
    pip install -r requirements.txt
fi

# Check if CUDA is available (optional but recommended)
if python3 -c "import torch; exit(0 if torch.cuda.is_available() else 1)" &> /dev/null; then
    echo "✅ CUDA GPU detected - optimal performance"
else
    echo "⚠️  No CUDA GPU detected - will use CPU (slower)"
fi

# Run the Qwen2-Audio music tutor with all provided arguments
echo "🎵 Starting Qwen2-Audio Music Tutor..."
python3 qwen_music_tutor.py "$@" 