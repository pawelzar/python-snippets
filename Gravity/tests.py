import unittest
from solution import slide_down


class GravityTest(unittest.TestCase):
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

    def test_simple(self):
        art = [
            '#.#',
            '.#.'
        ]

        result = [
            '...',
            '###'
        ]

        self.assertEqual(slide_down(art), result)

    def test_medium(self):
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

    def test_large(self):
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


if __name__ == '__main__':
    unittest.main()
