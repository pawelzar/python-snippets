import unittest
from solution import is_autobiographical


class AutobiographicalTest(unittest.TestCase):
    def testPositive(self):
        self.assertEqual(is_autobiographical(1210), 1)
        self.assertEqual(is_autobiographical(6210001000), 1)
        self.assertEqual(is_autobiographical(6210001000), 1)

    def testNegative(self):
        self.assertEqual(is_autobiographical(22), 0)
        self.assertEqual(is_autobiographical(224122), 0)
        self.assertEqual(is_autobiographical(12345), 0)


if __name__ == '__main__':
    unittest.main()
