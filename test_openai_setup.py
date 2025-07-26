#!/usr/bin/env python3
"""
OpenAI API Setup Test
Simple script to test your OpenAI API key and account setup
"""

from tinyllama_runner import MusicTutorRunner

def test_openai_setup():
    """Test OpenAI API setup with proper error handling"""
    print("🔍 OpenAI API Setup Test")
    print("=" * 40)
    
    # Initialize the music tutor
    print("🔧 Initializing Music Tutor...")
    runner = MusicTutorRunner(
        model="gpt-3.5-turbo",
        music_only=True
    )
    
    # Check if API key is loaded
    if not runner.api_key:
        print("❌ No API key found!")
        print("The API key should be automatically loaded from the code.")
        return
    
    print(f"✅ API key loaded: {runner.api_key[:10]}...{runner.api_key[-10:]}")
    
    # Test connection
    print("\n🔍 Testing OpenAI connection...")
    try:
        if runner.check_connection():
            print("✅ Successfully connected to OpenAI API!")
        else:
            print("❌ Failed to connect to OpenAI API")
            return
    except Exception as e:
        print(f"❌ Connection error: {str(e)}")
        return
    
    # Test a simple query
    print("\n🎵 Testing music query...")
    test_question = "What is C major?"
    
    try:
        print(f"📝 Question: {test_question}")
        print("🤖 Response: ", end="", flush=True)
        
        response_received = False
        for chunk in runner.generate_response(test_question, stream=True):
            if chunk and not chunk.startswith("Error:"):
                print(chunk, end="", flush=True)
                response_received = True
            elif chunk.startswith("Error:"):
                print(f"\n❌ {chunk}")
                
                # Check for specific error types
                if "insufficient_quota" in chunk or "429" in chunk:
                    print("\n💳 BILLING ISSUE DETECTED:")
                    print("   Your OpenAI account needs billing setup or has reached usage limits.")
                    print("   Steps to fix:")
                    print("   1. Visit: https://platform.openai.com/billing")
                    print("   2. Add a payment method")
                    print("   3. Set usage limits")
                    print("   4. Check your account balance")
                    print("   5. New accounts often get $5 free credit")
                
                elif "invalid" in chunk.lower() or "unauthorized" in chunk.lower():
                    print("\n🔑 API KEY ISSUE:")
                    print("   Your API key may be invalid or expired.")
                    print("   Steps to fix:")
                    print("   1. Visit: https://platform.openai.com/api-keys")
                    print("   2. Create a new API key")
                    print("   3. Update the key in the code")
                
                return
        
        if response_received:
            print(f"\n\n🎉 SUCCESS! Your OpenAI Music Tutor is working perfectly!")
            print("✅ API key is valid")
            print("✅ Connection established") 
            print("✅ Billing/quota is sufficient")
            print("✅ Music knowledge system is active")
            
            print(f"\n💡 Ready to use:")
            print(f"   python tinyllama_runner.py --interactive")
        else:
            print(f"\n⚠️ No response received - there may be an issue")
            
    except Exception as e:
        print(f"\n❌ Error during query: {str(e)}")
        
        if "insufficient_quota" in str(e) or "429" in str(e):
            print("\n💳 BILLING SETUP REQUIRED:")
            print("   Visit: https://platform.openai.com/billing")
            print("   Add payment method and check usage limits")

if __name__ == "__main__":
    test_openai_setup() 