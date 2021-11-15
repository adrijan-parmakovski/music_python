NOTES = [
    ['G##', 'A', 'Bbb'],
    ['A#', 'Bb', 'Cbb'],
    ['A##', 'B', 'Cb'],
    ['B#', 'C', 'Dbb'],
    ['B##', 'C#', 'Db'],
    ['C##', 'D', 'Ebb'],
    ['D#', 'Eb', 'Fbb'],
    ['D##', 'E', 'Fb'],
    ['E#', 'F', 'Gbb'],
    ['E##', 'F#', 'Gb'],
    ['F##', 'G', 'Abb'],
    ['G#', 'Ab']
]

ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# Scales in terms of half-steps relative to the tonic degree
MAJOR_SCALE_HALFSTEPS = [0, 2, 4, 5, 7, 9, 11]

SCALES = { # by degrees in relation to the major scale
    'major': ['1', '2', '3', '4', '5', '6', '7'],
    'minor': ['1', '2', '3b', '4', '5', '6b', '7b'],
    'harmonic minor': ['1', '2', '3b', '4', '5', '6b', '7'],
    'Dorian': ['1', '2', '3b', '4', '5', '6', '7b'],
    'Locrian': ['1', '2b', '3b', '4', '5b', '6b', '7b'],
    'Phrygian': ['1', '2b', '3b', '4', '5', '6b', '7b'],
    'major pentatonic': ['1', '2', '3', '5', '6'],
    'harmonic major': ['1', '2', '3', '4', '5', '6b', '7']
}


CHORDS = {
    'major': {
        'I': ['1', '3', '5'],
        'ii': ['2', '4', '6'],
        'iii': ['3', '5', '7'],
        'IV': ['4', '6', '1'],
        'V': ['5', '7', '2'],
        'vi': ['6', '1', '3'],
        'vii˚': ['7', '2', '4']
    }
}

SHARP_SIGN = '\u266f'
FLAT_SIGN = '\u266d'


INTERVALS_BY_SEMITONES = {
    0: ['P1', 'd2'],
    1: ['m2', 'A1'],
    2: ['M2', 'd3'],
    3: ['m3', 'A2'],
    4: ['M3', 'd4'],
    5: ['P4', 'A3'],
    6: ['d5', 'A4'],
    7: ['P5', 'd6'],
    8: ['m6', 'A5'],
    9: ['M6', 'd7'],
    10: ['m7', 'A6'],
    11: ['M7', 'd8'],
    12: ['P8', 'A7']
}

