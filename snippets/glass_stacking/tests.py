from unittest import TestCase

from .solution import glass_stack


class GlassStackingTestCase(TestCase):
    def test_single_glass(self):
        result = [
            ' *** ',
            ' * * ',
            ' * * ',
            '*****'
        ]

        self.assertEqual(glass_stack(1), result)

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

        self.assertEqual(glass_stack(4), result)

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

        self.assertEqual(glass_stack(10), result)

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

        self.assertEqual(glass_stack(21), result)
        self.assertEqual(glass_stack(22), result)
        self.assertEqual(glass_stack(23), result)
        self.assertEqual(glass_stack(24), result)
        self.assertEqual(glass_stack(25), result)
        self.assertEqual(glass_stack(26), result)
        self.assertEqual(glass_stack(27), result)

        self.assertNotEqual(glass_stack(28), result)
        self.assertNotEqual(glass_stack(29), result)
