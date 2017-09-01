from unittest import TestCase

from .solution import slide_down


class GravityTestCase(TestCase):
    def test_single_element(self):
        art = [
            '.'
        ]

        result = [
            '.'
        ]

        self.assertEqual(slide_down(art), result)

    def test_one_fall(self):
        art = [
            '#',
            '.'
        ]

        result = [
            '.',
            '#'
        ]

        self.assertEqual(slide_down(art), result)

    def test_small_array(self):
        art = [
            '#.#',
            '.#.'
        ]

        result = [
            '...',
            '###'
        ]

        self.assertEqual(slide_down(art), result)

    def test_medium_array(self):
        art = [
            '...#...#.#.#...#.',
            '.#..#...#....#...',
            '..........#......',
            '..###...###..##..',
            '#################'
        ]

        result = [
            '.................',
            '.................',
            '...##...###..#...',
            '.####..#####.###.',
            '#################'
        ]

        self.assertEqual(slide_down(art), result)

    def test_large_array(self):
        art = [
            '#####.#####.####..#####.#...#.#####.#####.#...#.#####',
            '#.....#...#.#...#...#...##..#.#.....#...#.##.##.#....',
            '#.....#...#.#...#...#...#.#.#.#.###.#####.#.#.#.###..',
            '#.....#...#.#...#...#...#..##.#..#..#...#.#...#.#....',
            '#####.#####.####..#####.#...#.####..#...#.#...#.#####'
        ]

        result = [
            '#.....#...#.#.......#...#...#.#.....#...#.#...#.#....',
            '#.....#...#.#.......#...#...#.#..#..#...#.#...#.#....',
            '#.....#...#.#...#...#...#...#.#.##..#...#.#...#.###..',
            '#####.#####.#####.#####.#...#.#####.#####.#...#.#####',
            '#####.#####.#####.#####.#####.#####.#####.#####.#####'
        ]

        self.assertEqual(slide_down(art), result)
