from exercise_002.unique_in_order import unique_in_order
from unittest import TestCase

class TestUniqueInOrder(TestCase):

    def test_unique(self):
        self.assertEqual(unique_in_order('AAAABBBCCDAABBB'), ['A', 'B', 'C', 'D', 'A', 'B'], 'is good')
        self.assertEqual(unique_in_order('ABBCcAD'), ['A', 'B', 'C', 'c', 'A', 'D'], 'is good')
        self.assertEqual(unique_in_order([1, 2, 2, 3, 3]), [1, 2, 3], 'is good')
        self.assertEqual(unique_in_order([1, 2, 2, 3, 3, 5, 5, 111]), [1, 2, 3, 5, 111], 'is good')

