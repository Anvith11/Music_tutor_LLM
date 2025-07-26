#!/usr/bin/env python3
"""
Music Tutor using OpenAI - Four-Pillar Music Knowledge System
Enhanced with comprehensive four-pillar knowledge integration:
1. Nashville Numbers - Practical chord notation and transposition
2. Slakh Dataset - Professional instrument and production knowledge  
3. Music Theory - Complete educational curriculum from musictheory.net
4. Professional Performance - Advanced performance, ear training, and live techniques
"""

import sys
import argparse
import re
import os
import time
from typing import Generator, Optional

# OpenAI imports
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("Warning: openai not available. Install with: pip install openai")

# TTS imports (optional)
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("Warning: pyttsx3 not available. Install with: pip install pyttsx3")

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
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo", 
                 temperature: float = 0.7, max_tokens: int = 800, concise: bool = False,
                 single_mode: bool = False, context_limit: int = 6, music_only: bool = True,
                 enable_tts: bool = False, tts_device: str = "auto", audio_output_dir: str = "audio_output",
                 audio_prompt_path: Optional[str] = None, save_audio: bool = False):
        # OpenAI Configuration
        self.api_key = api_key or os.getenv('OPENAI_API_KEY')
        if not self.api_key and OPENAI_AVAILABLE:
            print("Warning: No OpenAI API key provided. Set OPENAI_API_KEY environment variable or pass api_key parameter.")
        
        # Initialize OpenAI client
        self.openai_client = None
        if OPENAI_AVAILABLE and self.api_key:
            self.openai_client = OpenAI(api_key=self.api_key)
        
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.concise = concise
        self.single_mode = single_mode
        self.context_limit = context_limit
        self.music_only = music_only
        
        # TTS Configuration
        self.enable_tts = enable_tts and TTS_AVAILABLE
        self.tts_device = tts_device
        self.audio_output_dir = audio_output_dir
        self.audio_prompt_path = audio_prompt_path
        self.save_audio = save_audio
        self.tts_model = None
        
        # Initialize TTS if enabled
        if self.enable_tts:
            self._initialize_tts()
        
        # Create audio output directory if TTS is enabled
        if self.enable_tts and not os.path.exists(self.audio_output_dir):
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
    
    def _initialize_tts(self):
        """Initialize the TTS engine"""
        try:
            self.tts_model = pyttsx3.init()
            
            # Configure TTS settings
            voices = self.tts_model.getProperty('voices')
            if voices:
                # Set voice if available
                if self.audio_prompt_path and self.audio_prompt_path in [voice.id for voice in voices]:
                    self.tts_model.setProperty('voice', self.audio_prompt_path)
                else:
                    # Use default voice or first available
                    self.tts_model.setProperty('voice', voices[0].id)
            
            # Set speech rate and volume
            self.tts_model.setProperty('rate', 180)  # Speed of speech
            self.tts_model.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)
            
            print("🔊 TTS initialized successfully")
        except Exception as e:
            print(f"❌ Failed to initialize TTS: {str(e)}")
            self.enable_tts = False
            self.tts_model = None
    
    def generate_speech(self, text: str, interactive: bool = True) -> bool:
        """Generate speech from text with interactive playback"""
        if not self.enable_tts or not self.tts_model:
            return False
        
        try:
            # Clean text for TTS (remove special characters that might cause issues)
            clean_text = text.replace("🎯", "").replace("📚", "").replace("🎛️", "").replace("🎸", "")
            clean_text = re.sub(r'[^\w\s\.\,\!\?\-\:]', '', clean_text).strip()
            
            if not clean_text:
                return False
            
            if interactive:
                # Interactive mode - ask user if they want to hear it
                print(f"\n🔊 Audio available for this response.")
                user_input = input("Press [ENTER] to play audio, or type 'skip' to continue: ").strip().lower()
                
                if user_input == 'skip':
                    return False
                
                # Play the audio
                print(f"🔊 Playing audio...")
                self.tts_model.say(clean_text)
                self.tts_model.runAndWait()
                print("✅ Audio playback complete.")
                
                # Optionally save to file
                if self.save_audio:
                    filepath = self.save_speech_to_file(text)
                    if filepath:
                        print(f"💾 Audio also saved to: {filepath}")
                
                return True
            else:
                # Non-interactive mode - just play it
                print(f"🔊 Playing audio...")
                self.tts_model.say(clean_text)
                self.tts_model.runAndWait()
                
                # Optionally save to file
                if self.save_audio:
                    filepath = self.save_speech_to_file(text)
                    if filepath:
                        print(f"💾 Audio also saved to: {filepath}")
                
                return True
            
        except Exception as e:
            print(f"❌ TTS playback failed: {str(e)}")
            return False
    
    def save_speech_to_file(self, text: str, filename_prefix: str = "response") -> Optional[str]:
        """Save speech to file (optional feature)"""
        if not self.enable_tts or not self.tts_model:
            return None
        
        try:
            # Clean text for TTS
            clean_text = text.replace("🎯", "").replace("📚", "").replace("🎛️", "").replace("🎸", "")
            clean_text = re.sub(r'[^\w\s\.\,\!\?\-\:]', '', clean_text).strip()
            
            if not clean_text:
                return None
            
            # Generate timestamp for unique filename
            timestamp = int(time.time())
            filename = f"{filename_prefix}_{timestamp}.wav"
            filepath = os.path.join(self.audio_output_dir, filename)
            
            # Save to file
            self.tts_model.save_to_file(clean_text, filepath)
            self.tts_model.runAndWait()
            
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
        
    def check_connection(self) -> bool:
        """Check if OpenAI API is accessible"""
        if not OPENAI_AVAILABLE:
            return False
        
        if not self.openai_client:
            return False
            
        try:
            # Test API connection with a simple request
            self.openai_client.models.list()
            return True
        except Exception as e:
            print(f"OpenAI API connection failed: {str(e)}")
            return False
    
    def check_model_exists(self) -> bool:
        """Check if the specified model is available"""
        if not OPENAI_AVAILABLE or not self.openai_client:
            return False
            
        try:
            models = self.openai_client.models.list()
            available_models = [model.id for model in models.data]
            return self.model in available_models
        except Exception as e:
            print(f"Model check failed: {str(e)}")
            # Return True for common models even if we can't check
            common_models = ["gpt-3.5-turbo", "gpt-4", "gpt-4-turbo-preview", "gpt-3.5-turbo-16k"]
            return self.model in common_models
    
    def generate_response(self, prompt: str, stream: bool = True) -> Generator[str, None, None]:
        """Generate response from OpenAI with comprehensive knowledge integration"""
        if not OPENAI_AVAILABLE or not self.openai_client:
            yield "Error: OpenAI API not available or API key not set"
            return
            
        # Check if question is music-related
        if not self.is_music_related(prompt):
            capabilities = self.get_comprehensive_capabilities()
            response_text = f"I'm sorry, I can only explain music-related questions or concepts. I specialize in {capabilities}. Please ask me about music theory, Nashville numbers, chord progressions, instruments, or other musical topics!"
            yield response_text
            
            # Generate TTS for non-music response if enabled
            if self.enable_tts:
                self.generate_speech(response_text, interactive=False)
            return
        
        # Enrich the prompt with relevant knowledge context
        enriched_prompt = self.enrich_context_with_knowledge(prompt)
        
        # Build comprehensive capability description
        capability_desc = self.get_comprehensive_capabilities()
        
        if self.concise:
            system_content = f"You are a comprehensive music expert with knowledge of {capability_desc}. Give very brief, direct answers about music. Connect concepts across Nashville numbers, professional instruments, and music theory when relevant."
            # Use smaller token limit for concise mode
            token_limit = min(self.max_tokens, 300)
        else:
            system_content = f"You are a comprehensive music expert with knowledge of {capability_desc}. Answer concisely and accurately about music theory, instruments, and musical concepts. Connect concepts across Nashville numbers, professional instruments, and music theory when relevant. If you don't know something, say so. Keep responses educational and practical."
            token_limit = self.max_tokens
        
        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": enriched_prompt}
        ]
        
        try:
            if stream:
                response = self.openai_client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=token_limit,
                    temperature=self.temperature,
                    top_p=0.9,
                    stream=True
                )
                
                full_response = ""
                for chunk in response:
                    if chunk.choices and len(chunk.choices) > 0:
                        delta = chunk.choices[0].delta
                        if delta.content:
                            content = delta.content
                            full_response += content
                            yield content
                
                # Generate TTS for the complete response if enabled
                if self.enable_tts and full_response.strip():
                    self.generate_speech(full_response, interactive=True)
            else:
                response = self.openai_client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=token_limit,
                    temperature=self.temperature,
                    top_p=0.9
                )
                
                if response.choices:
                    response_text = response.choices[0].message.content
                    yield response_text
                    
                    # Generate TTS for the complete response if enabled
                    if self.enable_tts and response_text.strip():
                        self.generate_speech(response_text, interactive=True)
                
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            yield error_msg
            if self.enable_tts:
                self.generate_speech(error_msg, interactive=False)
    
    def chat_response(self, messages: list, stream: bool = True) -> Generator[str, None, None]:
        """Generate chat response from OpenAI with comprehensive knowledge integration"""
        if not OPENAI_AVAILABLE or not self.openai_client:
            yield "Error: OpenAI API not available or API key not set"
            return
            
        # Check if the latest user message is music-related
        user_messages = [msg for msg in messages if msg.get("role") == "user"]
        if user_messages and not self.is_music_related(user_messages[-1].get("content", "")):
            capabilities = self.get_comprehensive_capabilities()
            response_text = f"I'm sorry, I can only explain music-related questions or concepts. I specialize in {capabilities}. Please ask me about music theory, Nashville numbers, chord progressions, instruments, or other musical topics!"
            yield response_text
            
            # Generate TTS for non-music response if enabled
            if self.enable_tts:
                self.generate_speech(response_text, interactive=False)
            return
        
        # Enrich the latest user message with knowledge context if available
        if user_messages:
            latest_message = user_messages[-1]
            enriched_content = self.enrich_context_with_knowledge(latest_message.get("content", ""))
            if enriched_content != latest_message.get("content", ""):
                # Update the latest message with enriched content
                for i, msg in enumerate(messages):
                    if msg.get("role") == "user" and msg.get("content") == latest_message.get("content"):
                        messages[i] = {**msg, "content": enriched_content}
                        break
        
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
            # Use smaller token limit for concise mode
            token_limit = min(self.max_tokens, 300)
        else:
            system_content = f"You are a comprehensive music expert assistant. {expertise_desc}. Give concise, accurate answers about music topics. Connect concepts across Nashville numbers, professional instruments, and music theory when relevant. If you don't know something about music, say so. Keep responses educational and practical."
            token_limit = self.max_tokens
        
        system_prompt = {
            "role": "system", 
            "content": system_content
        }
        
        # Insert system prompt if not already present
        if not messages or messages[0].get("role") != "system":
            messages = [system_prompt] + messages
        
        try:
            if stream:
                response = self.openai_client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=token_limit,
                    temperature=self.temperature,
                    top_p=0.9,
                    stream=True
                )
                
                full_response = ""
                for chunk in response:
                    if chunk.choices and len(chunk.choices) > 0:
                        delta = chunk.choices[0].delta
                        if delta.content:
                            content = delta.content
                            full_response += content
                            yield content
                
                # Generate TTS for the complete response if enabled
                if self.enable_tts and full_response.strip():
                    self.generate_speech(full_response, interactive=True)
            else:
                response = self.openai_client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=token_limit,
                    temperature=self.temperature,
                    top_p=0.9
                )
                
                if response.choices:
                    response_text = response.choices[0].message.content
                    yield response_text
                    
                    # Generate TTS for the complete response if enabled
                    if self.enable_tts and response_text.strip():
                        self.generate_speech(response_text, interactive=True)
                    
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            yield error_msg
            if self.enable_tts:
                self.generate_speech(error_msg, interactive=False)
    
    def interactive_mode(self):
        """Run in interactive chat mode"""
        print("🎵 Music Tutor Interactive Mode - Comprehensive Music Expert")
        print("-" * 70)
        
        # Show knowledge system status
        knowledge_status = self.get_knowledge_status()
        print("📚 Four-Pillar Knowledge Systems Available:")
        print(f"  🎯 Nashville Numbers: ✅ Always available")
        print(f"  🎛️ Slakh Professional: {'✅' if knowledge_status['slakh_professional'] else '❌'} {'(' + str(knowledge_status.get('slakh_instruments', 0)) + ' instruments)' if knowledge_status['slakh_professional'] else ''}")
        print(f"  📖 Music Theory: {'✅' if knowledge_status['music_theory'] else '❌'} {'(' + str(knowledge_status.get('theory_sections', 0)) + ' sections)' if knowledge_status['music_theory'] else ''}")
        print(f"  🎸 Professional Performance: {'✅' if knowledge_status['professional_performance'] else '❌'} {'(' + str(knowledge_status.get('performance_sections', 0)) + ' areas)' if knowledge_status['professional_performance'] else ''}")
        print(f"  📊 Total Keywords: {knowledge_status['total_keywords']}")
        print(f"  🔊 Text-to-Speech: {'✅ Enabled' if self.enable_tts else '❌ Disabled'}")
        if self.enable_tts:
            print(f"      Mode: {'🎙️ Interactive playback' if not self.save_audio else '🎙️ Interactive + 💾 File saving'}")
            if self.save_audio:
                print(f"      Audio Output: {self.audio_output_dir}")
            if self.audio_prompt_path:
                print(f"      Voice: {self.audio_prompt_path}")
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
        print("  Type 'status' to show knowledge system status")
        if self.enable_tts:
            print("  🔊 After each response, you'll be prompted to play audio")
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
                
                # Prepare messages for this interaction
                if single_question_mode:
                    # Single question mode - no conversation history
                    current_messages = [{"role": "user", "content": user_input}]
                else:
                    # Conversational mode - add to history and manage length
                    conversation_history.append({"role": "user", "content": user_input})
                    
                    # Limit conversation history to prevent excessive context
                    if len(conversation_history) > max_history_length:
                        # Keep system message (if any) and recent exchanges
                        system_messages = [msg for msg in conversation_history if msg.get("role") == "system"]
                        recent_messages = conversation_history[-max_history_length:]
                        conversation_history = system_messages + recent_messages
                    
                    current_messages = conversation_history.copy()
                
                print("🤖 Music Tutor: ", end="", flush=True)
                
                # Generate response
                response_content = ""
                for chunk in self.chat_response(current_messages):
                    if chunk and not chunk.startswith("Error:"):
                        print(chunk, end="", flush=True)
                        response_content += chunk
                    elif chunk.startswith("Error:"):
                        print(f"\n❌ {chunk}")
                        break
                
                if response_content:
                    if not single_question_mode:
                        # Add assistant response to history only in conversational mode
                        conversation_history.append({"role": "assistant", "content": response_content})
                    print()  # New line after response
                    
            except KeyboardInterrupt:
                print("\n👋 Goodbye!")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="Music Tutor using OpenAI")
    parser.add_argument("--prompt", "-p", type=str, help="Single prompt to send to the music tutor")
    parser.add_argument("--model", "-m", type=str, default="gpt-3.5-turbo", help="Model name (default: gpt-3.5-turbo)")
    parser.add_argument("--api-key", "-k", type=str, help="OpenAI API key (or set OPENAI_API_KEY environment variable)")
    parser.add_argument("--no-stream", action="store_true", help="Disable streaming responses")
    parser.add_argument("--interactive", "-i", action="store_true", help="Run in interactive mode")
    parser.add_argument("--temperature", "-t", type=float, default=0.7, help="Temperature for response generation (0.0-1.0, default: 0.7)")
    parser.add_argument("--max-tokens", type=int, default=800, help="Maximum number of tokens to generate (default: 800)")
    parser.add_argument("--concise", action="store_true", help="Force very concise responses")
    parser.add_argument("--single-mode", action="store_true", help="Start in single-question mode (no conversation context)")
    parser.add_argument("--context-limit", type=int, default=6, help="Maximum conversation history length (default: 6)")
    parser.add_argument("--allow-all-topics", action="store_true", help="Allow non-music questions (default: music-only mode)")
    
    # TTS arguments
    parser.add_argument("--enable-tts", action="store_true", help="Enable text-to-speech for responses")
    parser.add_argument("--tts-device", type=str, default="auto", help="TTS device: 'auto', 'cuda', or 'cpu' (default: auto)")
    parser.add_argument("--audio-output-dir", type=str, default="audio_output", help="Directory for audio output files (default: audio_output)")
    parser.add_argument("--audio-prompt-path", type=str, help="Voice ID for specific system voice (see tts_demo.py voice for list)")
    parser.add_argument("--save-audio", action="store_true", help="Also save audio responses to files")
    
    args = parser.parse_args()
    
    # Initialize runner
    runner = MusicTutorRunner(
        api_key=args.api_key,
        model=args.model,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        concise=args.concise,
        single_mode=args.single_mode,
        context_limit=args.context_limit,
        music_only=not args.allow_all_topics,
        enable_tts=args.enable_tts,
        tts_device=args.tts_device,
        audio_output_dir=args.audio_output_dir,
        audio_prompt_path=args.audio_prompt_path,
        save_audio=args.save_audio
    )
    
    # Check connection
    print("🔍 Checking OpenAI API connection...")
    if not runner.check_connection():
        print("❌ Error: Cannot connect to OpenAI API.")
        print("   Make sure you have set your OPENAI_API_KEY environment variable or passed --api-key")
        print("   Get your API key from: https://platform.openai.com/api-keys")
        sys.exit(1)
    
    print("✅ Connected to OpenAI API!")
    
    # Check model
    print(f"🔍 Checking if model '{args.model}' is available...")
    if not runner.check_model_exists():
        print(f"❌ Error: Model '{args.model}' may not be available.")
        print(f"   Available models: gpt-3.5-turbo, gpt-4, gpt-4-turbo-preview")
        print(f"   Continuing anyway...")
    else:
        print(f"✅ Model '{args.model}' is available!")
    
    # Show four-pillar knowledge system status
    knowledge_status = runner.get_knowledge_status()
    print(f"\n📚 Four-Pillar Knowledge System Loaded:")
    print(f"  🎯 Nashville Numbers: ✅")
    print(f"  🎛️ Slakh Professional: {'✅' if knowledge_status['slakh_professional'] else '❌'} {'(' + str(knowledge_status.get('slakh_instruments', 0)) + ' instruments)' if knowledge_status['slakh_professional'] else ''}")
    print(f"  📖 Music Theory: {'✅' if knowledge_status['music_theory'] else '❌'} {'(' + str(knowledge_status.get('theory_sections', 0)) + ' sections)' if knowledge_status['music_theory'] else ''}")
    print(f"  🎸 Professional Performance: {'✅' if knowledge_status['professional_performance'] else '❌'} {'(' + str(knowledge_status.get('performance_sections', 0)) + ' areas)' if knowledge_status['professional_performance'] else ''}")
    print(f"  📊 Total Keywords: {knowledge_status['total_keywords']}")
    print(f"  🔊 Text-to-Speech: {'✅ Enabled' if runner.enable_tts else '❌ Disabled'}")
    if runner.enable_tts:
        print(f"      Mode: {'🎙️ Interactive playback' if not runner.save_audio else '🎙️ Interactive + 💾 File saving'}")
        if runner.save_audio:
            print(f"      Audio Output: {runner.audio_output_dir}")
        if runner.audio_prompt_path:
            print(f"      Voice: {runner.audio_prompt_path}")
    
    # Calculate enhancement factor
    base_keywords = 25  # Original Nashville numbers keywords
    if knowledge_status['total_keywords'] > base_keywords:
        enhancement_factor = knowledge_status['total_keywords'] / base_keywords
        print(f"  🚀 Enhancement: {enhancement_factor:.1f}x knowledge expansion!")
    print()
    
    # Run based on arguments
    if args.interactive or (not args.prompt and not args.interactive):
        runner.interactive_mode()
    elif args.prompt:
        print(f"🔹 Prompt: {args.prompt}")
        print("🤖 Music Tutor: ", end="", flush=True)
        
        for chunk in runner.generate_response(args.prompt, stream=not args.no_stream):
            if chunk and not chunk.startswith("Error:"):
                print(chunk, end="", flush=True)
            elif chunk.startswith("Error:"):
                print(f"\n❌ {chunk}")
                break
        print()  # New line after response

if __name__ == "__main__":
    main() 