from unittest import TestCase

from .solution import decrypt_vigenere


class VigenereCipherTestCase(TestCase):
    def test_basic(self):
        self.assertEqual(
            decrypt_vigenere('cpfioiang', 'abcabcabc'), 'codingame'
        )
