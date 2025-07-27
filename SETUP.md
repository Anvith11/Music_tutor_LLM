# Setup Guide - Qwen2-Audio Music Tutor

**Local AI-powered music education with native audio input/output capabilities**

## Prerequisites

- **Python**: 3.8 or higher
- **GPU**: NVIDIA GPU with 16GB+ VRAM (recommended)
- **RAM**: 32GB+ system memory
- **Storage**: 20GB+ free disk space for model downloads
- **CUDA**: 11.8 or higher for GPU acceleration

## Installation

### 1. Clone the repository:
```bash
git clone <your-repo-url>
cd <repo-name>
```

### 2. Install dependencies:
```bash
pip install -r requirements.txt
```

**Note**: This will install PyTorch, Transformers, audio processing libraries, and other dependencies needed for Qwen2-Audio.

### 3. Verify installation:
```bash
# Check GPU availability
python -c "import torch; print('GPU Available:', torch.cuda.is_available())"

# Check audio processing
python -c "import librosa, soundfile; print('Audio libraries ready')"

# Check Transformers
python -c "from transformers import AutoProcessor; print('Transformers ready')"
```

## Quick Start

### Basic Usage:
```bash
# Interactive mode
python qwen_music_tutor.py --interactive

# Single text question
python qwen_music_tutor.py --prompt "What is the circle of fifths?"

# Audio analysis
python qwen_music_tutor.py --audio song.wav --prompt "What key is this in?"
```

### Model Selection:
```bash
# Default model (16GB+ VRAM)
python qwen_music_tutor.py --interactive

# Memory-optimized model (12GB+ VRAM)
python qwen_music_tutor.py --model Qwen/Qwen2.5-Omni-7B-AWQ --interactive

# Full audio generation model (24GB+ VRAM)
python qwen_music_tutor.py --model Qwen/Qwen2.5-Omni-7B --interactive
```

## Model Options

| Model | VRAM | Features | Best For |
|-------|------|----------|----------|
| `Qwen/Qwen2-Audio-7B-Instruct` | 16GB+ | Text + Audio input | General use (default) |
| `Qwen/Qwen2.5-Omni-7B` | 24GB+ | Text + Audio I/O | Audio generation |
| `Qwen/Qwen2.5-Omni-7B-AWQ` | 12GB+ | Quantized version | Lower VRAM |

## Advanced Configuration

### Memory Optimization:
```bash
# Use quantized model
python qwen_music_tutor.py --model Qwen/Qwen2.5-Omni-7B-AWQ

# Reduce token limits
python qwen_music_tutor.py --max-tokens 400 --context-limit 3

# Concise responses
python qwen_music_tutor.py --concise
```

### Audio Settings:
```bash
# Save audio responses
python qwen_music_tutor.py --save-audio --audio-output-dir my_audio

# Custom sampling rate
python qwen_music_tutor.py --audio-sampling-rate 22050

# Device selection
python qwen_music_tutor.py --device cuda  # or 'cpu' for CPU-only
```

### Conversation Modes:
```bash
# Single question mode (no context)
python qwen_music_tutor.py --single-mode

# Allow non-music questions
python qwen_music_tutor.py --allow-all-topics

# Custom temperature
python qwen_music_tutor.py --temperature 0.5
```

## Audio Input Support

### Supported Formats:
- **WAV** - Uncompressed audio (recommended)
- **MP3** - Compressed audio
- **M4A** - Apple audio format
- **FLAC** - Lossless compression

### Audio Guidelines:
- **Max Length**: 30 seconds recommended
- **Sample Rate**: Automatically resampled to 16kHz
- **Quality**: Clear audio with minimal background noise works best
- **Content**: Music questions, music audio, or musical examples

### Example Audio Commands:
```bash
# Audio-only input
python qwen_music_tutor.py --audio question.wav

# Audio + text prompt
python qwen_music_tutor.py --audio song.wav --prompt "Analyze the harmony"

# Interactive mode with audio support
python qwen_music_tutor.py --interactive
# Then type: audio path/to/file.wav
```

## Troubleshooting

### GPU Memory Issues:
```bash
# Check GPU memory
nvidia-smi

# Try quantized model
python qwen_music_tutor.py --model Qwen/Qwen2.5-Omni-7B-AWQ

# Reduce memory usage
python qwen_music_tutor.py --max-tokens 300 --context-limit 2
```

### Model Loading Problems:
```bash
# Check internet connection (first download)
ping huggingface.co

# Clear Hugging Face cache if corrupted
rm -rf ~/.cache/huggingface/

# Check disk space
df -h
```

### Audio Processing Issues:
```bash
# Test audio file
python -c "import librosa; data, sr = librosa.load('your_audio.wav'); print(f'Loaded {len(data)} samples at {sr}Hz')"

# Check audio format
file your_audio.wav

# Convert audio format if needed
ffmpeg -i input.mp3 output.wav
```

### CUDA Issues:
```bash
# Check NVIDIA driver
nvidia-smi

# Check CUDA installation
nvcc --version

# Test PyTorch CUDA
python -c "import torch; print(torch.version.cuda)"

# Force CPU mode if needed
python qwen_music_tutor.py --device cpu
```

## Performance Optimization

### For Best Performance:
1. **Use SSD storage** for faster model loading
2. **Ensure adequate cooling** for sustained GPU performance
3. **Close other GPU applications** to free VRAM
4. **Use quantized models** if memory constrained
5. **Batch multiple questions** in interactive mode

### Monitoring:
```bash
# Monitor GPU usage
watch nvidia-smi

# Check Python memory usage
python -c "import psutil; print(f'RAM: {psutil.virtual_memory().percent}%')"
```

## Security Notes

- **Local Processing**: All data stays on your machine
- **Model Downloads**: Models downloaded from Hugging Face (trusted source)
- **No API Keys**: No external API keys or internet required after setup
- **Privacy**: Your audio and conversations remain private

## System Requirements by Use Case

### Music Student (Basic):
- **GPU**: 12GB VRAM (RTX 3060 Ti, 4070)
- **Model**: Qwen2.5-Omni-7B-AWQ
- **Usage**: Text questions, basic audio analysis

### Music Teacher (Standard):
- **GPU**: 16GB VRAM (RTX 4080, 4070 Ti)
- **Model**: Qwen2-Audio-7B-Instruct
- **Usage**: Interactive lessons, audio analysis, demonstrations

### Music Professional (Advanced):
- **GPU**: 24GB VRAM (RTX 4090, A5000)
- **Model**: Qwen2.5-Omni-7B
- **Usage**: Audio generation, complex analysis, studio work

## Getting Help

If you encounter issues:

1. **Check system requirements** - Ensure your hardware meets minimums
2. **Update drivers** - Latest NVIDIA drivers recommended
3. **Check logs** - Error messages provide diagnostic information
4. **Try different models** - AWQ versions require less memory
5. **Monitor resources** - Use `nvidia-smi` and `htop` to check usage

For additional support, check the project documentation or open an issue with:
- Your system specifications
- Error messages
- Steps to reproduce the problem 