from functions.settings import INTERVALS_BY_HALFSTEPS

from functions.alphabet import tonic_to_alph_order, return_note_letter
from functions.halfsteps import notes_to_halfsteps


def notes_to_interval(notes: list) -> str:
    """
    Returns the interval name given two notes.

    Steps:
        - looks at how many halfsteps the notes are apart
        - determines by the note letters what degree would be between these notes
        - from the list of intervals by halfsteps, picks the one that corresponds to the degree
    """

    first_note_letter = return_note_letter(notes[0])
    second_note_letter = return_note_letter(notes[1])
    
    alph = tonic_to_alph_order(
        first_note_letter
    )
    degree = str(alph.index(
        second_note_letter
    ) + 1)

    hs = notes_to_halfsteps(notes)
    INTERVALS_BY_HALFSTEPS[hs]

    if second_note_letter == first_note_letter and hs == 11:
        degree = '8'
    if degree == '7' and hs == 0:
        hs = 12

    return [x for x in INTERVALS_BY_HALFSTEPS[hs] if degree in x][0]

if __name__ == '__main__':

    print(notes_to_interval(['C', 'Cb']))

