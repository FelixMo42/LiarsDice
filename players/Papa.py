from game.player import Player
from util.probability import atleast

class Papa(Player):
    name = "Papa"

    def play(self, input):
        prevNum = input.getBetHistory()[-1, 0]
        prevDie = input.getBetHistory()[-1, 1]

        return [prevNum + 1, prevDie]

    def verify(self, input):
        lastBet = input.getBetHistory()[-1]
        lastBetQty = lastBet[0]
        lastBetDie = lastBet[1] + 1

        # accept bet if quantity is less than 1/3 of total quantity of dice
        acceptBet = (lastBetQty * 3 < input.getTotalDice())
        likelyOrNot = "likely" if acceptBet else "unlikely"
        print(f"Papa thinks last bet of {lastBetQty} dice is {likelyOrNot} given that there's {input.getTotalDice()} total dice")
        return acceptBet
