from exercise_002.ex_22_nines import nines
from unittest import TestCase


class TestNines(TestCase):

    def test_nines(self):

        self.assertEqual(nines(1), 0, "With n = 1")
        self.assertEqual(nines(10), 1, "With n = 10")
        self.assertEqual(nines(100), 19, "With n = 100")
        self.assertEqual(nines(1000), 271, "With n = 1000")
        self.assertEqual(nines(3950), 1035, "With n = 3950")
