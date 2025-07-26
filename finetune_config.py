"""
Configuration file for TinyLlama Music Instructor Fine-tuning
"""

from dataclasses import dataclass
from typing import Optional, List

@dataclass
class ModelConfig:
    """Configuration for the base model"""
    model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
    cache_dir: Optional[str] = "./model_cache"
    torch_dtype: str = "float16"
    device_map: str = "auto"
    trust_remote_code: bool = True

@dataclass
class LoRAConfig:
    """Configuration for LoRA (Low-Rank Adaptation)"""
    r: int = 16  # Rank of adaptation
    lora_alpha: int = 32  # LoRA scaling parameter
    target_modules: Optional[List[str]] = None  # Will be set to ["q_proj", "v_proj", "k_proj", "o_proj", "gate_proj", "up_proj", "down_proj"]
    lora_dropout: float = 0.1  # LoRA dropout
    bias: str = "none"  # Bias type for LoRA
    task_type: str = "CAUSAL_LM"  # Task type
    
    def __post_init__(self):
        if self.target_modules is None:
            self.target_modules = [
                "q_proj", "v_proj", "k_proj", "o_proj", 
                "gate_proj", "up_proj", "down_proj"
            ]

@dataclass
class TrainingConfig:
    """Configuration for training parameters"""
    output_dir: str = "./tinyllama_music_instructor"
    per_device_train_batch_size: int = 2
    per_device_eval_batch_size: int = 2
    gradient_accumulation_steps: int = 8
    learning_rate: float = 2e-4
    max_steps: int = 1000
    warmup_steps: int = 100
    logging_steps: int = 10
    evaluation_strategy: str = "steps"
    eval_steps: int = 100
    save_steps: int = 200
    save_total_limit: int = 3
    load_best_model_at_end: bool = True
    metric_for_best_model: str = "eval_loss"
    greater_is_better: bool = False
    report_to: str = "wandb"  # or "tensorboard" or None
    run_name: str = "tinyllama_music_instructor"
    seed: int = 42
    data_seed: int = 42
    remove_unused_columns: bool = False
    dataloader_pin_memory: bool = True
    gradient_checkpointing: bool = True
    fp16: bool = True
    bf16: bool = False
    max_grad_norm: float = 1.0
    weight_decay: float = 0.01
    adam_beta1: float = 0.9
    adam_beta2: float = 0.999
    adam_epsilon: float = 1e-8
    lr_scheduler_type: str = "cosine"

@dataclass
class DataConfig:
    """Configuration for data processing"""
    dataset_path: str = "music_theory_dataset.json"
    max_seq_length: int = 512
    train_split: float = 0.8
    val_split: float = 0.1
    test_split: float = 0.1
    shuffle_seed: int = 42
    
    # Template for instruction formatting
    instruction_template: str = "### Instruction:\n{instruction}\n\n### Response:\n{output}"
    
    # Comprehensive system prompt with four-pillar knowledge system
    system_prompt: str = """You are an expert music instructor with comprehensive knowledge across four core areas:

1. NASHVILLE NUMBERS: Expert in the Nashville number system for chord progressions, transposition, and practical music communication.

2. PROFESSIONAL INSTRUMENTS: Complete understanding of 34 professional instrument classes, 187 synthesis patches, MIDI programming, and music production techniques from the Slakh dataset including sample libraries, velocity layers, round-robin sampling, and professional mixing techniques.

3. MUSIC THEORY: Comprehensive curriculum covering notation, staff systems, rhythm and meter, scales and key signatures, intervals, chord construction, harmonic analysis, functional harmony, cadences, nonharmonic tones, and advanced concepts from musictheory.net.

4. PROFESSIONAL PERFORMANCE: Advanced performance techniques, professional ear training methodologies, sophisticated chord voicings, live performance skills, improvisation strategies, studio communication, and creative musical expression techniques.

Provide clear, accurate, and educational responses that integrate these knowledge areas. Connect practical Nashville numbers with theoretical concepts, professional production techniques, and performance applications. Keep explanations applicable for musicians, students, producers, performers, and music technology users at all levels."""

@dataclass
class InferenceConfig:
    """Configuration for inference"""
    max_new_tokens: int = 256
    temperature: float = 0.7
    top_p: float = 0.9
    do_sample: bool = True
    pad_token_id: int = 0
    eos_token_id: int = 2
    repetition_penalty: float = 1.1

# Global configuration instances
model_config = ModelConfig()
lora_config = LoRAConfig()
training_config = TrainingConfig()
data_config = DataConfig()
inference_config = InferenceConfig() 