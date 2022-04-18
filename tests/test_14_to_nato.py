from unittest import  TestCase
from exercise_002.ex_14_to_nato import to_nato

# 'Alfa',
# 'Bravo',
# 'Charlie',
# 'Delta',
# 'Echo',
# 'Foxtrot',
# 'Golf',
# 'Hotel',
# 'India',
# 'Juliett',
# 'Kilo',
# 'Lima',
# 'Mike',
# 'November',
# 'Oscar',
# 'Papa',
# 'Quebec',
# 'Romeo',
# 'Sierra',
# 'Tango',
# 'Uniform',
# 'Victor',
# 'Whiskey',
# 'Xray',
# 'Yankee',
# 'Zulu'



class TestToNato(TestCase):


    def test_to_nato(self):
        self.assertEqual(to_nato('tt'), "Tango Tango")
        self.assertEqual(to_nato('If you can read'),
                         "India Foxtrot Yankee Oscar Uniform Charlie Alfa November Romeo Echo Alfa Delta")
        self.assertEqual(to_nato('Did not see that coming'),
                         "Delta India Delta November Oscar Tango Sierra Echo "
                         "Echo Tango Hotel Alfa Tango Charlie Oscar Mike India November Golf")
        self.assertEqual(to_nato('.d?d!', '. Delta ? Delta !'))
