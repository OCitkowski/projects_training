# Rock-Paper-Scissors Big Bang Style
#
# According to Sheldon Cooper the following is true:
#
#     Scissors cuts Paper
#     Paper covers Rock
#     Rock crushes Lizard
#     Lizard poisons Spock
#     Spock smashes Scissors
#     Scissors decapitates Lizard
#     Lizard eats Paper
#     Paper disproves Spock
#     Spock vaporizes Rock
#     Rock crushes Scissors

#   */*         Scissors    Paper   Rock    Lizard  Spock
#   Scissors        x         s       r        s     sp
#   Paper           s         x       p        l      p
#   Rock            r         p       x        r     sp
#   Lizard          s         l       r        x      l
#   Spock           sp        p       sp       l      x

# Given two values from the above game, return the Player result as "Player 1 Won!", "Player 2 Won!" or "Draw!".
#
# Values will be given as one of "rock", "spock", "paper", "lizard", "scissors".


from unittest import TestCase
from exercise_002.rock_paper_scissors import rpsls

class TestRPS(TestCase):

    def test_first_won(self):

        self.assertEqual(rpsls('rock', 'lizard'), 'Player 1 Won!')
        self.assertEqual(rpsls('paper', 'rock'), 'Player 1 Won!')
        self.assertEqual(rpsls('scissors', 'lizard'), 'Player 1 Won!')
        self.assertEqual(rpsls('lizard', 'paper'), 'Player 1 Won!')
        self.assertEqual(rpsls('spock', 'rock'), 'Player 1 Won!')


    def test_secand_won(self):
        self.assertEqual(rpsls('lizard', 'scissors'), 'Player 2 Won!')
        self.assertEqual(rpsls('spock', 'lizard'), 'Player 2 Won!')
        self.assertEqual(rpsls('paper', 'lizard'), 'Player 2 Won!')
        self.assertEqual(rpsls('scissors', 'spock'), 'Player 2 Won!')
        self.assertEqual(rpsls('rock', 'spock'), 'Player 2 Won!')

    def test_draw(self):
        self.assertEqual(rpsls('rock', 'rock'), 'Draw!')
        self.assertEqual(rpsls('spock', 'spock'), 'Draw!')