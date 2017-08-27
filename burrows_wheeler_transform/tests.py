import unittest
from .solution import bw_transform


class BWTransformTest(unittest.TestCase):
    def test_positive(self):
        self.assertEqual(bw_transform("BAHAMAS"), "4BHMSAAA")

    def test_negative(self):
        self.assertNotEqual(bw_transform("BAHAMAS"), "7SBAHAMA")


if __name__ == '__main__':
    unittest.main()
