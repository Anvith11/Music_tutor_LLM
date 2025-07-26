# TinyLLAMA Runner

A simple Python interface to run TinyLLAMA locally through Ollama.

## Prerequisites

1. **Install Ollama**: Download and install Ollama from [https://ollama.ai](https://ollama.ai)
2. **Install TinyLLAMA**: Run the following command to download the TinyLLAMA model:
   ```bash
   ollama pull tinyllama
   ```
3. **Start Ollama**: Make sure Ollama is running:
   ```bash
   ollama serve
   ```

## Installation

1. Clone or download this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Interactive Mode (Default)

Run the script without any arguments to start an interactive chat session:

```bash
python tinyllama_runner.py
```

or explicitly:

```bash
python tinyllama_runner.py --interactive
```

### Single Prompt Mode

Send a single prompt and get a response:

```bash
python tinyllama_runner.py --prompt "What is the capital of France?"
```

### Command Line Options

- `--prompt`, `-p`: Single prompt to send to TinyLLAMA
- `--model`, `-m`: Model name (default: tinyllama)
- `--url`, `-u`: Ollama base URL (default: http://localhost:11434)
- `--no-stream`: Disable streaming responses
- `--interactive`, `-i`: Run in interactive mode
- `--temperature`, `-t`: Temperature for response generation (0.0-1.0, default: 0.7)
- `--max-tokens`: Maximum number of tokens to generate (default: 800)
- `--concise`: Force very concise responses to reduce hallucination
- `--single-mode`: Start in single-question mode (no conversation context)
- `--context-limit`: Maximum conversation history length (default: 6)
- `--allow-all-topics`: Allow non-music questions (default: music-only mode)

### Examples

1. **Basic usage**:
   ```bash
   python tinyllama_runner.py
   ```

2. **Single question**:
   ```bash
   python tinyllama_runner.py -p "Explain quantum computing in simple terms"
   ```

3. **Use a different model**:
   ```bash
   python tinyllama_runner.py -m "llama2" -p "Tell me a joke"
   ```

4. **Use custom Ollama URL**:
   ```bash
   python tinyllama_runner.py -u "http://192.168.1.100:11434" -p "Hello"
   ```

5. **Disable streaming**:
   ```bash
   python tinyllama_runner.py --no-stream -p "What is AI?"
   ```

6. **Force concise responses** (to reduce hallucination):
   ```bash
   python tinyllama_runner.py --concise -p "What is the capital of France?"
   ```

7. **Lower temperature for more focused responses**:
   ```bash
   python tinyllama_runner.py -t 0.3 -p "Explain machine learning"
   ```

8. **Shorter responses**:
   ```bash
   python tinyllama_runner.py --max-tokens 200 -p "What is C major scale?"
   ```

9. **Single-question mode** (no context bleeding):
   ```bash
   python tinyllama_runner.py --single-mode -p "What is machine learning?"
   ```

10. **Limited conversation context**:
    ```bash
    python tinyllama_runner.py --context-limit 2 -i
    ```

11. **Allow all topics** (disable music-only mode):
    ```bash
    python tinyllama_runner.py --allow-all-topics -p "What is Python programming?"
    ```

## Interactive Mode Commands

When in interactive mode, you can use these special commands:

- `quit`, `exit`, or `bye`: Exit the program
- `clear`: Clear the conversation history
- `single`: Switch to single-question mode (no context between questions)
- `context`: Switch to conversational mode (maintains context)

**Mode Explanation**:
- **Single Mode**: Each question is treated independently - perfect for unrelated questions
- **Context Mode**: Maintains conversation history - good for follow-up questions on the same topic

**Topic Filtering**:
- **Music-Only Mode** (default): Only answers music-related questions, politely declines others
- **All-Topics Mode**: Answers any question (use `--allow-all-topics` to enable)

## Features

- ✅ Interactive chat mode with conversation history
- ✅ Single prompt mode for quick queries
- ✅ Streaming responses for real-time output
- ✅ Connection and model validation
- ✅ Error handling and user-friendly messages
- ✅ Customizable model and server settings
- ✅ Clean, colorful terminal interface
- ✅ Anti-hallucination features to reduce verbose/inaccurate responses
- ✅ Configurable response length and temperature controls
- ✅ Smart conversation management to prevent context bleeding
- ✅ Single-question mode for independent queries
- ✅ Music-focused responses with polite topic filtering
- ✅ Comprehensive music keyword detection system

## Troubleshooting

### "Cannot connect to Ollama"
- Make sure Ollama is installed and running: `ollama serve`
- Check if the Ollama URL is correct (default: http://localhost:11434)

### "Model 'tinyllama' not found"
- Pull the model: `ollama pull tinyllama`
- Check available models: `ollama list`

### "Module 'requests' not found"
- Install dependencies: `pip install -r requirements.txt`

### Model giving verbose or inaccurate responses (hallucination)
- Use the `--concise` flag for shorter, more focused responses
- Lower the temperature with `-t 0.3` for more deterministic output
- Reduce response length with `--max-tokens 200` or use `--concise` (automatically limits to 300 tokens)
- Example: `python tinyllama_runner.py --concise -t 0.3 -p "Your question"`

### Model responses are being cut off or incomplete ✅ FIXED
- **Issue resolved!** Responses now complete properly with natural conclusions
- Fixed by removing `repeat_penalty` parameter and adding explicit stop sequence control
- If you still need longer responses, use `--max-tokens 1200` for detailed explanations
- Example: `python tinyllama_runner.py --max-tokens 1200 -p "Explain jazz harmony"`

### Model connecting unrelated questions (context bleeding)
- Use `--single-mode` to treat each question independently
- Type `single` in interactive mode to disable conversation context
- Limit conversation history with `--context-limit 4`
- Example: `python tinyllama_runner.py --single-mode -p "Your question"`

### Want to ask non-music questions
- The model is configured for music-only by default to prevent hallucinations
- Use `--allow-all-topics` to enable general question answering
- Example: `python tinyllama_runner.py --allow-all-topics -p "What is Python?"`
- Note: Music-only mode provides more accurate and focused responses

## License

This project is open source and available under the MIT License. 