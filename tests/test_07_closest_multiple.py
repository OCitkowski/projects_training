from exercise_002.closest_multiple import closest_multiple_10
from unittest import TestCase

class TestClosestMultiple(TestCase):

    def test_closest_multiple(self):
        self.assertEqual(closest_multiple_10(54), 50, 'should return 54 for num = 50')
        self.assertEqual(closest_multiple_10(55), 60, 'should return 55 for num = 60')
        self.assertEqual(closest_multiple_10(22), 20, 'should return 22 for num = 20')
        self.assertEqual(closest_multiple_10(25), 30, 'should return 25 for num = 30')
        self.assertEqual(closest_multiple_10(37), 40, 'should return 37 for num = 40')
        self.assertEqual(closest_multiple_10(40), 40, 'should return 40 for num = 40')

