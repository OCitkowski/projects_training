from unittest import TestCase
from exercise_002.ex_18_white_black_areas import white_black_areas


class TestAreas(TestCase):
    """# https://www.codewars.com/kata/6262f9f7afc4729d8f5bef48/train/python"""

    def test_areas(self):
        self.assertEqual(white_black_areas([3, 1, 2, 7, 1], [1, 8, 4, 5, 2]), (146, 134))
        self.assertEqual(type(white_black_areas([3, 1, 2, 7, 1], [1, 8, 4, 5, 2])), tuple)
        self.assertEqual(white_black_areas([3, 1, 2, 7, 1, 11, 12, 3, 8, 1], [1, 8, 4, 5, 2, 21, 5, 2, 2, 17]),
                         (1583, 1700))
        # self.assertEqual(white_black_areas(([3], [2]), (6, 0)))
