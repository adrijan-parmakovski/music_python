# main note vocabulary, or alphabet
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# All existing notes and their eharmonic equivalents
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


# Major scale in terms of half-steps relative to the tonic
MAJOR_SCALE_HALFSTEPS = [0, 2, 4, 5, 7, 9, 11]
# major scale in terms of degrees
MAJOR_SCALE_DEGREES = ['1', '2', '3', '4', '5', '6', '7']
# major scale in terms of intervals
MAJOR_SCALE_INTERVALS = ['M2', 'M3', 'P4', 'P5', 'M6', 'M7']

# intervals by halfsteps
INTERVALS_BY_HALFSTEPS = {
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

SCALES = {
    'major': ['1', '2', '3', '4', '5', '6', '7'],
    'minor': ['1', '2', 'b3', '4', '5', 'b6', 'b7'],
    'harmonic_minor': ['1', '2', 'b3', '4', '5', 'b6', '7'],
    # duatonic scales
    'ionian': ['1', '2', '3', '4', '5', '6', '7'],
    'dorian': ['1', '2', 'b3', '4', '5', '6', 'b7'],
    'phrygian': ['1', 'b2', 'b3', '4', '5', 'b6', 'b7'],
    'lydian': ['1', '2', '3', '#4', '5', '6', '7'],
    'mixolydian ': ['1', '2', '3', '4', '5', '6', 'b7'],
    'aeolian': ['1', '2', 'b3', '4', '5', 'b6', 'b7'],
    'locrian': ['1', 'b2', 'b3', '4', 'b5', 'b6', 'b7'],
    # pentatonic
    'major_pentatonic': ['1', '2', '3', '5', '7'],
    'minor_pentatonic': ['1', 'b3', '4', '5', 'b7']
}



CHORDS = {
    'major': ['1', '3', '5'],
    'minor': ['1', 'b3', '5'],
    'major_6th': ['1', '3', '5', '6'],
    'minor_6th': ['1', 'b3', '5', '6'],
    'major_7th': ['1', '3', '5', '7'],
    'dominant_7th': ['1', '3', '5', 'b7'],
    'minor_7th': ['1', 'b3', '5', 'b7'],
    'major_9th': ['1', '3', '5', '7', '9'],
    'minor_9th': ['1', 'b3', '5', 'b7', '9'],
    'dominant_9th': ['1', '3', '5', 'b7', '9'],
    'dominant_11th': ['1', '3', '5', 'b7', '9', '11'],
    'major_13th': ['1', '3', '5', '7', '9', '11', '13'],
    'dominant_13th': ['1', '3', '5', 'b7', '9', '11', '13'],
}


SHARP_SIGN = '\u266F'
FLAT_SIGN = '\u266D'

