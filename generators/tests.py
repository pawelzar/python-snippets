import unittest
from .generators import Generator as g


class SquaresGeneratorTest(unittest.TestCase):
    def test_simple(self):
        sq = g.squares()
        self.assertEqual(next(sq), 1,
                         'Should return 1.')
        self.assertEqual(next(sq), 1,
                         'Should return square of 1.')
        self.assertEqual(next(sq), 2,
                         'Should return 2.')
        self.assertEqual(next(sq), 4,
                         'Should return square of 2.')

    def test_listed_squares(self):
        squares_generator = g.squares()
        generated = {}

        for i in range(10):
            number = next(squares_generator)
            square = next(squares_generator)
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
            10: 100
        }

        self.assertEqual(generated, proper)


class FibonacciGeneratorTest(unittest.TestCase):
    def test_empty(self):
        generated = [x for x in g.fibonacci(0)]
        self.assertEqual(generated, [], 'Should return empty list.')

    def test_singular(self):
        generated = [x for x in g.fibonacci(1)]
        self.assertEqual(generated, [0], 'Should return only one element.')

    def test_few(self):
        generated = [x for x in g.fibonacci(6)]
        self.assertEqual(generated, [0, 1,	1, 2, 3, 5],
                         'Should return 6 numbers from Fibonacci sequence.')

    def test_many(self):
        generated = [x for x in g.fibonacci(20)]
        proper = [0, 1,	1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377,
                  610, 987, 1597, 2584, 4181]
        self.assertEqual(generated, proper,
                         'Should return 20 numbers from Fibonacci sequence.')


class SplitGeneratorTest(unittest.TestCase):
    def test_simple(self):
        split_generator = g.split('This is a sample sentence', 'is')
        generated = []

        try:
            while True:
                word = next(split_generator)
                generated.append(word)
        except StopIteration:
            pass

        self.assertEqual(generated, ['Th', ' ', ' a sample sentence'])


if __name__ == '__main__':
    unittest.main()
