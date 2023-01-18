from exercise_002.ex_25_square_sum import square_sum
import unittest


class TestSquareSum(unittest.TestCase):

    def test_unique(self):
        self.assertEqual(square_sum([1, 2]), 5)
        self.assertEqual(square_sum([0, 3, 4, 5]), 50)
        self.assertEqual(square_sum([]), 0)
        self.assertEqual(square_sum([-1, -2]), 5)
        self.assertEqual(square_sum([-1, 0, 1]), 2)


if __name__ == '__main__':
    unittest.main()
