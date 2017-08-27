import unittest
from .solution import correct_names


class CorrectNamesTestCase(unittest.TestCase):
    def test_basic(self):
        correct = [
            'Montpellier',
            'New York'
        ]

        incorrect = [
            'new york',
            'NewYork',
            'montpellier',
        ]

        corrected = [
            'New York',
            'New York',
            'Montpellier'
        ]

        self.assertEqual(correct_names(correct, incorrect), corrected)

    def test_same_letters(self):
        correct = [
            'Kyoto',
            'Tokyo'
        ]

        incorrect = [
            'tokyo'
        ]

        corrected = [
            'Tokyo'
        ]

        self.assertEqual(correct_names(correct, incorrect), corrected)

    def test_divided_name(self):
        correct = [
            'Saint Petersburg',
            'San Francisco'
        ]

        incorrect = [
            'San Fran Cisco'
        ]

        corrected = [
            'San Francisco'
        ]

        self.assertEqual(correct_names(correct, incorrect), corrected)

    def test_already_correct(self):
        correct = [
            'Helsinki',
            'Hanoi'
        ]

        incorrect = [
            'Helsinki',
            'Hanoi'
        ]

        corrected = [
            'Helsinki',
            'Hanoi'
        ]

        self.assertEqual(correct_names(correct, incorrect), corrected)

    def test_diverse_set(self):
        correct = [
            'Sydney',
            'Newcastle upon Tyne',
            'Marrakech',
            'Le Mans',
            'Vienna'
        ]

        incorrect = [
            'le mans',
            'Newcastle Upon Tyne',
            'MarraKech',
            'sydney',
            'LeMans',
            'VIENNA',
            'NEWCASTLEuponTYNE',
            'SYDNEY',
            'Marr a kech',
            'Newcastle upon Tyne',
            'vienna',
            'marrakech',
            'Vien na',
            'le Mans',
            'Newcastleupon Tyne',
            'Sydney',
            'Lemans',
            'm A R R A K E C H',
            'VIenna',
            'SydneY'
        ]

        corrected = [
            'Le Mans',
            'Newcastle upon Tyne',
            'Marrakech',
            'Sydney',
            'Le Mans',
            'Vienna',
            'Newcastle upon Tyne',
            'Sydney',
            'Marrakech',
            'Newcastle upon Tyne',
            'Vienna',
            'Marrakech',
            'Vienna',
            'Le Mans',
            'Newcastle upon Tyne',
            'Sydney',
            'Le Mans',
            'Marrakech',
            'Vienna',
            'Sydney'
        ]

        self.assertEqual(correct_names(correct, incorrect), corrected)


if __name__ == '__main__':
    unittest.main()
