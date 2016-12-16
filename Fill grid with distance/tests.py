import unittest
from solution import grid_with_distance


class GridWithDistanceTest(unittest.TestCase):
    def test_rectangle_4x3(self):
        correct_grid = [
            'X112',
            '1122',
            '122X'
        ]

        params = [4, 3, (0, 0), (3, 2)]

        self.assertEqual(grid_with_distance(*params), correct_grid)

    def test_square_10x10(self):
        correct_grid = [
            '1111111022',
            '1111111022',
            '1111111022',
            '1111111022',
            '1111111022',
            '1111X11022',
            '1111110222',
            '11111022X2',
            '1111102222',
            '1111102222'

        ]

        params = [10, 10, (4, 5), (8, 7)]

        self.assertEqual(grid_with_distance(*params), correct_grid)


if __name__ == '__main__':
    unittest.main()
