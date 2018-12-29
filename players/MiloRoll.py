from player import Player

class MiloRoll(Player):
    name = "Milo"

    def play(self, input):
        prevNum = input.getBetHistory()[-1, 0]
        prevDie = input.getBetHistory()[-1, 1]

        return [prevNum + 1, prevDie]

    def verify(self, input):
        return input.getBetHistory()[-1, 0] / input.getTotalDice() < .5
