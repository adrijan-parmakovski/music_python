import unittest

import sys, os
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)), os.environ["FUNCTIONS_DIR"]
    )
)

from test_settings import TEST_REVERSE_INTERVALS
from intervals import notes_to_interval

class TestReverseIntervals(unittest.TestCase):

    NOTES = ['C', 'Dbb', 'Db', 'C#', 'D', 'Ebb', 'Eb', 'D#', 'E', 'Fb', 'F', 'E#', 'Gb', 'F#', 'G', 'Abb', 'Ab', 'G#', 'A', 'Bbb', 'Bb', 'A#', 'B', 'Cb', 'B#']

    def test_reverse_intervals(self):
        for note in self.NOTES:
            notes = ['C', note]
            with self.subTest(notes=notes):
                self.assertEqual(
                    notes_to_interval(notes),
                    [key for key in list(TEST_REVERSE_INTERVALS.keys()) if notes == TEST_REVERSE_INTERVALS[key]][0] # real interval name
                )

if __name__ == "__main__":
    unittest.main()
