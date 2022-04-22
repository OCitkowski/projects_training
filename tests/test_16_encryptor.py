from unittest import TestCase
from exercise_002.ex_16_encryptor import encryptor


class TestEncryptor(TestCase):

    def test_encryptor(self):

        self.assertEqual(encryptor(13, ''), '')
        self.assertEqual(encryptor(13, 'Caesar Cipher'), 'Pnrfne Pvcure')
        self.assertEqual(encryptor(-5, 'Hello World!'), 'Czggj Rjmgy!')
        self.assertEqual(encryptor(27, 'Whoopi Goldberg'), 'Xippqj Hpmecfsh')