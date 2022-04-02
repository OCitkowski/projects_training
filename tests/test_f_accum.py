from exercise_002.f_accum import accum
import unittest

class TestAccum(unittest.TestCase):

    def test_accum(self):
        # self.assertEqual(accum("ZpglnRxqenU"), "ZpglnRxqenU")
        self.assertEqual(accum("ZpglnRxqenU"),
                           "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
        self.assertEqual(accum("NyffsGeyylB"),
                           "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
        self.assertEqual(accum("MjtkuBovqrU"),
                           "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
        self.assertEqual(accum("EvidjUnokmM"),
                           "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
        self.assertEqual(accum("HbideVbxncC"),
                           "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")

    # def test_type_value(self):
    #     self.assertRaises(TypeError, accum, "ZpglnRxqenU")

if __name__ == '__main__':
    unittest.main()
