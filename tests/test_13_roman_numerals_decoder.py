# Symbol    Value
# I          1
# V          5
# X          10
# L          50
# C          100
# D          500
# M          1,000

from unittest import TestCase
from exercise_002.ex_13_roman_numerals_decoder import solution


class TestSolution(TestCase):


    def test_solution(self):

        self.assertEqual(solution('XXI'), 21, 'XXI should == 21')
        self.assertEqual(solution('I'), 1, 'I should == 1')
        self.assertEqual(solution('IV'), 4, 'IV should == 4')
        self.assertEqual(solution('MMVIII'), 2008, 'MMVIII should == 2008')
        self.assertEqual(solution('MDCLXVI'), 1666, 'MDCLXVI should == 1666')
        self.assertEqual(solution('MCDXCIX'), 1499, 'MCDXCIX should == 1666')
        self.assertEqual(solution('MCMXCIX'), 1999, 'MCMXCIX should == 1666')
