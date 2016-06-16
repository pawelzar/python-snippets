import unittest
from solution import is_balanced


class BracketsTest(unittest.TestCase):
    def testPositive(self):
        self.assertEqual(is_balanced("()"), True)
        self.assertEqual(is_balanced("()[]{}"), True)
        self.assertEqual(is_balanced("(({([({{[{()}]}})])}))(()[{}])"), True)
        self.assertEqual(is_balanced("{This [(is)] f{i}ne}"), True)


    def testNegative(self):
        self.assertEqual(is_balanced("("), False)
        self.assertEqual(is_balanced("}"), False)
        self.assertEqual(is_balanced("    (([))]"), False)
        self.assertEqual(is_balanced("This ([is)] just wrong"), False)


if __name__ == '__main__':
    unittest.main()
