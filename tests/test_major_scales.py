import unittest

import sys, os
sys.path.append(
    os.path.join(
        os.path.dirname(os.path.dirname(__file__)), os.environ["FUNCTIONS_DIR"]
    )
)

from test_settings import TEST_MAJOR_SCALES
from scales import tonic_to_scale

class TestScales(unittest.TestCase):

    NOTES = ['C', 'C#', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

    def test_scales(self):
        for note in self.NOTES:
            with self.subTest(note=note):
                self.assertEqual(tonic_to_scale(tonic=note, scale='major'), TEST_MAJOR_SCALES[note][:7])

if __name__ == "__main__":
    unittest.main()
