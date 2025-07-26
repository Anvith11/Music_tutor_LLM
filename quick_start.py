#!/usr/bin/env python3
"""
Quick Start Script for OpenAI Music Tutor
This script demonstrates how to use the music tutor with your API key.
"""

import os
from tinyllama_runner import MusicTutorRunner

def load_api_key():
    """Load API key from .env file or environment"""
    # Try to load from .env file
    if os.path.exists('.env'):
        with open('.env', 'r') as f:
            for line in f:
                if line.startswith('export OPENAI_API_KEY='):
                    # Extract the key from the export statement
                    key = line.split('=', 1)[1].strip().strip('"\'')
                    return key
    
    # Fall back to environment variable
    return os.getenv('OPENAI_API_KEY')

def main():
    """Demo the music tutor capabilities"""
    print("🎵 OpenAI Music Tutor - Quick Start Demo")
    print("=" * 50)
    
    # Load API key
    api_key = load_api_key()
    if not api_key:
        print("❌ No API key found!")
        print("Make sure you have a .env file with your API key.")
        return
    
    print("✅ API key loaded successfully")
    
    # Initialize the music tutor
    print("\n🔧 Initializing Music Tutor...")
    runner = MusicTutorRunner(
        api_key=api_key,
        model="gpt-3.5-turbo",  # Use cost-effective model for demo
        music_only=True
    )
    
    # Test connection
    print("🔍 Testing OpenAI connection...")
    if not runner.check_connection():
        print("❌ Failed to connect to OpenAI API")
        return
    
    print("✅ Connected to OpenAI API!")
    
    # Demo questions covering all four pillars
    demo_questions = [
        "What does the Nashville number 1-6m-4-5 mean?",
        "What MIDI program number is used for acoustic piano?", 
        "Explain the circle of fifths",
        "How do you handle key changes during live performance?"
    ]
    
    print(f"\n🎯 Testing four-pillar knowledge system...")
    print("Asking sample questions...")
    
    for i, question in enumerate(demo_questions, 1):
        print(f"\n📝 Question {i}: {question}")
        print("🤖 Music Tutor: ", end="", flush=True)
        
        try:
            for chunk in runner.generate_response(question, stream=True):
                if chunk and not chunk.startswith("Error:"):
                    print(chunk, end="", flush=True)
                elif chunk.startswith("Error:"):
                    print(f"\n❌ {chunk}")
                    break
            print()  # New line after response
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
    
    print(f"\n🎉 Demo complete! Your music tutor is ready to use.")
    print(f"\n💡 To start interactive mode:")
    print(f"   python tinyllama_runner.py --interactive")
    print(f"\n💡 To ask a single question:")
    print(f"   python tinyllama_runner.py --prompt \"Your question here\"")

if __name__ == "__main__":
    main() 