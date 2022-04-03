from exercise_002.prime_number import is_prime
import unittest


class TestIsPrime(unittest.TestCase):

    def test_tests(self):
        self.assertEqual(is_prime(0), False, "0  is not prime")
        self.assertEqual(is_prime(1), False, "1  is not prime")
        self.assertEqual(is_prime(2), True, "2  is prime")
        self.assertEqual(is_prime(73), True, "73 is prime")
        self.assertEqual(is_prime(75), False, "75 is not prime")
        self.assertEqual(is_prime(-1), False, "-1 is not prime")


    def test_prime(self):
        self.assertEqual(is_prime(3), True, "3  is prime")
        self.assertEqual(is_prime(5), True, "5  is prime")
        self.assertEqual(is_prime(7), True, "7  is prime")
        self.assertEqual(is_prime(41), True, "41 is prime")
        self.assertEqual(is_prime(5099), True, "5099 is prime")

        self.assertEqual(is_prime(1485770339), True, "1485770339 is prime")
        self.assertEqual(is_prime(250294663), True, "250294663 is prime")
        self.assertEqual(is_prime(47933701), True, "47933701 is prime")



    def test_not_prime(self):
        self.assertEqual(is_prime(4), False, "4  is not prime")
        self.assertEqual(is_prime(6), False, "6  is not prime")
        self.assertEqual(is_prime(8), False, "8  is not prime")
        self.assertEqual(is_prime(9), False, "9 is not prime")
        self.assertEqual(is_prime(45), False, "45 is not prime")
        self.assertEqual(is_prime(-5), False, "-5 is not prime")
        self.assertEqual(is_prime(-8), False, "-8 is not prime")
        self.assertEqual(is_prime(-41), False, "-41 is not prime")

        self.assertEqual(is_prime(101223721), False, "101223721 is not prime")
        self.assertEqual(is_prime(274977013), False, "274977013 is not prime")

