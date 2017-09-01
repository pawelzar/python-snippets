from unittest import TestCase

from .solution import is_prime, is_semi_prime


class PrimeTestCase(TestCase):
    def test_positive(self):
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(43))
        self.assertTrue(is_prime(59))
        self.assertTrue(is_prime(107))
        self.assertTrue(is_prime(643))
        self.assertTrue(is_prime(821))

    def test_negative(self):
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(10))
        self.assertFalse(is_prime(350))
        self.assertFalse(is_prime(820))
        self.assertFalse(is_prime(2345))
        self.assertFalse(is_prime(4444))


class SemiPrimeTestCase(TestCase):
    def test_positive(self):
        self.assertTrue(is_semi_prime(4))
        self.assertTrue(is_semi_prime(14))
        self.assertTrue(is_semi_prime(166))
        self.assertTrue(is_semi_prime(8926))
        self.assertTrue(is_semi_prime(9347))
        self.assertTrue(is_semi_prime(2271))
        self.assertTrue(is_semi_prime(5398))
        self.assertTrue(is_semi_prime(8777))

    def test_negative(self):
        self.assertFalse(is_semi_prime(1))
        self.assertFalse(is_semi_prime(2))
        self.assertFalse(is_semi_prime(3))
        self.assertFalse(is_semi_prime(27))
        self.assertFalse(is_semi_prime(810))
        self.assertFalse(is_semi_prime(4342))
        self.assertFalse(is_semi_prime(4444))
