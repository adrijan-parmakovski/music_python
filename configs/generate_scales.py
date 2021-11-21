
from scales import (
    ALPHABET,
    NOTES,
    MAJOR_SCALE_HALFSTEPS,
    SCALES,
    SHARP_SIGN, FLAT_SIGN,
    INTERVALS_BY_SEMITONES,
    CHORDS_BY_INTERVAL
)
import json
import sys
import logging

START = sys.argv[1] if len(sys.argv) > 1 else 'C'
SCALE = sys.argv[2] if len(sys.argv) > 2 else 'major'

MAJOR_SCALE_DEGREES = SCALES['major']

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


def aug_dim_note(note: str, halfsteps: int) -> str:
    # find a note in the chromatic_scale that's that many halfsteps away and has the same note name
    
    note_name = note[0] # e.g. C# -> C
    chr_ = chromatic_scale(tonic_=note)

    note_group = chr_[halfsteps + 12 % 12]
    for x in note_group:
        if note_name in x:
            logging.info(f'Note {note} changed by {halfsteps} halfsteps returns note {x}.')
            return x


def find_intervals_hs(interval: str = 'P5') -> int:

    for key in INTERVALS_BY_SEMITONES:
        if interval in INTERVALS_BY_SEMITONES[key]:
            return key


def return_interval(
    starting_note: str = 'C',
    interval: str = 'P5'
    ) -> str:

    logging.info(f'Looking for the note that is {interval} away from {starting_note}')

    major_scale = scale_from_note(
        tonic_=starting_note,
        scale='major'
    )
    major_scale.append(starting_note)
    major_hs = MAJOR_SCALE_HALFSTEPS + [12]

    degree = int(interval[1]) # e.g. P5 -> 5
    hs = find_intervals_hs(interval) # find how many halfsteps from the root note the interval goes, e.g. P5 -> 7
    logging.info(f'Interval {interval} is {hs} halfsteps away from the root note.')
    degree_note_hs = major_hs[(degree - 1) % 8]

    return aug_dim_note(
        note=major_scale[(degree - 1) % 8],
        halfsteps = hs - degree_note_hs
    )

def return_chord_notes_by_interval(
    starting_note = 'C',
    interval_name = 'major'
    ):

    interval_steps = CHORDS_BY_INTERVAL[interval_name]

    chord_notes = [starting_note]

    for i in range(len(interval_steps)):
        if i == 0:
            chord_notes.append(return_interval(
                starting_note = starting_note,
                interval=interval_steps[i]
            ))
        elif i > 0:
            chord_notes.append(return_interval(
                starting_note=chord_notes[i],
                interval=interval_steps[i]
            ))
    print(f'\nThe {interval_name} chord starting at {starting_note} is: {chord_notes}.\n')
    # return chord_notes




if __name__ == "__main__":
    return_chord_notes_by_interval(
        starting_note='C',
        interval_name='major'
    )


