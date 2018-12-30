from game.player import Player
from util.probability import atleast

class Papa(Player):
    name = "Papa"

    def play(self, input):
        prevNum = input.getBetHistory()[-1, 0]
        prevDie = input.getBetHistory()[-1, 1]

        # if the last bet's die was not a six, go up a die and bet same quantity
        if (prevDie < 5):
            return [prevNum, prevDie + 1]
        # else increase quantity and stay at same die
        else:
            return [prevNum + 1, prevDie]

    def verify(self, input):
        lastBet = input.getBetHistory()[-1]
        lastBetQty = lastBet[0]

        # accept bet if quantity is less than 1/3 of total quantity of dice
        acceptBet = (lastBetQty * 3 < input.getTotalDice())
        likelyOrNot = "likely" if acceptBet else "NOT likely"
        #print(f"Papa thinks last bet of {lastBetQty} dice is {likelyOrNot} given that there's {input.getTotalDice()} total dice")
        return acceptBet
