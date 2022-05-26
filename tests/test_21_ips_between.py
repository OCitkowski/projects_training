from exercise_002.ex_21_ips_between import ips_between
from unittest import TestCase


class TestIPSBetween(TestCase):
    """# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them
# (including the first one, excluding the last one).
# All inputs will be valid IPv4 addresses in the form of strings.
# The last address will always be greater than the first one"""

    def test_IPS_between(self):
        self.assertEqual(ips_between("10.0.0.0", "10.0.0.50"), 50)
        self.assertEqual(ips_between("20.0.0.10", "20.0.1.0"), 246)

        self.assertEqual(ips_between("170.0.0.0", "170.1.0.0"), 65536)
        self.assertEqual(ips_between("50.0.0.0", "50.1.1.1"), 65793)




