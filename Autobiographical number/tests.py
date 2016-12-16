import unittest
from solution import is_autobiographical


class AutobiographicalNumberTest(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(is_autobiographical(1210))
        self.assertTrue(is_autobiographical(6210001000))
        self.assertTrue(is_autobiographical(6210001000))

    def test_negative(self):
        self.assertFalse(is_autobiographical(22))
        self.assertFalse(is_autobiographical(224122))
        self.assertFalse(is_autobiographical(12345))


if __name__ == '__main__':
    unittest.main()
