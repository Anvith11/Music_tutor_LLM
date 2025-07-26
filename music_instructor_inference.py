#!/usr/bin/env python3
"""
Music Instructor Inference Script
Load and test the fine-tuned TinyLlama music instructor model
"""

import os
import torch
import argparse
import json
import re
from pathlib import Path
from typing import Optional

from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import logging

from finetune_config import inference_config, data_config

# Import enhanced Slakh instrument data and comprehensive music theory
try:
    from slakh_instrument_data import (
        get_enhanced_music_keywords,
        is_professional_music_term,
        get_instrument_class,
        get_instrument_info,
        SLAKH_INSTRUMENT_CLASSES,
        MIDI_TO_SLAKH_CLASS,
        SYNTHESIS_KNOWLEDGE
    )
    SLAKH_AVAILABLE = True
except ImportError:
    SLAKH_AVAILABLE = False
    print("Warning: Slakh instrument data not available.")

# Import comprehensive music theory curriculum
try:
    from musictheory_net_data import (
        get_comprehensive_music_theory_keywords,
        is_music_theory_term,
        get_theory_explanation,
        MUSICTHEORY_NET_CURRICULUM,
        MUSIC_THEORY_TERMS,
        CIRCLE_OF_FIFTHS_DATA,
        SCALE_PATTERNS,
        CHORD_CONSTRUCTION
    )
    THEORY_AVAILABLE = True
except ImportError:
    THEORY_AVAILABLE = False
    print("Warning: Music theory curriculum data not available.")

# Import professional performance knowledge (Fourth Pillar)
try:
    from professional_performance_data import (
        get_professional_performance_keywords,
        is_professional_performance_term,
        get_performance_concept_info,
        get_related_performance_techniques,
        PROFESSIONAL_PERFORMANCE_KNOWLEDGE,
        PROFESSIONAL_PERFORMANCE_KEYWORDS,
        PERFORMANCE_METHODOLOGIES
    )
    PERFORMANCE_AVAILABLE = True
except ImportError:
    PERFORMANCE_AVAILABLE = False
    print("Warning: Professional performance data not available.")

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MusicInstructorModel:
    """Fine-tuned music instructor model for inference"""
    
    def __init__(self, model_path: str, base_model_name: str = "TinyLlama/TinyLlama-1.1B-Chat-v1.0", music_only: bool = True):
        self.model_path = model_path
        self.base_model_name = base_model_name
        self.model = None
        self.tokenizer = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.music_only = music_only
        
        # Four-pillar comprehensive music keywords system
        enhanced_keywords = set()
        
        # Add Slakh professional instrument keywords
        if SLAKH_AVAILABLE:
            enhanced_keywords.update(get_enhanced_music_keywords())
        
        # Add comprehensive music theory keywords
        if THEORY_AVAILABLE:
            enhanced_keywords.update(get_comprehensive_music_theory_keywords())
        
        # Add professional performance keywords
        if PERFORMANCE_AVAILABLE:
            enhanced_keywords.update(get_professional_performance_keywords())
        
        if enhanced_keywords:
            self.music_keywords = enhanced_keywords
        else:
            # Fallback to basic keywords if enhanced data unavailable
            self.music_keywords = {
            # Nashville Numbers
            'nashville', 'numbers', 'number system', 'chord progression', 'chord progressions',
            # Basic Music Theory
            'music', 'musical', 'theory', 'chord', 'chords', 'scale', 'scales', 'key', 'keys',
            'note', 'notes', 'interval', 'intervals', 'harmony', 'harmonic', 'melody', 'melodic',
            'rhythm', 'rhythmic', 'tempo', 'beat', 'measure', 'measures', 'bar', 'bars',
            # Chord Types
            'major', 'minor', 'diminished', 'augmented', 'suspended', 'dominant', 'seventh',
            'ninth', 'eleventh', 'thirteenth', 'add9', 'sus2', 'sus4', 'maj7', 'min7', 'm7', '7th',
            # Modes and Scales
            'ionian', 'dorian', 'phrygian', 'lydian', 'mixolydian', 'aeolian', 'locrian',
            'pentatonic', 'blues scale', 'chromatic', 'whole tone', 'natural minor', 'harmonic minor',
            'melodic minor', 'major scale', 'minor scale',
            # Instruments
            'guitar', 'piano', 'bass', 'drums', 'violin', 'cello', 'trumpet', 'saxophone',
            'keyboard', 'synth', 'organ', 'ukulele', 'mandolin', 'banjo', 'harmonica',
            # Music Styles/Genres
            'jazz', 'blues', 'rock', 'pop', 'country', 'folk', 'classical', 'latin', 'salsa',
            'bossa nova', 'funk', 'soul', 'r&b', 'gospel', 'reggae', 'metal', 'punk',
            # Musical Concepts
            'transpose', 'transposition', 'modulation', 'cadence', 'resolution', 'tension',
            'voice leading', 'inversion', 'inversions', 'roman numerals', 'function', 'functional',
            'tonic', 'subdominant', 'predominant', 'circle of fifths', 'borrowed chord', 'borrowed chords',
            'secondary dominant', 'substitution', 'tritone', 'passing chord', 'diminished passing',
            # Performance Terms
            'strum', 'strumming', 'fingerpicking', 'arpeggiate', 'arpeggio', 'glissando',
            'vibrato', 'bend', 'slide', 'hammer-on', 'pull-off', 'mute', 'palm mute',
            # Time Signatures
            '4/4', '3/4', '2/4', '6/8', '12/8', '5/4', '7/8', 'time signature', 'meter',
            # Musical Notation
            'staff', 'clef', 'treble', 'bass clef', 'sharp', 'flat', 'natural', 'accidental',
            'whole note', 'half note', 'quarter note', 'eighth note', 'sixteenth note',
            # Common Progressions
            'ii-v-i', 'ii-V-I', 'vi-IV-V-I', 'I-vi-IV-V', '12-bar blues', 'turnaround',
            # Degrees
            '1st', '2nd', '3rd', '4th', '5th', '6th', '7th', 'root', 'third', 'fifth', 'octave'
            }
        
    def is_music_related(self, text: str) -> bool:
        """Check if the input text is music-related using four-pillar comprehensive detection"""
        if not self.music_only:
            return True  # If music_only is disabled, allow all questions
        
        # Use enhanced professional instrument detection
        if SLAKH_AVAILABLE:
            if is_professional_music_term(text):
                return True
        
        # Use comprehensive music theory detection
        if THEORY_AVAILABLE:
            if is_music_theory_term(text):
                return True
        
        # Use professional performance detection
        if PERFORMANCE_AVAILABLE:
            if is_professional_performance_term(text):
                return True
            
        text_lower = text.lower()
        
        # Check for explicit music keywords
        for keyword in self.music_keywords:
            if keyword in text_lower:
                return True
        
        # Check for Nashville number patterns (numbers with 'm' or symbols)
        nashville_patterns = [
            r'\b[1-7]m?\b',  # 1, 2m, 3m, etc.
            r'\b[1-7]7\b',   # 17, 27, etc.
            r'\b[1-7]°\b',   # 1°, 7°, etc.
            r'\b[1-7]/[1-7]\b',  # 1/3, 5/7, etc.
            r'\bb[1-7]\b',   # b7, b3, etc.
            r'\b[1-7]sus[24]\b',  # 1sus4, 5sus2, etc.
        ]
        
        for pattern in nashville_patterns:
            if re.search(pattern, text_lower):
                return True
        
        # Check for chord notation patterns
        chord_patterns = [
            r'\b[A-G][#b]?m?7?9?11?13?\b',  # C, Dm, F#maj7, etc.
            r'\b[A-G][#b]?sus[24]\b',       # Csus4, F#sus2, etc.
            r'\b[A-G][#b]?dim\b',           # Cdim, F#dim, etc.
            r'\b[A-G][#b]?aug\b',           # Caug, F#aug, etc.
        ]
        
        for pattern in chord_patterns:
            if re.search(pattern, text):  # Case sensitive for chord names
                return True
        
        return False
        
    def load_model(self):
        """Load the fine-tuned model and tokenizer"""
        logger.info(f"Loading fine-tuned model from {self.model_path}")
        logger.info(f"Base model: {self.base_model_name}")
        logger.info(f"Device: {self.device}")
        
        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        
        # Load base model
        self.model = AutoModelForCausalLM.from_pretrained(
            self.base_model_name,
            torch_dtype=torch.float16 if self.device.type == "cuda" else torch.float32,
            device_map="auto" if self.device.type == "cuda" else None,
            trust_remote_code=True
        )
        
        # Load fine-tuned weights
        self.model = PeftModel.from_pretrained(self.model, self.model_path)
        
        # Move to device if not using device_map
        if self.device.type == "cpu":
            self.model = self.model.to(self.device)
        
        logger.info("Model loaded successfully!")
        
    def generate_response(self, instruction: str, max_new_tokens: Optional[int] = None) -> str:
        """Generate a response to a music theory instruction"""
        if self.model is None or self.tokenizer is None:
            raise ValueError("Model not loaded. Call load_model() first.")
        
        # Check if question is music-related
        if not self.is_music_related(instruction):
            return "I'm sorry, I can only explain music-related questions or concepts. Please ask me about music theory, Nashville numbers, chord progressions, instruments, or other musical topics!"
        
        # Format the prompt
        prompt = f"{data_config.system_prompt}\n\n### Instruction:\n{instruction}\n\n### Response:\n"
        
        # Tokenize
        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        ).to(self.device)
        
        # Generate
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens or inference_config.max_new_tokens,
                temperature=inference_config.temperature,
                top_p=inference_config.top_p,
                do_sample=inference_config.do_sample,
                pad_token_id=self.tokenizer.pad_token_id or inference_config.pad_token_id,
                eos_token_id=self.tokenizer.eos_token_id or inference_config.eos_token_id,
                repetition_penalty=inference_config.repetition_penalty,
                use_cache=True
            )
        
        # Decode response
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        
        # Extract only the generated part
        response = response[len(prompt):].strip()
        
        return response
    
    def interactive_mode(self):
        """Run interactive music instruction session"""
        print("🎵 Music Instructor - Interactive Mode")
        print("Ask me anything about music theory, Nashville numbers, chord progressions, etc.")
        print("Type 'quit', 'exit', or 'bye' to exit")
        print("Type 'help' for example questions")
        print("Type 'single' to toggle single-question mode (no context)")
        print("Type 'context' to toggle context mode (maintains conversation)")
        if self.music_only:
            print("🎵 Music-only mode: I can only answer music-related questions")
        else:
            print("🌍 All-topics mode: I can answer any question")
        print("-" * 70)
        
        conversation_history = []
        single_question_mode = True  # Default to single mode for music theory
        max_history_length = 4  # Keep last 2 exchanges for music theory
        
        print(f"💬 Mode: {'Single Question' if single_question_mode else 'Conversational'}")
        print("💡 Tip: Single mode is recommended for unrelated music theory questions")
        
        while True:
            try:
                user_input = input("\n🎼 Your question: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("👋 Keep practicing! Goodbye!")
                    break
                    
                if user_input.lower() == 'help':
                    self.show_help()
                    continue
                    
                if user_input.lower() == 'single':
                    single_question_mode = True
                    conversation_history = []
                    print("🔀 Switched to single-question mode (no context carried over)")
                    print("💡 Perfect for independent music theory questions!")
                    continue
                    
                if user_input.lower() == 'context':
                    single_question_mode = False
                    print("🔀 Switched to conversational mode (context maintained)")
                    print("💡 Good for follow-up questions on the same topic!")
                    continue
                    
                if not user_input:
                    continue
                
                print("🎵 Music Instructor: ", end="", flush=True)
                
                if single_question_mode:
                    # Single question mode - fresh context each time
                    response = self.generate_response(user_input)
                else:
                    # Conversational mode - build context-aware prompt
                    if conversation_history:
                        # Build conversation context
                        context_parts = []
                        for msg in conversation_history[-max_history_length:]:
                            if msg['role'] == 'user':
                                context_parts.append(f"Previous question: {msg['content']}")
                            else:
                                context_parts.append(f"Previous answer: {msg['content']}")
                        
                        context = "\n".join(context_parts)
                        contextual_prompt = f"Previous conversation:\n{context}\n\nCurrent question: {user_input}"
                        response = self.generate_response(contextual_prompt)
                    else:
                        response = self.generate_response(user_input)
                    
                    # Add to conversation history
                    conversation_history.append({"role": "user", "content": user_input})
                    conversation_history.append({"role": "assistant", "content": response})
                
                print(response)
                
            except KeyboardInterrupt:
                print("\n👋 Keep practicing! Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")
                logger.error(f"Error during generation: {str(e)}")
    
    def show_help(self):
        """Show example questions"""
        examples = [
            "What is the Nashville number system?",
            "Convert C-Am-F-G to Nashville numbers",
            "What are the Nashville numbers for a 12-bar blues?",
            "How do you indicate seventh chords in Nashville numbers?",
            "What is a ii-V-I progression?",
            "Explain borrowed chords in Nashville numbers",
            "What are the modes and their characteristics?",
            "How do you transpose a song using Nashville numbers?",
            "What is voice leading in chord progressions?",
            "Explain the circle of fifths"
        ]
        
        print("\n🎵 Example questions you can ask:")
        for i, example in enumerate(examples, 1):
            print(f"{i:2d}. {example}")

def test_model(model_path: str, base_model_name: str, allow_all_topics: bool = False):
    """Test the model with sample questions"""
    print("🧪 Testing the fine-tuned music instructor model...")
    
    # Load model
    instructor = MusicInstructorModel(model_path, base_model_name, music_only=not allow_all_topics)
    instructor.load_model()
    
    # Test questions
    test_questions = [
        "What is the Nashville number system?",
        "Convert the chord progression C-Am-F-G to Nashville numbers",
        "What is a ii-V-I progression in Nashville numbers?",
        "How do you indicate seventh chords in Nashville numbers?"
    ]
    
    print("\n📝 Test Results:")
    print("=" * 70)
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n{i}. Question: {question}")
        print("-" * 50)
        response = instructor.generate_response(question)
        print(f"Answer: {response}")
        print("=" * 70)

def main():
    parser = argparse.ArgumentParser(description="Music Instructor Inference")
    parser.add_argument("--model_path", "-m", type=str, default="./tinyllama_music_instructor",
                       help="Path to the fine-tuned model directory")
    parser.add_argument("--base_model", "-b", type=str, default="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
                       help="Base model name")
    parser.add_argument("--interactive", "-i", action="store_true",
                       help="Run in interactive mode")
    parser.add_argument("--test", "-t", action="store_true",
                       help="Run model tests")
    parser.add_argument("--question", "-q", type=str,
                       help="Ask a single question")
    parser.add_argument("--max_tokens", type=int, default=None,
                       help="Maximum tokens to generate")
    parser.add_argument("--allow-all-topics", action="store_true",
                       help="Allow non-music questions (default: music-only mode)")
    
    args = parser.parse_args()
    
    # Check if model directory exists
    if not os.path.exists(args.model_path):
        print(f"❌ Error: Model directory not found: {args.model_path}")
        print("Please make sure you have trained the model first using:")
        print("python3 finetune_tinyllama.py")
        return
    
    # Check if it's a valid model directory
    if not os.path.exists(os.path.join(args.model_path, "adapter_model.bin")) and \
       not os.path.exists(os.path.join(args.model_path, "adapter_model.safetensors")):
        print(f"❌ Error: No adapter model found in {args.model_path}")
        print("This doesn't appear to be a valid fine-tuned model directory.")
        return
    
    # Load model
    instructor = MusicInstructorModel(args.model_path, args.base_model, music_only=not args.allow_all_topics)
    instructor.load_model()
    
    if args.test:
        test_model(args.model_path, args.base_model, args.allow_all_topics)
    elif args.question:
        print(f"🎼 Question: {args.question}")
        print("🎵 Music Instructor: ", end="", flush=True)
        response = instructor.generate_response(args.question, args.max_tokens)
        print(response)
    elif args.interactive:
        instructor.interactive_mode()
    else:
        # Default to interactive mode
        instructor.interactive_mode()

if __name__ == "__main__":
    main() 