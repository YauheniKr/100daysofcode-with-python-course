class Roll(object):

    def __init__(self, name):
        self.name = name

    def can_defeat(self, p2_roll):
        wins = {'scissor' : 'paper',
                'paper' : 'rock',
                'rock': 'scissor'}
        #print(p2_roll.name, self.name)
        if p2_roll.name == wins[self.name]:
            return True
        elif p2_roll.name == self.name:
            return 'Draw'
        elif p2_roll.name != wins[self.name]:
            return False



class Player():

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

