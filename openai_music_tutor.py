#!/usr/bin/env python3
"""
Music Tutor using OpenAI - Four-Pillar Music Knowledge System
Enhanced with comprehensive four-pillar knowledge integration:
1. Nashville Numbers - Practical chord notation and transposition
2. Slakh Dataset - Professional instrument and production knowledge  
3. Music Theory - Complete educational curriculum from musictheory.net
4. Professional Performance - Advanced performance, ear training, and live techniques

Now powered by OpenAI GPT models with optional Text-to-Speech capabilities!
"""

import sys
import argparse
import re
import os
import time
from typing import Generator, Optional, List, Dict, Any

# OpenAI imports
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    print("Error: OpenAI not available. Install with: pip install openai")
    sys.exit(1)

# TTS imports (optional)
try:
    import pyttsx3
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False
    print("Warning: TTS not available. Install with: pip install pyttsx3")

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

class MusicTutor:
    """
    OpenAI-powered Music Tutor with four-pillar knowledge integration
    """

    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo",
                 enable_tts: bool = False, tts_device: Optional[str] = None,
                 audio_output_dir: str = "audio_output"):
        """Initialize the Music Tutor with OpenAI API"""
        
        # Set up OpenAI API key
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key required. Set OPENAI_API_KEY environment variable or pass as argument.")
        
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        
        # TTS setup
        self.enable_tts = enable_tts and TTS_AVAILABLE
        self.tts_engine = None
        self.audio_output_dir = audio_output_dir
        
        if self.enable_tts:
            try:
                self.tts_engine = pyttsx3.init()
                if tts_device:
                    voices = self.tts_engine.getProperty('voices')
                    for voice in voices:
                        if tts_device in voice.id:
                            self.tts_engine.setProperty('voice', voice.id)
                            break
                
                # Create audio output directory
                os.makedirs(self.audio_output_dir, exist_ok=True)
            except Exception as e:
                print(f"Warning: TTS initialization failed: {e}")
                self.enable_tts = False

        self.conversation_history = []
        
        # Load knowledge systems
        self.music_knowledge = self._load_enhanced_music_knowledge()
        
        print(f"✓ OpenAI Music Tutor initialized with model: {self.model}")
        if self.enable_tts:
            print("✓ Text-to-Speech enabled")
        if SLAKH_AVAILABLE:
            print("✓ Slakh dataset integration loaded")

    def _load_enhanced_music_knowledge(self) -> Dict[str, Any]:
        """Load comprehensive music knowledge from all sources"""
        knowledge = {}
        
        # Load Nashville Numbers data
        try:
            import json
            with open("four_pillar_training_data.json", "r") as f:
                four_pillar_data = json.load(f)
                knowledge["four_pillar"] = four_pillar_data
        except FileNotFoundError:
            print("Warning: Four-pillar training data not found")
        
        # Load music theory data
        try:
            with open("music_theory_dataset.json", "r") as f:
                theory_data = json.load(f)
                knowledge["theory"] = theory_data
        except FileNotFoundError:
            print("Warning: Music theory dataset not found")
        
        # Add Slakh knowledge if available
        if SLAKH_AVAILABLE:
            knowledge["slakh"] = {
                "instrument_classes": SLAKH_INSTRUMENT_CLASSES,
                "midi_mapping": MIDI_TO_SLAKH_CLASS,
                "synthesis": SYNTHESIS_KNOWLEDGE
            }
        
        return knowledge

    def check_connection(self) -> bool:
        """Test OpenAI API connection"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": "Test"}],
                max_tokens=1
            )
            return True
        except Exception as e:
            print(f"OpenAI connection failed: {e}")
            return False

    def check_model_exists(self, model_name: str) -> bool:
        """Check if the specified model exists and is accessible"""
        try:
            response = self.client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": "Test"}],
                max_tokens=1
            )
            return True
        except Exception as e:
            print(f"Model {model_name} not accessible: {e}")
            return False

    def _create_system_prompt(self) -> str:
        """Create comprehensive system prompt with four-pillar knowledge"""
        base_prompt = """You are an expert music instructor with comprehensive knowledge across four key areas:

**1. NASHVILLE NUMBERS SYSTEM:**
- Convert chord progressions to/from Nashville numbers
- Explain transposition using numbers (1-7)
- Help with practical chord notation
- Major scale relationships: 1(major), 2(minor), 3(minor), 4(major), 5(major), 6(minor), 7(diminished)

**2. SLAKH DATASET KNOWLEDGE:**
- Professional music production techniques
- Instrument families and their characteristics
- MIDI programming and synthesis
- Audio production workflows
- Genre-specific instrument usage

**3. MUSIC THEORY FUNDAMENTALS:**
- Scales, modes, and intervals
- Chord construction and progressions
- Key signatures and circle of fifths
- Rhythm, meter, and time signatures
- Harmonic analysis and voice leading

**4. PROFESSIONAL PERFORMANCE:**
- Performance techniques for all instruments
- Ear training and sight-reading
- Live performance preparation
- Practice methodologies
- Musical expression and interpretation

**RESPONSE GUIDELINES:**
- Always provide practical, actionable advice
- Use examples relevant to the student's level
- Include Nashville numbers when discussing chord progressions
- Mention relevant instruments from professional contexts
- Focus on building both theoretical understanding and practical skills
- For chord progressions, always show both traditional notation and Nashville numbers
- When discussing production, reference appropriate instrument classes and techniques

**RESTRICTIONS:**
- Only answer music-related questions
- If asked non-music questions, politely redirect: "I'm here to help with music-related questions. What would you like to learn about music today?"
- Keep responses educational and encouraging
- Adapt complexity to the user's apparent level"""

        return base_prompt

    def is_music_related(self, prompt: str) -> bool:
        """Enhanced music content detection using multiple knowledge sources"""
        
        # Check against enhanced music keywords
        if SLAKH_AVAILABLE:
            enhanced_keywords = get_enhanced_music_keywords()
            if any(keyword in prompt.lower() for keyword in enhanced_keywords):
                return True
            
            # Check for professional music terms
            if is_professional_music_term(prompt):
                return True
        
        # Basic music keywords as fallback
        music_keywords = [
            'music', 'chord', 'scale', 'note', 'key', 'rhythm', 'melody', 'harmony',
            'instrument', 'guitar', 'piano', 'bass', 'drum', 'violin', 'saxophone',
            'nashville', 'progression', 'theory', 'composition', 'song', 'practice',
            'performance', 'audio', 'recording', 'production', 'mixing', 'mastering',
            'tempo', 'beat', 'measure', 'interval', 'octave', 'sharp', 'flat',
            'major', 'minor', 'diminished', 'augmented', 'jazz', 'blues', 'rock',
            'classical', 'pop', 'folk', 'country', 'electronic', 'synthesizer'
        ]
        
        return any(keyword in prompt.lower() for keyword in music_keywords)

    def generate_response(self, prompt: str, temperature: float = 0.7, 
                         max_tokens: int = 800, stream: bool = True,
                         context_limit: int = 6, allow_all_topics: bool = False) -> Generator[str, None, None]:
        """Generate streaming response using OpenAI API"""
        
        if not allow_all_topics and not self.is_music_related(prompt):
            yield "I'm sorry, I can only explain music-related questions or concepts. What would you like to learn about music today?"
            return

        try:
            # Build messages with conversation history
            messages = [{"role": "system", "content": self._create_system_prompt()}]
            
            # Add recent conversation history (limited)
            recent_history = self.conversation_history[-context_limit*2:] if context_limit > 0 else []
            messages.extend(recent_history)
            
            # Add current user message
            messages.append({"role": "user", "content": prompt})

            # Make API call
            if stream:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=temperature,
                    stream=True
                )
                
                full_response = ""
                for chunk in response:
                    if chunk.choices[0].delta.get("content"):
                        content = chunk.choices[0].delta.content
                        full_response += content
                        yield content
                
                # Store in conversation history
                self.conversation_history.append({"role": "user", "content": prompt})
                self.conversation_history.append({"role": "assistant", "content": full_response})
                
            else:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    max_tokens=max_tokens,
                    temperature=temperature
                )
                
                full_response = response.choices[0].message.content
                yield full_response
                
                # Store in conversation history
                self.conversation_history.append({"role": "user", "content": prompt})
                self.conversation_history.append({"role": "assistant", "content": full_response})

        except Exception as e:
            yield f"Error generating response: {str(e)}"

    def chat_response(self, prompt: str, **kwargs) -> str:
        """Get complete response as string"""
        response_parts = list(self.generate_response(prompt, **kwargs))
        return "".join(response_parts)

    def speak_response(self, text: str, save_to_file: bool = False) -> None:
        """Convert text to speech using TTS"""
        if not self.enable_tts or not self.tts_engine:
            return
        
        try:
            if save_to_file:
                # Create unique filename
                timestamp = int(time.time())
                filename = os.path.join(self.audio_output_dir, f"response_{timestamp}.wav")
                self.tts_engine.save_to_file(text, filename)
                print(f"Audio saved to: {filename}")
            
            # Speak the text
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
            
        except Exception as e:
            print(f"TTS error: {e}")

    def interactive_mode(self, stream: bool = True, context_limit: int = 6,
                        allow_all_topics: bool = False, enable_tts_prompts: bool = False,
                        save_audio: bool = False):
        """Run interactive chat session"""
        print("\n" + "="*60)
        print("🎵 INTERACTIVE MUSIC TUTOR SESSION 🎵")
        print("="*60)
        print("Ask me about music theory, Nashville numbers, instruments, production, or performance!")
        print("Type 'quit', 'exit', or 'bye' to end the session.")
        print("Type 'clear' to clear conversation history.")
        if self.enable_tts:
            print("Type 'tts on/off' to toggle text-to-speech.")
        print("="*60 + "\n")

        while True:
            try:
                user_input = input("🎵 You: ").strip()
                
                if not user_input:
                    continue
                
                # Handle special commands
                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("\n👋 Thanks for learning music with me! Keep practicing! 🎵")
                    break
                
                if user_input.lower() == 'clear':
                    self.conversation_history = []
                    print("🧹 Conversation history cleared!")
                    continue
                
                if user_input.lower().startswith('tts '):
                    if user_input.lower() == 'tts on':
                        self.enable_tts = True and TTS_AVAILABLE
                        print("🔊 TTS enabled" if self.enable_tts else "❌ TTS not available")
                    elif user_input.lower() == 'tts off':
                        self.enable_tts = False
                        print("🔇 TTS disabled")
                    continue

                print("\n🤖 Tutor: ", end="", flush=True)
                
                full_response = ""
                for chunk in self.generate_response(
                    user_input, 
                    stream=stream, 
                    context_limit=context_limit,
                    allow_all_topics=allow_all_topics
                ):
                    print(chunk, end="", flush=True)
                    full_response += chunk
                
                print("\n")
                
                # TTS output
                if self.enable_tts and enable_tts_prompts:
                    self.speak_response(full_response, save_to_file=save_audio)

            except KeyboardInterrupt:
                print("\n\n👋 Session interrupted. Thanks for learning music! 🎵")
                break
            except Exception as e:
                print(f"\n❌ Error: {e}")
                continue

def main():
    """Main function with comprehensive argument parsing"""
    parser = argparse.ArgumentParser(
        description="Music Tutor using OpenAI - Four-Pillar Knowledge System",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python openai_music_tutor.py --interactive
  python openai_music_tutor.py -p "What is the Nashville number system?"
  python openai_music_tutor.py -k "your-api-key" -p "Explain ii-V-I progression"
  python openai_music_tutor.py --enable-tts -p "How do I practice scales?"
        """
    )
    
    # Core arguments
    parser.add_argument('--prompt', '-p', type=str, help='Single prompt to send to the music tutor')
    parser.add_argument('--model', '-m', type=str, default='gpt-3.5-turbo', help='OpenAI model name')
    parser.add_argument('--api-key', '-k', type=str, help='OpenAI API key (or set OPENAI_API_KEY env var)')
    parser.add_argument('--no-stream', action='store_true', help='Disable streaming responses')
    parser.add_argument('--interactive', '-i', action='store_true', help='Run in interactive mode')
    
    # Response parameters
    parser.add_argument('--temperature', '-t', type=float, default=0.7, help='Temperature (0.0-1.0)')
    parser.add_argument('--max-tokens', type=int, default=800, help='Maximum tokens to generate')
    parser.add_argument('--concise', action='store_true', help='Force concise responses')
    parser.add_argument('--single-mode', action='store_true', help='Single question mode (no context)')
    parser.add_argument('--context-limit', type=int, default=6, help='Conversation history limit')
    parser.add_argument('--allow-all-topics', action='store_true', help='Allow non-music questions')
    
    # TTS arguments
    parser.add_argument('--enable-tts', action='store_true', help='Enable text-to-speech')
    parser.add_argument('--save-audio', action='store_true', help='Save audio responses to files')
    parser.add_argument('--audio-output-dir', type=str, default='audio_output', help='Audio output directory')
    parser.add_argument('--tts-device', type=str, help='TTS voice ID or device name')
    
    args = parser.parse_args()
    
    # Adjust parameters for concise mode
    if args.concise:
        args.max_tokens = min(args.max_tokens, 300)
        args.temperature = 0.3

    try:
        # Initialize tutor
        tutor = MusicTutor(
            api_key=args.api_key,
            model=args.model,
            enable_tts=args.enable_tts,
            tts_device=args.tts_device,
            audio_output_dir=args.audio_output_dir
        )
        
        # Test connection
        if not tutor.check_connection():
            print("❌ Failed to connect to OpenAI API. Please check your API key and internet connection.")
            return
        
        context_limit = 0 if args.single_mode else args.context_limit
        
        if args.prompt:
            # Single prompt mode
            print(f"\n🎵 Music Question: {args.prompt}")
            print("🤖 Tutor Response:")
            print("-" * 50)
            
            full_response = ""
            for chunk in tutor.generate_response(
                args.prompt,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
                stream=not args.no_stream,
                context_limit=context_limit,
                allow_all_topics=args.allow_all_topics
            ):
                print(chunk, end="", flush=True)
                full_response += chunk
            
            print("\n" + "-" * 50)
            
            # TTS for single prompt
            if args.enable_tts:
                tutor.speak_response(full_response, save_to_file=args.save_audio)
        
        elif args.interactive:
            # Interactive mode
            tutor.interactive_mode(
                stream=not args.no_stream,
                context_limit=context_limit,
                allow_all_topics=args.allow_all_topics,
                enable_tts_prompts=args.enable_tts,
                save_audio=args.save_audio
            )
        
        else:
            # Default to interactive if no prompt provided
            print("No prompt provided. Starting interactive mode...")
            tutor.interactive_mode(
                stream=not args.no_stream,
                context_limit=context_limit,
                allow_all_topics=args.allow_all_topics,
                enable_tts_prompts=args.enable_tts,
                save_audio=args.save_audio
            )

    except KeyboardInterrupt:
        print("\n👋 Goodbye! Keep making music! 🎵")
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 