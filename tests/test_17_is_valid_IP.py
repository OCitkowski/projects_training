# Write an algorithm that will identify valid IPv4 addresses in dot-decimal format.
# IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.
# Valid inputs examples:
#
# Examples of valid inputs:
# 1.2.3.4
# 123.45.67.89
#
# Invalid input examples:
#
# 1.2.3
# 1.2.3.4.5
# 123.456.78.90
# 123.045.067.089
#
# Notes:
#
#     Leading zeros (e.g. 01.02.03.04) are considered invalid
#     Inputs are guaranteed to be a single string
from unittest import TestCase
from exercise_002.ex_17_is_valid_IP import is_valid_IP

class TestIsValid(TestCase):


    def test_is_valid_IP(self):

        self.assertEqual(is_valid_IP('12.255.56.1'),     True)
        self.assertEqual(is_valid_IP(''),                False)
        self.assertEqual(is_valid_IP('abc.def.ghi.jkl'), False)
        self.assertEqual(is_valid_IP('123.456.789.0'),   False)
        self.assertEqual(is_valid_IP('12.34.56'),        False)
        self.assertEqual(is_valid_IP('12.34.56 .1'),     False)
        self.assertEqual(is_valid_IP('12.34.56.-1'),     False)
        self.assertEqual(is_valid_IP('123.045.067.089'), False)
        self.assertEqual(is_valid_IP('127.1.1.0'),        True)
        self.assertEqual(is_valid_IP('0.0.0.0'),          True)
        self.assertEqual(is_valid_IP('0.34.82.53'),       True)
        self.assertEqual(is_valid_IP('192.168.1.300'),   False)