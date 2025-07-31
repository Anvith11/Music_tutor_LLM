#!/bin/bash

echo "🎵 OpenAI Music Tutor Setup & Launch Script"
echo "============================================"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7 or later."
    exit 1
fi

echo "✅ Python found: $(python3 --version)"

# Check for required packages
echo "🔍 Checking OpenAI dependencies..."

if ! python3 -c "import openai" 2>/dev/null; then
    echo "❌ OpenAI package not found. Installing..."
    pip install openai>=0.28.0
fi

# Check for optional TTS package
if ! python3 -c "import pyttsx3" 2>/dev/null; then
    echo "⚠️  TTS package (pyttsx3) not found. Installing for voice features..."
    pip install pyttsx3
fi

echo "✅ All dependencies checked!"

# Check for API key
if [ -z "$OPENAI_API_KEY" ]; then
    echo "⚠️  OPENAI_API_KEY environment variable not set."
    echo "   You can:"
    echo "   1. Set it: export OPENAI_API_KEY='your-api-key'"
    echo "   2. Pass it as argument: --api-key 'your-api-key'"
    echo ""
fi

echo "🚀 Launching OpenAI Music Tutor..."
echo ""

# Run the music tutor
python3 openai_music_tutor.py "$@" 