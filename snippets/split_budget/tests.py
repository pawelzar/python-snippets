from unittest import TestCase

from .solution import split_budgets


class SplitBudgetsTestCase(TestCase):
    def test_three_positive(self):
        self.assertEqual(split_budgets([3, 3, 3], 3), [1, 1, 1])
        self.assertEqual(split_budgets([10, 100, 100], 100), [10, 45, 45])
        self.assertEqual(split_budgets([3, 45, 100], 100), [3, 45, 52])
        self.assertEqual(split_budgets([3, 100, 100], 100), [3, 48, 49])
        self.assertEqual(split_budgets([40, 40, 40], 100), [33, 33, 34])
        self.assertEqual(split_budgets([100, 1, 60], 100), [1, 49, 50])

    def test_several_solutions(self):
        self.assertEqual(split_budgets([5, 10, 5], 10), [3, 3, 4])

    def test_impossible(self):
        self.assertEqual(split_budgets([1, 1, 1], 4), 'IMPOSSIBLE')
        self.assertEqual(split_budgets([20, 20, 40], 100), 'IMPOSSIBLE')
