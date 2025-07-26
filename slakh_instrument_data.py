#!/usr/bin/env python3
"""
Slakh Dataset Instrument Classifications
Enhanced instrument knowledge derived from Slakh2100 dataset
Contains 34 professional instrument classes and detailed MIDI mappings
"""

# Slakh 34 Instrument Classes (professional categorization)
SLAKH_INSTRUMENT_CLASSES = {
    # String Instruments
    'Acoustic Guitar': {
        'description': 'Acoustic steel-string and nylon-string guitars',
        'midi_programs': [24, 25],  # Acoustic Guitar (nylon), Acoustic Guitar (steel)
        'characteristics': 'Natural resonance, percussive attack, harmonic overtones',
        'techniques': ['fingerpicking', 'strumming', 'harmonics', 'alternate picking']
    },
    'Electric Guitar': {
        'description': 'Clean and distorted electric guitars',
        'midi_programs': [26, 27, 28, 29, 30, 31],  # Electric Guitar (jazz to overdriven)
        'characteristics': 'Sustain, distortion, effects processing, dynamic range',
        'techniques': ['bending', 'vibrato', 'palm muting', 'tapping', 'slide']
    },
    'Bass': {
        'description': 'Electric and acoustic bass guitars',
        'midi_programs': [32, 33, 34, 35, 36, 37, 38, 39],  # All bass programs
        'characteristics': 'Low frequency foundation, rhythmic pulse, harmonic support',
        'techniques': ['slapping', 'popping', 'fingerstyle', 'pick playing']
    },
    'Violin': {
        'description': 'Orchestral and solo violin',
        'midi_programs': [40],
        'characteristics': 'Continuous bowing, vibrato, wide dynamic range',
        'techniques': ['legato', 'staccato', 'pizzicato', 'tremolo', 'double stops']
    },
    'Viola': {
        'description': 'Mid-range string instrument',
        'midi_programs': [41],
        'characteristics': 'Warmer than violin, darker tone, alto clef',
        'techniques': ['bowing', 'pizzicato', 'vibrato', 'sul ponticello']
    },
    'Cello': {
        'description': 'Bass-range bowed string instrument',
        'midi_programs': [42],
        'characteristics': 'Rich low frequencies, expressive bowing, wide range',
        'techniques': ['arco', 'pizzicato', 'harmonics', 'thumb position']
    },
    'Contrabass': {
        'description': 'Double bass, orchestral bass',
        'midi_programs': [43],
        'characteristics': 'Lowest string instrument, fundamental bass support',
        'techniques': ['bowing', 'pizzicato', 'slapping']
    },

    # Keyboard Instruments
    'Piano': {
        'description': 'Acoustic grand and upright pianos',
        'midi_programs': [0, 1, 2, 3],  # Grand Piano variations
        'characteristics': 'Percussive attack, sustain pedal, wide dynamic range',
        'techniques': ['legato', 'staccato', 'pedaling', 'voicing', 'articulation']
    },
    'Electric Piano': {
        'description': 'Electric and digital pianos',
        'midi_programs': [4, 5],  # Electric Piano 1 & 2
        'characteristics': 'Bell-like attack, chorus effects, vintage character',
        'techniques': ['velocity sensitivity', 'tremolo', 'effects processing']
    },
    'Harpsichord': {
        'description': 'Baroque keyboard instrument',
        'midi_programs': [6],
        'characteristics': 'Plucked strings, percussive attack, no dynamics',
        'techniques': ['articulation', 'ornamentation', 'registration']
    },
    'Clavinet': {
        'description': 'Funky electric keyboard',
        'midi_programs': [7],
        'characteristics': 'Percussive, funky, often with wah effects',
        'techniques': ['staccato playing', 'effects processing']
    },
    'Organ': {
        'description': 'Hammond and pipe organs',
        'midi_programs': [16, 17, 18, 19, 20, 21, 22, 23],  # All organ types
        'characteristics': 'Sustained tones, drawbar harmonics, rotary speaker',
        'techniques': ['registration', 'drawbar settings', 'leslie speaker effects']
    },

    # Wind Instruments
    'Flute': {
        'description': 'Concert flute family',
        'midi_programs': [73],
        'characteristics': 'Breathy attack, pure tone, wide range',
        'techniques': ['vibrato', 'flutter tonguing', 'breath control']
    },
    'Oboe': {
        'description': 'Double-reed woodwind',
        'midi_programs': [68],
        'characteristics': 'Nasal tone, expressive, difficult intonation',
        'techniques': ['reed control', 'vibrato', 'dynamics']
    },
    'Clarinet': {
        'description': 'Single-reed woodwind',
        'midi_programs': [71],
        'characteristics': 'Woody tone, wide range, register breaks',
        'techniques': ['embouchure control', 'altissimo', 'multiphonics']
    },
    'Saxophone': {
        'description': 'Alto, tenor, soprano, baritone saxophone',
        'midi_programs': [64, 65, 66, 67],  # Soprano, Alto, Tenor, Baritone Sax
        'characteristics': 'Reedy tone, expressive, jazz association',
        'techniques': ['vibrato', 'growling', 'altissimo', 'overtones']
    },
    'Trumpet': {
        'description': 'Brass instrument, highest brass',
        'midi_programs': [56],
        'characteristics': 'Bright, penetrating, fanfare-like',
        'techniques': ['lip trills', 'muting', 'double tonguing', 'valve techniques']
    },
    'French Horn': {
        'description': 'Orchestral brass instrument',
        'midi_programs': [60],
        'characteristics': 'Warm, mellow, complex harmonics',
        'techniques': ['hand stopping', 'lip trills', 'rips']
    },
    'Trombone': {
        'description': 'Slide brass instrument',
        'midi_programs': [57],
        'characteristics': 'Slide glissando, powerful low register',
        'techniques': ['glissando', 'lip trills', 'multiphonics']
    },
    'Tuba': {
        'description': 'Lowest brass instrument',
        'midi_programs': [58],
        'characteristics': 'Deep fundamental, brass choir foundation',
        'techniques': ['breath support', 'articulation', 'pedal tones']
    },

    # Percussion
    'Drums': {
        'description': 'Acoustic drum kit',
        'midi_programs': [128],  # Special drum channel
        'characteristics': 'Percussive transients, rhythmic foundation',
        'techniques': ['rudiments', 'ghost notes', 'dynamics', 'fills']
    },
    'Pitched Percussion': {
        'description': 'Xylophone, marimba, vibes, timpani',
        'midi_programs': [8, 9, 10, 11, 12, 13, 14, 15],  # Chromatic percussion
        'characteristics': 'Mallet instruments, pitch and percussion combined',
        'techniques': ['mallet techniques', 'rolls', 'tremolo']
    },

    # Ethnic & World Instruments
    'Ethnic': {
        'description': 'World music instruments',
        'midi_programs': [104, 105, 106, 107, 108, 109, 110, 111],  # Ethnic instruments
        'characteristics': 'Cultural authenticity, unique timbres',
        'techniques': ['traditional playing methods', 'microtonal inflections']
    },

    # Synthesizers & Electronic
    'Synth Lead': {
        'description': 'Synthesizer lead sounds',
        'midi_programs': [80, 81, 82, 83, 84, 85, 86, 87],  # Synth Lead
        'characteristics': 'Electronic timbres, filter sweeps, modulation',
        'techniques': ['filter modulation', 'LFO effects', 'portamento']
    },
    'Synth Pad': {
        'description': 'Synthesizer pad sounds',
        'midi_programs': [88, 89, 90, 91, 92, 93, 94, 95],  # Synth Pad
        'characteristics': 'Sustained textures, atmospheric, ambient',
        'techniques': ['slow attacks', 'filter sweeps', 'reverb']
    },
    'Synth Effects': {
        'description': 'Special synthesizer effects',
        'midi_programs': [96, 97, 98, 99, 100, 101, 102, 103],  # Synth Effects
        'characteristics': 'Atmospheric, textural, sound design',
        'techniques': ['sound design', 'effects processing']
    },

    # Vocals
    'Voice': {
        'description': 'Human vocals and vocal ensembles',
        'midi_programs': [52, 53, 54, 55],  # Choir and voice sounds
        'characteristics': 'Lyrical content, human expression, formants',
        'techniques': ['vibrato', 'dynamics', 'articulation', 'breath control']
    },

    # Additional Categories
    'Harp': {
        'description': 'Concert harp',
        'midi_programs': [46],
        'characteristics': 'Arpeggiated textures, glissando effects',
        'techniques': ['glissando', 'harmonics', 'pedal techniques']
    },
    'Dulcimer': {
        'description': 'Hammered dulcimer',
        'midi_programs': [15],
        'characteristics': 'Mallet-struck strings, folk character',
        'techniques': ['hammer techniques', 'roll patterns']
    },
    'Banjo': {
        'description': 'Five-string banjo',
        'midi_programs': [105],
        'characteristics': 'Bright, percussive, folk/bluegrass',
        'techniques': ['clawhammer', 'three-finger picking', 'rolls']
    },
    'Fiddle': {
        'description': 'Folk violin playing style',
        'midi_programs': [110],
        'characteristics': 'Folk ornamentation, driving rhythms',
        'techniques': ['shuffle bowing', 'double stops', 'drones']
    },
    'Accordion': {
        'description': 'Bellows-driven reed instrument',
        'midi_programs': [21, 22, 23],
        'characteristics': 'Bellows expression, folk character',
        'techniques': ['bellows control', 'bass/chord accompaniment']
    },
    'Harmonica': {
        'description': 'Diatonic and chromatic harmonica',
        'midi_programs': [22],
        'characteristics': 'Breath-driven, bending notes, blues association',
        'techniques': ['bending', 'overblowing', 'vibrato']
    },
    'Strings': {
        'description': 'Orchestral string sections',
        'midi_programs': [48, 49, 50, 51],  # String ensemble sounds
        'characteristics': 'Lush orchestral textures, bowing articulations',
        'techniques': ['ensemble bowing', 'divisi', 'dynamics']
    }
}

# Enhanced MIDI Program to Instrument Class Mapping
MIDI_TO_SLAKH_CLASS = {
    # Piano Family (0-7)
    0: 'Piano', 1: 'Piano', 2: 'Piano', 3: 'Piano',
    4: 'Electric Piano', 5: 'Electric Piano',
    6: 'Harpsichord', 7: 'Clavinet',
    
    # Chromatic Percussion (8-15)
    8: 'Pitched Percussion', 9: 'Pitched Percussion', 10: 'Pitched Percussion',
    11: 'Pitched Percussion', 12: 'Pitched Percussion', 13: 'Pitched Percussion',
    14: 'Pitched Percussion', 15: 'Dulcimer',
    
    # Organ Family (16-23)
    16: 'Organ', 17: 'Organ', 18: 'Organ', 19: 'Organ',
    20: 'Organ', 21: 'Accordion', 22: 'Harmonica', 23: 'Accordion',
    
    # Guitar Family (24-31)
    24: 'Acoustic Guitar', 25: 'Acoustic Guitar',
    26: 'Electric Guitar', 27: 'Electric Guitar', 28: 'Electric Guitar',
    29: 'Electric Guitar', 30: 'Electric Guitar', 31: 'Electric Guitar',
    
    # Bass Family (32-39)
    32: 'Bass', 33: 'Bass', 34: 'Bass', 35: 'Bass',
    36: 'Bass', 37: 'Bass', 38: 'Bass', 39: 'Bass',
    
    # Strings (40-47)
    40: 'Violin', 41: 'Viola', 42: 'Cello', 43: 'Contrabass',
    44: 'Violin', 45: 'Violin', 46: 'Harp', 47: 'Strings',
    
    # Ensemble (48-55)
    48: 'Strings', 49: 'Strings', 50: 'Strings', 51: 'Strings',
    52: 'Voice', 53: 'Voice', 54: 'Voice', 55: 'Voice',
    
    # Brass (56-63)
    56: 'Trumpet', 57: 'Trombone', 58: 'Tuba', 59: 'Trumpet',
    60: 'French Horn', 61: 'Brass', 62: 'Brass', 63: 'Brass',
    
    # Reed (64-71)
    64: 'Saxophone', 65: 'Saxophone', 66: 'Saxophone', 67: 'Saxophone',
    68: 'Oboe', 69: 'English Horn', 70: 'Bassoon', 71: 'Clarinet',
    
    # Pipe (72-79)
    72: 'Piccolo', 73: 'Flute', 74: 'Recorder', 75: 'Pan Flute',
    76: 'Blown Bottle', 77: 'Shakuhachi', 78: 'Whistle', 79: 'Ocarina',
    
    # Synth Lead (80-87)
    80: 'Synth Lead', 81: 'Synth Lead', 82: 'Synth Lead', 83: 'Synth Lead',
    84: 'Synth Lead', 85: 'Synth Lead', 86: 'Synth Lead', 87: 'Synth Lead',
    
    # Synth Pad (88-95)
    88: 'Synth Pad', 89: 'Synth Pad', 90: 'Synth Pad', 91: 'Synth Pad',
    92: 'Synth Pad', 93: 'Synth Pad', 94: 'Synth Pad', 95: 'Synth Pad',
    
    # Synth Effects (96-103)
    96: 'Synth Effects', 97: 'Synth Effects', 98: 'Synth Effects', 99: 'Synth Effects',
    100: 'Synth Effects', 101: 'Synth Effects', 102: 'Synth Effects', 103: 'Synth Effects',
    
    # Ethnic (104-111)
    104: 'Ethnic', 105: 'Banjo', 106: 'Ethnic', 107: 'Ethnic',
    108: 'Ethnic', 109: 'Ethnic', 110: 'Fiddle', 111: 'Ethnic',
    
    # Percussive (112-119)
    112: 'Pitched Percussion', 113: 'Pitched Percussion', 114: 'Pitched Percussion', 115: 'Pitched Percussion',
    116: 'Pitched Percussion', 117: 'Pitched Percussion', 118: 'Pitched Percussion', 119: 'Pitched Percussion',
    
    # Sound effects (120-127)
    120: 'Synth Effects', 121: 'Synth Effects', 122: 'Synth Effects', 123: 'Synth Effects',
    124: 'Synth Effects', 125: 'Synth Effects', 126: 'Synth Effects', 127: 'Synth Effects',
    
    # Drums (channel 10, program 128 in 0-based)
    128: 'Drums'
}

# Professional synthesis knowledge from Slakh
SYNTHESIS_KNOWLEDGE = {
    'sample_libraries': {
        'description': 'Professional sample-based virtual instruments used in Slakh',
        'examples': [
            'Native Instruments Komplete 12',
            'Professional orchestral libraries',
            'Vintage electric piano samples',
            'Multi-velocity drum samples',
            'Guitar amp simulations'
        ]
    },
    'synthesis_techniques': {
        'sampling': 'Multiple velocity layers, round-robin samples, articulation switching',
        'modeling': 'Physical modeling of acoustic instruments',
        'effects': 'Reverb, EQ, compression applied during synthesis',
        'dynamics': 'Velocity-sensitive samples with crossfading'
    },
    'multi_track_production': {
        'mixing': 'ITU-R BS.1770-4 loudness normalization',
        'panning': 'Spatial placement of instruments',
        'effects': 'Professional mixing with EQ, compression, reverb',
        'mastering': 'Final level balancing and peak limiting'
    }
}

# Professional instrument terminology for enhanced keyword detection
PROFESSIONAL_INSTRUMENT_TERMS = {
    # Advanced Guitar Terms
    'guitar_advanced': [
        'amp simulation', 'cabinet modeling', 'pickup selection', 'coil splitting',
        'overdrive', 'distortion', 'fuzz', 'chorus', 'delay', 'reverb',
        'wah pedal', 'volume swells', 'feedback', 'sustain', 'attack',
        'les paul', 'stratocaster', 'telecaster', 'hollow body', 'semi-hollow'
    ],
    
    # Advanced Piano Terms
    'piano_advanced': [
        'velocity layers', 'pedal resonance', 'string resonance', 'hammer noise',
        'release samples', 'una corda', 'sostenuto pedal', 'soft pedal',
        'prepared piano', 'pianissimo', 'fortissimo', 'voicing'
    ],
    
    # Professional Brass Terms
    'brass_advanced': [
        'embouchure', 'mouthpiece', 'valve technique', 'slide positions',
        'lip trills', 'double tonguing', 'triple tonguing', 'flutter tonguing',
        'stopped horn', 'open horn', 'muted trumpet', 'harmon mute', 'cup mute'
    ],
    
    # Professional Woodwind Terms
    'woodwind_advanced': [
        'reed strength', 'embouchure', 'altissimo', 'multiphonics',
        'circular breathing', 'flutter tonguing', 'key clicks', 'subtone',
        'growling', 'honking', 'bending', 'pitch bending'
    ],
    
    # Professional String Terms
    'strings_advanced': [
        'bowing technique', 'bow pressure', 'bow speed', 'bow placement',
        'sul ponticello', 'sul tasto', 'col legno', 'pizzicato', 'arco',
        'harmonics', 'double stops', 'vibrato', 'portamento', 'glissando'
    ],
    
    # Professional Drum Terms
    'drums_advanced': [
        'ghost notes', 'flams', 'paradiddles', 'rolls', 'rim shots',
        'cross sticking', 'hi-hat control', 'bass drum technique',
        'snare tuning', 'cymbal technique', 'polyrhythms', 'linear playing'
    ],
    
    # Professional Synthesis Terms
    'synthesis_advanced': [
        'oscillator', 'filter cutoff', 'resonance', 'envelope', 'ADSR',
        'LFO', 'modulation', 'frequency modulation', 'amplitude modulation',
        'ring modulation', 'granular synthesis', 'wavetable synthesis',
        'additive synthesis', 'subtractive synthesis'
    ],
    
    # Professional Production Terms
    'production_advanced': [
        'sample rate', 'bit depth', 'latency', 'buffer size', 'MIDI CC',
        'velocity sensitivity', 'aftertouch', 'pitch bend', 'modulation wheel',
        'expression pedal', 'breath controller', 'round robin sampling'
    ]
}

# Enhanced music keywords combining current system with Slakh professional terms
def get_enhanced_music_keywords():
    """Return comprehensive music keywords including Slakh-derived professional terms"""
    
    # Flatten all professional terms into a single set
    professional_terms = set()
    for category in PROFESSIONAL_INSTRUMENT_TERMS.values():
        professional_terms.update(category)
    
    # Instrument class names
    instrument_names = set(SLAKH_INSTRUMENT_CLASSES.keys())
    
    # Combine with existing keywords (maintaining current functionality)
    current_keywords = {
        # Nashville Numbers
        'nashville', 'numbers', 'number system', 'chord progression', 'chord progressions',
        # Basic Music Theory  
        'music', 'musical', 'theory', 'chord', 'chords', 'scale', 'scales', 'key', 'keys',
        'note', 'notes', 'interval', 'intervals', 'harmony', 'harmonic', 'melody', 'melodic',
        'rhythm', 'rhythmic', 'tempo', 'beat', 'measure', 'measures', 'bar', 'bars',
        # Basic instruments (keeping for compatibility)
        'guitar', 'piano', 'bass', 'drums', 'violin', 'cello', 'trumpet', 'saxophone',
        'keyboard', 'synth', 'organ', 'ukulele', 'mandolin', 'banjo', 'harmonica',
    }
    
    return current_keywords | professional_terms | {name.lower() for name in instrument_names}

# Function to get instrument class from MIDI program number
def get_instrument_class(midi_program):
    """Get Slakh instrument class from MIDI program number"""
    return MIDI_TO_SLAKH_CLASS.get(midi_program, 'Unknown')

# Function to get detailed instrument information
def get_instrument_info(class_name):
    """Get detailed information about an instrument class"""
    return SLAKH_INSTRUMENT_CLASSES.get(class_name, {})

# Function to check if term is related to professional music/instruments
def is_professional_music_term(text):
    """Enhanced music term detection using Slakh-derived professional terminology"""
    text_lower = text.lower()
    enhanced_keywords = get_enhanced_music_keywords()
    
    # Check for any enhanced keywords
    for keyword in enhanced_keywords:
        if keyword in text_lower:
            return True
    
    # Check instrument class names (case insensitive)
    for class_name in SLAKH_INSTRUMENT_CLASSES.keys():
        if class_name.lower() in text_lower:
            return True
    
    return False 