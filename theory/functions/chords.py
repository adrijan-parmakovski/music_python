from settings import CHORDS
from notes import degree_to_note
import sys

def return_chord_notes(
    root: str,
    chord_name: str
    ) -> list:

    degrees = CHORDS[chord_name]
    chord = [degree_to_note(starting_note=root, degree=degree) for degree in degrees]

    return chord


if __name__ == '__main__':
    print(
        return_chord_notes(root=sys.argv[1], chord_name=sys.argv[2])
    )
