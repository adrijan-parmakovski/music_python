from settings import INTERVALS_BY_HALFSTEPS

from alphabet import tonic_to_alph_order, return_note_letter
from halfsteps import notes_to_halfsteps


def notes_to_interval(notes: list) -> str:
    """
    Returns the interval name given two notes.

    Steps:
        - looks at how many halfsteps the notes are apart
        - determines by the note letters what degree would be between these notes
        - from the list of intervals by halfsteps, picks the one that corresponds to the degree
    """

    alph = tonic_to_alph_order(
        return_note_letter(notes[0])
    )
    degree = str(alph.index(
        return_note_letter(notes[1])
    ) + 1)

    hs = notes_to_halfsteps(notes)
    print(hs)
    INTERVALS_BY_HALFSTEPS[hs]

    return [x for x in INTERVALS_BY_HALFSTEPS[hs] if degree in x][0]

if __name__ == '__main__':

    print(notes_to_interval(['C', 'Cb']))

