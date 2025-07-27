#!/usr/bin/env python3
"""
Music Tutor using Qwen2-Audio - Four-Pillar Music Knowledge System
Enhanced with comprehensive four-pillar knowledge integration:
1. Nashville Numbers - Practical chord notation and transposition
2. Slakh Dataset - Professional instrument and production knowledge  
3. Music Theory - Complete educational curriculum from musictheory.net
4. Professional Performance - Advanced performance, ear training, and live techniques

Now powered by Qwen2-Audio for native audio input/output capabilities!
"""

import sys
import argparse
import re
import os
import time
import torch
import librosa
import numpy as np
from typing import Generator, Optional, List, Dict, Any
from io import BytesIO
import soundfile as sf
import tempfile

# Qwen2-Audio imports
try:
    from transformers import Qwen2AudioForConditionalGeneration, AutoProcessor
    import transformers
    QWEN_AVAILABLE = True
except ImportError:
    QWEN_AVAILABLE = False
    print("Warning: Qwen2-Audio not available. Install with: pip install transformers librosa soundfile")

# Import enhanced Slakh instrument data and music theory knowledge
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

class MusicTutorRunner:
    def __init__(self, model_name: str = "Qwen/Qwen2-Audio-7B-Instruct", 
                 device: str = "auto", temperature: float = 0.7, max_tokens: int = 800, concise: bool = False,
                 single_mode: bool = False, context_limit: int = 6, music_only: bool = True,
                 audio_output_dir: str = "audio_output", save_audio: bool = False,
                 audio_input_sampling_rate: int = 16000):
        
        # Qwen2-Audio Configuration
        self.model_name = model_name
        self.device = device
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.concise = concise
        self.single_mode = single_mode
        self.context_limit = context_limit
        self.music_only = music_only
        self.audio_output_dir = audio_output_dir
        self.save_audio = save_audio
        self.audio_input_sampling_rate = audio_input_sampling_rate
        
        # Initialize Qwen2-Audio model
        self.processor = None
        self.model = None
        if QWEN_AVAILABLE:
            self._initialize_qwen_model()
        
        # Create audio output directory
        if not os.path.exists(self.audio_output_dir):
            os.makedirs(self.audio_output_dir)
            print(f"📁 Created audio output directory: {self.audio_output_dir}")
        
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
    
    def _initialize_qwen_model(self):
        """Initialize Qwen2-Audio model and processor"""
        try:
            print(f"🔄 Loading Qwen2-Audio model: {self.model_name}")
            print("📦 This may take a few minutes on first run...")
            
            # Load processor
            self.processor = AutoProcessor.from_pretrained(self.model_name)
            
            # Load model with device mapping
            if self.device == "auto":
                device_map = "auto"
            else:
                device_map = None
                
            self.model = Qwen2AudioForConditionalGeneration.from_pretrained(
                self.model_name,
                device_map=device_map,
                torch_dtype=torch.bfloat16,
                attn_implementation="flash_attention_2" if torch.cuda.is_available() else None
            )
            
            if device_map is None:
                self.model.to(self.device)
            
            print("✅ Qwen2-Audio model loaded successfully!")
            print(f"🎯 Device: {next(self.model.parameters()).device}")
            
        except Exception as e:
            print(f"❌ Failed to load Qwen2-Audio model: {str(e)}")
            print("💡 Make sure you have sufficient GPU memory (recommended: 16GB+ VRAM)")
            self.processor = None
            self.model = None
    
    def load_audio_file(self, audio_path: str) -> Optional[np.ndarray]:
        """Load audio file and resample to required sample rate"""
        try:
            audio_data, sample_rate = librosa.load(audio_path, sr=self.audio_input_sampling_rate)
            return audio_data
        except Exception as e:
            print(f"❌ Error loading audio file {audio_path}: {str(e)}")
            return None
    
    def save_audio_response(self, audio_data: np.ndarray, filename_prefix: str = "response") -> Optional[str]:
        """Save audio response to file"""
        try:
            timestamp = int(time.time())
            filename = f"{filename_prefix}_{timestamp}.wav"
            filepath = os.path.join(self.audio_output_dir, filename)
            
            # Save audio using soundfile
            sf.write(filepath, audio_data, self.audio_input_sampling_rate)
            
            if os.path.exists(filepath):
                return filepath
            return None
            
        except Exception as e:
            print(f"❌ Audio file save failed: {str(e)}")
            return None
    
    def get_knowledge_status(self) -> dict:
        """Get status of all four-pillar knowledge systems"""
        status = {
            "nashville_numbers": True,  # Always available
            "slakh_professional": SLAKH_AVAILABLE,
            "music_theory": THEORY_AVAILABLE,
            "professional_performance": PERFORMANCE_AVAILABLE,
            "qwen_audio": QWEN_AVAILABLE and self.model is not None,
            "total_keywords": len(self.music_keywords) if hasattr(self, 'music_keywords') else 0
        }
        
        if SLAKH_AVAILABLE:
            status["slakh_instruments"] = len(SLAKH_INSTRUMENT_CLASSES)
            status["midi_programs"] = len(MIDI_TO_SLAKH_CLASS)
        
        if THEORY_AVAILABLE:
            status["theory_sections"] = len(MUSICTHEORY_NET_CURRICULUM)
            status["chord_types"] = len(CHORD_CONSTRUCTION["triads"]) + len(CHORD_CONSTRUCTION["seventh_chords"])
        
        if PERFORMANCE_AVAILABLE:
            status["performance_sections"] = len(PROFESSIONAL_PERFORMANCE_KNOWLEDGE)
            status["performance_categories"] = sum(len(section["concepts"]) for section in PROFESSIONAL_PERFORMANCE_KNOWLEDGE.values())
        
        return status
    
    def enrich_context_with_knowledge(self, user_input: str) -> str:
        """Enrich user input with relevant knowledge context"""
        context_additions = []
        
        # Add relevant Slakh instrument context
        if SLAKH_AVAILABLE:
            # Check for MIDI program mentions
            for program_num in range(128):
                if str(program_num) in user_input:
                    instrument_class = get_instrument_class(program_num)
                    if instrument_class:
                        context_additions.append(f"MIDI {program_num} maps to {instrument_class}")
            
            # Check for instrument mentions
            for instrument_name in SLAKH_INSTRUMENT_CLASSES.keys():
                if instrument_name.lower() in user_input.lower():
                    info = get_instrument_info(instrument_name)
                    if info:
                        context_additions.append(f"{instrument_name}: {info.get('description', '')}")
        
        # Add relevant music theory context
        if THEORY_AVAILABLE:
            # Check for theory concepts
            concept_found = get_theory_explanation(user_input)
            if concept_found:
                context_additions.append(f"Theory context: {concept_found['explanation']}")
        
        # Add relevant professional performance context
        if PERFORMANCE_AVAILABLE:
            # Check for performance concepts
            performance_concept = get_performance_concept_info(user_input)
            if performance_concept:
                context_additions.append(f"Performance context: {performance_concept['description']}")
        
        if context_additions:
            return f"{user_input}\n\nRelevant context: {' | '.join(context_additions[:3])}"  # Limit to avoid overwhelming
        
        return user_input
    
    def get_comprehensive_capabilities(self) -> str:
        """Get a description of four-pillar comprehensive capabilities"""
        capabilities = ["Nashville numbers and chord progressions"]
        
        if SLAKH_AVAILABLE:
            capabilities.append("34 professional instrument classes with MIDI mappings")
            capabilities.append("advanced synthesis and production techniques")
        
        if THEORY_AVAILABLE:
            capabilities.append("complete music theory curriculum")
            capabilities.append("harmonic analysis and voice leading")
            capabilities.append("notation, rhythm, scales, and intervals")
        
        if PERFORMANCE_AVAILABLE:
            capabilities.append("professional performance and ear training")
            capabilities.append("advanced chord voicings and live techniques")
            capabilities.append("studio communication and arrangement skills")
        
        return ", ".join(capabilities)
        
    def check_model_status(self) -> bool:
        """Check if Qwen2-Audio model is loaded and ready"""
        return QWEN_AVAILABLE and self.model is not None and self.processor is not None
    
    def generate_response(self, prompt: str = None, audio_path: str = None, 
                         stream: bool = False, output_audio: bool = True) -> Dict[str, Any]:
        """Generate response from Qwen2-Audio with comprehensive knowledge integration"""
        if not self.check_model_status():
            return {
                "text": "Error: Qwen2-Audio model not available or not loaded properly",
                "audio": None,
                "audio_path": None
            }
        
        # Prepare conversation
        conversation = []
        
        # Check if question is music-related (for text inputs)
        if prompt and not self.is_music_related(prompt):
            capabilities = self.get_comprehensive_capabilities()
            response_text = f"I'm sorry, I can only explain music-related questions or concepts. I specialize in {capabilities}. Please ask me about music theory, Nashville numbers, chord progressions, instruments, or other musical topics!"
            return {
                "text": response_text,
                "audio": None,
                "audio_path": None
            }
        
        # Build conversation based on inputs
        user_content = []
        
        if audio_path:
            # Load and validate audio
            audio_data = self.load_audio_file(audio_path)
            if audio_data is None:
                return {
                    "text": "Error: Could not load audio file",
                    "audio": None,
                    "audio_path": None
                }
            user_content.append({"type": "audio", "audio": audio_data})
        
        if prompt:
            # Enrich the prompt with relevant knowledge context
            enriched_prompt = self.enrich_context_with_knowledge(prompt)
            user_content.append({"type": "text", "text": enriched_prompt})
        
        if not user_content:
            return {
                "text": "Error: No input provided (need either text prompt or audio)",
                "audio": None,
                "audio_path": None
            }
        
        conversation.append({"role": "user", "content": user_content})
        
        # Build comprehensive system prompt
        capability_desc = self.get_comprehensive_capabilities()
        
        if self.concise:
            system_content = f"You are a comprehensive music expert with knowledge of {capability_desc}. Give very brief, direct answers about music. Connect concepts across Nashville numbers, professional instruments, and music theory when relevant."
        else:
            system_content = f"You are a comprehensive music expert with knowledge of {capability_desc}. Answer concisely and accurately about music theory, instruments, and musical concepts. Connect concepts across Nashville numbers, professional instruments, and music theory when relevant. If you don't know something, say so. Keep responses educational and practical."
        
        # Add system message
        conversation.insert(0, {"role": "system", "content": system_content})
        
        try:
            # Apply chat template
            text = self.processor.apply_chat_template(conversation, add_generation_prompt=True, tokenize=False)
            
            # Prepare audio inputs
            audios = []
            for message in conversation:
                if isinstance(message["content"], list):
                    for ele in message["content"]:
                        if ele.get("type") == "audio" and "audio" in ele:
                            audios.append(ele["audio"])
            
            # Process inputs
            inputs = self.processor(text=text, audios=audios if audios else None, return_tensors="pt", padding=True)
            
            # Move inputs to device
            device = next(self.model.parameters()).device
            inputs.input_ids = inputs.input_ids.to(device)
            if hasattr(inputs, 'attention_mask'):
                inputs.attention_mask = inputs.attention_mask.to(device)
            if hasattr(inputs, 'audio_input_ids'):
                inputs.audio_input_ids = inputs.audio_input_ids.to(device)
            
            # Generate response
            with torch.no_grad():
                generate_ids = self.model.generate(
                    **inputs, 
                    max_new_tokens=self.max_tokens,
                    do_sample=True,
                    temperature=self.temperature,
                    top_p=0.9,
                    pad_token_id=self.processor.tokenizer.eos_token_id
                )
            
            # Decode response
            generate_ids = generate_ids[:, inputs.input_ids.size(1):]
            response_text = self.processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
            
            # Prepare return value
            result = {
                "text": response_text,
                "audio": None,
                "audio_path": None
            }
            
            # Note: Qwen2-Audio primarily generates text responses
            # For audio output, you would need Qwen2.5-Omni which has audio generation capabilities
            # For now, we'll return text responses only
            
            return result
            
        except Exception as e:
            error_msg = f"Error generating response: {str(e)}"
            return {
                "text": error_msg,
                "audio": None,
                "audio_path": None
            }
    
    def chat_response(self, messages: list, stream: bool = False) -> Dict[str, Any]:
        """Generate chat response from Qwen2-Audio with comprehensive knowledge integration"""
        if not self.check_model_status():
            return {
                "text": "Error: Qwen2-Audio model not available or not loaded properly",
                "audio": None,
                "audio_path": None
            }
            
        # Check if the latest user message is music-related
        user_messages = [msg for msg in messages if msg.get("role") == "user"]
        if user_messages:
            latest_content = user_messages[-1].get("content", "")
            # Extract text from content if it's a list
            if isinstance(latest_content, list):
                text_parts = [item.get("text", "") for item in latest_content if item.get("type") == "text"]
                latest_text = " ".join(text_parts)
            else:
                latest_text = latest_content
            
            if latest_text and not self.is_music_related(latest_text):
                capabilities = self.get_comprehensive_capabilities()
                response_text = f"I'm sorry, I can only explain music-related questions or concepts. I specialize in {capabilities}. Please ask me about music theory, Nashville numbers, chord progressions, instruments, or other musical topics!"
                return {
                    "text": response_text,
                    "audio": None,
                    "audio_path": None
                }
        
        # Build comprehensive system prompt
        capability_desc = self.get_comprehensive_capabilities()
        knowledge_status = self.get_knowledge_status()
        
        knowledge_details = []
        if knowledge_status["slakh_professional"]:
            knowledge_details.append(f"{knowledge_status.get('slakh_instruments', 34)} professional instrument classes with MIDI mappings")
        if knowledge_status["music_theory"]:
            knowledge_details.append(f"complete music theory curriculum with {knowledge_status.get('theory_sections', 8)} major sections")
        
        expertise_desc = f"You specialize in {capability_desc}"
        if knowledge_details:
            expertise_desc += f" including {', '.join(knowledge_details)}"
            
        if self.concise:
            system_content = f"You are a comprehensive music expert assistant. {expertise_desc}. Give very brief, direct answers about music topics only. Connect concepts across Nashville numbers, professional instruments, and music theory when relevant."
        else:
            system_content = f"You are a comprehensive music expert assistant. {expertise_desc}. Give concise, accurate answers about music topics. Connect concepts across Nashville numbers, professional instruments, and music theory when relevant. If you don't know something about music, say so. Keep responses educational and practical."
        
        # Insert system prompt if not already present
        if not messages or messages[0].get("role") != "system":
            messages = [{"role": "system", "content": system_content}] + messages
        
        try:
            # Apply chat template
            text = self.processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
            
            # Prepare audio inputs
            audios = []
            for message in messages:
                if isinstance(message.get("content"), list):
                    for ele in message["content"]:
                        if ele.get("type") == "audio" and "audio" in ele:
                            audios.append(ele["audio"])
            
            # Process inputs
            inputs = self.processor(text=text, audios=audios if audios else None, return_tensors="pt", padding=True)
            
            # Move inputs to device
            device = next(self.model.parameters()).device
            inputs.input_ids = inputs.input_ids.to(device)
            if hasattr(inputs, 'attention_mask'):
                inputs.attention_mask = inputs.attention_mask.to(device)
            if hasattr(inputs, 'audio_input_ids'):
                inputs.audio_input_ids = inputs.audio_input_ids.to(device)
            
            # Generate response
            with torch.no_grad():
                generate_ids = self.model.generate(
                    **inputs,
                    max_new_tokens=self.max_tokens,
                    do_sample=True,
                    temperature=self.temperature,
                    top_p=0.9,
                    pad_token_id=self.processor.tokenizer.eos_token_id
                )
            
            # Decode response
            generate_ids = generate_ids[:, inputs.input_ids.size(1):]
            response_text = self.processor.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
            
            return {
                "text": response_text,
                "audio": None,
                "audio_path": None
            }
            
        except Exception as e:
            error_msg = f"Error generating chat response: {str(e)}"
            return {
                "text": error_msg,
                "audio": None,
                "audio_path": None
            }
    
    def interactive_mode(self):
        """Run in interactive chat mode"""
        print("🎵 Qwen2-Audio Music Tutor Interactive Mode - Comprehensive Music Expert")
        print("-" * 70)
        
        # Show knowledge system status
        knowledge_status = self.get_knowledge_status()
        print("📚 Four-Pillar Knowledge Systems Available:")
        print(f"  🎯 Nashville Numbers: ✅ Always available")
        print(f"  🎛️ Slakh Professional: {'✅' if knowledge_status['slakh_professional'] else '❌'} {'(' + str(knowledge_status.get('slakh_instruments', 0)) + ' instruments)' if knowledge_status['slakh_professional'] else ''}")
        print(f"  📖 Music Theory: {'✅' if knowledge_status['music_theory'] else '❌'} {'(' + str(knowledge_status.get('theory_sections', 0)) + ' sections)' if knowledge_status['music_theory'] else ''}")
        print(f"  🎸 Professional Performance: {'✅' if knowledge_status['professional_performance'] else '❌'} {'(' + str(knowledge_status.get('performance_sections', 0)) + ' areas)' if knowledge_status['professional_performance'] else ''}")
        print(f"  🔊 Qwen2-Audio: {'✅ Ready' if knowledge_status.get('qwen_audio', False) else '❌ Not Available'}")
        print(f"  📊 Total Keywords: {knowledge_status['total_keywords']}")
        print(f"  💾 Audio Output: {'✅ Enabled' if self.save_audio else '❌ Disabled'}")
        if self.save_audio:
            print(f"      Directory: {self.audio_output_dir}")
        print()
        
        # Show capabilities
        capabilities = self.get_comprehensive_capabilities()
        print(f"🎵 I specialize in: {capabilities}")
        print()
        
        print("💬 Commands:")
        print("  Type 'quit', 'exit', or 'bye' to exit")
        print("  Type 'clear' to clear conversation history")
        print("  Type 'single' to toggle single-question mode (no context)")
        print("  Type 'context' to toggle context mode (maintains conversation)")
        print("  Type 'audio <path>' to include audio file in your message")
        print("  Type 'status' to show knowledge system status")
        if self.music_only:
            print("🎵 Music-only mode: I can only answer music-related questions")
        else:
            print("🌍 All-topics mode: I can answer any question")
        print("-" * 70)
        
        conversation_history = []
        single_question_mode = self.single_mode
        max_history_length = self.context_limit
        
        print(f"💬 Mode: {'Single Question' if single_question_mode else 'Conversational'}")
        if single_question_mode:
            print("💡 Each question is treated independently - no context from previous questions")
        
        while True:
            try:
                user_input = input("\n🔹 You: ").strip()
                
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("👋 Goodbye!")
                    break
                    
                if user_input.lower() == 'clear':
                    conversation_history = []
                    print("🧹 Conversation history cleared!")
                    continue
                    
                if user_input.lower() == 'single':
                    single_question_mode = True
                    conversation_history = []
                    print("🔀 Switched to single-question mode (no context carried over)")
                    continue
                    
                if user_input.lower() == 'context':
                    single_question_mode = False
                    print("🔀 Switched to conversational mode (context maintained)")
                    continue
                
                if user_input.lower() == 'status':
                    knowledge_status = self.get_knowledge_status()
                    capabilities = self.get_comprehensive_capabilities()
                    print("\n📊 Current Four-Pillar Knowledge System Status:")
                    print(f"  🎯 Nashville Numbers: ✅ Always available")
                    print(f"  🎛️ Slakh Professional: {'✅' if knowledge_status['slakh_professional'] else '❌'}")
                    if knowledge_status['slakh_professional']:
                        print(f"      - Instruments: {knowledge_status.get('slakh_instruments', 0)}")
                        print(f"      - MIDI Programs: {knowledge_status.get('midi_programs', 0)}")
                    print(f"  📖 Music Theory: {'✅' if knowledge_status['music_theory'] else '❌'}")
                    if knowledge_status['music_theory']:
                        print(f"      - Theory Sections: {knowledge_status.get('theory_sections', 0)}")
                        print(f"      - Chord Types: {knowledge_status.get('chord_types', 0)}")
                    print(f"  🎸 Professional Performance: {'✅' if knowledge_status['professional_performance'] else '❌'}")
                    if knowledge_status['professional_performance']:
                        print(f"      - Performance Sections: {knowledge_status.get('performance_sections', 0)}")
                        print(f"      - Performance Categories: {knowledge_status.get('performance_categories', 0)}")
                    print(f"  📊 Total Keywords: {knowledge_status['total_keywords']}")
                    print(f"  🎵 Capabilities: {capabilities}")
                    continue
                    
                if not user_input:
                    continue
                
                # Check for audio file input
                audio_path = None
                if user_input.lower().startswith('audio '):
                    parts = user_input.split(' ', 1)
                    if len(parts) > 1:
                        audio_path = parts[1].strip()
                        user_input = input("🔹 Text (optional): ").strip()
                        if not user_input and not audio_path:
                            continue
                
                # Prepare message content
                user_content = []
                if audio_path:
                    # Load audio
                    audio_data = self.load_audio_file(audio_path)
                    if audio_data is not None:
                        user_content.append({"type": "audio", "audio": audio_data})
                        print(f"🎵 Audio loaded: {audio_path}")
                    else:
                        print(f"❌ Could not load audio file: {audio_path}")
                        continue
                
                if user_input:
                    user_content.append({"type": "text", "text": user_input})
                
                if not user_content:
                    continue
                
                # Prepare messages for this interaction
                if single_question_mode:
                    # Single question mode - no conversation history
                    current_messages = [{"role": "user", "content": user_content}]
                else:
                    # Conversational mode - add to history and manage length
                    conversation_history.append({"role": "user", "content": user_content})
                    
                    # Limit conversation history to prevent excessive context
                    if len(conversation_history) > max_history_length:
                        # Keep system message (if any) and recent exchanges
                        system_messages = [msg for msg in conversation_history if msg.get("role") == "system"]
                        recent_messages = conversation_history[-max_history_length:]
                        conversation_history = system_messages + recent_messages
                    
                    current_messages = conversation_history.copy()
                
                print("🤖 Qwen Music Tutor: ", end="", flush=True)
                
                # Generate response
                result = self.chat_response(current_messages)
                
                if result["text"] and not result["text"].startswith("Error:"):
                    print(result["text"])
                    
                    if not single_question_mode:
                        # Add assistant response to history only in conversational mode
                        conversation_history.append({"role": "assistant", "content": result["text"]})
                    
                    # Save audio if generated
                    if result["audio"] is not None and self.save_audio:
                        audio_path = self.save_audio_response(result["audio"])
                        if audio_path:
                            print(f"💾 Audio saved: {audio_path}")
                    
                elif result["text"].startswith("Error:"):
                    print(f"\n❌ {result['text']}")
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Music Tutor using Qwen2-Audio")
    parser.add_argument("--prompt", "-p", type=str, help="Single text prompt to send to the music tutor")
    parser.add_argument("--audio", "-a", type=str, help="Audio file path for audio input")
    parser.add_argument("--model", "-m", type=str, default="Qwen/Qwen2-Audio-7B-Instruct", help="Qwen2-Audio model name")
    parser.add_argument("--device", "-d", type=str, default="auto", help="Device for model (auto, cuda, cpu)")
    parser.add_argument("--interactive", "-i", action="store_true", help="Run in interactive mode")
    parser.add_argument("--temperature", "-t", type=float, default=0.7, help="Temperature for response generation (0.0-1.0, default: 0.7)")
    parser.add_argument("--max-tokens", type=int, default=800, help="Maximum number of tokens to generate (default: 800)")
    parser.add_argument("--concise", action="store_true", help="Force very concise responses")
    parser.add_argument("--single-mode", action="store_true", help="Start in single-question mode (no conversation context)")
    parser.add_argument("--context-limit", type=int, default=6, help="Maximum conversation history length (default: 6)")
    parser.add_argument("--allow-all-topics", action="store_true", help="Allow non-music questions (default: music-only mode)")
    parser.add_argument("--audio-output-dir", type=str, default="audio_output", help="Directory for audio output files (default: audio_output)")
    parser.add_argument("--save-audio", action="store_true", help="Save audio responses to files")
    parser.add_argument("--audio-sampling-rate", type=int, default=16000, help="Audio input sampling rate (default: 16000)")
    
    args = parser.parse_args()
    
    # Initialize runner
    runner = MusicTutorRunner(
        model_name=args.model,
        device=args.device,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        concise=args.concise,
        single_mode=args.single_mode,
        context_limit=args.context_limit,
        music_only=not args.allow_all_topics,
        audio_output_dir=args.audio_output_dir,
        save_audio=args.save_audio,
        audio_input_sampling_rate=args.audio_sampling_rate
    )
    
    # Check model status
    print("🔍 Checking Qwen2-Audio model status...")
    if not runner.check_model_status():
        print("❌ Error: Qwen2-Audio model not loaded properly.")
        print("   Make sure you have:")
        print("   1. Sufficient GPU memory (recommended: 16GB+ VRAM)")
        print("   2. Installed required packages: pip install transformers librosa soundfile torch")
        print("   3. Internet connection for model download (first run)")
        sys.exit(1)
    
    print("✅ Qwen2-Audio model ready!")
    
    # Show four-pillar knowledge system status
    knowledge_status = runner.get_knowledge_status()
    print(f"\n📚 Four-Pillar Knowledge System Loaded:")
    print(f"  🎯 Nashville Numbers: ✅")
    print(f"  🎛️ Slakh Professional: {'✅' if knowledge_status['slakh_professional'] else '❌'} {'(' + str(knowledge_status.get('slakh_instruments', 0)) + ' instruments)' if knowledge_status['slakh_professional'] else ''}")
    print(f"  📖 Music Theory: {'✅' if knowledge_status['music_theory'] else '❌'} {'(' + str(knowledge_status.get('theory_sections', 0)) + ' sections)' if knowledge_status['music_theory'] else ''}")
    print(f"  🎸 Professional Performance: {'✅' if knowledge_status['professional_performance'] else '❌'} {'(' + str(knowledge_status.get('performance_sections', 0)) + ' areas)' if knowledge_status['professional_performance'] else ''}")
    print(f"  🔊 Qwen2-Audio: {'✅ Ready' if knowledge_status.get('qwen_audio', False) else '❌ Not Available'}")
    print(f"  📊 Total Keywords: {knowledge_status['total_keywords']}")
    print(f"  💾 Audio Output: {'✅ Enabled' if runner.save_audio else '❌ Disabled'}")
    if runner.save_audio:
        print(f"      Directory: {runner.audio_output_dir}")
    
    # Calculate enhancement factor
    base_keywords = 25  # Original Nashville numbers keywords
    if knowledge_status['total_keywords'] > base_keywords:
        enhancement_factor = knowledge_status['total_keywords'] / base_keywords
        print(f"  🚀 Enhancement: {enhancement_factor:.1f}x knowledge expansion!")
    print()
    
    # Run based on arguments
    if args.interactive or (not args.prompt and not args.audio):
        runner.interactive_mode()
    elif args.prompt or args.audio:
        print(f"🔹 Processing request...")
        if args.prompt:
            print(f"   Text: {args.prompt}")
        if args.audio:
            print(f"   Audio: {args.audio}")
        
        print("🤖 Qwen Music Tutor: ")
        
        result = runner.generate_response(
            prompt=args.prompt,
            audio_path=args.audio,
            output_audio=True
        )
        
        if result["text"] and not result["text"].startswith("Error:"):
            print(result["text"])
            
            # Save audio if generated
            if result["audio"] is not None and args.save_audio:
                audio_path = runner.save_audio_response(result["audio"])
                if audio_path:
                    print(f"\n💾 Audio saved: {audio_path}")
                    
        elif result["text"].startswith("Error:"):
            print(f"❌ {result['text']}")

if __name__ == "__main__":
    main() 