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

        #print(f"Last bet: {lastBet}")
        print(f"Last bet qty: {lastBetQty}")
        #print(f"Last bet die: {lastBetDie}")
        print(f"Total dice: {input.getTotalDice()}")

        # accept bet if quantity is less than 1/3 of total quantity of dice
        response = (lastBetQty * 3 < input.getTotalDice())
        responseStr = "likely" if response else "unlikely"
        print(f"Papa thinks last bet of {lastBetQty} dice is {responseStr} given that there's {input.getTotalDice()} total dice")
        return response
        #return atleast(input.getBetHistory()[-1, 0], input.getTotalDice()) < .75
        #return False
