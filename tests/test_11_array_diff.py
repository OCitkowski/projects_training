from unittest import TestCase
from exercise_002.ex_11_array_diff import array_diff

class TextArrayDiff(TestCase):


    def test_array_diff(self):

        self.assertEquals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        self.assertEquals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
        self.assertEquals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        self.assertEquals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
        self.assertEquals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
        self.assertEquals(array_diff([1,2,3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")