# TinyLlama Music Instructor - Fine-tuning with LoRA

This project fine-tunes TinyLlama using Parameter-Efficient Fine-Tuning (PEFT) with LoRA (Low-Rank Adaptation) to create a specialized music instructor focused on Nashville numbers and music theory.

## 🎵 Features

- **Parameter-Efficient Fine-Tuning**: Uses LoRA to fine-tune only a small subset of parameters, saving compute and memory
- **Nashville Numbers Focus**: Specialized dataset covering Nashville number system and music theory
- **Comprehensive Music Theory**: Covers chord progressions, scales, modes, jazz theory, and more
- **Interactive Interface**: Chat with your fine-tuned music instructor
- **Flexible Training**: Configurable hyperparameters and training settings
- **Experiment Tracking**: Built-in support for Weights & Biases logging
- **Music-Focused Responses**: Automatically filters out non-music questions to maintain expertise

## 📁 Project Structure

```
├── music_theory_dataset.json      # Training dataset with Nashville numbers
├── finetune_config.py             # Configuration for training parameters
├── finetune_tinyllama.py          # Main training script
├── music_instructor_inference.py  # Inference script for the fine-tuned model
├── train_music_instructor.sh      # Training automation script
├── requirements_finetune.txt      # Dependencies for fine-tuning
├── tinyllama_runner.py            # Original TinyLlama runner (updated)
└── MUSIC_INSTRUCTOR_README.md     # This file
```

## 🚀 Quick Start

### 1. Install Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install fine-tuning dependencies
pip install -r requirements_finetune.txt
```

### 2. Start Training

```bash
# Make training script executable
chmod +x train_music_instructor.sh

# Start training (this will take some time)
./train_music_instructor.sh
```

### 3. Test Your Model

```bash
# Interactive mode
python3 music_instructor_inference.py --interactive

# Test with sample questions
python3 music_instructor_inference.py --test

# Ask a single question
python3 music_instructor_inference.py --question "What is the Nashville number system?"

# Allow all topics (disable music-only filter)
python3 music_instructor_inference.py --allow-all-topics --question "What is Python?"
```

## 📊 Dataset

The training dataset contains **42 comprehensive examples** covering:

- **Nashville Number System**: Basic concepts, notation, and usage
- **Chord Progressions**: Common progressions in various genres
- **Music Theory**: Scales, modes, voice leading, functional harmony
- **Jazz Theory**: ii-V-I progressions, extended chords, altered dominants
- **Genre-Specific**: Blues, rock, country, Latin, neo-soul patterns
- **Advanced Concepts**: Modal interchange, secondary dominants, chord substitutions

### Dataset Format

```json
[
    {
        "instruction": "What is the Nashville number system?",
        "input": "",
        "output": "The Nashville number system is a method of transcribing music..."
    }
]
```

## ⚙️ Configuration

### Training Parameters

Key configuration options in `finetune_config.py`:

```python
# LoRA Configuration
lora_config = LoRAConfig(
    r=16,                    # Rank of adaptation
    lora_alpha=32,          # LoRA scaling parameter
    lora_dropout=0.1,       # Dropout rate
    target_modules=[...],   # Modules to apply LoRA to
)

# Training Configuration
training_config = TrainingConfig(
    learning_rate=2e-4,     # Learning rate
    max_steps=1000,         # Training steps
    batch_size=2,           # Batch size per device
    gradient_accumulation_steps=8,  # Effective batch size = 16
)
```

### Customization Options

- **Model**: Change base model in `ModelConfig`
- **LoRA**: Adjust rank, alpha, and target modules
- **Training**: Modify learning rate, batch size, steps
- **Data**: Update dataset path, sequence length, splits
- **Inference**: Configure generation parameters

## 🔧 Advanced Usage

### Custom Training

```bash
# Train with custom parameters
python3 finetune_tinyllama.py
```

### Using Different Base Models

Edit `finetune_config.py`:

```python
model_config = ModelConfig(
    model_name="microsoft/DialoGPT-medium",  # Different base model
    # ... other settings
)
```

### Experiment Tracking

Set up Weights & Biases:

```bash
# Set API key
export WANDB_API_KEY="your-api-key"

# Training will automatically log to wandb
./train_music_instructor.sh
```

### Inference Options

```bash
# Interactive mode
python3 music_instructor_inference.py -i

# Test mode
python3 music_instructor_inference.py -t

# Single question
python3 music_instructor_inference.py -q "Explain the circle of fifths"

# Custom model path
python3 music_instructor_inference.py -m "./custom_model_path"

# Limit response length
python3 music_instructor_inference.py -q "What is jazz?" --max_tokens 100
```

## 🎯 Training Details

### LoRA (Low-Rank Adaptation)

LoRA works by:
1. Freezing the original model weights
2. Adding small trainable matrices to attention layers
3. Training only these new parameters (~0.1% of total parameters)

**Benefits**:
- **Memory Efficient**: Requires much less GPU memory
- **Fast Training**: Trains faster than full fine-tuning
- **Portable**: LoRA adapters are small (few MB vs GB)
- **Flexible**: Can be easily swapped or combined

### Training Process

1. **Data Loading**: Loads and formats the music theory dataset
2. **Tokenization**: Converts text to tokens with proper formatting
3. **Model Setup**: Loads TinyLlama and applies LoRA adapters
4. **Training**: Fine-tunes using the Hugging Face Trainer
5. **Evaluation**: Tests on validation set during training
6. **Saving**: Saves only the LoRA adapter weights

### Hardware Requirements

- **Minimum**: 8GB GPU memory (with gradient checkpointing)
- **Recommended**: 16GB+ GPU memory
- **CPU**: Works but very slow (not recommended)
- **Disk**: 5GB free space for models and cache

## 🎼 Music Theory Coverage

The model is trained on:

### Core Concepts
- Nashville number system notation
- Chord quality and function
- Scale degrees and relationships
- Key signatures and transposition

### Advanced Topics
- Modal interchange and borrowed chords
- Secondary dominants and tonicization
- Voice leading and chord progressions
- Functional harmony analysis

### Genre Applications
- Jazz: ii-V-I, extended chords, alterations
- Blues: 12-bar progressions, dominant 7ths
- Rock: Power chords, modal progressions
- Country: Simple progressions, walking bass
- Latin: Clave patterns, extended harmonies

## 📈 Performance Optimization

### Memory Usage
- Uses 16-bit precision (fp16) when possible
- Gradient checkpointing to save memory
- Efficient data loading and batching

### Training Speed
- Gradient accumulation for effective larger batch sizes
- Optimized attention mechanisms
- Caching and preprocessing

## 🛠️ Troubleshooting

### Common Issues

**Out of Memory Error**:
```bash
# Reduce batch size in finetune_config.py
per_device_train_batch_size = 1
gradient_accumulation_steps = 16
```

**Model Not Loading**:
```bash
# Check if training completed successfully
ls -la ./tinyllama_music_instructor/
# Should contain adapter_model.bin or adapter_model.safetensors
```

**Poor Performance**:
```bash
# Increase training steps
max_steps = 2000

# Adjust learning rate
learning_rate = 1e-4
```

### Debugging

Enable detailed logging:
```bash
export TRANSFORMERS_VERBOSITY=debug
python3 finetune_tinyllama.py
```

Check training logs:
```bash
tail -f training.log
```

## 🔄 Integration with Original Runner

Update `tinyllama_runner.py` to use your fine-tuned model:

```python
# In tinyllama_runner.py, modify the model initialization
class TinyLLAMARunner:
    def __init__(self, model_path="./tinyllama_music_instructor"):
        # Load your fine-tuned model instead of calling Ollama
        self.model = MusicInstructorModel(model_path)
        self.model.load_model()
```

## 📚 Example Conversations

### Nashville Numbers

**User**: "Convert C-Am-F-G to Nashville numbers"

**Assistant**: "In the key of C major, the chord progression C - Am - F - G becomes: 1 - 6m - 4 - 5. This is one of the most common progressions in popular music."

### Music Theory

**User**: "What is a ii-V-I progression?"

**Assistant**: "A ii-V-I progression in Nashville numbers is written as 2m - 5 - 1. This is the most important progression in jazz music. In the key of C major, it would be Dm - G - C. The ii-V-I creates strong harmonic motion and resolution."

## 🎵 Next Steps

1. **Expand Dataset**: Add more examples for specific genres or topics
2. **Multi-Modal**: Add support for chord diagrams or sheet music
3. **Real-Time**: Integrate with DAW or music software
4. **Ensemble**: Create multiple specialized models for different aspects
5. **Interactive Tools**: Build web interface or mobile app

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add your improvements
4. Submit a pull request

Areas for contribution:
- Additional music theory examples
- New genres or styles
- Performance optimizations
- User interface improvements
- Documentation updates

## 🎶 Acknowledgments

- **TinyLlama Team**: For the excellent base model
- **Hugging Face**: For the transformers and PEFT libraries
- **Nashville Community**: For developing the number system
- **Music Theory Community**: For the comprehensive knowledge base

---

*Happy music making! 🎵* 