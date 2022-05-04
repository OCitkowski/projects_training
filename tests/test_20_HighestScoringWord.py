from unittest import TestCase
from exercise_002.ex_20_HighestScoringWord import high

class TestHighestScoringWorld(TestCase):


    def test_HSW(self):


        self.assertEqual(high('man i need a taxi up to ubud'), 'taxi')
        self.assertEqual(high('what time are we climbing up the volcano'), 'volcano')
        self.assertEqual(high('take me to semynak'), 'semynak')
        self.assertEqual(high('aa b'), 'aa')
        self.assertEqual(high('b aa'), 'b')
        self.assertEqual(high('bb d'), 'bb')
        self.assertEqual(high('d bb'), 'd')
        self.assertEqual(high("aaa b"), "aaa")