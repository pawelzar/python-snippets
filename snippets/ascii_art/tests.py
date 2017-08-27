from unittest import TestCase

from .solution import ascii_art


class AsciiArtTestCase(TestCase):
    def setUp(self):
        part_a_o = [
            ' #  ##   ## ##  ### ###  ## # # ###  ## # # #   # # ###  #  ',
            '# # # # #   # # #   #   #   # #  #    # # # #   ### # # # # ',
            '### ##  #   # # ##  ##  # # ###  #    # ##  #   ### # # # # ',
            '# # # # #   # # #   #   # # # #  #  # # # # #   # # # # # # ',
            '# # ##   ## ##  ### #    ## # # ###  #  # # ### # # # #  #  ',
        ]

        part_p_z = [
            '##   #  ##   ## ### # # # # # # # # # # ### ### ',
            '# # # # # # #    #  # # # # # # # # # #   #   # ',
            '##  # # ##   #   #  # # # # ###  #   #   #   ## ',
            '#    ## # #   #  #  # # # # ### # #  #  #       ',
            '#     # # # ##   #  ###  #  # # # #  #  ###  #  ',
        ]

        self.width = 4
        self.height = 5
        self.art = [a + b for a, b in zip(part_a_o, part_p_z)]

    def test_one_sign(self):
        result = [
            '### ',
            '#   ',
            '##  ',
            '#   ',
            '### '
        ]

        self.assertEqual(
            ascii_art(self.width, self.height, self.art, 'E'), result,
            'Should return letter \'E\' in ASCII art.'
        )

        result = [
            '### ',
            '  # ',
            ' ## ',
            '    ',
            ' #  '
        ]

        self.assertEqual(
            ascii_art(self.width, self.height, self.art, '?'), result,
            'Should return sign \'?\' in ASCII art.'
        )

    def test_manhattan(self):
        result = [
            '# #  #  ### # #  #  ### ###  #  ### ',
            '### # # # # # # # #  #   #  # # # # ',
            '### ### # # ### ###  #   #  ### # # ',
            '# # # # # # # # # #  #   #  # # # # ',
            '# # # # # # # # # #  #   #  # # # # ',
        ]

        self.assertEqual(
            ascii_art(self.width, self.height, self.art, 'MANHATTAN'), result,
            'Should return \'MANHATTAN\' in ASCII art.'
        )

        self.assertEqual(
            ascii_art(self.width, self.height, self.art, 'ManhAtTan'), result,
            'Should recognize lower and upper case.'
        )

    def test_manhattan_mixed(self):
        result = [
            '# # ### ### # # ### ### ### ### ### ',
            '###   # # # # #   #  #   #    # # # ',
            '###  ## # # ###  ##  #   #   ## # # ',
            '# #     # # # #      #   #      # # ',
            '# #  #  # # # #  #   #   #   #  # # '
        ]

        self.assertEqual(
            ascii_art(self.width, self.height, self.art, 'M@NH@TT@N'), result,
            'Should place \'?\' for \'@\' in M@NH@TT@N.'
        )
