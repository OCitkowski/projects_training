from exercise_mate.loops import print_numbers
from unittest import TestCase


# Допиши функцію print_numbers так, щоб вона виводила числа від 0 до n - 1 включно, в окремих рядках.
class TestLoops(TestCase):

    # todo test
    def test_unique(self):
        self.assertEqual(print_numbers(10), '0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9', 'is good')
