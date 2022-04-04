
#   */*         Scissors    Paper   Rock    Lizard  Spock
#   Scissors        x         s       r        s     sp
#   Paper           s         x       p        l      p
#   Rock            r         p       x        r     sp
#   Lizard          s         l       r        x      l
#   Spock           sp        p       sp       l      x

def rpsls(pl1, pl2):
    solved_problems = {}
    solved_problems['scissors'] = {'scissors': None, 'paper': True, 'rock': False, 'lizard': True, 'spock': False}
    solved_problems['paper'] = {'scissors': False, 'paper': None, 'rock': True, 'lizard': False, 'spock': True}
    solved_problems['rock'] = {'scissors': True, 'paper': False, 'rock': None, 'lizard': True, 'spock': False}
    solved_problems['lizard'] = {'scissors': False, 'paper': True, 'rock': False, 'lizard': None, 'spock': True}
    solved_problems['spock'] = {'scissors': True, 'paper': False, 'rock': True, 'lizard': False, 'spock': None}

    if solved_problems.get(pl1).get(pl2) == None:
        winner_text = 'Draw!'
    elif solved_problems.get(pl1).get(pl2):
        winner_text = 'Player 1 Won!'
    else:
        winner_text = 'Player 2 Won!'

    return winner_text

def bestpr_rpsls(p1, p2):
    ORDER = "rock lizard spock scissors paper spock rock scissors lizard paper rock"
    return ( "Player 1 Won!" if f"{p1} {p2}" in ORDER
        else "Player 2 Won!" if f"{p2} {p1}" in ORDER
        else "Draw!" )

if __name__ == '__main__':
    assert rpsls('rock', 'lizard') =='Player 1 Won!'
    assert rpsls('rock', 'rock') == 'Draw!'