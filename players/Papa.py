from game.player import Player
from util.probability import atleast

class Papa(Player):
    name = "Papa"

    def play(self, input):
        prevQty = input.getBetHistory()[-1, 0]
        prevDie = input.getBetHistory()[-1, 1]

        # find my die with highest quantity
        myHighest = self.getMyHighestDie(input.getYourDice())
        myHighestQty = myHighest[0]
        myHighestDie = myHighest[1]
        #print(f"Papa's highest is {myHighestQty} {myHighestDie+1}")
        # if my higest is higher than previous bet, bet it
        if (myHighestQty > prevQty):
            return myHighest
        # else if my higest + 1 is higher than previous bet, bet it
        elif ((myHighestQty + 1) > prevQty):
            return [myHighestQty + 1, myHighestDie]
        # else if the last bet's die was not a six, go up a die and bet same quantity
        elif (prevDie < 5):
            return [prevQty, prevDie + 1]
        # else stay at same die and increase quantity
        else:
            return [prevQty + 1, prevDie]

    def verify(self, input):
        lastBet = input.getBetHistory()[-1]
        lastBetQty = lastBet[0]
        lastBetDie = lastBet[1]
        myDieQty = input.getYourDice()[lastBetDie]
        lastBetQtyMinusMyDice = lastBetQty - myDieQty
        totalDiceMinusMyDice = input.getTotalDice() - myDieQty

        # accept bet if quantity is less than 1/3 of total quantity of dice, excluding my dice
        acceptBet = (lastBetQtyMinusMyDice * 3 < totalDiceMinusMyDice)
        likelyOrNot = "likely" if acceptBet else "NOT likely"
        print(f"Papa thinks last bet of {lastBetQty} dice is {likelyOrNot} given that there's {input.getTotalDice()} total dice and I have {myDieQty}")
        return acceptBet

    def getMyHighestDie(self, myDice):
        higestQty = 0
        highestDie = -1
        for i, qty in enumerate(myDice):
            if (qty > higestQty):
                highestQty = qty
                highestDie = i
        return [highestQty, highestDie]