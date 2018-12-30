from game.player import Player
from util.probability import atleast

class Template(Player):
    name = "template"

    def play(self, input):
        prevNum = input.getBetHistory()[-1, 0]
        prevDie = input.getBetHistory()[-1, 1]

        return [prevNum + 1, prevDie]

    def verify(self, input):
        return atleast(input.getBetHistory()[-1, 0], input.getTotalDice()) < .75
