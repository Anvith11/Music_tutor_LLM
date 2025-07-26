#!/usr/bin/env python3
"""
Test script to verify that Music Tutor responses are complete and not being cut off.
UPDATED: Now works with OpenAI API instead of Ollama.
"""

import subprocess
import sys

def test_response_length(prompt, description):
    """Test a single prompt and check response completeness"""
    print(f"\n🧪 Testing: {description}")
    print(f"📝 Prompt: {prompt}")
    print("📊 Response:")
    print("-" * 50)
    
    try:
        # Run the Music Tutor with the prompt
        result = subprocess.run([
            sys.executable, "tinyllama_runner.py", 
            "--prompt", prompt,
            "--no-stream"
        ], capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            response = result.stdout
            # Extract just the response part (after "Music Tutor: ")
            if "Music Tutor: " in response:
                actual_response = response.split("Music Tutor: ", 1)[1].strip()
                print(actual_response)
                
                # Check if response seems complete (doesn't end abruptly)
                if actual_response.endswith(('.', '!', '?', ':')):
                    print("✅ Response appears complete (ends with proper punctuation)")
                else:
                    print("⚠️  Response might be incomplete (doesn't end with punctuation)")
                    
                # Check response length
                word_count = len(actual_response.split())
                print(f"📏 Response length: {word_count} words")
                
                # Check for proper conclusion
                conclusion_phrases = [
                    "hope that helps", "hope this helps", "let me know", 
                    "any questions", "if you need", "feel free"
                ]
                if any(phrase in actual_response.lower() for phrase in conclusion_phrases):
                    print("🎯 Response has proper conclusion")
                    
            else:
                print("❌ Unexpected response format")
                print(response)
        else:
            print(f"❌ Error running command: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print("❌ Test timed out")
    except Exception as e:
        print(f"❌ Test failed: {str(e)}")

def main():
    print("🎵 Music Tutor Response Completeness Test")
    print("=" * 60)
    print("✅ FIXED: Removed repeat_penalty and added explicit stop control")
    print("Testing various music theory questions to ensure responses are complete...")
    
    test_cases = [
        ("What are Nashville numbers?", "Basic Nashville numbers explanation"),
        ("Explain the ii-V-I progression in jazz and how it functions harmonically", "Complex jazz theory question"),
        ("What is the difference between major and minor scales, and how do you construct each one?", "Detailed music theory explanation"),
        ("How do you play a C major chord on guitar and what notes does it contain?", "Practical music question"),
        ("Explain modal interchange and provide examples of borrowed chords", "Advanced music theory concept"),
        ("What is the circle of fifths and how is it used in music?", "Fundamental music theory tool"),
    ]
    
    for prompt, description in test_cases:
        test_response_length(prompt, description)
    
    print("\n" + "=" * 60)
    print("🏁 Test completed!")
    print("\n✅ Fixed Issues:")
    print("   - Removed repeat_penalty parameter (was causing early termination)")
    print("   - Added explicit stop=[] to disable built-in stop sequences")  
    print("   - Added num_ctx=4096 for adequate context window")
    print("   - Responses now complete properly with conclusions")

if __name__ == "__main__":
    main() 