# Setup Guide

## Prerequisites
- Python 3.8 or higher
- OpenAI API key

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. **Install dependencies:**
   ```bash
   # Basic requirements
   pip install -r requirements.txt
   
   # For fine-tuning functionality
   pip install -r requirements_finetune.txt
   
   # For OpenAI integration
   pip install -r requirements_openai.txt
   
   # For text-to-speech features
   pip install -r requirements_tts.txt
   ```

3. **Set up environment variables:**
   ```bash
   # Create .env file or set environment variable
   export OPENAI_API_KEY="your_openai_api_key_here"
   ```

4. **Quick start:**
   ```bash
   # Interactive mode
   python tinyllama_runner.py --interactive
   
   # Single query
   python tinyllama_runner.py --prompt "Explain the Nashville number system"
   
   # With text-to-speech
   python tinyllama_runner.py --interactive --enable-tts
   ```

## Security Note
Never commit your API keys to the repository. Always use environment variables or `.env` files (which are excluded from git). 