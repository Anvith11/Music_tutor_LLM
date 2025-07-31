# Music Tutor using OpenAI

A comprehensive Python interface to run an AI music tutor using OpenAI's GPT models with four-pillar music knowledge integration.

## 🎵 Four-Pillar Knowledge System

This music tutor integrates four comprehensive knowledge sources:

1. **🎯 Nashville Numbers** - Practical chord notation and transposition
2. **🎛️ Slakh Dataset** - Professional instrument and production knowledge  
3. **📚 Music Theory** - Complete educational curriculum from musictheory.net
4. **🎸 Professional Performance** - Advanced performance, ear training, and live techniques

## ✨ Key Features

- **🤖 OpenAI GPT Integration**: Powered by GPT-3.5-turbo or GPT-4 for intelligent responses
- **🎵 Music-Only Mode**: Focused exclusively on music education (default)
- **🔊 Text-to-Speech**: Optional voice output for responses
- **💬 Interactive Chat**: Conversational learning experience
- **📚 Comprehensive Knowledge**: Four integrated knowledge systems
- **🔐 Secure**: Uses environment variables for API key management

## Prerequisites

1. **OpenAI API Key**: Get your API key from [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
2. **Python 3.7+**: Make sure Python is installed on your system

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your OpenAI API key**:
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

3. **Run the music tutor**:
   ```bash
   python openai_music_tutor.py --interactive
   ```

## Usage Examples

### Interactive Mode (Recommended)

Start a conversational music learning session:

```bash
python openai_music_tutor.py --interactive
```

### Single Question Mode

Ask a specific music question:

```bash
python openai_music_tutor.py --prompt "What is the Nashville number system?"
```

### With Different Models

Use GPT-4 for more detailed responses:

```bash
python openai_music_tutor.py --model "gpt-4" --prompt "Explain jazz harmony principles"
```

### Enable Text-to-Speech

Get spoken responses:

```bash
python openai_music_tutor.py --enable-tts --interactive
```

## Command Line Options

| Option | Short | Description |
|--------|-------|-------------|
| `--prompt` | `-p` | Single prompt to send to the music tutor |
| `--model` | `-m` | OpenAI model name (default: gpt-3.5-turbo) |
| `--api-key` | `-k` | OpenAI API key (or set OPENAI_API_KEY env var) |
| `--interactive` | `-i` | Run in interactive mode |
| `--no-stream` | | Disable streaming responses |
| `--temperature` | `-t` | Temperature for response generation (0.0-1.0) |
| `--max-tokens` | | Maximum number of tokens to generate |
| `--concise` | | Force very concise responses |
| `--single-mode` | | Single question mode (no context) |
| `--context-limit` | | Maximum conversation history length |
| `--allow-all-topics` | | Allow non-music questions |
| `--enable-tts` | | Enable text-to-speech |
| `--save-audio` | | Save audio responses to files |

## Example Conversations

**Nashville Numbers:**
```
You: Convert C-Am-F-G to Nashville numbers
Tutor: In the key of C major, that progression would be:
C-Am-F-G = 1-6m-4-5

This is one of the most popular progressions in music!
```

**Music Theory:**
```
You: What's a ii-V-I progression?
Tutor: A ii-V-I is a fundamental chord progression where:
- ii: minor chord built on the 2nd degree
- V: major (dominant) chord on the 5th degree  
- I: major chord on the 1st degree (home)

In C major: Dm-G-C (2m-5-1)
```

**Instruments & Production:**
```
You: What's the difference between a Stratocaster and Les Paul?
Tutor: Key differences:
- Stratocaster: Bright, articulate tone with single-coil pickups
- Les Paul: Warm, thick tone with humbucker pickups
- Body: Strat uses alder/ash, Les Paul uses mahogany with maple cap
```

## System Requirements

- **Python**: 3.7 or later
- **Internet**: Required for OpenAI API calls
- **Memory**: 100MB+ available RAM
- **Storage**: 50MB for knowledge files
- **Optional**: Audio device for TTS features

## Setup and Configuration

For detailed setup instructions, see [SETUP.md](SETUP.md).

### Environment Variables

```bash
# Required
export OPENAI_API_KEY="your-api-key-here"

# Optional
export OPENAI_ORG_ID="your-org-id"  # If using organization
```

### Configuration Files

The system automatically loads these knowledge files if available:
- `four_pillar_training_data.json` - Nashville Numbers and comprehensive data
- `music_theory_dataset.json` - Music theory curriculum
- `slakh_instrument_data.py` - Professional instrument knowledge

## Knowledge System Details

### 1. Nashville Numbers (🎯)
- Chord progression notation using numbers 1-7
- Automatic transposition capabilities
- Major and minor scale relationships
- Practical chord substitutions

### 2. Slakh Dataset (🎛️)
- 34 professional instrument classes
- MIDI program mappings
- Synthesis and production techniques
- Genre-specific instrument usage

### 3. Music Theory (📚)
- Complete musictheory.net curriculum
- Scales, modes, and intervals
- Harmonic analysis and voice leading
- Notation and rhythm fundamentals

### 4. Professional Performance (🎸)
- Advanced performance techniques
- Ear training methodologies
- Live performance preparation
- Studio recording practices

## Troubleshooting

### Common Issues

1. **API Key Errors**:
   ```bash
   export OPENAI_API_KEY="your-actual-api-key"
   ```

2. **Import Errors**:
   ```bash
   pip install --upgrade openai
   ```

3. **TTS Issues**:
   ```bash
   pip install pyttsx3
   ```

### Test Your Setup

Run the setup test script:

```bash
python test_openai_setup.py
```

## Development

### Running Tests

```bash
python test_openai_setup.py
```

### File Structure

```
.
├── openai_music_tutor.py          # Main application
├── requirements.txt               # Dependencies
├── test_openai_setup.py          # Setup verification
├── run_openai_tutor.sh           # Launch script
├── four_pillar_training_data.json # Nashville Numbers data
├── music_theory_dataset.json     # Theory curriculum
└── slakh_instrument_data.py       # Instrument knowledge
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test with `python test_openai_setup.py`
5. Submit a pull request

## License

This project is open source. See LICENSE file for details.

## Acknowledgments

- **OpenAI** for providing the GPT models and API
- **Nashville Numbers System** for practical chord notation
- **Slakh Dataset** for professional music production knowledge
- **musictheory.net** for comprehensive music theory curriculum
- **Music Education Community** for inspiration and feedback

---

🎵 **Happy Learning!** Whether you're a beginner or professional, this tutor adapts to help you grow musically! 