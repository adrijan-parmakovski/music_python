from functions.settings import INTERVALS_BY_HALFSTEPS
import re

def interval_to_degree(interval: str) -> str:
    return re.search('[0-9]', interval).group() # e.g. m3 -> 3

def notes_to_degree(notes: list) -> str:
    return None

def degree_order(degree: str) -> int:
    return re.search('[0-9]', degree).group()