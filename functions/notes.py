from settings import MAJOR_SCALE_HALFSTEPS

from halfsteps import interval_to_halfsteps, degree_to_halfsteps
from alphabet import return_chromatic_scale, degree_to_alph_letter

import logging


def aug_dim_note(
    note: str,
    halfsteps: int
    ) -> str:
    """
    Augment or diminish a note, by a certain number of halfsteps.

    Steps:
        - get the note name
        - find the note name that is as many halfsteps away in the chromatic scale, and has the same note name, e.g
    """
    
    note_name = note[0] # e.g. C# -> C
    chr_ = return_chromatic_scale(tonic=note)

    note_group = chr_[halfsteps + 12 % 12] # e.g. return the 10th note group if the change is supposed to be -2 halfsteps
    for x in note_group:
        if note_name in x:
            logging.info(f'Note {note} changed by {halfsteps} halfsteps returns note {x}.')
            return x


def degree_to_note(
    starting_note: str,
    degree: str
    ) -> str:
    """
    Return the note from a given degree.
    """

    chr_ = return_chromatic_scale(starting_note)

    note_letter = degree_to_alph_letter(tonic=starting_note, degree=degree)
    hs = degree_to_halfsteps(degree)

    note_group = chr_[hs]
    
    return [x for x in note_group if note_letter in x][0]


def interval_to_note(
    starting_note: str,
    interval: str
    ) -> str:
    """
    Return the note that is a given interval away from a given starting note.

    Steps:
        - generate the major scale for the given starting note
        - find how many halfsteps away the given interval is
        - find out how many halfsteps the interval is from the major scale degree, e.g m5 is one halfstep away from the 5th degree of the major scale
        - return the note that is as many halfsteps away from the major scale degree
    """

    logging.info(f'Looking for the note that is {interval} away from {starting_note}')
    
    hs = interval_to_halfsteps(interval) # find how many halfsteps from the root note the interval goes, e.g. P5 -> 7
    logging.info(f'Interval {interval} is {hs} halfsteps away from the root note.')

    degree = int(interval[1]) # e.g. P5 -> 5

    major_hs = MAJOR_SCALE_HALFSTEPS + [12]
    degree_note_hs = major_hs[(degree - 1) % 8] # return how many halfsteps away the major scale degree is from the starting note
    
    degree_note = degree_to_note(starting_note, str(degree))

    return aug_dim_note(
        note=degree_note,
        halfsteps = hs - degree_note_hs # the number of halfsteps is the difference between the interval and the major scale degree
    )


def halfsteps_to_note(
    starting_note: str,
    halfsteps: int
    ) -> list:
    """
    Return all possible notes that are given halfsteps away from a starting note
    """

    chr_ = return_chromatic_scale(starting_note)

    return chr_[halfsteps]


if __name__ == '__main__':
    print(
        # halfsteps_to_note(starting_note='C', halfsteps=7)
        # degree_to_note(starting_note='C#', degree='5')
        interval_to_note(starting_note='Db', interval='P5')
    )