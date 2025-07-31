#!/usr/bin/env python3
"""
Music Topic Detection Demo
Demonstrates how the TinyLLAMA runner filters music vs non-music questions
"""

import sys
import os

# Add current directory to path to import openai_music_tutor
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from openai_music_tutor import MusicTutor

def test_music_detection():
    """Test the music topic detection functionality"""
    
    # Create a runner instance with music-only mode enabled
    runner = MusicTutor()
    
    # Test questions - music-related
    music_questions = [
        "What is the Nashville number system?",
        "Convert C-Am-F-G to Nashville numbers",
        "What is a ii-V-I progression?",
        "How do you play a Dmaj7 chord?",
        "What are the modes in music theory?",
        "Explain the circle of fifths",
        "What is a 12-bar blues progression?",
        "How do you transpose from C to G?",
        "What's the difference between major and minor scales?",
        "Can you explain jazz harmony?",
        "What does 1-4-5 mean in Nashville numbers?",
        "How do you strum a guitar?",
        "What is a diminished chord?",
        "Explain voice leading",
        "What is the dominant 7th chord?"
    ]
    
    # Test questions - non-music related
    non_music_questions = [
        "What is Python programming?",
        "How do I cook pasta?",
        "What is the capital of France?",
        "Explain machine learning",
        "What is quantum physics?",
        "How do I fix my car?",
        "What is the weather like?",
        "Tell me about history",
        "What is artificial intelligence?",
        "How do stocks work?",
        "What is cryptocurrency?",
        "Explain photosynthesis",
        "What is the meaning of life?",
        "How do I learn Spanish?",
        "What is calculus?"
    ]
    
    print("🎵 Music Topic Detection Demo")
    print("=" * 50)
    
    print("\n✅ MUSIC-RELATED QUESTIONS (should be allowed):")
    print("-" * 50)
    for i, question in enumerate(music_questions, 1):
        is_music = runner.is_music_related(question)
        status = "✅ ALLOWED" if is_music else "❌ BLOCKED"
        print(f"{i:2d}. {question}")
        print(f"    → {status}")
        if not is_music:  # This shouldn't happen for music questions
            print(f"    ⚠️  ERROR: Music question was incorrectly blocked!")
    
    print("\n❌ NON-MUSIC QUESTIONS (should be blocked):")
    print("-" * 50)
    for i, question in enumerate(non_music_questions, 1):
        is_music = runner.is_music_related(question)
        status = "✅ ALLOWED" if is_music else "❌ BLOCKED"
        print(f"{i:2d}. {question}")
        print(f"    → {status}")
        if is_music:  # This shouldn't happen for non-music questions
            print(f"    ⚠️  WARNING: Non-music question was incorrectly allowed!")
    
    # Calculate accuracy
    music_correct = sum(1 for q in music_questions if runner.is_music_related(q))
    non_music_correct = sum(1 for q in non_music_questions if not runner.is_music_related(q))
    total_correct = music_correct + non_music_correct
    total_questions = len(music_questions) + len(non_music_questions)
    accuracy = (total_correct / total_questions) * 100
    
    print("\n📊 DETECTION ACCURACY:")
    print("-" * 50)
    print(f"Music questions correctly identified: {music_correct}/{len(music_questions)}")
    print(f"Non-music questions correctly blocked: {non_music_correct}/{len(non_music_questions)}")
    print(f"Overall accuracy: {accuracy:.1f}% ({total_correct}/{total_questions})")
    
    if accuracy >= 90:
        print("🎉 Excellent detection accuracy!")
    elif accuracy >= 80:
        print("👍 Good detection accuracy!")
    else:
        print("⚠️  Detection accuracy could be improved")

def test_response_examples():
    """Show example responses with music filtering"""
    print("\n🎯 RESPONSE EXAMPLES:")
    print("=" * 50)
    
    # Create runner (music-only mode)
    runner = MusicTutor()
    
    test_cases = [
        ("What is the Nashville number system?", "Music question"),
        ("What is Python programming?", "Non-music question"),
        ("How do you play a C major chord?", "Music question"),
        ("What is artificial intelligence?", "Non-music question")
    ]
    
    for question, category in test_cases:
        print(f"\n📝 Question ({category}): {question}")
        print("🤖 Response:", end=" ")
        
        # Simulate the response generation
        if runner.is_music_related(question):
            print("[Would generate music theory response]")
        else:
            print("I'm sorry, I can only explain music-related questions or concepts. Please ask me about music theory, Nashville numbers, chord progressions, instruments, or other musical topics!")

if __name__ == "__main__":
    try:
        test_music_detection()
        test_response_examples()
        
        print("\n🔧 USAGE EXAMPLES:")
        print("-" * 50)
        print("# Music-only mode (default):")
        print("python openai_music_tutor.py -p \"What is a chord progression?\"")
        print("\n# Allow all topics:")
        print("python openai_music_tutor.py --allow-all-topics -p \"What is Python?\"")
        print("\n# Interactive music-only mode:")
        print("python openai_music_tutor.py -i")
        
    except ImportError as e:
        print(f"❌ Error: Could not import openai_music_tutor: {e}")
        print("Make sure openai_music_tutor.py is in the same directory")
    except Exception as e:
        print(f"❌ Error: {e}") 