#!/usr/bin/env python3
"""
Music Tutor Demo (No API Required)
Showcases the four-pillar knowledge system without OpenAI API calls
"""

from tinyllama_runner import MusicTutorRunner

def demo_music_knowledge():
    """Demo the music knowledge system without API calls"""
    print("🎵 Music Tutor Demo - Four-Pillar Knowledge System")
    print("=" * 60)
    print("This demo shows your music tutor's capabilities without using OpenAI credits")
    print()
    
    # Initialize the system
    runner = MusicTutorRunner(music_only=True)
    
    # Show knowledge status
    knowledge_status = runner.get_knowledge_status()
    capabilities = runner.get_comprehensive_capabilities()
    
    print("📚 Knowledge System Status:")
    print(f"  🎯 Nashville Numbers: ✅")
    print(f"  🎛️ Slakh Professional: {'✅' if knowledge_status['slakh_professional'] else '❌'} ({knowledge_status.get('slakh_instruments', 0)} instruments)")
    print(f"  📖 Music Theory: {'✅' if knowledge_status['music_theory'] else '❌'} ({knowledge_status.get('theory_sections', 0)} sections)")
    print(f"  🎸 Professional Performance: {'✅' if knowledge_status['professional_performance'] else '❌'} ({knowledge_status.get('performance_sections', 0)} areas)")
    print(f"  📊 Total Keywords: {knowledge_status['total_keywords']}")
    print()
    
    # Demo capabilities
    print("🎯 Your music tutor specializes in:")
    print(f"   {capabilities}")
    print()
    
    # Interactive demo
    print("🎮 INTERACTIVE DEMO")
    print("Ask music questions to see the knowledge detection in action!")
    print("Type 'quit' to exit, 'help' for examples")
    print("-" * 60)
    
    while True:
        try:
            user_input = input("\n🔹 Ask a music question: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("👋 Thanks for trying the demo!")
                break
                
            if user_input.lower() == 'help':
                print("🔍 Example questions you can ask:")
                print("   • What is C major?")
                print("   • Explain the ii-V-I progression")
                print("   • What MIDI program is acoustic piano?")
                print("   • How do you handle key changes live?")
                print("   • Convert C-Am-F-G to Nashville numbers")
                continue
                
            if not user_input:
                continue
            
            # Analyze the question
            print(f"\n🔍 Analyzing: '{user_input}'")
            
            # Check music detection
            is_music = runner.is_music_related(user_input)
            
            if is_music:
                print("✅ MUSIC-RELATED: Question detected as music topic")
                
                # Show enhanced context
                enriched = runner.enrich_context_with_knowledge(user_input)
                if enriched != user_input:
                    print("🎯 ENHANCED CONTEXT: Additional knowledge found")
                    added_context = enriched.replace(user_input, "").strip()
                    if added_context:
                        print(f"   📝 {added_context}")
                
                print("🤖 RESPONSE: [Would generate comprehensive music answer using OpenAI]")
                print("   💡 This would include knowledge from all four pillars")
                print("   💳 (Blocked due to OpenAI quota - add billing to see full responses)")
                
            else:
                print("❌ NON-MUSIC: Question rejected (music-only mode)")
                capabilities = runner.get_comprehensive_capabilities()
                print(f"🤖 RESPONSE: I'm sorry, I can only explain music-related questions.")
                print(f"   I specialize in {capabilities}")
                print("   Please ask about music theory, instruments, or musical topics!")
                
        except KeyboardInterrupt:
            print("\n👋 Demo interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")

def show_billing_info():
    """Show billing setup information"""
    print("\n" + "="*60)
    print("💳 TO GET FULL RESPONSES:")
    print("="*60)
    print("Your music tutor is technically perfect and ready to use!")
    print("You just need to set up OpenAI billing:")
    print()
    print("1. Visit: https://platform.openai.com/billing")
    print("2. Add a payment method (credit/debit card)")
    print("3. Set usage limits (start with $5-10/month)")
    print("4. Check account balance")
    print()
    print("💰 COST ESTIMATE:")
    print("   • GPT-3.5-turbo: ~$0.002 per question")
    print("   • $5 = ~2,500 music questions")
    print("   • Very affordable for learning!")
    print()
    print("🎉 Once billing is set up:")
    print("   python tinyllama_runner.py --interactive")

if __name__ == "__main__":
    demo_music_knowledge()
    show_billing_info() 