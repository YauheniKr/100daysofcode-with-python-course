from pieces_actors import Roll, Player
import random

def main():

    print_header()

    rolls = build_rolls()

    name = get_players_name()

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def get_players_name():
    name = input('Input player name:')
    return name


def print_header():
    print('---------------------------------')
    print('    ROCK PAPER SCISSOR GAME')
    print('---------------------------------')
    print()


def build_rolls():
    paper = Roll('paper')
    scissor = Roll('scissor')
    rock = Roll('rock')
    lizard = Roll('lizard')
    spock = Roll('spock')

    roll = [paper, scissor, rock, lizard, spock]
    return roll


def game_loop(player1, player2, rolls):
    roll_list = [roll.name for roll in rolls]
    count = 1
    while count < 4:
        print('Round {} starts'.format(count))
        p2_roll = random.choice(build_rolls())
        p1_roll = input('Choose a roll from a list(rock, paper, scissor, lizard, spock):')
        p1_roll = Roll(p1_roll)

        while p1_roll.name not in roll_list:
            print('You enter incorrect roll. Insert correct roll')
            p1_roll = input('Choose a roll from a list(rock, paper, scissor, lizard, spock):')
            p1_roll = Roll(p1_roll)
            print(p1_roll.name, build_rolls())

        outcome = p1_roll.can_defeat(p2_roll)
        print('{} rolls {}'.format(player1.name, p1_roll.name))
        print('{} rolls {}'.format(player2.name, p2_roll.name))
        if outcome == 'True':
            print('{} won in round {} and take 1 score'.format(player1.name, count))

            player1.score += 1
        elif outcome == 'Draw':
            print('In round {} draw. Rerun round'.format(count))
            continue
        else:
            print('{} won in round {} and take 1 score'.format(player2.name, count))
            player2.score += 1
            # display throws
            # display winner for this round

        count += 1

    if player1.score > player2.score:
        print('{} won the game with score {} : {}'.format(player1.name, player1.score, player2.score))
    else:
        print('{} won the game with score {} : {}'.format(player2.name, player2.score, player1.score))


main()