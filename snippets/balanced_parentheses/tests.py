from unittest import TestCase

from .solution import is_balanced


class BracketsTestCase(TestCase):
    def test_positive(self):
        self.assertTrue(is_balanced('()'))
        self.assertTrue(is_balanced('()[]{}'))
        self.assertTrue(is_balanced('(({([({{[{()}]}})])}))(()[{}])'))
        self.assertTrue(is_balanced('{This [(is)] f{i}ne}'))
        self.assertTrue(is_balanced('W12{}{}L{}'))
        self.assertTrue(is_balanced('{C{}[{[a]}RqhL]{y2}}'))
        self.assertTrue(is_balanced('{([]){}()}'))

    def test_negative(self):
        self.assertFalse(is_balanced('('))
        self.assertFalse(is_balanced('}'))
        self.assertFalse(is_balanced('    (([))]'))
        self.assertFalse(is_balanced('This ([is)] just wrong'))
        self.assertFalse(is_balanced(']['))
        self.assertFalse(is_balanced('{[{iHTSc}]}p(R)m(){q({})'))
        self.assertFalse(is_balanced('h{Pn{GT{h}(c))}'))
        self.assertFalse(is_balanced('{([{S}]]6K[()]}'))
