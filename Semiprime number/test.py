import unittest
from solution import is_semiprime


class SemiPrimeTest(unittest.TestCase):
    def testPositive(self):
        self.assertEqual(is_semiprime(4), True)
        self.assertEqual(is_semiprime(14), True)
        self.assertEqual(is_semiprime(166), True)
        self.assertEqual(is_semiprime(8926), True)
        self.assertEqual(is_semiprime(9347), True)
        self.assertEqual(is_semiprime(2271), True)
        self.assertEqual(is_semiprime(5398), True)
        self.assertEqual(is_semiprime(8777), True)

    def testNegative(self):
        self.assertEqual(is_semiprime(1), False)
        self.assertEqual(is_semiprime(2), False)
        self.assertEqual(is_semiprime(3), False)
        self.assertEqual(is_semiprime(27), False)
        self.assertEqual(is_semiprime(810), False)
        self.assertEqual(is_semiprime(4342), False)
        self.assertEqual(is_semiprime(4444), False)


if __name__ == '__main__':
    unittest.main()
