from settings import SCALES

from notes import degree_to_note


def tonic_to_scale(
    tonic: str,
    scale: str
    ) -> list:
    
    # find the list of degrees for the given scale
    degrees = SCALES[scale]

    notes = [degree_to_note(starting_note=tonic, degree=degree) for degree in degrees]
    
    return notes


if __name__ == '__main__':
    print(
        tonic_to_scale('C', 'minor')
    )
