import unittest
from .solution import ascii_art


class AsciiArtTest(unittest.TestCase):
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

        self.art = [a + b for a, b in zip(part_a_o, part_p_z)]

    def test_one_sign(self):
        result = [
            '### ',
            '#   ',
            '##  ',
            '#   ',
            '### '
        ]

        self.assertEqual(ascii_art(4, 5, 'E', self.art), result,
                         'Should return letter \'E\' in ASCII art.')

        result = [
            '### ',
            '  # ',
            ' ## ',
            '    ',
            ' #  '
        ]

        self.assertEqual(ascii_art(4, 5, '?', self.art), result,
                         'Should return sign \'?\' in ASCII art.')

    def test_manhattan(self):
        result = [
            '# #  #  ### # #  #  ### ###  #  ### ',
            '### # # # # # # # #  #   #  # # # # ',
            '### ### # # ### ###  #   #  ### # # ',
            '# # # # # # # # # #  #   #  # # # # ',
            '# # # # # # # # # #  #   #  # # # # ',
        ]

        self.assertEqual(ascii_art(4, 5, 'MANHATTAN', self.art), result,
                         'Should return \'MANHATTAN\' in ASCII art.')

        self.assertEqual(ascii_art(4, 5, 'ManhAtTan', self.art), result,
                         'Should recognize lower and upper case.')

    def test_manhattan_mixed(self):
        result = [
            '# # ### ### # # ### ### ### ### ### ',
            '###   # # # # #   #  #   #    # # # ',
            '###  ## # # ###  ##  #   #   ## # # ',
            '# #     # # # #      #   #      # # ',
            '# #  #  # # # #  #   #   #   #  # # '
        ]

        self.assertEqual(ascii_art(4, 5, 'M@NH@TT@N', self.art), result,
                         'Should place \'?\' for \'@\' in M@NH@TT@N.')


if __name__ == '__main__':
    unittest.main()
