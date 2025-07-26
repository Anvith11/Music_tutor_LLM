# 🔊 Text-to-Speech Integration for TinyLLAMA Music Tutor

Your TinyLLAMA Music Tutor now supports **text-to-speech (TTS)** functionality using Huggingface's chatterbox TTS model. This allows all music education responses to be converted to high-quality speech automatically.

## 🚀 Quick Start

### Installation

```bash
# Install TTS dependencies
pip install -r requirements_tts.txt

# Or install individually
pip install chatterbox-tts torch torchaudio
```

### Basic Usage

```bash
# Enable interactive TTS (prompted after each response)
python tinyllama_runner.py --enable-tts --interactive

# Single question with TTS
python tinyllama_runner.py --enable-tts --prompt "What is a ii-V-I progression?"

# Enable TTS with file saving (saves audio files + interactive playback)
python tinyllama_runner.py --enable-tts --save-audio --interactive

# Run TTS demo
python tts_demo.py
```

## 🛠️ Configuration Options

### Command Line Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `--enable-tts` | Enable interactive text-to-speech | `False` |
| `--save-audio` | Also save audio responses to files | `False` |
| `--tts-device` | Device for TTS: 'auto', 'cuda', 'cpu' | `auto` |
| `--audio-output-dir` | Directory for audio files (if saving) | `audio_output` |
| `--audio-prompt-path` | Voice ID for specific system voice | `None` |

### Examples

```bash
# Basic TTS on CPU
python tinyllama_runner.py --enable-tts --tts-device cpu

# TTS with custom output directory
python tinyllama_runner.py --enable-tts --audio-output-dir my_audio

# Voice cloning with custom voice
python tinyllama_runner.py --enable-tts --audio-prompt-path my_voice.wav
```

## 🎭 Voice Cloning

The TTS system supports voice cloning using an audio prompt:

### Preparing Voice Samples

1. **Create a clear audio recording** (3-10 seconds)
2. **Save as WAV format** with good quality
3. **Use consistent speaking style** for best results

### Using Voice Cloning

```bash
# Record your voice sample
python tinyllama_runner.py --enable-tts --audio-prompt-path your_voice.wav --interactive

# Test voice cloning
python tts_demo.py voice
```

### Voice Sample Requirements

- **Format**: WAV file
- **Duration**: 3-10 seconds
- **Quality**: Clear speech, minimal background noise
- **Content**: Natural speaking voice (not singing)

## 🎵 Music Education Applications

### Perfect for:

**🎓 Music Students**
- Hear explanations while practicing instruments
- Audio feedback for theory concepts
- Hands-free learning during practice sessions

**👨‍🏫 Music Educators** 
- Create audio content for lessons
- Provide spoken explanations for complex concepts
- Generate audio materials for different learning styles

**🎸 Musicians**
- Voice guidance during practice
- Audio explanations of techniques
- Hands-free music theory reference

## 📁 Audio Output Management

### File Organization

```
audio_output/
├── music_response_1703123456.wav      # Standard music responses
├── music_chat_1703123789.wav          # Interactive chat responses  
├── non_music_response_1703124012.wav  # Non-music topic responses
└── error_response_1703124234.wav      # Error messages
```

### File Naming Convention

- **Prefix**: Response type (`music_response`, `music_chat`, etc.)
- **Timestamp**: Unix timestamp for uniqueness
- **Extension**: `.wav` audio format

### Managing Audio Files

```bash
# View generated audio files
ls -la audio_output/

# Play audio (macOS)
afplay audio_output/music_response_*.wav

# Play audio (Linux)
aplay audio_output/music_response_*.wav

# Clean up old audio files
rm audio_output/*.wav
```

## ⚡ Performance Considerations

### GPU Acceleration

**CUDA (Recommended for fastest generation):**
```bash
# Install CUDA-enabled PyTorch
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu118

# Use CUDA device
python tinyllama_runner.py --enable-tts --tts-device cuda
```

**CPU (Slower but works everywhere):**
```bash
# Force CPU usage
python tinyllama_runner.py --enable-tts --tts-device cpu
```

### Performance Tips

1. **GPU Usage**: CUDA dramatically speeds up TTS generation
2. **Device Auto-detection**: Use `--tts-device auto` for automatic optimization
3. **Batch Processing**: TTS generates after complete responses for efficiency
4. **Memory**: TTS requires ~2-4GB GPU memory or 4-8GB system RAM

## 🔧 Technical Integration

### Code Integration

```python
from tinyllama_runner import TinyLLAMARunner

# Initialize with TTS
runner = TinyLLAMARunner(
    enable_tts=True,
    tts_device="auto",
    audio_output_dir="my_audio",
    audio_prompt_path="my_voice.wav"  # Optional
)

# Generate response with automatic TTS
for chunk in runner.generate_response("Explain the circle of fifths"):
    print(chunk, end="")
# Audio file automatically saved to my_audio/
```

### Streaming + TTS Workflow

1. **Text Generation**: LLM generates response in chunks
2. **Text Collection**: Full response collected for TTS
3. **Speech Synthesis**: Complete response converted to audio
4. **File Output**: Audio saved with timestamp

## 🎛️ Advanced Features

### System Status Display

```
📚 Four-Pillar Knowledge System Loaded:
  🎯 Nashville Numbers: ✅
  🎛️ Slakh Professional: ✅ (34 instruments)
  📖 Music Theory: ✅ (7 sections)
  🎸 Professional Performance: ✅ (5 areas)
  📊 Total Keywords: 484
  🔊 Text-to-Speech: ✅ Enabled
      Audio Output: audio_output
      Voice Prompt: my_voice.wav
```

### Error Handling

- **Graceful Degradation**: TTS failures don't break text responses
- **Fallback Mode**: Continues without TTS if initialization fails
- **Error Audio**: Even error messages can be synthesized to speech

### Interactive Mode Commands

```bash
🔹 You: What is a dominant seventh chord?
🤖 TinyLLAMA: [Streams response text...]
🔊 Audio saved: audio_output/music_chat_1703123456.wav
```

## 🚀 Example Workflows

### 1. Music Practice Session

```bash
# Start interactive session with TTS
python tinyllama_runner.py --enable-tts --interactive

# Ask questions while practicing
"How do I voice a Cmaj7 chord?"
"What's the Nashville number for a ii-V-I in G major?"
"Explain voice leading in jazz piano"

# Audio files saved for later review
```

### 2. Music Education Content Creation

```bash
# Generate educational audio content
python tinyllama_runner.py --enable-tts --prompt "Explain the circle of fifths and its practical applications"

# Create series of lessons
for topic in theory_topics:
    python tinyllama_runner.py --enable-tts --prompt f"Explain {topic}"
```

### 3. Voice-Customized Tutor

```bash
# Record your preferred teaching voice
# Save as teacher_voice.wav

# Use your voice for all responses
python tinyllama_runner.py --enable-tts --audio-prompt-path teacher_voice.wav --interactive
```

## 🔍 Troubleshooting

### Common Issues

**TTS Not Working:**
```bash
# Check dependencies
pip install chatterbox-tts torch torchaudio

# Check device compatibility
python -c "import torch; print(torch.cuda.is_available())"
```

**Audio Quality Issues:**
- Use higher quality voice samples for cloning
- Ensure proper microphone setup for recordings
- Test with different `--tts-device` settings

**Performance Issues:**
- Use CUDA for faster generation
- Close other GPU-intensive applications
- Consider using CPU for lower memory systems

### Debug Mode

```bash
# Run with verbose output
python tinyllama_runner.py --enable-tts --interactive -v
```

## 🎉 Benefits Summary

✅ **Hands-Free Learning**: Listen while practicing instruments  
✅ **Accessibility**: Audio support for visual learners  
✅ **Voice Customization**: Clone preferred teaching voices  
✅ **Content Creation**: Generate audio educational materials  
✅ **Multi-Modal Learning**: Combine text and audio for better retention  
✅ **Practice Integration**: Audio guidance during music practice  

## 📚 Next Steps

1. **Try the Demo**: Run `python tts_demo.py` to test functionality
2. **Create Voice Sample**: Record your preferred teaching voice
3. **Practice Integration**: Use during instrument practice sessions
4. **Educational Content**: Generate audio lessons for students

---

**Your TinyLLAMA Music Tutor now speaks! 🎵🔊**

*Total Enhancement: Four-pillar knowledge system + professional TTS integration = Complete audio-visual music education platform* 