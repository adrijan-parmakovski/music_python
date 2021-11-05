from configs.scales import major, minor, sharp_tones, flat_tones
import json
import sys

START = sys.argv[1] if len(sys.argv) > 1 else 'C'

def major_scale(starting_note: str) -> dict:

    for i in range(0, len(sharp_tones)):
        if sharp_tones[i] == starting_note:
            start_pos = i

    maj_steps = [(i + start_pos) % len(sharp_tones) for i in major]
    maj_scale = [sharp_tones[(i + start_pos) % len(sharp_tones)] for i in major]
    
    return {
        "notes": maj_scale,
        "steps": maj_steps
    }

def minor_scale(major_scale_steps: list) -> dict:

    min_steps = []

    for i in range(0, len(major_scale_steps)):
        if i + 1 in [3, 6, 7]:
            min_steps.append(major_scale_steps[i] - 1)
        else:
            min_steps.append(major_scale_steps[i])

    return {
        'notes': [sharp_tones[i] for i in min_steps],
        'steps': min_steps
    }

def harmonic_minor_scale(major_scale_steps: list) -> dict:

    min_steps = []

    for i in range(0, len(major_scale_steps)):
        if i + 1 in [3, 6]:
            min_steps.append(major_scale_steps[i] - 1)
        else:
            min_steps.append(major_scale_steps[i])

    return {
        'notes': [sharp_tones[i] for i in min_steps],
        'steps': min_steps
    }
    

    

if __name__ == "__main__":
    maj = major_scale(starting_note=START)
    print(f'{START} major')
    print(maj)
    print(f'{START} minor')
    print(minor_scale(major_scale_steps=maj['steps']))
    print(f'{START} harmonic minor')
    print(harmonic_minor_scale(major_scale_steps=maj['steps']))
