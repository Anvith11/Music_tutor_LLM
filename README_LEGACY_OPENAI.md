# Music Tutor using OpenAI

A comprehensive Python interface to run an AI music tutor using OpenAI's GPT models with four-pillar music knowledge integration.

## 🎵 Four-Pillar Knowledge System

This music tutor integrates four comprehensive knowledge sources:

1. **🎯 Nashville Numbers** - Practical chord notation and transposition
2. **🎛️ Slakh Dataset** - Professional instrument and production knowledge  
3. **📚 Music Theory** - Complete educational curriculum from musictheory.net
4. **🎸 Professional Performance** - Advanced performance, ear training, and live techniques

## Prerequisites

1. **OpenAI API Key**: Get your API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. **Python 3.7+**: Make sure Python is installed on your system

## Installation

1. Clone or download this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements_openai.txt
   ```
3. Set your OpenAI API key:
   ```bash
   # Option 1: Environment variable (recommended)
   export OPENAI_API_KEY="your-api-key-here"
   
   # Option 2: Pass as argument (see usage examples)
   ```

## Usage

### Interactive Mode (Default)

Run the script without any arguments to start an interactive chat session:

```bash
python tinyllama_runner.py --interactive
```

### Single Prompt Mode

Send a single prompt and get a response:

```bash
python tinyllama_runner.py --prompt "What is the Nashville number system?"
```

### With API Key as Argument

If you haven't set the environment variable:

```bash
python tinyllama_runner.py --api-key "your-api-key" --prompt "What is a ii-V-I progression?"
```

### Command Line Options

- `--prompt`, `-p`: Single prompt to send to the music tutor
- `--model`, `-m`: Model name (default: gpt-3.5-turbo)
- `--api-key`, `-k`: OpenAI API key (or set OPENAI_API_KEY environment variable)
- `--no-stream`: Disable streaming responses
- `--interactive`, `-i`: Run in interactive mode
- `--temperature`, `-t`: Temperature for response generation (0.0-1.0, default: 0.7)
- `--max-tokens`: Maximum number of tokens to generate (default: 800)
- `--concise`: Force very concise responses
- `--single-mode`: Start in single-question mode (no conversation context)
- `--context-limit`: Maximum conversation history length (default: 6)
- `--allow-all-topics`: Allow non-music questions (default: music-only mode)

### TTS (Text-to-Speech) Options

- `--enable-tts`: Enable interactive text-to-speech for responses
- `--save-audio`: Also save audio responses to files
- `--audio-output-dir`: Directory for audio files (default: audio_output)
- `--audio-prompt-path`: Voice ID for specific system voice

### Examples

1. **Basic usage with interactive mode**:
   ```bash
   python tinyllama_runner.py --interactive
   ```

2. **Single question about Nashville numbers**:
   ```bash
   python tinyllama_runner.py -p "Convert C-Am-F-G to Nashville numbers"
   ```

3. **Use GPT-4 model**:
   ```bash
   python tinyllama_runner.py -m "gpt-4" -p "Explain jazz harmony principles"
   ```

4. **Concise responses for quick answers**:
   ```bash
   python tinyllama_runner.py --concise -p "What is a diminished chord?"
   ```

5. **Music theory with TTS enabled**:
   ```bash
   python tinyllama_runner.py --enable-tts -p "Explain the circle of fifths"
   ```

6. **Professional performance question**:
   ```bash
   python tinyllama_runner.py -p "How do you handle key changes during live performance?"
   ```

7. **Slakh instrument knowledge**:
   ```bash
   python tinyllama_runner.py -p "What MIDI program numbers are used for piano sounds?"
   ```

## Interactive Mode Commands

When in interactive mode, you can use these special commands:

- `quit`, `exit`, or `bye`: Exit the program
- `clear`: Clear the conversation history
- `single`: Switch to single-question mode (no context between questions)
- `context`: Switch to conversational mode (maintains context)
- `status`: Show four-pillar knowledge system status

## Features

- ✅ Interactive chat mode with conversation history
- ✅ Single prompt mode for quick queries
- ✅ Streaming responses for real-time output
- ✅ OpenAI API integration with multiple model support
- ✅ Four-pillar comprehensive music knowledge system
- ✅ Music-focused responses with intelligent topic filtering
- ✅ Text-to-speech support for audio learning
- ✅ Professional-grade music theory and performance knowledge
- ✅ Nashville numbers with advanced applications
- ✅ Slakh dataset professional instrument knowledge
- ✅ Complete musictheory.net curriculum integration
- ✅ Advanced performance and ear training concepts

## Knowledge Capabilities

### 🎯 Nashville Numbers
- Chord notation and transposition
- Professional studio communication
- Advanced progressions and substitutions

### 🎛️ Slakh Professional Instruments  
- 34 professional instrument classes
- MIDI program mappings
- Synthesis and production techniques

### 📚 Music Theory
- Complete curriculum from musictheory.net
- Scales, intervals, and chord construction
- Voice leading and harmonic analysis

### 🎸 Professional Performance
- Advanced ear training methodologies
- Live performance techniques
- Studio arrangement skills

## Troubleshooting

### "OpenAI API connection failed"
- Check your API key is correct
- Ensure you have credits available in your OpenAI account
- Verify your internet connection

### "Model may not be available"
- The script supports: gpt-3.5-turbo, gpt-4, gpt-4-turbo-preview
- Check [OpenAI's model documentation](https://platform.openai.com/docs/models) for availability

### API Rate Limits
- OpenAI has rate limits based on your plan
- Consider upgrading your OpenAI plan for higher limits
- The script handles rate limit errors gracefully

### TTS Issues
- Install TTS dependencies: `pip install pyttsx3`
- TTS uses system voices and doesn't require additional API calls
- Use `--tts-device cpu` if you encounter device issues

## Cost Considerations

- OpenAI charges per token (input + output)
- GPT-3.5-turbo is more cost-effective than GPT-4
- Use `--concise` and `--max-tokens 300` to reduce costs
- Interactive mode maintains context which uses more tokens

## Environment Variables

```bash
# Required
export OPENAI_API_KEY="your-api-key-here"

# Optional
export OPENAI_MODEL="gpt-3.5-turbo"  # Default model to use
```

## Files Structure

- `tinyllama_runner.py` - Main script (now using OpenAI)
- `requirements_openai.txt` - OpenAI-specific dependencies  
- `slakh_instrument_data.py` - Professional instrument knowledge
- `musictheory_net_data.py` - Music theory curriculum
- `professional_performance_data.py` - Performance knowledge
- `tts_demo.py` - Text-to-speech demonstration
- `test_music_filter.py` - Music topic detection testing

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Areas for improvement:
- Additional music theory examples
- New instrument knowledge
- Performance technique expansion
- User interface enhancements 