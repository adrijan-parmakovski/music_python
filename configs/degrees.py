from settings import MAJOR_SCALE_HALFSTEPS, ALPHABET
from typing import Union

import logging

def degree_to_halfsteps(degree: str) -> int:
    """
    A function returning how many halfstepts from the tonic a given degree is.
    Since non-accented degrees respond to the notes of the major scale, we take the major scale halfsteps as base, and either augment or diminish them based on the degree given.

    For example, the 5th degree from C is G, while the 3b degree would be Eb
    """

    degree_order = degree[0] # return only the degree order, e.g. 3b -> 3
    
    if len(degree) == 1:
        return MAJOR_SCALE_HALFSTEPS[(int(degree_order) - 1) % 7]
    
    if '#' in degree:
        return MAJOR_SCALE_HALFSTEPS[(int(degree_order) - 1) % 7] + 1

    if 'b' in degree:
        return MAJOR_SCALE_HALFSTEPS[(int(degree_order) - 1) % 7] - 1


def degree_to_note_letter(
    degree: str,
    tonic: str
    ) -> str:
    """
    Return the note letter from a given degree
    DOES NOT augment or diminish it.

    e.g. 5th degree from C is G, while 5b will also return G.    
    """

    degree_order = degree[0]
    # 
    ind = ALPHABET.index(tonic[0])
    alph = ALPHABET[ind:] + ALPHABET[:ind]

    return alph[int(degree_order) - 1 % 7]






if __name__ == '__main__':
    print(
        degree_to_note_letter('5', 'C')
    )
