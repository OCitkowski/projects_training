from exercise_002.ex_23_Stop_gninnipS_My_sdroW import spin_words
from unittest import TestCase


class TestSpinWords(TestCase):

    def test_spin_words(self):

        self.assertEqual(spin_words("Welcome"), "emocleW", "Single word")
        self.assertEqual(spin_words("to"), "to", "Single word")
        self.assertEqual(spin_words("CodeWars"), "sraWedoC", "Single word")
        self.assertEqual(spin_words("Hey fellow warriors"), "Hey wollef sroirraw", "Multiple words")
        self.assertEqual(spin_words("This sentence is a sentence"), "This ecnetnes is a ecnetnes", "Multiple words")
