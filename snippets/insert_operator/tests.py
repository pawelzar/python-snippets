from unittest import TestCase

from .solution import insert_operator


class InsertOperatorTestCase(TestCase):
    def test_addition(self):
        self.assertEqual(insert_operator(3034, 64), '30+34')
        self.assertEqual(insert_operator(3034, 307), '303+4')
        self.assertEqual(insert_operator(3034, 3034), '+3034')

    def test_subtraction(self):
        self.assertEqual(insert_operator(5621, -5621), '-5621')
        self.assertEqual(insert_operator(5621, -616), '5-621')
        self.assertEqual(insert_operator(5621, 561), '562-1')

    def test_division(self):
        self.assertEqual(insert_operator(213, 7), '21/3')
        self.assertEqual(insert_operator(750025, 300), '7500/25')

    def test_multiplication(self):
        self.assertEqual(insert_operator(56, 30), '5*6')
        self.assertEqual(insert_operator(9840, 0), '984*0')
