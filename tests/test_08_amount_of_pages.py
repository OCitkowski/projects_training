# Every book has n pages with page numbers 1 to n. The summary is
# made by adding up the number of digits of all page numbers.
#
# Task: Given the summary, find the number of pages n the book has.
# Example
#
# If the input is summary=25, then the output must be n=17:
# The numbers 1 to 17 have 25 digits in total: 1234567891011121314151617.
#
# Be aware that you'll get enormous books having up to 100.000 pages.
#
# All inputs will be valid.

from exercise_002.amount_of_pages import amount_of_pages
from unittest import TestCase

class TestAmountPages(TestCase):

    def test_page(self):
        self.assertEqual(amount_of_pages(5), 5)
        self.assertEqual(amount_of_pages(25), 17)

        self.assertEqual(amount_of_pages(185), 97)
        self.assertEqual(amount_of_pages(660), 256)

        self.assertEqual(amount_of_pages(1095), 401)
        # self.assertEqual(amount_of_pages(192304), 40682)

