from exercise_002.xbonacci import xbonacci as Xbonacci
import unittest

class TestXbonacci(unittest.TestCase):

    def test_fibonacci(self):

         self.assertEqual(Xbonacci([0,1],10),[0,1,1,2,3,5,8,13,21,34])
         self.assertEqual(Xbonacci([1,1],10),[1,1,2,3,5,8,13,21,34,55])

    def test_threebonacci(self):

         self.assertEqual(Xbonacci([0,0,1],10),[0,0,1,1,2,4,7,13,24,44])
         self.assertEqual(Xbonacci([1,1,1],10),[1,1,1,3,5,9,17,31,57,105])

    def test_xbonacci(self):

        self.assertEqual(Xbonacci([0, 0, 0, 0, 1], 10), [0, 0, 0, 0, 1, 1, 2, 4, 8, 16])
        self.assertEqual(Xbonacci([1, 0, 0, 0, 0, 0, 1], 10), [1, 0, 0, 0, 0, 0, 1, 2, 3, 6])
        self.assertEqual(Xbonacci([1, 0, 0, 0, 0, 0, 0, 0, 0, 0], 20),
                           [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 4, 8, 16, 32, 64, 128, 256])
        self.assertEqual(Xbonacci([16, 14, 20, 11, 7, 17, 3, 3, 15, 2, 5, 20], 3), [16, 14, 20])

if __name__ == '__main__':
    unittest.main()

