#!/usr/bin/env python3
"""
Comprehensive Music Knowledge Demonstration
Shows the three-pillar system: Nashville Numbers + Slakh Instruments + Music Theory
"""

# Import all knowledge systems
try:
    from slakh_instrument_data import (
        get_enhanced_music_keywords,
        is_professional_music_term,
        get_instrument_class,
        get_instrument_info,
        SLAKH_INSTRUMENT_CLASSES,
        MIDI_TO_SLAKH_CLASS
    )
    SLAKH_AVAILABLE = True
except ImportError:
    SLAKH_AVAILABLE = False

try:
    from musictheory_net_data import (
        get_comprehensive_music_theory_keywords,
        is_music_theory_term,
        get_theory_explanation,
        MUSICTHEORY_NET_CURRICULUM,
        CIRCLE_OF_FIFTHS_DATA,
        SCALE_PATTERNS,
        CHORD_CONSTRUCTION
    )
    THEORY_AVAILABLE = True
except ImportError:
    THEORY_AVAILABLE = False

def demo_three_pillar_integration():
    """Demonstrate how the three knowledge systems work together"""
    print("🎵 Three-Pillar Music Knowledge Integration")
    print("=" * 60)
    
    # Example progression analysis using all three systems
    progression = "C - Am - F - G"
    key = "C major"
    
    print(f"Analyzing progression: {progression} in {key}")
    print("-" * 40)
    
    # Pillar 1: Nashville Numbers
    nashville = "1 - 6m - 4 - 5"
    print(f"🎯 NASHVILLE NUMBERS: {nashville}")
    print("   Function: Tonic - Submediant - Subdominant - Dominant")
    print("   Easily transposes to any key")
    
    # Pillar 2: Music Theory Analysis
    print(f"\n📚 MUSIC THEORY ANALYSIS:")
    print("   Roman Numerals: I - vi - IV - V")
    print("   Functional Harmony: Tonic → Tonic → Predominant → Dominant")
    print("   Scale Degrees: 1-3-5, 6-1-3, 4-6-1, 5-7-2")
    print("   Voice Leading: Common tones and stepwise motion")
    
    # Pillar 3: Professional Instrumentation (if available)
    if SLAKH_AVAILABLE:
        print(f"\n🎛️ PROFESSIONAL INSTRUMENTATION:")
        print("   Piano (MIDI 0-3): Full chord voicings with pedal resonance")
        print("   Acoustic Guitar (MIDI 24-25): Strumming or fingerpicking patterns")  
        print("   Electric Guitar (MIDI 26-31): Power chords or clean arpeggios")
        print("   Bass (MIDI 32-39): Root motion outlining 1-6-4-5 progression")
        print("   Strings (MIDI 48-51): Sustained pad with bowing articulations")
        print("   Drums (MIDI 128): Rhythmic foundation supporting harmonic rhythm")
    
    print("\n" + "=" * 60)

def demo_comprehensive_detection():
    """Show enhanced music detection across all systems"""
    print("\n🔍 Comprehensive Music Term Detection")
    print("=" * 50)
    
    test_phrases = [
        # Nashville Numbers
        "What does 2m-5-1 mean in Nashville numbers?",
        "How do you transpose 1-4-5 to different keys?",
        
        # Music Theory
        "Explain the difference between authentic and plagal cadences",
        "What is a secondary dominant chord?",
        "How do you construct a diminished seventh chord?",
        
        # Professional Instruments
        "How do velocity layers work in piano samples?",
        "What's the difference between sul ponticello and arco?",
        "How does round-robin sampling prevent machine gun effect?",
        
        # Combined Knowledge
        "How do you voice a ii-V-I progression on piano using professional samples?",
        "What MIDI programs work best for a 1-6m-4-5 progression?",
        
        # Non-music (should be rejected)
        "What is the weather forecast?",
        "How do I program in Python?"
    ]
    
    for phrase in test_phrases:
        # Check all detection systems
        slakh_detected = is_professional_music_term(phrase) if SLAKH_AVAILABLE else False
        theory_detected = is_music_theory_term(phrase) if THEORY_AVAILABLE else False
        
        # Simple Nashville detection
        nashville_detected = any(term in phrase.lower() for term in [
            'nashville', 'numbers', '1', '2m', '3m', '4', '5', '6m', '7°',
            'chord progression', 'transpose'
        ])
        
        detected_systems = []
        if slakh_detected:
            detected_systems.append("Slakh")
        if theory_detected:
            detected_systems.append("Theory")
        if nashville_detected:
            detected_systems.append("Nashville")
        
        if detected_systems:
            status = f"✅ MUSIC ({', '.join(detected_systems)})"
        else:
            status = "❌ NOT MUSIC"
        
        print(f"{status}: {phrase}")

def demo_professional_arrangements():
    """Show how professional knowledge enhances arrangements"""
    print("\n🎼 Professional Arrangement Knowledge")
    print("=" * 50)
    
    if not SLAKH_AVAILABLE:
        print("Slakh data not available - showing basic examples")
        return
    
    arrangement_scenarios = [
        {
            "style": "Classical String Quartet",
            "progression": "1-6m-4-5",
            "instrumentation": {
                "Violin I": "Melody line with vibrato and bowing articulations",
                "Violin II": "Counter-melody and harmonic support", 
                "Viola": "Inner voices using alto clef",
                "Cello": "Bass line outlining root motion"
            }
        },
        {
            "style": "Jazz Combo",
            "progression": "2m7-57-1maj7",
            "instrumentation": {
                "Piano": "Chord voicings with velocity-sensitive layers",
                "Upright Bass": "Walking bass line connecting chord roots",
                "Drums": "Swing rhythm with ghost notes and dynamics",
                "Saxophone": "Melodic improvisation over changes"
            }
        },
        {
            "style": "Rock Band",
            "progression": "1-b7-4-1",
            "instrumentation": {
                "Electric Guitar": "Power chords with distortion (MIDI 30)",
                "Bass Guitar": "Root motion with pick attack",
                "Drums": "Steady rock beat with rim shots",
                "Keyboard": "Organ or pad sounds for texture"
            }
        }
    ]
    
    for scenario in arrangement_scenarios:
        print(f"\n{scenario['style']} - {scenario['progression']}:")
        for instrument, role in scenario['instrumentation'].items():
            print(f"  • {instrument}: {role}")

def demo_cross_system_knowledge():
    """Show how knowledge systems enhance each other"""
    print("\n🔗 Cross-System Knowledge Integration")
    print("=" * 50)
    
    examples = [
        {
            "concept": "Dominant Seventh Chord",
            "nashville": "57 - Creates tension, resolves to 1",
            "theory": "Major triad + minor 7th, contains tritone (3rd & 7th)",
            "professional": "Often sampled with multiple velocity layers for dynamic expression"
        },
        {
            "concept": "Voice Leading", 
            "nashville": "Smooth progression like 1-1/3-4 (stepwise bass)",
            "theory": "Movement of individual voices between chords",
            "professional": "String sections excel at legato voice leading with bowing"
        },
        {
            "concept": "Modulation",
            "nashville": "Change key center - 1 in C becomes 1 in G",
            "theory": "Pivot chords and secondary dominants facilitate key changes",
            "professional": "Orchestral libraries capture modulation through dynamic sampling"
        }
    ]
    
    for example in examples:
        print(f"\n{example['concept']}:")
        print(f"  🎯 Nashville: {example['nashville']}")
        print(f"  📚 Theory: {example['theory']}")
        if SLAKH_AVAILABLE:
            print(f"  🎛️ Professional: {example['professional']}")

def demo_keyword_statistics():
    """Show the massive expansion of music knowledge"""
    print("\n📊 Knowledge Base Statistics")
    print("=" * 50)
    
    stats = {}
    
    # Basic Nashville terms (approximate)
    stats["Nashville Numbers"] = 25
    
    # Slakh professional terms
    if SLAKH_AVAILABLE:
        slakh_keywords = get_enhanced_music_keywords()
        stats["Slakh Professional"] = len(slakh_keywords)
    else:
        stats["Slakh Professional"] = "Not available"
    
    # Music theory terms
    if THEORY_AVAILABLE:
        theory_keywords = get_comprehensive_music_theory_keywords()
        stats["Music Theory"] = len(theory_keywords)
    else:
        stats["Music Theory"] = "Not available"
    
    # Total if available
    total_available = sum(v for v in stats.values() if isinstance(v, int))
    if total_available > stats["Nashville Numbers"]:
        stats["TOTAL ENHANCED"] = total_available
        improvement = total_available / stats["Nashville Numbers"]
        stats["IMPROVEMENT"] = f"{improvement:.1f}x increase"
    
    for category, count in stats.items():
        print(f"  {category}: {count}")

def main():
    """Run comprehensive demonstration"""
    print("🦙 TinyLLAMA Music Tutor - Comprehensive Knowledge Demo")
    print("=" * 70)
    print("This demonstrates the three-pillar knowledge system:")
    print("1. 🎯 Nashville Numbers - Practical chord notation")
    print("2. 🎛️ Slakh Dataset - Professional instrument knowledge") 
    print("3. 📚 Musictheory.net - Comprehensive theoretical foundation")
    print("=" * 70)
    
    # Show availability
    print("Knowledge Systems Available:")
    print(f"  ✅ Nashville Numbers: Always available")
    print(f"  {'✅' if SLAKH_AVAILABLE else '❌'} Slakh Professional: {SLAKH_AVAILABLE}")
    print(f"  {'✅' if THEORY_AVAILABLE else '❌'} Music Theory: {THEORY_AVAILABLE}")
    print()
    
    demo_three_pillar_integration()
    demo_comprehensive_detection()
    demo_professional_arrangements()
    demo_cross_system_knowledge()
    demo_keyword_statistics()
    
    print("\n" + "=" * 70)
    print("🎵 COMPREHENSIVE MUSIC KNOWLEDGE INTEGRATION COMPLETE!")
    print("Your music tutor now combines:")
    print("• Practical Nashville numbers for musicians")
    print("• Professional instrument knowledge from industry datasets") 
    print("• Complete music theory curriculum from educational resources")
    print("• Seamless integration across all knowledge domains")
    print("=" * 70)

if __name__ == "__main__":
    main() 