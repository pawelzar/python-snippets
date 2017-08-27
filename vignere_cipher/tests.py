import unittest
from .solution import decrypt_vigenere


class VigenereCipherTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(decrypt_vigenere('cpfioiang', 'abcabcabc'),
                         'codingame')


if __name__ == '__main__':
    unittest.main()
