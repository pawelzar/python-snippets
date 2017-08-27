from unittest import TestCase

from .solution import bw_transform, bw_transform_minimized


class BWTransformTestCase(TestCase):
    def test_positive(self):
        self.assertEqual(bw_transform('BAHAMAS'), '4BHMSAAA')
        self.assertEqual(bw_transform_minimized('BAHAMAS'), '4BHMSAAA')

    def test_negative(self):
        self.assertNotEqual(bw_transform('BAHAMAS'), '7SBAHAMA')
        self.assertNotEqual(bw_transform_minimized('BAHAMAS'), '7SBAHAMA')
