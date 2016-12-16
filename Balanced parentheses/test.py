import unittest
from solution import is_balanced


class BracketsTest(unittest.TestCase):
    def testPositive(self):
        self.assertTrue(is_balanced("()"))
        self.assertTrue(is_balanced("()[]{}"))
        self.assertTrue(is_balanced("(({([({{[{()}]}})])}))(()[{}])"))
        self.assertTrue(is_balanced("{This [(is)] f{i}ne}"))

    def testNegative(self):
        self.assertFalse(is_balanced("("))
        self.assertFalse(is_balanced("}"))
        self.assertFalse(is_balanced("    (([))]"))
        self.assertFalse(is_balanced("This ([is)] just wrong"))


if __name__ == '__main__':
    unittest.main()
