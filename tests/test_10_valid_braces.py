# Write a function that takes a string of braces, and determines if the order of the braces is valid.
# It should return true if the string is valid, and false if it's invalid.
#
# This Kata is similar to the Valid Parentheses Kata, but introduces new characters: brackets [],
# and curly braces {}. Thanks to @arnedag for the idea!
#
# All input strings will be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}.
# What is considered Valid?
#
# A string of braces is considered valid if all braces are matched with the correct brace.
# Examples
#
# "(){}[]"   =>  True
# "([{}])"   =>  True
# "(}"       =>  False
# "[(])"     =>  False
# "[({})](]" =>  False



from  unittest import TestCase
from exercise_002.valid_braces_10 import valid_braces

class TestValidVbraces(TestCase):


    def test_valid_true(self):

        self.assertTrue(valid_braces("()"))
        self.assertTrue(valid_braces("[]"))
        self.assertTrue(valid_braces("{}"))
        self.assertTrue(valid_braces("{}()[]"))
        self.assertTrue(valid_braces("([{}])"))
        self.assertTrue(valid_braces("{}({})[]"))
        self.assertTrue(valid_braces("(({{[[]]}}))"))


    def test_valid_false(self):
        self.assertFalse(valid_braces("(((({{"))
        self.assertFalse(valid_braces(")(}{]["))
        self.assertFalse(valid_braces("())({}}{()][]["))
        self.assertFalse(valid_braces("(}"))
        self.assertFalse(valid_braces("[(])"))
        self.assertFalse(valid_braces("([}{])"))

