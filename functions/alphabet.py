from settings import ALPHABET, NOTES

def tonic_to_alph_order(tonic: str) -> list:
    """"
    Return the alphabet order for a given tonic.
    
    e.g. For C, the alphabet order is: ['C', 'D', 'E', 'F', 'G', 'A', 'B']
    """

    index = ALPHABET.index(tonic[0]) # take the first character, in case the tonic is a flat or sharp
    
    return ALPHABET[index:] + ALPHABET[:index]

def return_chromatic_scale(tonic: str) -> list:
    """
    Return the chromatic scale starting on the given tonic.
    
    Rearranges the NOTES object from settings, to start at the tonic
    """

    for note in NOTES:
        if tonic in note:
            ind = NOTES.index(note)

    return NOTES[ind:] + NOTES[:ind]

def degree_to_alph_letter(
    tonic: str,
    degree: str
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
        tonic_to_alph_order('C')
    )