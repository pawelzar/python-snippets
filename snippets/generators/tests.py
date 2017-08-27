from unittest import TestCase

from .generators import Generator


class SquaresGeneratorTestCase(TestCase):
    def test_basic(self):
        squares = Generator.squares()
        self.assertEqual(next(squares), 1,
                         'Should return 1.')
        self.assertEqual(next(squares), 1,
                         'Should return square of 1.')
        self.assertEqual(next(squares), 2,
                         'Should return 2.')
        self.assertEqual(next(squares), 4,
                         'Should return square of 2.')

    def test_listed_squares(self):
        squares = Generator.squares()
        generated = {}

        for i in range(10):
            number = next(squares)
            square = next(squares)
            generated[number] = square

        proper = {
            1: 1,
            2: 4,
            3: 9,
            4: 16,
            5: 25,
            6: 36,
            7: 49,
            8: 64,
            9: 81,
            10: 100,
        }

        self.assertEqual(generated, proper)


class FibonacciGeneratorTestCase(TestCase):
    def test_empty(self):
        generated = [number for number in Generator.fibonacci(0)]
        self.assertEqual(generated, [], 'Should return empty list.')

    def test_singular(self):
        generated = [number for number in Generator.fibonacci(1)]
        self.assertEqual(generated, [0], 'Should return only one element.')

    def test_few(self):
        generated = [number for number in Generator.fibonacci(6)]
        self.assertEqual(generated, [0, 1, 1, 2, 3, 5],
                         'Should return 6 numbers from Fibonacci sequence.')

    def test_many(self):
        generated = [number for number in Generator.fibonacci(20)]
        proper = [
            0, 1, 1, 2, 3, 5, 8, 13, 21,
            34, 55, 89, 144, 233, 377,
            610, 987, 1597, 2584, 4181,
        ]
        self.assertEqual(generated, proper,
                         'Should return 20 numbers from Fibonacci sequence.')


class SplitGeneratorTestCase(TestCase):
    def test_space_separator(self):
        generated = [
            number for number in Generator.split('This is a sample sentence')
        ]

        self.assertEqual(generated, ['This', 'is', 'a', 'sample', 'sentence'])

    def test_word_separator(self):
        generated = [
            number for number in Generator.split(
                'This is a sample sentence', 'is'
            )
        ]

        self.assertEqual(generated, ['Th', ' ', ' a sample sentence'])
