from unittest import TestCase
from exercise_002.ex_12_solution import solution

class TestSolution(TestCase):


    def test_solution(self):

        self.assertEqual(solution(4), 3)
        self.assertEqual(solution(6), 8)
        self.assertEqual(solution(16), 60)
        self.assertEqual(solution(5), 3)
        self.assertEqual(solution(15), 45)
        self.assertEqual(solution(-1), 0)
        self.assertEqual(solution(10), 23)
        self.assertEqual(solution(20), 78)
        self.assertEqual(solution(200), 9168)


