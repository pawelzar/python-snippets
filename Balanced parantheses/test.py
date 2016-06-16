import unittest
from solution import is_balanced


class BracketsTest(unittest.TestCase):
    def testPositive(self):
        self.assertEqual(is_balanced("()"), True)
        self.assertEqual(is_balanced("()[]{}"), True)
        self.assertEqual(is_balanced("(({([({{[{()}]}})])}))(()[{}])"), True)

    def testNegative(self):
        self.assertEqual(is_balanced("("), False)
        self.assertEqual(is_balanced("}"), False)
        self.assertEqual(is_balanced("    (([))]"), False)


if __name__ == '__main__':
    unittest.main()
