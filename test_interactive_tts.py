#!/usr/bin/env python3
"""
Test script for interactive TTS functionality
"""

from qwen_music_tutor import MusicTutorRunner

def test_interactive_tts():
    """Test the interactive TTS feature"""
    print("🎵 Testing Interactive TTS Functionality")
    print("=" * 50)
    
    # Test 1: Interactive mode
    print("\n1. Testing Interactive TTS Mode")
    runner = MusicTutorRunner(enable_tts=True)
    
    if runner.enable_tts:
        test_text = "A major scale consists of seven notes with a specific pattern of whole and half steps."
        print(f"Test text: {test_text}")
        result = runner.generate_speech(test_text, interactive=True)
        print(f"Result: {'✅ Success' if result else '❌ Failed'}")
    else:
        print("❌ TTS not available")
    
    # Test 2: Non-interactive mode  
    print("\n2. Testing Non-Interactive TTS Mode")
    if runner.enable_tts:
        test_text = "This is a non-interactive TTS test."
        print(f"Test text: {test_text}")
        result = runner.generate_speech(test_text, interactive=False)
        print(f"Result: {'✅ Success' if result else '❌ Failed'}")
    
    # Test 3: File saving mode
    print("\n3. Testing TTS with File Saving")
    runner_with_save = MusicTutorRunner(enable_tts=True, save_audio=True)
    
    if runner_with_save.enable_tts:
        test_text = "This response will also be saved to a file."
        print(f"Test text: {test_text}")
        result = runner_with_save.generate_speech(test_text, interactive=False)
        print(f"Result: {'✅ Success' if result else '❌ Failed'}")
    
    print("\n" + "=" * 50)
    print("🎉 TTS Test Complete!")

if __name__ == "__main__":
    test_interactive_tts() 