import unittest
from solution import glass_stacking


class GlassStackingTest(unittest.TestCase):
    def test_single_glass(self):
        result = [
            ' *** ',
            ' * * ',
            ' * * ',
            '*****'
        ]
        self.assertEqual(glass_stacking(1), result)

    def test_4_glasses(self):
        result = [
            '    ***    ',
            '    * *    ',
            '    * *    ',
            '   *****   ',
            ' ***   *** ',
            ' * *   * * ',
            ' * *   * * ',
            '***** *****'
        ]
        self.assertEqual(glass_stacking(4), result)

    def test_10_glasses(self):
        result = [
            '          ***          ',
            '          * *          ',
            '          * *          ',
            '         *****         ',
            '       ***   ***       ',
            '       * *   * *       ',
            '       * *   * *       ',
            '      ***** *****      ',
            '    ***   ***   ***    ',
            '    * *   * *   * *    ',
            '    * *   * *   * *    ',
            '   ***** ***** *****   ',
            ' ***   ***   ***   *** ',
            ' * *   * *   * *   * * ',
            ' * *   * *   * *   * * ',
            '***** ***** ***** *****'
        ]
        self.assertEqual(glass_stacking(10), result)

    def test_25_glasses(self):
        result = [
            '                ***                ',
            '                * *                ',
            '                * *                ',
            '               *****               ',
            '             ***   ***             ',
            '             * *   * *             ',
            '             * *   * *             ',
            '            ***** *****            ',
            '          ***   ***   ***          ',
            '          * *   * *   * *          ',
            '          * *   * *   * *          ',
            '         ***** ***** *****         ',
            '       ***   ***   ***   ***       ',
            '       * *   * *   * *   * *       ',
            '       * *   * *   * *   * *       ',
            '      ***** ***** ***** *****      ',
            '    ***   ***   ***   ***   ***    ',
            '    * *   * *   * *   * *   * *    ',
            '    * *   * *   * *   * *   * *    ',
            '   ***** ***** ***** ***** *****   ',
            ' ***   ***   ***   ***   ***   *** ',
            ' * *   * *   * *   * *   * *   * * ',
            ' * *   * *   * *   * *   * *   * * ',
            '***** ***** ***** ***** ***** *****'
        ]
        self.assertEqual(glass_stacking(25), result)


if __name__ == '__main__':
    unittest.main()
