from exercise_002.find_outlier import find_outlier
from unittest import TestCase

class TestFindOutlier(TestCase):

    def test_find_outlier(self):

        self.assertEqual(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
        self.assertEqual(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
        self.assertEqual(find_outlier([2, 4, 6, 8, 10, 3]), 3)
        self.assertEqual(find_outlier([2, 4, 0, 102, 4, 13, 2602, 36]), 13)
        self.assertEqual(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
