#!/usr/bin/env python3
"""
Qwen2-Audio Setup Test
Simple script to test your Qwen2-Audio model setup and system requirements
"""

from qwen_music_tutor import MusicTutorRunner

def test_qwen_setup():
    """Test Qwen2-Audio setup with proper error handling"""
    print("🔍 Qwen2-Audio Setup Test")
    print("=" * 40)
    
    # Test system requirements
    print("🔧 Checking system requirements...")
    
    # Check Python packages
    try:
        import torch
        print(f"✅ PyTorch: {torch.__version__}")
        
        import transformers
        print(f"✅ Transformers: {transformers.__version__}")
        
        import librosa
        print(f"✅ Librosa: {librosa.__version__}")
        
        import soundfile
        print(f"✅ SoundFile: {soundfile.__version__}")
        
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Run: pip install -r requirements.txt")
        return False
    
    # Check CUDA availability
    print("\n🎮 Checking GPU availability...")
    if torch.cuda.is_available():
        gpu_count = torch.cuda.device_count()
        gpu_name = torch.cuda.get_device_name(0)
        gpu_memory = torch.cuda.get_device_properties(0).total_memory / 1024**3
        print(f"✅ CUDA available: {gpu_count} GPU(s)")
        print(f"   Primary GPU: {gpu_name}")
        print(f"   VRAM: {gpu_memory:.1f}GB")
        
        if gpu_memory < 12:
            print("⚠️  Warning: Less than 12GB VRAM may cause issues with larger models")
    else:
        print("⚠️  No CUDA GPU detected - will use CPU (much slower)")
    
    # Initialize the music tutor
    print("\n🔧 Initializing Qwen2-Audio Music Tutor...")
    try:
        runner = MusicTutorRunner(
            model_name="Qwen/Qwen2-Audio-7B-Instruct",
            device="auto",
            music_only=True
        )
        
        # Check if model is loaded
        if runner.check_model_status():
            print("✅ Qwen2-Audio model loaded successfully!")
        else:
            print("❌ Failed to load Qwen2-Audio model")
            print("This is normal on first run - model will be downloaded")
            return False
            
    except Exception as e:
        print(f"❌ Error initializing model: {str(e)}")
        return False
    
    # Test basic functionality
    print("\n🧪 Testing basic functionality...")
    try:
        result = runner.generate_response(
            prompt="What is a C major chord?",
            stream=False
        )
        
        if result["text"] and not result["text"].startswith("Error:"):
            print("✅ Basic text generation working!")
            print(f"📝 Sample response: {result['text'][:100]}...")
        else:
            print(f"❌ Text generation failed: {result['text']}")
            return False
            
    except Exception as e:
        print(f"❌ Error testing functionality: {str(e)}")
        return False
    
    # Test knowledge systems
    print("\n📚 Checking knowledge systems...")
    knowledge_status = runner.get_knowledge_status()
    
    print(f"🎯 Nashville Numbers: {'✅' if knowledge_status['nashville_numbers'] else '❌'}")
    print(f"🎛️ Slakh Professional: {'✅' if knowledge_status['slakh_professional'] else '❌'}")
    print(f"📖 Music Theory: {'✅' if knowledge_status['music_theory'] else '❌'}")
    print(f"🎸 Professional Performance: {'✅' if knowledge_status['professional_performance'] else '❌'}")
    print(f"📊 Total Keywords: {knowledge_status['total_keywords']}")
    
    print("\n🎉 Qwen2-Audio setup test completed successfully!")
    print("\nYou can now run:")
    print("  python qwen_music_tutor.py --interactive")
    
    return True

if __name__ == "__main__":
    success = test_qwen_setup()
    if not success:
        print("\n💡 Setup issues detected. Please check the requirements and try again.")
        exit(1)
    else:
        print("\n✅ Your system is ready for Qwen2-Audio Music Tutor!") 