# 🎵 Music Tutor LLM - Qwen2-Audio Edition

**AI-Powered Music Education with Four-Pillar Knowledge System**

Powered by **Qwen2-Audio** for native audio input/output capabilities and local inference

## 🌟 Key Features

### 🔊 **Native Audio Capabilities**
- **Audio Input**: Speak your music questions naturally
- **Audio Analysis**: Analyze music files and audio recordings
- **Multimodal**: Combine text and audio for rich interactions
- **Local Processing**: All audio processing happens on your machine

### 🖥️ **Local & Private**
- **No API costs** - Free to use after setup
- **Privacy focused** - Your data stays on your machine
- **Offline capable** - Works without internet after model download
- **GPU accelerated** - Powerful local inference

## 🎯 Four-Pillar Music Knowledge System

Comprehensive music knowledge covering:

1. **🎵 Nashville Numbers** - Practical chord notation and transposition
2. **🎛️ Slakh Dataset** - 34 professional instrument classes with MIDI mappings
3. **📖 Music Theory** - Complete educational curriculum from musictheory.net
4. **🎸 Professional Performance** - Advanced techniques, ear training, and live skills

## 🚀 Quick Start

### 1. System Requirements
- **GPU**: NVIDIA with 16GB+ VRAM (recommended)
- **RAM**: 32GB+ system memory
- **Storage**: 20GB+ free space for model download
- **Python**: 3.8 or higher

### 2. Installation

#### For macOS users (Recommended):
```bash
# Clone repository
git clone <your-repo-url>
cd <repo-name>

# Install macOS-compatible dependencies
pip install -r requirements_macos.txt
```

#### For Linux/Windows with CUDA:
```bash
# Clone repository
git clone <your-repo-url>
cd <repo-name>

# Install full dependencies (includes CUDA optimizations)
pip install -r requirements.txt
```

### 3. Run the Music Tutor
```bash
# Interactive mode
python qwen_music_tutor.py --interactive

# Single text question
python qwen_music_tutor.py --prompt "What is the circle of fifths?"

# Audio analysis
python qwen_music_tutor.py --audio song.wav --prompt "What key is this in?"

# Both text and audio input
python qwen_music_tutor.py --audio question.wav --prompt "Also explain the theory"
```

## 📊 Model Options

| Model | VRAM | Features | Best For |
|-------|------|----------|----------|
| `Qwen/Qwen2-Audio-7B-Instruct` | 16GB+ | Text + Audio input | General use (default) |
| `Qwen/Qwen2.5-Omni-7B` | 24GB+ | Text + Audio I/O | Audio generation |
| `Qwen/Qwen2.5-Omni-7B-AWQ` | 12GB+ | Memory optimized | Lower VRAM |

```bash
# Use specific model
python qwen_music_tutor.py --model Qwen/Qwen2.5-Omni-7B-AWQ --interactive
```

## 💬 Usage Examples

### Basic Music Questions
```bash
python qwen_music_tutor.py --prompt "Explain secondary dominants in jazz"
```

### Audio Analysis
```bash
# Analyze audio file
python qwen_music_tutor.py --audio guitar_riff.wav --prompt "What chords are being played?"

# Voice questions
python qwen_music_tutor.py --audio voice_question.wav
```

### Nashville Numbers
```
🔹 You: "Convert C-Am-F-G to Nashville numbers"
🤖 Response: "That's 1-6m-4-5 in the key of C major..."
```

### Professional Analysis
```
🔹 You: [Audio of piano performance]
🤖 Response: "I hear a jazz voicing with a maj7#11 chord, played with rootless voicing technique..."
```

## 🎼 Interactive Mode Commands

```bash
python qwen_music_tutor.py --interactive
```

**Commands available:**
- `quit`, `exit`, `bye` - Exit the program
- `clear` - Clear conversation history
- `single` - Toggle single-question mode
- `context` - Toggle conversational mode
- `audio <path>` - Include audio file in message
- `status` - Show system status

## 🔧 Advanced Configuration

### Memory Optimization
```bash
# Use quantized model for lower VRAM
python qwen_music_tutor.py --model Qwen/Qwen2.5-Omni-7B-AWQ

# Reduce context and token limits
python qwen_music_tutor.py --max-tokens 400 --context-limit 3
```

### Audio Settings
```bash
# Save audio responses to files
python qwen_music_tutor.py --save-audio --audio-output-dir my_audio

# Custom audio sampling rate
python qwen_music_tutor.py --audio-sampling-rate 22050
```

### Response Style
```bash
# Concise responses
python qwen_music_tutor.py --concise --max-tokens 300

# Allow non-music questions
python qwen_music_tutor.py --allow-all-topics
```

## 📈 Performance & Capabilities

### Audio Processing
- **Formats**: WAV, MP3, M4A, FLAC
- **Sample Rate**: Automatically resampled to 16kHz
- **Max Length**: 30 seconds recommended
- **Processing**: Real-time audio analysis

### Knowledge Base
- **500+ music keywords** for intelligent topic detection
- **Nashville number system** with automatic conversion
- **34 instrument classes** from professional Slakh dataset
- **Complete music theory** covering all major topics
- **Performance techniques** for all skill levels

## 🔍 Troubleshooting

### Common Issues

**Out of Memory:**
```bash
# Try quantized model
python qwen_music_tutor.py --model Qwen/Qwen2.5-Omni-7B-AWQ

# Reduce memory usage
python qwen_music_tutor.py --max-tokens 300 --context-limit 2
```

**Model Loading Issues:**
```bash
# Check GPU status
nvidia-smi

# Verify CUDA installation
python -c "import torch; print(torch.cuda.is_available())"
```

**Audio Problems:**
```bash
# Test audio loading
python -c "import librosa; librosa.load('your_audio.wav')"

# Check supported formats
echo "Supported: WAV, MP3, M4A, FLAC"
```

## 🎯 System Requirements Details

### Minimum Requirements
- **GPU**: 12GB+ VRAM (with AWQ model)
- **RAM**: 16GB+ system memory
- **Storage**: 15GB+ free space
- **Internet**: Required for initial model download

### Recommended Requirements
- **GPU**: 16GB+ VRAM (RTX 4080, A4000, or better)
- **RAM**: 32GB+ system memory
- **Storage**: 25GB+ free space (SSD preferred)
- **CUDA**: 11.8 or higher

### Optimal Performance
- **GPU**: 24GB+ VRAM (RTX 4090, A5000, or better)
- **RAM**: 64GB+ system memory
- **Storage**: 50GB+ NVMe SSD
- **CPU**: 8+ cores for audio preprocessing

## 🤝 Contributing

1. Fork the repository
2. Test with diverse musical content
3. Add new knowledge to the four-pillar system
4. Enhance audio processing capabilities
5. Submit pull request with examples

## 📄 License

This project is open source and available under the MIT License.

## 🎉 Acknowledgments

- **Qwen Team** - For the amazing Qwen2-Audio multimodal model
- **Music Theory Community** - For comprehensive educational resources
- **Slakh Dataset** - For professional instrument and MIDI data
- **Open Source Community** - For the tools and libraries that make this possible

---

**🎵 Ready to revolutionize your music learning with local AI? Get started now!**

```bash
# Check if your system is ready
python -c "import torch; print('✅ Ready!' if torch.cuda.is_available() else '⚠️ GPU recommended')"

# Start learning!
python qwen_music_tutor.py --interactive
``` 