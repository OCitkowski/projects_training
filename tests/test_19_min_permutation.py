from unittest import TestCase
from exercise_002.ex_19_min_permutation import min_permutation

class TestMinPer(TestCase):

    def test_min_per(self):

        self.assertEqual(min_permutation(-9876452310), -1023456789)
        self.assertEqual(min_permutation(0), 0)
        self.assertEqual(min_permutation(-20), -20)
        self.assertEqual(min_permutation(10), 10)
        self.assertEqual(min_permutation(29394), 23499)
        self.assertEqual(min_permutation(290394), 203499)
        self.assertEqual(min_permutation(293094), 203499)


