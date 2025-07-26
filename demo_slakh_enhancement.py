#!/usr/bin/env python3
"""
Demonstration of Slakh Dataset Enhancement for Music Tutor LLM
Shows the improved instrument knowledge and professional music capabilities
"""

from slakh_instrument_data import (
    get_enhanced_music_keywords,
    is_professional_music_term,
    get_instrument_class,
    get_instrument_info,
    SLAKH_INSTRUMENT_CLASSES,
    MIDI_TO_SLAKH_CLASS,
    SYNTHESIS_KNOWLEDGE
)

def demo_enhanced_detection():
    """Demonstrate enhanced music term detection"""
    print("🎵 Enhanced Music Term Detection")
    print("=" * 50)
    
    test_phrases = [
        "What is overdrive on electric guitar?",
        "How do velocity layers work in sample libraries?",
        "Explain the embouchure technique for trumpet",
        "What's the difference between sul ponticello and arco?",
        "How does round-robin sampling prevent machine gun effect?",
        "What MIDI CC controls filter cutoff frequency?",
        "Tell me about programming",  # Non-music term
        "What is the weather?",       # Non-music term
    ]
    
    for phrase in test_phrases:
        is_music = is_professional_music_term(phrase)
        status = "✅ MUSIC" if is_music else "❌ NOT MUSIC"
        print(f"{status}: {phrase}")

def demo_instrument_classification():
    """Demonstrate MIDI to instrument class mapping"""
    print("\n🎹 MIDI Program to Instrument Class Mapping")
    print("=" * 50)
    
    test_programs = [0, 25, 30, 40, 56, 73, 80, 88, 128]
    
    for program in test_programs:
        instrument_class = get_instrument_class(program)
        info = get_instrument_info(instrument_class)
        
        print(f"MIDI {program:3d} → {instrument_class}")
        if info:
            print(f"         Description: {info.get('description', 'N/A')}")
            print(f"         Techniques: {', '.join(info.get('techniques', [])[:3])}")
        print()

def demo_professional_knowledge():
    """Demonstrate access to professional synthesis knowledge"""
    print("\n🎛️ Professional Synthesis Knowledge")
    print("=" * 50)
    
    # Sample libraries info
    print("Sample Libraries:")
    for lib in SYNTHESIS_KNOWLEDGE['sample_libraries']['examples']:
        print(f"  • {lib}")
    
    print(f"\nSampling: {SYNTHESIS_KNOWLEDGE['synthesis_techniques']['sampling']}")
    print(f"Modeling: {SYNTHESIS_KNOWLEDGE['synthesis_techniques']['modeling']}")
    
    # Multi-track production info
    print(f"\nMixing: {SYNTHESIS_KNOWLEDGE['multi_track_production']['mixing']}")

def demo_keyword_expansion():
    """Show the massive expansion of music keywords"""
    print("\n📝 Keyword Expansion Statistics")
    print("=" * 50)
    
    enhanced_keywords = get_enhanced_music_keywords()
    
    print(f"Total enhanced keywords: {len(enhanced_keywords)}")
    print(f"Instrument classes: {len(SLAKH_INSTRUMENT_CLASSES)}")
    print(f"MIDI program mappings: {len(MIDI_TO_SLAKH_CLASS)}")
    
    # Sample of new professional terms
    print("\nSample professional terms now detected:")
    professional_samples = [
        'velocity layers', 'round-robin sampling', 'embouchure',
        'sul ponticello', 'overdrive', 'filter cutoff', 'LFO',
        'amp simulation', 'lip trills', 'pitch bending'
    ]
    
    for term in professional_samples:
        print(f"  • {term}")

def demo_comprehensive_instrument_info():
    """Show detailed information about instrument classes"""
    print("\n🎸 Comprehensive Instrument Information")
    print("=" * 50)
    
    # Show detailed info for a few key instruments
    key_instruments = ['Electric Guitar', 'Piano', 'Saxophone', 'Synth Lead']
    
    for instrument in key_instruments:
        info = get_instrument_info(instrument)
        if info:
            print(f"\n{instrument}:")
            print(f"  MIDI Programs: {info['midi_programs']}")
            print(f"  Characteristics: {info['characteristics']}")
            print(f"  Techniques: {', '.join(info['techniques'])}")

def main():
    """Run all demonstrations"""
    print("🦙 TinyLLAMA Music Tutor - Slakh Dataset Enhancement Demo")
    print("=" * 60)
    print("This demo shows how the Slakh dataset enhances the music tutor")
    print("with professional instrument knowledge and production techniques.")
    print("=" * 60)
    
    demo_enhanced_detection()
    demo_instrument_classification()
    demo_professional_knowledge()
    demo_keyword_expansion()
    demo_comprehensive_instrument_info()
    
    print("\n" + "=" * 60)
    print("✨ Enhancement Complete!")
    print("Your music tutor now has professional-grade instrument knowledge")
    print("from the Slakh dataset with 34 classes and 187 patches!")
    print("=" * 60)

if __name__ == "__main__":
    main() 