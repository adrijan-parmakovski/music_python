from settings import INTERVALS_BY_HALFSTEPS, MAJOR_SCALE_HALFSTEPS, NOTES
from alphabet import return_chromatic_scale, return_note_letter, tonic_to_alph_order

from degrees import degree_order


def interval_to_halfsteps(interval: str) -> int:
    # return the number of halfsteps an interval covers

    for hs, intervals in INTERVALS_BY_HALFSTEPS.items():
        if interval in intervals:
            return hs


def degree_to_halfsteps(degree: str) -> int:
    """
    A function returning how many halfstepts from the tonic a given degree is.
    Since non-accented degrees respond to the notes of the major scale, we take the major scale halfsteps as base, and either augment or diminish them based on the degree given.

    For example, the 5th degree from C is G, while the 3b degree would be Eb
    """

    deg_ord = degree_order(degree=degree) # return only the degree order, e.g. 3b -> 3
    
    if len(degree) == 1:
        return MAJOR_SCALE_HALFSTEPS[(int(deg_ord) - 1) % 7]
    
    if '#' in degree:
        return MAJOR_SCALE_HALFSTEPS[(int(deg_ord) - 1) % 7] + 1

    if 'b' in degree:
        return MAJOR_SCALE_HALFSTEPS[(int(deg_ord) - 1) % 7] - 1


def notes_to_halfsteps(notes: list) -> int:
    """
    Determine how many halfsteps apart two given notes are.

    The function creates a chromatic scale based on the first note in list, and returns in which place the second note is in the list.
    That directly corresponds to the number of halfsteps those notes would be apart.
    """

    chr_ = return_chromatic_scale(notes[0]) # return chromatic scale based on first note

    for note in chr_:
        if notes[1] in note:
            return chr_.index(note)


def notes_to_halfsteps(notes: list) -> int:
    """
    Determines how many halfsteps apart the notes are.
    
    Steps:
        - return the chromatic scale starting at the first note
        - find the index of the note group containing the second note
    """

    chr_ = return_chromatic_scale(notes[0])

    for i in range(len(chr_)):
        if notes[1] in chr_[i]:
            return i
   

if __name__ == '__main__':
    print(interval_to_halfsteps('M3'))
    print(notes_to_halfsteps(['C', 'G']))