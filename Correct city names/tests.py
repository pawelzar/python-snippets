import unittest
from solution import correct_names


class CorrectNamesTest(unittest.TestCase):
    def test_simple(self):
        well_written = [
            'Montpellier',
            'New York'
        ]

        bad_written = [
            'new york',
            'NewYork',
            'montpellier',
        ]

        correct = [
            'New York',
            'New York',
            'Montpellier'
        ]

        self.assertEqual(correct_names(well_written, bad_written), correct)

    def test_same_letters(self):
        well_written = [
            'Kyoto',
            'Tokyo'
        ]

        bad_written = [
            'tokyo'
        ]

        correct = [
            'Tokyo'
        ]

        self.assertEqual(correct_names(well_written, bad_written), correct)

    def test_divided(self):
        well_written = [
            'Saint Petersburg',
            'San Francisco'
        ]

        bad_written = [
            'San Fran Cisco'
        ]

        correct = [
            'San Francisco'
        ]

        self.assertEqual(correct_names(well_written, bad_written), correct)

    def test_good(self):
        well_written = [
            'Helsinki',
            'Hanoi'
        ]

        bad_written = [
            'Helsinki',
            'Hanoi'
        ]

        correct = [
            'Helsinki',
            'Hanoi'
        ]

        self.assertEqual(correct_names(well_written, bad_written), correct)

    def test_diverse_set(self):
        well_written = [
            'Sydney',
            'Newcastle upon Tyne',
            'Marrakech',
            'Le Mans',
            'Vienna'
        ]

        bad_written = [
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

        correct = [
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

        self.assertEqual(correct_names(well_written, bad_written), correct)


if __name__ == '__main__':
    unittest.main()
