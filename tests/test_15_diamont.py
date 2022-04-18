# Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. ' \
#                                 'Since James doesn't know how to make this happen, he needs your help.
# Task
#
# You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*)
# characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).
#
# Return null/nil/None/... if the input is an even number or negative,
# as it is not possible to print a diamond of even or negative size.
# Examples
#
# A size 3 diamond:
#
#  *
# ***
#  *


from unittest import TestCase
from exercise_002.ex_15_diamond import diamond


class TestDiamont(TestCase):

    def test_diamont(self):
        # self.assertEqual(diamond(1), "*\n")
        self.assertEqual(diamond(2), None)
        # self.assertEqual(diamond(3), expected)
        self.assertEqual(diamond(5), "  *\n ***\n*****\n ***\n  *\n")
        self.assertEqual(diamond(0), None)
        self.assertEqual(diamond(-3), None)
