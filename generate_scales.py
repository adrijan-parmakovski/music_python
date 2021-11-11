from configs.scales import ALPHABET, NOTES, MAJOR_SCALE, SCALES, SHARP_SIGN, FLAT_SIGN
import json
import sys

START = sys.argv[1] if len(sys.argv) > 1 else 'C'

def return_alphabet_order(tonic_: str = 'C') -> list:
    ind = ALPHABET.index(tonic_[0])
    return ALPHABET[ind:] + ALPHABET[:ind]


def chromatic_scale(tonic_: str = 'C') -> list:
    
    for i in range(len(NOTES)):
        if tonic_ in NOTES[i]:
            ind = i

    return NOTES[ind:] + NOTES[:ind]


def degrees_to_halfsteps(
    degrees: list
    ) -> list:

    halfsteps = []

    for i in range(len(degrees)):
        if len(degrees[i]) == 1:
            halfsteps.append(MAJOR_SCALE[i])
        if '#' in degrees[i]:
            halfsteps.append(MAJOR_SCALE[i] + 1)
        if 'b' in degrees[i]:
            halfsteps.append(MAJOR_SCALE[i] - 1)
    
    return halfsteps


def halfsteps_to_scale(
    alph_order: list,
    chromatic_scale: list,
    halfsteps: list
    ) -> list:

    note_groups = [chromatic_scale[i] for i in halfsteps]

    scale_notes = []

    for i in range(len(note_groups)):
        scale_notes.extend([x.replace('#', SHARP_SIGN).replace('b', FLAT_SIGN) for x in note_groups[i] if alph_order[i] in x])
    
    return scale_notes


def scales_per_note(
    tonic_: str,
    ) -> dict:

    alph = return_alphabet_order(tonic_)
    chr_ = chromatic_scale(tonic_)

    for scale in SCALES:
        print(f'{tonic_} {scale}')
        hs = degrees_to_halfsteps(SCALES[scale])
        notes = halfsteps_to_scale(alph_order=alph, chromatic_scale=chr_, halfsteps=hs)
        print(notes)


    

if __name__ == "__main__":
    scales_per_note(START)

