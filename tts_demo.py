#!/usr/bin/env python3
"""
TTS Demo for TinyLLAMA Music Tutor
Demonstrates text-to-speech functionality with music education responses
"""

import sys
import os
from qwen_music_tutor import MusicTutorRunner

def demo_tts_music_tutor():
    """Demonstrate TTS functionality with music questions"""
    print("🎵 Music Tutor - TTS Demo")
    print("=" * 50)
    
    # Check if TTS is available
    try:
        import pyttsx3
        print("✅ TTS dependencies available")
    except ImportError:
        print("❌ TTS dependencies not found!")
        print("Please install with: pip install -r requirements_tts.txt")
        return
    
    # Initialize Music Tutor with TTS enabled
    print("\n🔧 Initializing Music Tutor with TTS...")
    runner = MusicTutorRunner(
        enable_tts=True,
        tts_device="auto",  # Will try CUDA first, fall back to CPU
        audio_output_dir="demo_audio",
        music_only=True
    )
    
    if not runner.enable_tts:
        print("❌ Failed to initialize TTS")
        return
    
    print("✅ TTS enabled successfully!")
    
    # Test questions for different knowledge pillars
    test_questions = [
        {
            "question": "What does the Nashville number 1-6m-4-5 mean?",
            "description": "Nashville Numbers (Basic)"
        },
        {
            "question": "How do you voice a ii-V-I progression using jazz chord voicings?",
            "description": "Professional Performance + Theory"
        },
        {
            "question": "What MIDI program numbers are used for piano sounds?",
            "description": "Slakh Professional Knowledge"
        },
        {
            "question": "Explain the circle of fifths and its applications",
            "description": "Music Theory Curriculum"
        },
        {
            "question": "How do you handle last-minute key changes during live performance?",
            "description": "Professional Performance Skills"
        }
    ]
    
    print(f"\n🎯 Testing {len(test_questions)} music questions with interactive TTS...")
    print("After each response, you'll be prompted to play the audio.")
    
    for i, test in enumerate(test_questions, 1):
        print(f"\n--- Question {i}: {test['description']} ---")
        print(f"Q: {test['question']}")
        print("A: ", end="", flush=True)
        
        # Generate response with TTS
        full_response = ""
        for chunk in runner.generate_response(test['question']):
            if not chunk.startswith("Error:"):
                print(chunk, end="", flush=True)
                full_response += chunk
            else:
                print(f"\n❌ {chunk}")
                break
        
        print()  # New line after response
    
    print("\n" + "=" * 50)
    print("🎉 TTS Demo Complete!")
    print("Your music tutor can now speak responses interactively!")

def demo_voice_selection():
    """Demonstrate different system voices available"""
    print("\n🎭 Voice Selection Demo")
    print("-" * 30)
    
    try:
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        
        if voices:
            print(f"📝 Found {len(voices)} system voices:")
            for i, voice in enumerate(voices):
                print(f"  {i+1}. {voice.name} ({voice.id})")
            
            print("\nTo use a specific voice:")
            print("python qwen_music_tutor.py --enable-tts --audio-prompt-path <voice_id>")
            print("(Where <voice_id> is one of the IDs shown above)")
        else:
            print("❌ No system voices found")
            
        engine.stop()
        
    except Exception as e:
        print(f"❌ Failed to enumerate voices: {str(e)}")
    
    # Test with different voice
    runner = MusicTutorRunner(
        enable_tts=True,
        audio_output_dir="voice_demo_output"
    )
    
    if runner.enable_tts:
        print("✅ TTS initialized with default voice!")
        print("Ask a music question to hear the TTS response")
    else:
        print("❌ Failed to initialize TTS")

def main():
    """Main demo function"""
    if len(sys.argv) > 1 and sys.argv[1] == "voice":
        demo_voice_selection()
    else:
        demo_tts_music_tutor()
        
        if len(sys.argv) == 1:  # No arguments provided
            print("\n💡 Tip: Run 'python tts_demo.py voice' to see voice selection demo")

if __name__ == "__main__":
    main() 