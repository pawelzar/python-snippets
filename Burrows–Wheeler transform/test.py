import unittest
from solution import bw_transform


class BWTransformTest(unittest.TestCase):
    def testPositive(self):
        self.assertEqual(bw_transform("BAHAMAS"), "4BHMSAAA")

    def testNegative(self):
        self.assertNotEqual(bw_transform("BAHAMAS"), "7SBAHAMA")


if __name__ == '__main__':
    unittest.main()
