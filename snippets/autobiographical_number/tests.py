from unittest import TestCase

from .solution import is_autobiographical, is_autobiographical_minimized


class AutobiographicalNumberTestCase(TestCase):
    def test_positive(self):
        self.assertTrue(is_autobiographical(1210))
        self.assertTrue(is_autobiographical(6210001000))
        self.assertTrue(is_autobiographical(6210001000))

        self.assertTrue(is_autobiographical_minimized(1210))
        self.assertTrue(is_autobiographical_minimized(6210001000))
        self.assertTrue(is_autobiographical_minimized(6210001000))

    def test_negative(self):
        self.assertFalse(is_autobiographical(22))
        self.assertFalse(is_autobiographical(224122))
        self.assertFalse(is_autobiographical(12345))

        self.assertFalse(is_autobiographical_minimized(22))
        self.assertFalse(is_autobiographical_minimized(224122))
        self.assertFalse(is_autobiographical_minimized(12345))
