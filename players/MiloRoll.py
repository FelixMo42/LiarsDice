from player import Player

class MiloRoll(Player):
    name = "template"

    def play(self, history, players, totalDice, numDice, dice):
        prevNum = history[-1, 0]
        prevDie = history[-1, 1]

        return [prevNum + 1, prevDie]

    def verify(self, history, players, totalDice, numDice, dice):
        return history[-1][0] / totalDice < .5