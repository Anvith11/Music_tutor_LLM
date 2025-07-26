#!/bin/bash

# TinyLlama Music Instructor Training Script
# This script sets up the environment and starts the fine-tuning process

set -e  # Exit on any error

echo "🎵 Starting TinyLlama Music Instructor Fine-tuning..."

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed or not in PATH"
    exit 1
fi

# Check if we're in a virtual environment
if [[ -z "${VIRTUAL_ENV}" ]]; then
    echo "⚠️  Warning: Not in a virtual environment. It's recommended to use a virtual environment."
    read -p "Do you want to continue anyway? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Exiting. Please create and activate a virtual environment first."
        exit 1
    fi
fi

# Install dependencies if needed
echo "📦 Checking dependencies..."
if ! python3 -c "import torch" &> /dev/null; then
    echo "Installing PyTorch and other dependencies..."
    pip install -r requirements_finetune.txt
    echo "✅ Dependencies installed"
else
    echo "✅ Dependencies already installed"
fi

# Check if CUDA is available
if python3 -c "import torch; print('CUDA available:', torch.cuda.is_available())" | grep -q "True"; then
    echo "🚀 CUDA is available - training will use GPU acceleration"
else
    echo "⚠️  CUDA not available - training will use CPU (this will be slow)"
fi

# Check if dataset exists
if [[ ! -f "music_theory_dataset.json" ]]; then
    echo "❌ Error: music_theory_dataset.json not found"
    echo "Please make sure the dataset file is in the current directory"
    exit 1
fi

# Check available disk space
REQUIRED_SPACE_GB=5
AVAILABLE_SPACE=$(df . | tail -1 | awk '{print $4}')
AVAILABLE_SPACE_GB=$((AVAILABLE_SPACE / 1024 / 1024))

if [[ $AVAILABLE_SPACE_GB -lt $REQUIRED_SPACE_GB ]]; then
    echo "⚠️  Warning: Low disk space. You have ${AVAILABLE_SPACE_GB}GB available, but at least ${REQUIRED_SPACE_GB}GB is recommended."
    read -p "Do you want to continue anyway? (y/n): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "Exiting. Please free up some disk space first."
        exit 1
    fi
fi

# Create output directory
mkdir -p "./tinyllama_music_instructor"
echo "📁 Output directory created: ./tinyllama_music_instructor"

# Check if we want to use wandb
if [[ -n "${WANDB_API_KEY}" ]]; then
    echo "🔍 Weights & Biases API key detected - experiment tracking enabled"
else
    echo "📊 No wandb API key found - training will run without experiment tracking"
    echo "To enable wandb tracking, set WANDB_API_KEY environment variable"
fi

# Start training
echo "🎯 Starting fine-tuning process..."
echo "📝 Training logs will be saved to training.log"
echo "💾 Model checkpoints will be saved to ./tinyllama_music_instructor/"

# Run the training script
python3 finetune_tinyllama.py 2>&1 | tee training_session.log

# Check if training completed successfully
if [[ $? -eq 0 ]]; then
    echo "✅ Training completed successfully!"
    echo "🎵 Your music instructor model is ready!"
    echo "📂 Model saved in: ./tinyllama_music_instructor/"
    echo "📋 Training logs saved in: training.log and training_session.log"
    echo ""
    echo "🚀 Next steps:"
    echo "1. Test your model with: python3 music_instructor_inference.py"
    echo "2. Update the tinyllama_runner.py to use your fine-tuned model"
else
    echo "❌ Training failed. Check the logs for details."
    echo "📋 Check training.log and training_session.log for error details"
    exit 1
fi 