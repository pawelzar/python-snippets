from unittest import TestCase

from .solution import grid_with_distance, manhattan_distance


class ManhattanDistanceTestCase(TestCase):
    def test_positive_points(self):
        point_1 = (0, 5)
        point_2 = (2, 2)

        self.assertEqual(manhattan_distance(point_1, point_2), 5)

    def test_negative_points(self):
        point_1 = (-3, 0)
        point_2 = (2, 3)

        self.assertEqual(manhattan_distance(point_1, point_2), 8)

    def test_same_horizontal_axis(self):
        point_1 = (0, -3)
        point_2 = (0, 0)

        self.assertEqual(manhattan_distance(point_1, point_2), 3)

    def test_same_vertical_axis(self):
        point_1 = (12, 0)
        point_2 = (5, 0)

        self.assertEqual(manhattan_distance(point_1, point_2), 7)


class GridWithDistanceTestCase(TestCase):
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
