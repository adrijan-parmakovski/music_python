
from sys import float_repr_style


SHARP_SIGN = '\u266F'
FLAT_SIGN = '\u266D'

def pprint_note(note: str) -> str:
    return note.replace('b', FLAT_SIGN).replace('#', SHARP_SIGN)



def print_music_theory(
    tonic: str = 'C'
    ) -> dict:

    

    return None