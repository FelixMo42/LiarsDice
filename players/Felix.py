from game.player import Player

class Felix(Player):
    name = "Felix"

    def play(self, input):
        prevNum = input.getBetHistory()[-1, 0]
        prevDie = input.getBetHistory()[-1, 1]

        if prevDie >= 5:
            return [prevNum + 1, 0]
        else:
            return [prevNum, prevDie + 1]

    def verify(self, input):
        return input.getBetHistory()[-1, 0] / input.getTotalDice() < .5
