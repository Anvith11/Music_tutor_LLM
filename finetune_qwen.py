#!/usr/bin/env python3
"""
Fine-tune TinyLlama with LoRA for Music Instruction
Using Parameter-Efficient Fine-Tuning (PEFT) with LoRA
"""

import os
import json
import torch
import logging
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass, field

import pandas as pd
from datasets import Dataset, DatasetDict
from transformers import (
    AutoTokenizer, 
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling,
    set_seed
)
from peft import (
    LoraConfig,
    get_peft_model,
    prepare_model_for_kbit_training,
    TaskType
)
import wandb
from sklearn.model_selection import train_test_split

from finetune_config import (
    model_config, 
    lora_config, 
    training_config, 
    data_config,
    inference_config
)

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('training.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class MusicInstructorDataset:
    """Dataset handler for music instruction fine-tuning"""
    
    def __init__(self, config: Any):
        self.config = config
        self.tokenizer = None
        
    def load_dataset(self) -> DatasetDict:
        """Load and prepare the music theory dataset"""
        logger.info(f"Loading dataset from {self.config.dataset_path}")
        
        # Load JSON data
        with open(self.config.dataset_path, 'r') as f:
            data = json.load(f)
        
        # Convert to DataFrame for easier manipulation
        df = pd.DataFrame(data)
        
        # Create formatted training text
        df['text'] = df.apply(self._format_instruction, axis=1)
        
        # Split the data
        train_df, temp_df = train_test_split(
            df, 
            test_size=(1 - self.config.train_split), 
            random_state=self.config.shuffle_seed
        )
        
        val_size = self.config.val_split / (self.config.val_split + self.config.test_split)
        val_df, test_df = train_test_split(
            temp_df, 
            test_size=(1 - val_size), 
            random_state=self.config.shuffle_seed
        )
        
        # Create datasets
        train_dataset = Dataset.from_pandas(train_df)
        val_dataset = Dataset.from_pandas(val_df)
        test_dataset = Dataset.from_pandas(test_df)
        
        dataset_dict = DatasetDict({
            'train': train_dataset,
            'validation': val_dataset,
            'test': test_dataset
        })
        
        logger.info(f"Dataset splits - Train: {len(train_dataset)}, Val: {len(val_dataset)}, Test: {len(test_dataset)}")
        
        return dataset_dict
    
    def _format_instruction(self, row) -> str:
        """Format instruction data for training"""
        instruction = row['instruction']
        output = row['output']
        
        # Add system prompt and format
        formatted_text = f"{self.config.system_prompt}\n\n{self.config.instruction_template.format(instruction=instruction, output=output)}"
        
        return formatted_text
    
    def tokenize_dataset(self, dataset: DatasetDict, tokenizer: AutoTokenizer) -> DatasetDict:
        """Tokenize the dataset"""
        self.tokenizer = tokenizer
        
        def tokenize_function(examples):
            # Tokenize the text
            tokenized = tokenizer(
                examples['text'],
                truncation=True,
                padding=False,
                max_length=self.config.max_seq_length,
                return_tensors=None
            )
            
            # For causal LM, labels are the same as input_ids
            tokenized['labels'] = tokenized['input_ids'].copy()
            
            return tokenized
        
        # Tokenize all splits
        tokenized_dataset = dataset.map(
            tokenize_function,
            batched=True,
            remove_columns=dataset['train'].column_names,
            desc="Tokenizing dataset"
        )
        
        return tokenized_dataset

class MusicInstructorTrainer:
    """Trainer class for music instruction fine-tuning"""
    
    def __init__(self):
        self.model = None
        self.tokenizer = None
        self.trainer = None
        
    def setup_model_and_tokenizer(self):
        """Initialize model and tokenizer"""
        logger.info(f"Loading model: {model_config.model_name}")
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_config.model_name,
            cache_dir=model_config.cache_dir,
            trust_remote_code=model_config.trust_remote_code
        )
        
        # Add padding token if not present
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
            
        # Load model
        self.model = AutoModelForCausalLM.from_pretrained(
            model_config.model_name,
            cache_dir=model_config.cache_dir,
            torch_dtype=getattr(torch, model_config.torch_dtype),
            device_map=model_config.device_map,
            trust_remote_code=model_config.trust_remote_code
        )
        
        # Prepare model for training
        self.model = prepare_model_for_kbit_training(self.model)
        
        # Configure LoRA
        peft_config = LoraConfig(
            r=lora_config.r,
            lora_alpha=lora_config.lora_alpha,
            target_modules=lora_config.target_modules,
            lora_dropout=lora_config.lora_dropout,
            bias=lora_config.bias,
            task_type=TaskType.CAUSAL_LM
        )
        
        # Apply LoRA
        self.model = get_peft_model(self.model, peft_config)
        
        logger.info("Model and tokenizer setup complete")
        logger.info(f"Trainable parameters: {self.model.get_nb_trainable_parameters()}")
        
    def train(self, tokenized_dataset: DatasetDict):
        """Train the model"""
        logger.info("Starting training...")
        
        # Setup training arguments
        training_args = TrainingArguments(
            output_dir=training_config.output_dir,
            per_device_train_batch_size=training_config.per_device_train_batch_size,
            per_device_eval_batch_size=training_config.per_device_eval_batch_size,
            gradient_accumulation_steps=training_config.gradient_accumulation_steps,
            learning_rate=training_config.learning_rate,
            max_steps=training_config.max_steps,
            warmup_steps=training_config.warmup_steps,
            logging_steps=training_config.logging_steps,
            evaluation_strategy=training_config.evaluation_strategy,
            eval_steps=training_config.eval_steps,
            save_steps=training_config.save_steps,
            save_total_limit=training_config.save_total_limit,
            load_best_model_at_end=training_config.load_best_model_at_end,
            metric_for_best_model=training_config.metric_for_best_model,
            greater_is_better=training_config.greater_is_better,
            report_to=training_config.report_to,
            run_name=training_config.run_name,
            seed=training_config.seed,
            data_seed=training_config.data_seed,
            remove_unused_columns=training_config.remove_unused_columns,
            dataloader_pin_memory=training_config.dataloader_pin_memory,
            gradient_checkpointing=training_config.gradient_checkpointing,
            fp16=training_config.fp16,
            bf16=training_config.bf16,
            max_grad_norm=training_config.max_grad_norm,
            weight_decay=training_config.weight_decay,
            adam_beta1=training_config.adam_beta1,
            adam_beta2=training_config.adam_beta2,
            adam_epsilon=training_config.adam_epsilon,
            lr_scheduler_type=training_config.lr_scheduler_type,
        )
        
        # Data collator
        data_collator = DataCollatorForLanguageModeling(
            tokenizer=self.tokenizer,
            mlm=False,  # We're doing causal LM, not masked LM
            pad_to_multiple_of=8
        )
        
        # Initialize trainer
        self.trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=tokenized_dataset['train'],
            eval_dataset=tokenized_dataset['validation'],
            data_collator=data_collator,
            tokenizer=self.tokenizer
        )
        
        # Start training
        self.trainer.train()
        
        # Save the final model
        self.trainer.save_model()
        if self.tokenizer is not None:
            self.tokenizer.save_pretrained(training_config.output_dir)
        
        logger.info("Training completed!")
        
    def evaluate(self, tokenized_dataset: DatasetDict):
        """Evaluate the model"""
        if self.trainer is None:
            logger.error("Model not trained yet. Please run train() first.")
            return
            
        logger.info("Evaluating model...")
        
        # Evaluate on test set
        eval_results = self.trainer.evaluate(tokenized_dataset['test'])
        
        logger.info(f"Test Results: {eval_results}")
        
        # Save evaluation results
        with open(os.path.join(training_config.output_dir, 'eval_results.json'), 'w') as f:
            json.dump(eval_results, f, indent=2)
        
        return eval_results

def main():
    """Main training function"""
    # Set random seed
    set_seed(training_config.seed)
    
    # Initialize wandb if configured
    if training_config.report_to == "wandb":
        wandb.init(
            project="tinyllama-music-instructor",
            name=training_config.run_name,
            config={
                "model": model_config.__dict__,
                "lora": lora_config.__dict__,
                "training": training_config.__dict__,
                "data": data_config.__dict__
            }
        )
    
    # Create output directory
    Path(training_config.output_dir).mkdir(parents=True, exist_ok=True)
    
    # Initialize dataset handler
    dataset_handler = MusicInstructorDataset(data_config)
    
    # Load and prepare dataset
    dataset = dataset_handler.load_dataset()
    
    # Initialize trainer
    trainer = MusicInstructorTrainer()
    trainer.setup_model_and_tokenizer()
    
    # Tokenize dataset
    tokenized_dataset = dataset_handler.tokenize_dataset(dataset, trainer.tokenizer)
    
    # Train model
    trainer.train(tokenized_dataset)
    
    # Evaluate model
    trainer.evaluate(tokenized_dataset)
    
    # Save configuration
    config_dict = {
        "model_config": model_config.__dict__,
        "lora_config": lora_config.__dict__,
        "training_config": training_config.__dict__,
        "data_config": data_config.__dict__,
        "inference_config": inference_config.__dict__
    }
    
    with open(os.path.join(training_config.output_dir, 'training_config.json'), 'w') as f:
        json.dump(config_dict, f, indent=2)
    
    logger.info("Training pipeline completed successfully!")
    
    if training_config.report_to == "wandb":
        wandb.finish()

if __name__ == "__main__":
    main() 