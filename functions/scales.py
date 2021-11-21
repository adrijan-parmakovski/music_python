from settings import NOTES, SCALES

from alphabet import degree_to_alph_letter, return_chromatic_scale
from halfsteps import degree_to_halfsteps
from notes import halfsteps_to_note


def tonic_to_scale(
    tonic: str,
    scale: str
    ) -> list:

    chr_ = return_chromatic_scale(tonic)
    
    # find the list of degrees for the given scale
    degrees = SCALES[scale]

    alph = [degree_to_alph_letter(tonic=tonic, degree=degree) for degree in degrees]
    halfsteps = [degree_to_halfsteps(degree) for degree in degrees]

    notes = []

    for i in range(len(halfsteps)):
        note_group = halfsteps_to_note(starting_note=tonic, halfsteps=halfsteps[i])
        
        note = [x for x in note_group if alph[i] in x][0]
        notes.append(note)
    
    return notes


if __name__ == '__main__':
    print(
        tonic_to_scale('C', 'major')
    )