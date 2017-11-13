from unittest import TestCase

from .solution import insert_to_palindrom


class InsertToPalindromTestCase(TestCase):
    def test_beginning(self):
        self.assertEqual(insert_to_palindrom('aa'), 0)

    def test_middle(self):
        self.assertEqual(insert_to_palindrom('aabcaa'), 2)

    def test_already_palindrom(self):
        self.assertEqual(insert_to_palindrom('abccba'), 2)
        self.assertEqual(insert_to_palindrom('abcdcba'), 3)

    def test_impossible(self):
        self.assertEqual(insert_to_palindrom('bcaa'), -1)
