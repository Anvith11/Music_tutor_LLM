# Setup Guide - OpenAI Music Tutor

This guide will help you set up the OpenAI Music Tutor with comprehensive four-pillar knowledge integration.

## Prerequisites

### 1. OpenAI API Key
- Visit [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- Create an account or sign in
- Generate a new API key
- Keep this key secure - you'll need it for setup

### 2. Python Environment
- **Python 3.7+** (recommended: Python 3.8 or later)
- **pip** package manager
- **Internet connection** for API calls

### 3. System Requirements
- **Memory**: 100MB+ available RAM
- **Storage**: 50MB for knowledge files
- **Audio**: Optional, for TTS features

## Installation

### Option 1: Quick Setup (Recommended)

1. **Clone or download the repository**
2. **Run the setup script**:
   ```bash
   chmod +x run_openai_tutor.sh
   ./run_openai_tutor.sh --help
   ```

The script will automatically:
- Check Python installation
- Install required packages
- Verify setup
- Launch the tutor

### Option 2: Manual Setup

1. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Verify installation**:
   ```bash
   python test_openai_setup.py
   ```

3. **Set up API key** (see Configuration section below)

## Configuration

### Environment Variable (Recommended)

Set your OpenAI API key as an environment variable:

**macOS/Linux:**
```bash
export OPENAI_API_KEY="your-api-key-here"
echo 'export OPENAI_API_KEY="your-api-key-here"' >> ~/.bashrc
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your-api-key-here"
[Environment]::SetEnvironmentVariable("OPENAI_API_KEY", "your-api-key-here", "User")
```

### Alternative: Command Line

Pass the API key directly when running:
```bash
python openai_music_tutor.py --api-key "your-api-key-here" --interactive
```

## Verification

### Test Basic Setup

```bash
python test_openai_setup.py
```

This will check:
- ✅ Python dependencies
- ✅ OpenAI API connection
- ✅ Knowledge system files
- ✅ Optional TTS capabilities

### Test Interactive Mode

```bash
python openai_music_tutor.py --interactive
```

Try asking: "What is a C major chord?"

### Expected Output

```
🎵 INTERACTIVE MUSIC TUTOR SESSION 🎵
============================================
Ask me about music theory, Nashville numbers, instruments, production, or performance!
Type 'quit', 'exit', or 'bye' to end the session.
============================================

🎵 You: What is a C major chord?

🤖 Tutor: A C major chord consists of three notes:
- C (root)
- E (major third)
- G (perfect fifth)

In Nashville numbers, this would be the "1" chord in the key of C major.
```

## Advanced Configuration

### Model Selection

Choose different OpenAI models:

```bash
# Use GPT-3.5-turbo (default, faster, cheaper)
python openai_music_tutor.py --model "gpt-3.5-turbo"

# Use GPT-4 (more intelligent, slower, more expensive)
python openai_music_tutor.py --model "gpt-4"

# Use GPT-4-turbo (balance of speed and intelligence)
python openai_music_tutor.py --model "gpt-4-turbo-preview"
```

### Response Customization

```bash
# Concise responses
python openai_music_tutor.py --concise

# Higher creativity
python openai_music_tutor.py --temperature 0.9

# More deterministic responses
python openai_music_tutor.py --temperature 0.3

# Longer responses
python openai_music_tutor.py --max-tokens 1200
```

### Text-to-Speech Setup

Enable voice responses:

```bash
# Install TTS dependencies
pip install pyttsx3

# Enable TTS
python openai_music_tutor.py --enable-tts --interactive

# Save audio files
python openai_music_tutor.py --enable-tts --save-audio
```

## Knowledge System Setup

The tutor includes four integrated knowledge systems:

### 1. Nashville Numbers (Built-in)
Always available - no additional setup required.

### 2. Slakh Dataset (Optional)
Professional instrument knowledge:
- File: `slakh_instrument_data.py`
- Status: Automatically loaded if present

### 3. Music Theory (Optional)
Comprehensive theory curriculum:
- File: `music_theory_dataset.json`
- Status: Automatically loaded if present

### 4. Professional Performance (Optional)
Advanced performance techniques:
- File: `four_pillar_training_data.json`
- Status: Automatically loaded if present

## Troubleshooting

### Common Issues

#### 1. API Key Errors

**Error**: `ValueError: OpenAI API key required`

**Solution**:
```bash
export OPENAI_API_KEY="sk-your-actual-key-here"
```

#### 2. Import Errors

**Error**: `ModuleNotFoundError: No module named 'openai'`

**Solution**:
```bash
pip install --upgrade openai
```

#### 3. Connection Errors

**Error**: `OpenAI API Connection - Failed`

**Solutions**:
- Check internet connection
- Verify API key is correct
- Check OpenAI service status
- Ensure you have API credits

#### 4. TTS Errors

**Error**: TTS not working

**Solutions**:
```bash
# Install TTS package
pip install pyttsx3

# On macOS, may need additional permissions
# System Preferences > Security & Privacy > Privacy > Accessibility
```

### Diagnostic Commands

```bash
# Test full setup
python test_openai_setup.py

# Test specific model
python openai_music_tutor.py --model "gpt-3.5-turbo" --prompt "test"

# Debug mode with verbose output
python openai_music_tutor.py --prompt "test" --no-stream
```

## Performance Optimization

### API Usage Optimization

```bash
# Use streaming for better perceived performance
python openai_music_tutor.py --interactive  # (streaming enabled by default)

# Disable streaming for batch processing
python openai_music_tutor.py --no-stream --prompt "your question"

# Limit conversation context to reduce costs
python openai_music_tutor.py --context-limit 4
```

### Cost Management

- **Model Choice**: GPT-3.5-turbo is ~10x cheaper than GPT-4
- **Token Limits**: Use `--max-tokens` to control response length
- **Context Management**: Use `--single-mode` for independent questions
- **Concise Mode**: Use `--concise` for shorter responses

## Integration Examples

### Bash Script Integration

```bash
#!/bin/bash
# ask_music_question.sh

question="$1"
if [ -z "$question" ]; then
    echo "Usage: $0 'your music question'"
    exit 1
fi

python openai_music_tutor.py --prompt "$question" --concise --no-stream
```

### Python Script Integration

```python
#!/usr/bin/env python3
import subprocess
import sys

def ask_music_question(question):
    result = subprocess.run([
        'python', 'openai_music_tutor.py',
        '--prompt', question,
        '--no-stream'
    ], capture_output=True, text=True)
    
    return result.stdout

# Example usage
answer = ask_music_question("What is a ii-V-I progression?")
print(answer)
```

## Next Steps

1. **Run the test**: `python test_openai_setup.py`
2. **Try interactive mode**: `python openai_music_tutor.py --interactive`
3. **Explore the four-pillar knowledge system**
4. **Customize settings for your needs**
5. **Start learning music!**

## Support

If you encounter issues:

1. Run `python test_openai_setup.py` for diagnostics
2. Check the troubleshooting section above
3. Verify your OpenAI API key and credits
4. Ensure you have the latest version of the code

---

🎵 **You're ready to start your musical journey with AI assistance!** 