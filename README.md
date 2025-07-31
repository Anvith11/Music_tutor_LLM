# 🎵 HorizonJam - Music Theory Tutor with GPT-4o

**HorizonJam** is a music-focused AI tutor powered by GPT-4o that **ONLY answers music-related questions**. It features comprehensive music filtering, Nashville Numbers System, professional instrument knowledge, and optional text-to-speech integration.

## ✨ Key Features

🎯 **Music-Only Filtering**: Advanced pre-filtering ensures responses are strictly music-related  
🤖 **GPT-4o Integration**: Latest OpenAI model for high-quality music education  
🎵 **Nashville Numbers**: Expert chord progression analysis and transposition  
🎸 **Instrument Knowledge**: Professional-grade instrument datasets (Slakh integration)  
🔊 **Text-to-Speech**: Optional voice responses for interactive learning  
⚡ **Streaming Responses**: Real-time response generation  

## 🚀 Quick Start

### 1. Setup API Key
```bash
# Set your OpenAI API key
export OPENAI_API_KEY="your-api-key-here"
echo 'export OPENAI_API_KEY="your-api-key"' > .env
```

### 2. Install Dependencies  
```bash
pip install -r requirements.txt

# Optional: For TTS features
pip install -r requirements_tts.txt
```

### 3. Run HorizonJam
```bash
# Interactive mode
python openai_music_tutor.py --interactive

# Single question
python openai_music_tutor.py --prompt "What is a C major scale?"

# With TTS enabled
python openai_music_tutor.py --interactive --tts
```

## 📁 File Structure

```
HorizonJam/
├── openai_music_tutor.py      # 🎵 Main HorizonJam wrapper
├── slakh_instrument_data.py   # 🎸 Professional instrument database
├── tts_demo.py               # 🔊 Text-to-speech integration
├── test_interactive_tts.py   # 🧪 TTS testing
├── run_openai_tutor.sh       # 🚀 Launch script
├── requirements.txt          # 📦 Core dependencies
├── requirements_tts.txt      # 🔊 TTS dependencies
├── audio_output/            # 📁 TTS audio files
├── voice_demo_output/       # 📁 Voice demo recordings
├── .env                     # 🔑 API key (create this)
└── README.md               # 📖 This file
```

## 🎯 Music-Only Filtering

HorizonJam is designed to be **laser-focused on music**:

✅ **Responds to**: Chords, scales, theory, instruments, Nashville numbers, production, practice tips  
❌ **Rejects**: Math, programming, general knowledge, non-music topics  

### Example Filtering:
```python
# ✅ Music questions (accepted)
"What is a C major scale?"
"Explain the circle of fifths"  
"How do I play a G7 chord?"
"What's the Nashville number for this progression?"

# ❌ Non-music questions (rejected)
"What is 2+2?"
"Who is the president?"
"How do I code in Python?"
```

## 🎵 Usage Examples

### Interactive Mode
```bash
python openai_music_tutor.py --interactive
```
```
🎵 You: What chords are in the key of G major?
🤖 HorizonJam: The chords in G major are:
   1. G major (I)
   2. A minor (ii) 
   3. B minor (iii)
   4. C major (IV)
   5. D major (V)
   6. E minor (vi)
   7. F# diminished (vii°)
   
   In Nashville Numbers: 1-2m-3m-4-5-6m-7°
```

### Single Questions
```bash
python openai_music_tutor.py --prompt "Explain sus chords"
```

### With Text-to-Speech
```bash
python openai_music_tutor.py --interactive --tts
```

## 🔧 Configuration Options

| Flag | Description |
|------|-------------|
| `--interactive` | Start interactive chat session |
| `--prompt "text"` | Ask single question |
| `--model gpt-4o` | Specify OpenAI model |
| `--tts` | Enable text-to-speech |
| `--no-stream` | Disable streaming responses |

## 🎸 Knowledge Areas

**Nashville Numbers System**
- Chord progression analysis
- Key transposition
- Roman numeral notation

**Instrument Knowledge** 
- Professional instrument data from Slakh dataset
- MIDI program numbers
- Instrument techniques and styles

**Music Theory**
- Scales, modes, intervals
- Chord construction and progressions  
- Voice leading and harmony

**Performance Practice**
- Practice techniques
- Performance tips
- Music production basics

## 🔊 Text-to-Speech Integration

HorizonJam includes optional TTS for voice responses:

```bash
# Test TTS functionality
python tts_demo.py

# Test interactive TTS
python test_interactive_tts.py

# Use TTS in main tutor
python openai_music_tutor.py --tts
```

TTS files are saved to `audio_output/` directory.

## 🛠️ Requirements

- **Python 3.7+**
- **OpenAI API key** with GPT-4o access
- **Internet connection** for API calls
- **Optional**: TTS dependencies for voice features

## 💡 Tips

1. **API Costs**: GPT-4o is ~$0.03 per question (vs GPT-3.5's ~$0.002)
2. **Billing**: Ensure OpenAI billing is set up with proper permissions
3. **Music Focus**: All questions must be music-related - the system will reject off-topic queries
4. **TTS**: Voice responses enhance the learning experience for auditory learners

## 🎉 Ready to Learn Music?

Start your musical journey with HorizonJam:
```bash
python openai_music_tutor.py --interactive
```

🎵 **Ask me about chords, scales, theory, instruments, or practice tips!**