#!/usr/bin/env python3
"""
Music Theory Curriculum Data from musictheory.net
Comprehensive music theory knowledge structure for enhanced LLM responses
Based on the complete musictheory.net lessons curriculum
"""

# Complete Music Theory Curriculum Structure
MUSICTHEORY_NET_CURRICULUM = {
    "the_basics": {
        "description": "Fundamental music notation and basic concepts",
        "lessons": {
            "staff": {
                "concepts": ["treble clef", "bass clef", "ledger lines", "grand staff", "alto clef", "tenor clef"],
                "explanation": "The staff is the foundation of music notation, consisting of five lines and four spaces where notes are placed.",
                "key_points": [
                    "Treble clef (G clef) - used for higher pitched instruments and voices",
                    "Bass clef (F clef) - used for lower pitched instruments and voices", 
                    "Ledger lines extend the staff for notes above or below",
                    "Grand staff combines treble and bass clefs for piano music"
                ]
            },
            "note_duration": {
                "concepts": ["whole note", "half note", "quarter note", "eighth note", "sixteenth note", "thirty-second note"],
                "explanation": "Note duration determines how long a sound is held in relation to the beat.",
                "key_points": [
                    "Whole note = 4 beats in 4/4 time",
                    "Half note = 2 beats", 
                    "Quarter note = 1 beat",
                    "Eighth note = 1/2 beat",
                    "Each subdivision divides the previous duration in half"
                ]
            },
            "measures_and_time_signatures": {
                "concepts": ["measure", "bar line", "double bar line", "time signature", "beat", "strong beat", "weak beat"],
                "explanation": "Measures organize music into regular groupings of beats, defined by time signatures.",
                "key_points": [
                    "Time signature: top number = beats per measure, bottom number = note value for one beat",
                    "4/4 time: 4 quarter note beats per measure",
                    "3/4 time: 3 quarter note beats per measure (waltz time)",
                    "2/4 time: 2 quarter note beats per measure (march time)"
                ]
            },
            "rests": {
                "concepts": ["whole rest", "half rest", "quarter rest", "eighth rest", "sixteenth rest", "silence"],
                "explanation": "Rests represent periods of silence with durations corresponding to note values.",
                "key_points": [
                    "Rests have the same duration relationships as notes",
                    "Whole rest hangs from the fourth line",
                    "Half rest sits on the third line",
                    "Quarter rest is the most complex symbol"
                ]
            },
            "dots_and_ties": {
                "concepts": ["dotted note", "tied note", "duration extension", "augmentation"],
                "explanation": "Dots and ties extend note durations beyond basic note values.",
                "key_points": [
                    "Dot adds half the original note value (dotted half = 3 beats)",
                    "Tie connects notes of the same pitch for combined duration",
                    "Ties can cross bar lines, dots cannot",
                    "Multiple dots possible but rare"
                ]
            },
            "steps_and_accidentals": {
                "concepts": ["half step", "whole step", "sharp", "flat", "natural", "enharmonic equivalents"],
                "explanation": "Steps define the distance between pitches, accidentals alter pitch by half steps.",
                "key_points": [
                    "Half step = smallest interval (semitone)",
                    "Whole step = two half steps",
                    "Sharp raises pitch by half step",
                    "Flat lowers pitch by half step",
                    "Natural cancels previous accidental"
                ]
            }
        }
    },
    
    "rhythm_and_meter": {
        "description": "Advanced rhythmic concepts and metric organization",
        "lessons": {
            "simple_meter": {
                "concepts": ["simple meter", "duple", "triple", "quadruple", "beat division", "subdivision"],
                "explanation": "Simple meters divide beats into two equal parts (binary division).",
                "key_points": [
                    "2/4, 3/4, 4/4 are simple meters",
                    "Beat divides into two eighth notes",
                    "Strong beats occur on beat 1 (and 3 in 4/4)",
                    "Conducting patterns reflect meter groupings"
                ]
            },
            "compound_meter": {
                "concepts": ["compound meter", "dotted note beat", "triple subdivision", "6/8", "9/8", "12/8"],
                "explanation": "Compound meters divide beats into three equal parts (ternary division).",
                "key_points": [
                    "6/8, 9/8, 12/8 are compound meters",
                    "Beat is dotted quarter note in compound time",
                    "Beat divides into three eighth notes",
                    "6/8 has two beats per measure (not six)"
                ]
            },
            "odd_meter": {
                "concepts": ["odd meter", "asymmetrical meter", "5/4", "7/8", "mixed meter", "additive rhythm"],
                "explanation": "Odd meters have unusual beat groupings that don't fit standard patterns.",
                "key_points": [
                    "5/4 can be grouped as 3+2 or 2+3",
                    "7/8 common in folk music and progressive rock",
                    "Mixed meters change time signature within pieces",
                    "Requires careful attention to beat groupings"
                ]
            }
        }
    },
    
    "scales_and_key_signatures": {
        "description": "Scale construction, key relationships, and tonal organization",
        "lessons": {
            "major_scales": {
                "concepts": ["major scale", "whole step", "half step", "scale pattern", "tonic", "diatonic"],
                "explanation": "Major scales follow the pattern W-W-H-W-W-W-H and establish key centers.",
                "key_points": [
                    "Pattern: Whole-Whole-Half-Whole-Whole-Whole-Half",
                    "Seven different pitches plus octave",
                    "Sounds bright and happy",
                    "Foundation for major key harmony"
                ]
            },
            "minor_scales": {
                "concepts": ["natural minor", "harmonic minor", "melodic minor", "relative minor", "parallel minor"],
                "explanation": "Minor scales create darker moods with different interval patterns.",
                "key_points": [
                    "Natural minor: W-H-W-W-H-W-W",
                    "Harmonic minor: raised 7th scale degree",
                    "Melodic minor: raised 6th and 7th ascending, natural descending",
                    "Relative minor shares key signature with major"
                ]
            },
            "scale_degrees": {
                "concepts": ["tonic", "supertonic", "mediant", "subdominant", "dominant", "submediant", "leading tone"],
                "explanation": "Scale degrees have specific names and harmonic functions.",
                "key_points": [
                    "1st degree: Tonic (home, stability)",
                    "5th degree: Dominant (tension, wants to resolve)",
                    "4th degree: Subdominant (departure from tonic)",
                    "7th degree: Leading tone (pulls to tonic)"
                ]
            },
            "key_signatures": {
                "concepts": ["key signature", "circle of fifths", "order of sharps", "order of flats", "enharmonic keys"],
                "explanation": "Key signatures indicate which notes to play sharp or flat throughout a piece.",
                "key_points": [
                    "Sharps: F# C# G# D# A# E# B#",
                    "Flats: Bb Eb Ab Db Gb Cb Fb",
                    "Circle of fifths shows key relationships",
                    "Major and minor keys share signatures"
                ]
            }
        }
    },
    
    "intervals": {
        "description": "Distance relationships between pitches",
        "lessons": {
            "generic_intervals": {
                "concepts": ["unison", "second", "third", "fourth", "fifth", "sixth", "seventh", "octave"],
                "explanation": "Generic intervals count letter names between pitches.",
                "key_points": [
                    "Count both starting and ending notes",
                    "C to E is a third (C-D-E = 3 letters)",
                    "Quality not specified in generic intervals",
                    "Foundation for specific interval identification"
                ]
            },
            "specific_intervals": {
                "concepts": ["perfect", "major", "minor", "augmented", "diminished", "interval quality"],
                "explanation": "Specific intervals combine generic interval with quality designation.",
                "key_points": [
                    "Perfect intervals: unison, 4th, 5th, octave",
                    "Major/minor intervals: 2nd, 3rd, 6th, 7th",
                    "Augmented = larger than major/perfect",
                    "Diminished = smaller than minor/perfect"
                ]
            },
            "interval_inversion": {
                "concepts": ["interval inversion", "complementary intervals", "compound intervals"],
                "explanation": "Inverted intervals flip the order of pitches and change quality predictably.",
                "key_points": [
                    "Generic intervals add to 9 when inverted",
                    "Perfect intervals stay perfect",
                    "Major becomes minor and vice versa",
                    "Augmented becomes diminished and vice versa"
                ]
            }
        }
    },
    
    "chords": {
        "description": "Harmonic structures built from intervals",
        "lessons": {
            "triads": {
                "concepts": ["triad", "root", "third", "fifth", "major triad", "minor triad", "diminished triad", "augmented triad"],
                "explanation": "Triads are three-note chords built with thirds, forming the basis of tonal harmony.",
                "key_points": [
                    "Major triad: major 3rd + minor 3rd",
                    "Minor triad: minor 3rd + major 3rd", 
                    "Diminished triad: minor 3rd + minor 3rd",
                    "Augmented triad: major 3rd + major 3rd"
                ]
            },
            "seventh_chords": {
                "concepts": ["seventh chord", "major seventh", "minor seventh", "dominant seventh", "half-diminished", "fully diminished"],
                "explanation": "Seventh chords add a seventh above the root to triads, creating richer harmony.",
                "key_points": [
                    "Major 7th: major triad + major 7th",
                    "Minor 7th: minor triad + minor 7th",
                    "Dominant 7th: major triad + minor 7th",
                    "Half-diminished: diminished triad + minor 7th"
                ]
            },
            "chord_inversions": {
                "concepts": ["root position", "first inversion", "second inversion", "third inversion", "bass note"],
                "explanation": "Inversions change which chord tone appears in the bass.",
                "key_points": [
                    "Root position: root in bass",
                    "First inversion: third in bass",
                    "Second inversion: fifth in bass", 
                    "Third inversion: seventh in bass (seventh chords only)"
                ]
            }
        }
    },
    
    "diatonic_chords": {
        "description": "Chords built from scale degrees within a key",
        "lessons": {
            "diatonic_triads": {
                "concepts": ["diatonic harmony", "chord progression", "tonic", "predominant", "dominant", "functional harmony"],
                "explanation": "Diatonic triads are built on each scale degree using only notes from the key.",
                "key_points": [
                    "Major key pattern: I ii iii IV V vi vii°",
                    "Minor key pattern: i ii° III iv v VI VII",
                    "Roman numerals indicate chord quality and scale degree",
                    "Each chord has harmonic function"
                ]
            },
            "roman_numeral_analysis": {
                "concepts": ["roman numerals", "chord symbols", "harmonic analysis", "chord function"],
                "explanation": "Roman numeral analysis shows chord relationships within keys.",
                "key_points": [
                    "Uppercase = major chords",
                    "Lowercase = minor chords", 
                    "° = diminished, + = augmented",
                    "Numbers show inversions (I6, V64)"
                ]
            }
        }
    },
    
    "chord_progressions": {
        "description": "Movement between chords and harmonic rhythm",
        "lessons": {
            "common_progressions": {
                "concepts": ["I-V-I", "ii-V-I", "vi-IV-I-V", "circle of fifths progression", "deceptive cadence"],
                "explanation": "Certain chord progressions create strong harmonic movement and resolution.",
                "key_points": [
                    "I-V-I: strongest progression in tonal music",
                    "ii-V-I: foundation of jazz harmony",
                    "vi-IV-I-V: popular music progression",
                    "Root motion by fifths is strongest"
                ]
            },
            "cadences": {
                "concepts": ["authentic cadence", "plagal cadence", "deceptive cadence", "half cadence"],
                "explanation": "Cadences provide points of rest and closure in musical phrases.",
                "key_points": [
                    "Authentic: V-I (strongest closure)",
                    "Plagal: IV-I (amen cadence)",
                    "Deceptive: V-vi (avoids expected resolution)",
                    "Half: ends on V (creates expectation)"
                ]
            },
            "nonharmonic_tones": {
                "concepts": ["passing tone", "neighbor tone", "suspension", "retardation", "anticipation", "escape tone"],
                "explanation": "Nonharmonic tones add melodic interest while temporarily stepping outside the harmony.",
                "key_points": [
                    "Passing tone: connects chord tones stepwise",
                    "Neighbor tone: steps away and returns",
                    "Suspension: resolves down by step",
                    "Anticipation: jumps early to next chord tone"
                ]
            }
        }
    }
}

# Music Theory Terminology for Enhanced Detection
MUSIC_THEORY_TERMS = {
    # Basic Notation
    "notation_terms": [
        "staff", "clef", "treble clef", "bass clef", "alto clef", "tenor clef",
        "ledger lines", "grand staff", "note head", "stem", "flag", "beam",
        "whole note", "half note", "quarter note", "eighth note", "sixteenth note",
        "dotted note", "tied note", "rest", "measure", "bar line", "time signature"
    ],
    
    # Rhythm and Meter
    "rhythm_terms": [
        "beat", "tempo", "meter", "simple meter", "compound meter", "duple", "triple", "quadruple",
        "syncopation", "polyrhythm", "hemiola", "augmentation", "diminution",
        "anacrusis", "upbeat", "downbeat", "strong beat", "weak beat"
    ],
    
    # Pitch and Scales  
    "pitch_terms": [
        "pitch", "frequency", "octave", "half step", "whole step", "semitone", "tone",
        "sharp", "flat", "natural", "double sharp", "double flat", "enharmonic",
        "scale", "mode", "major scale", "minor scale", "chromatic scale", "pentatonic",
        "blues scale", "whole tone scale", "octatonic scale"
    ],
    
    # Intervals
    "interval_terms": [
        "interval", "unison", "second", "third", "fourth", "fifth", "sixth", "seventh",
        "perfect", "major", "minor", "augmented", "diminished", "tritone",
        "consonant", "dissonant", "compound interval", "interval inversion"
    ],
    
    # Chords and Harmony
    "harmony_terms": [
        "chord", "triad", "seventh chord", "ninth chord", "eleventh chord", "thirteenth chord",
        "root", "third", "fifth", "seventh", "tension", "extension", "alteration",
        "inversion", "root position", "first inversion", "second inversion",
        "voice leading", "doubling", "spacing", "figured bass"
    ],
    
    # Key and Tonality
    "tonality_terms": [
        "key", "key signature", "tonic", "dominant", "subdominant", "relative key", "parallel key",
        "circle of fifths", "modulation", "tonicization", "pivot chord", "common tone",
        "major key", "minor key", "modal", "atonal", "chromatic"
    ],
    
    # Functional Harmony
    "functional_terms": [
        "tonic function", "predominant function", "dominant function",
        "resolution", "preparation", "tendency tone", "leading tone",
        "cadence", "authentic cadence", "plagal cadence", "deceptive cadence", "half cadence",
        "phrase", "period", "antecedent", "consequent"
    ],
    
    # Advanced Concepts
    "advanced_terms": [
        "nonharmonic tone", "passing tone", "neighbor tone", "suspension", "retardation",
        "anticipation", "escape tone", "appoggiatura", "changing tone",
        "secondary dominant", "borrowed chord", "neapolitan chord", "augmented sixth",
        "diminished seventh", "common tone diminished seventh"
    ]
}

# Key Signatures and Circle of Fifths Data
CIRCLE_OF_FIFTHS_DATA = {
    "sharp_keys": {
        "order": ["F#", "C#", "G#", "D#", "A#", "E#", "B#"],
        "major_keys": ["C", "G", "D", "A", "E", "B", "F#", "C#"],
        "minor_keys": ["Am", "Em", "Bm", "F#m", "C#m", "G#m", "D#m", "A#m"],
        "key_signatures": {
            "C": [], "G": ["F#"], "D": ["F#", "C#"], "A": ["F#", "C#", "G#"],
            "E": ["F#", "C#", "G#", "D#"], "B": ["F#", "C#", "G#", "D#", "A#"],
            "F#": ["F#", "C#", "G#", "D#", "A#", "E#"], "C#": ["F#", "C#", "G#", "D#", "A#", "E#", "B#"]
        }
    },
    "flat_keys": {
        "order": ["Bb", "Eb", "Ab", "Db", "Gb", "Cb", "Fb"],
        "major_keys": ["C", "F", "Bb", "Eb", "Ab", "Db", "Gb", "Cb"],
        "minor_keys": ["Am", "Dm", "Gm", "Cm", "Fm", "Bbm", "Ebm", "Abm"],
        "key_signatures": {
            "C": [], "F": ["Bb"], "Bb": ["Bb", "Eb"], "Eb": ["Bb", "Eb", "Ab"],
            "Ab": ["Bb", "Eb", "Ab", "Db"], "Db": ["Bb", "Eb", "Ab", "Db", "Gb"],
            "Gb": ["Bb", "Eb", "Ab", "Db", "Gb", "Cb"], "Cb": ["Bb", "Eb", "Ab", "Db", "Gb", "Cb", "Fb"]
        }
    }
}

# Scale Patterns and Modes
SCALE_PATTERNS = {
    "major_scale": {
        "pattern": ["W", "W", "H", "W", "W", "W", "H"],
        "degrees": ["1", "2", "3", "4", "5", "6", "7"],
        "names": ["tonic", "supertonic", "mediant", "subdominant", "dominant", "submediant", "leading tone"]
    },
    "natural_minor": {
        "pattern": ["W", "H", "W", "W", "H", "W", "W"],
        "degrees": ["1", "2", "b3", "4", "5", "b6", "b7"],
        "names": ["tonic", "supertonic", "mediant", "subdominant", "dominant", "submediant", "subtonic"]
    },
    "modes": {
        "ionian": {"pattern": ["W", "W", "H", "W", "W", "W", "H"], "characteristic": "major scale"},
        "dorian": {"pattern": ["W", "H", "W", "W", "W", "H", "W"], "characteristic": "minor with raised 6th"},
        "phrygian": {"pattern": ["H", "W", "W", "W", "H", "W", "W"], "characteristic": "minor with lowered 2nd"},
        "lydian": {"pattern": ["W", "W", "W", "H", "W", "W", "H"], "characteristic": "major with raised 4th"},
        "mixolydian": {"pattern": ["W", "W", "H", "W", "W", "H", "W"], "characteristic": "major with lowered 7th"},
        "aeolian": {"pattern": ["W", "H", "W", "W", "H", "W", "W"], "characteristic": "natural minor"},
        "locrian": {"pattern": ["H", "W", "W", "H", "W", "W", "W"], "characteristic": "diminished scale"}
    }
}

# Chord Construction Data
CHORD_CONSTRUCTION = {
    "triads": {
        "major": {"intervals": ["M3", "m3"], "formula": "1-3-5", "example": "C-E-G"},
        "minor": {"intervals": ["m3", "M3"], "formula": "1-b3-5", "example": "C-Eb-G"},
        "diminished": {"intervals": ["m3", "m3"], "formula": "1-b3-b5", "example": "C-Eb-Gb"},
        "augmented": {"intervals": ["M3", "M3"], "formula": "1-3-#5", "example": "C-E-G#"}
    },
    "seventh_chords": {
        "major_seventh": {"formula": "1-3-5-7", "quality": "maj7", "example": "Cmaj7"},
        "minor_seventh": {"formula": "1-b3-5-b7", "quality": "m7", "example": "Cm7"}, 
        "dominant_seventh": {"formula": "1-3-5-b7", "quality": "7", "example": "C7"},
        "half_diminished": {"formula": "1-b3-b5-b7", "quality": "ø7", "example": "Cø7"},
        "fully_diminished": {"formula": "1-b3-b5-bb7", "quality": "°7", "example": "C°7"}
    }
}

# Comprehensive Music Theory Keyword Collection
def get_comprehensive_music_theory_keywords():
    """Return all music theory terms for enhanced detection"""
    all_terms = set()
    
    # Add all terminology categories
    for category in MUSIC_THEORY_TERMS.values():
        all_terms.update(category)
    
    # Add curriculum concepts
    for section in MUSICTHEORY_NET_CURRICULUM.values():
        for lesson in section["lessons"].values():
            all_terms.update(lesson["concepts"])
    
    # Add scale and chord terms
    all_terms.update(SCALE_PATTERNS.keys())
    all_terms.update(CHORD_CONSTRUCTION["triads"].keys())
    all_terms.update(CHORD_CONSTRUCTION["seventh_chords"].keys())
    
    return all_terms

# Function to get theory explanation
def get_theory_explanation(concept):
    """Get detailed explanation for a music theory concept"""
    concept_lower = concept.lower()
    
    # Search through curriculum
    for section_name, section in MUSICTHEORY_NET_CURRICULUM.items():
        for lesson_name, lesson in section["lessons"].items():
            if concept_lower in [c.lower() for c in lesson["concepts"]]:
                return {
                    "section": section_name,
                    "lesson": lesson_name,
                    "explanation": lesson["explanation"],
                    "key_points": lesson["key_points"]
                }
    
    return None

# Function to check if term is music theory related
def is_music_theory_term(text):
    """Check if text contains music theory terminology"""
    text_lower = text.lower()
    theory_keywords = get_comprehensive_music_theory_keywords()
    
    for keyword in theory_keywords:
        if keyword.lower() in text_lower:
            return True
    
    return False 