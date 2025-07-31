#!/usr/bin/env python3
"""
Test script for OpenAI Music Tutor setup
Verifies that all required dependencies are properly installed
"""

import sys
import os

def test_import(module_name, package_name=None, optional=False):
    """Test if a module can be imported"""
    try:
        __import__(module_name)
        print(f"✅ {package_name or module_name} - OK")
        return True
    except ImportError as e:
        status = "⚠️" if optional else "❌"
        print(f"{status} {package_name or module_name} - {'Optional' if optional else 'Required'}: {e}")
        return not optional

def test_openai_connection():
    """Test OpenAI API connection"""
    try:
        from openai import OpenAI
        
        # Check for API key
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            print("⚠️  OpenAI API Key - Not set in OPENAI_API_KEY environment variable")
            return False
        
        client = OpenAI(api_key=api_key)
        
        # Test connection with a minimal request
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": "Test"}],
                max_tokens=1
            )
            print("✅ OpenAI API Connection - OK")
            return True
        except Exception as e:
            print(f"❌ OpenAI API Connection - Failed: {e}")
            return False
            
    except ImportError:
        print("❌ OpenAI package not found - Cannot test connection")
        return False

def main():
    print("🎵 OpenAI Music Tutor Setup Test")
    print("=" * 40)
    
    all_good = True
    
    # Test core Python modules
    print("\n📦 Core Dependencies:")
    all_good &= test_import("sys")
    all_good &= test_import("os")
    all_good &= test_import("argparse")
    all_good &= test_import("re")
    all_good &= test_import("time")
    all_good &= test_import("typing")
    
    # Test OpenAI package
    print("\n🤖 OpenAI Dependencies:")
    all_good &= test_import("openai", "OpenAI API")
    
    # Test optional packages
    print("\n🔊 Optional Dependencies:")
    test_import("pyttsx3", "Text-to-Speech (TTS)", optional=True)
    
    # Test knowledge system files
    print("\n📚 Knowledge System Files:")
    knowledge_files = [
        ("slakh_instrument_data.py", "Slakh Dataset"),
        ("four_pillar_training_data.json", "Four-Pillar Training Data"),
        ("music_theory_dataset.json", "Music Theory Dataset")
    ]
    
    for filename, description in knowledge_files:
        if os.path.exists(filename):
            print(f"✅ {description} - Found")
        else:
            print(f"⚠️  {description} - Not found (optional)")
    
    # Test OpenAI connection
    print("\n🌐 API Connection:")
    connection_ok = test_openai_connection()
    
    # Test main script
    print("\n🎵 Main Script:")
    if os.path.exists("openai_music_tutor.py"):
        print("✅ OpenAI Music Tutor - Found")
    else:
        print("❌ OpenAI Music Tutor - Not found")
        all_good = False
    
    # Final status
    print("\n" + "=" * 40)
    if all_good and connection_ok:
        print("🎉 All systems ready! You can run:")
        print("   python3 openai_music_tutor.py --interactive")
        print("   or")
        print("   ./run_openai_tutor.sh")
    elif all_good:
        print("⚠️  Core setup complete, but API connection failed.")
        print("   Make sure to set your OPENAI_API_KEY environment variable.")
        print("   Get your API key from: https://platform.openai.com/api-keys")
    else:
        print("❌ Setup incomplete. Please install missing dependencies:")
        print("   pip install -r requirements.txt")
    
    return 0 if (all_good and connection_ok) else 1

if __name__ == "__main__":
    sys.exit(main()) 