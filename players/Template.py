from player import Player

class Template(Player):
    name = "template"

    def play(self, history, players, totalDice, numDice, dice, prevPlayer):
        prevNum = history[-1, 0]
        prevDie = history[-1, 1]

        return [prevNum + 1, prevDie]

    def verify(self, history, players, totalDice, numDice, dice, prevPlayer):
        return history[-1][0] / totalDice < .5
