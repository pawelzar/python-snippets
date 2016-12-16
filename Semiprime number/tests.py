import unittest
from solution import is_semiprime


class SemiPrimeTest(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(is_semiprime(4))
        self.assertTrue(is_semiprime(14))
        self.assertTrue(is_semiprime(166))
        self.assertTrue(is_semiprime(8926))
        self.assertTrue(is_semiprime(9347))
        self.assertTrue(is_semiprime(2271))
        self.assertTrue(is_semiprime(5398))
        self.assertTrue(is_semiprime(8777))

    def test_negative(self):
        self.assertFalse(is_semiprime(1))
        self.assertFalse(is_semiprime(2))
        self.assertFalse(is_semiprime(3))
        self.assertFalse(is_semiprime(27))
        self.assertFalse(is_semiprime(810))
        self.assertFalse(is_semiprime(4342))
        self.assertFalse(is_semiprime(4444))


if __name__ == '__main__':
    unittest.main()
