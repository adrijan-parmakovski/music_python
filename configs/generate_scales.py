
from scales import ALPHABET, NOTES, MAJOR_SCALE_HALFSTEPS, SCALES, SHARP_SIGN, FLAT_SIGN, INTERVALS_BY_SEMITONES
import json
import sys

START = sys.argv[1] if len(sys.argv) > 1 else 'C'
SCALE = sys.argv[2] if len(sys.argv) > 2 else 'major'

def chromatic_scale(tonic_: str = 'C') -> list:
    
    for i in range(len(NOTES)):
        if tonic_ in NOTES[i]:
            ind = i

    return NOTES[ind:] + NOTES[:ind]

def degrees_to_alph_order(
    degrees: list,
    tonic_: str = 'C'
    ) -> list:

    ind = ALPHABET.index(tonic_[0])
    full_alph = ALPHABET[ind:] + ALPHABET[:ind]

    degs = [int(x[0]) for x in degrees] 
    alphabet_order = [full_alph[(x - 1) % 7] for x in degs]

    return alphabet_order
    

def degrees_to_halfsteps(
    degrees: list
    ) -> list:

    halfsteps = []

    for i in range(len(degrees)):
        if len(degrees[i]) == 1:
            halfsteps.append(
                MAJOR_SCALE_HALFSTEPS[(int(degrees[i][0]) - 1) % 7]
            )
        if '#' in degrees[i]:
            halfsteps.append(
                MAJOR_SCALE_HALFSTEPS[(int(degrees[i][0]) - 1) % 7] + 1
            )
        if 'b' in degrees[i]:
            halfsteps.append(
                MAJOR_SCALE_HALFSTEPS[(int(degrees[i][0]) - 1) % 7] - 1
            )
    
    return halfsteps


def halfsteps_to_scale(
    alph_order: list,
    chromatic_scale: list,
    halfsteps: list
    ) -> list:

    note_groups = [chromatic_scale[i] for i in halfsteps]

    scale_notes = []

    for i in range(len(note_groups)):
        scale_notes.extend([x for x in note_groups[i] if alph_order[i] in x])
    
    return scale_notes


def scale_from_note(
    tonic_: str = 'C',
    scale: str = 'major'
    ) -> dict:

    chr_ = chromatic_scale(tonic_)

    alph = degrees_to_alph_order(tonic_=tonic_, degrees=SCALES[scale])
    hs = degrees_to_halfsteps(SCALES[scale])
    notes = halfsteps_to_scale(alph_order=alph, chromatic_scale=chr_, halfsteps=hs)

    return notes


def fix_notation(note: str) -> str:
    return note.replace('#', SHARP_SIGN).replace('b', FLAT_SIGN)


# def aug_dim_note(note: str, halfsteps: int) -> str:

    # find a note in the chromatic_scale that's that many halfsteps away and has the same note name




def find_intervals_hs(interval: str = 'P5') -> int:

    for key in INTERVALS_BY_SEMITONES:
        if interval in INTERVALS_BY_SEMITONES[key]:
            return key



def return_interval_from_note(
    starting_note: str = 'C',
    interval: str = 'P5'
    ) -> str:

    # print(f'Getting {interval} from {starting_note}')

    MAJOR_SCALE_HALFSTEPS = scale_from_note(
        tonic_=starting_note,
        scale='major'
    )

    degree = int(interval[1])
    int_type = interval[0]

    hs = find_intervals_hs(interval)

    if int_type in ['P', 'M']:
        return MAJOR_SCALE_HALFSTEPS[(degree - 1) % 7]
    if int_type == 'A':
        return augment_note(MAJOR_SCALE_HALFSTEPS[(degree - 1) % 7])
    if int_type == 'm':
        return diminish_note(MAJOR_SCALE_HALFSTEPS[(degree - 1) % 7])
    if int_type == 'd':
        return diminish_note(diminish_note(MAJOR_SCALE_HALFSTEPS[(degree - 1) % 7]))



TEST_DICT = {'P1': 'C',
 'd2': 'Dbb',
 'm2': 'Db',
 'A1': 'C#',
 'M2': 'D',
 'd3': 'Ebb',
 'm3': 'Eb',
 'A2': 'D#',
 'M3': 'E',
 'd4': 'Fb',
 'P4': 'F',
 'A3': 'E#',
 'd5': 'Gb',
 'A4': 'F#',
 'P5': 'G',
 'd6': 'Abb',
 'm6': 'Ab',
 'A5': 'G#',
 'M6': 'A',
 'd7': 'Bbb',
 'm7': 'Bb',
 'A6': 'A#',
 'M7': 'B',
 'd8': 'Cb',
 'P8': 'C',
 'A7': 'B#'}

    

if __name__ == "__main__":
    # print(scale_from_note(
    #     tonic_=START,
    #     scale=SCALE
    # ))

    intervals = {}
    for i in INTERVALS_BY_SEMITONES:
        for hs in INTERVALS_BY_SEMITONES[i]:
            # intervals[hs] = return_interval_from_note(START, hs)
            print(f'{hs} - {find_intervals_hs(hs)}')

    # print(json.dumps(intervals, indent=4))

    # for key in intervals:
    #     c = intervals[key] == TEST_DICT[key]
    #     if c is False:
    #         print(f'for {key} wrong: {intervals[key]} - RIGHT: {TEST_DICT[key]}')
        # print(f'for {key} the result is {c}')




