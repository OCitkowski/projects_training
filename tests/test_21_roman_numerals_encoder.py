from unittest import TestCase
from exercise_002.ex_21_roman_numerals_encoder import solution

class TestHighestScoringWorld(TestCase):


    def test_solution(self):

        self.assertEqual(solution(1),'I', "solution(1),'I'")
        self.assertEqual(solution(4),'IV', "solution(4),'IV'")
        self.assertEqual(solution(6),'VI', "solution(6),'VI'")
        self.assertEqual(solution(14),'XIV', "solution(14),'XIV")
        self.assertEqual(solution(21),'XXI', "solution(21),'XXI'")
        self.assertEqual(solution(89),'LXXXIX', "solution(89),'LXXXIX'")
        self.assertEqual(solution(91),'XCI', "solution(91),'XCI'")
        self.assertEqual(solution(984),'CMLXXXIV', "solution(984),'CMLXXXIV'")
        self.assertEqual(solution(1000), 'M', 'solution(1000), M')
        self.assertEqual(solution(1889),'MDCCCLXXXIX', "solution(1889),'MDCCCLXXXIX'")
        self.assertEqual(solution(1989),'MCMLXXXIX', "solution(1989),'MCMLXXXIX'")