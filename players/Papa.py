from game.player import Player

class Papa(Player):
    name = "Papa"

    def play(self, input):
        prevQty = input.getBetHistory()[-1, 0]
        prevDie = input.getBetHistory()[-1, 1]

        # if the last bet's die was not a six, go up a die and bet same quantity
        if (prevDie < 5):
            return [prevQty, prevDie + 1]

        # find my die with highest quantity
        myHighest = self.getMyHighestDie(input.getYourDice())
        myHighestQty = myHighest[0]
        myHighestDie = myHighest[1]

        # if my higest qty is higher than previous qty, bet it
        if (myHighestQty > prevQty):
            return myHighest
        # if my higest qty is the same as the previous qty but is a higher die, bet it
        elif (myHighestQty == prevQty and myHighestDie > prevDie):
            return myHighest
        # if my higest qty + 1 is higher than previous qty, bet it
        elif ((myHighestQty + 1) > prevQty):
            return [myHighestQty + 1, myHighestDie]
        # if I can go up a die and bet same quantity
        elif (prevDie < 5):
            return [prevQty, prevDie + 1]
        # else stay at same die and increase quantity
        else:
            return [prevQty + 1, prevDie]

    def verify(self, input):
        prevBet = input.getBetHistory()[-1]
        prevQty = prevBet[0]
        prevDie = prevBet[1]
        myQty = input.getYourDice()[prevDie]

        # accept bet if quantity is less than 1/3 of total quantity of dice, excluding my qty of same die
        prevQtyMinusMyDice = prevQty - myQty
        totalDiceMinusMyDice = input.getTotalDice() - myQty
        acceptBet = (prevQtyMinusMyDice * 3 < totalDiceMinusMyDice)
        likelyOrNot = "likely" if acceptBet else "NOT likely"
        #print(f"Papa thinks last bet of {lastBetQty} dice is {likelyOrNot} given that there's {input.getTotalDice()} total dice and I have {myDieQty}")
        #print(f"Papa thinks last bet of {prevQty} {prevDie+1}'s is {likelyOrNot} given that there's {input.getTotalDice()} total dice and I have {myQty} {prevDie+1}'s")
        return acceptBet

    def getMyHighestDie(self, myDice):
        higestQty = 0
        highestDie = -1
        for i, qty in enumerate(myDice):
            if (qty > higestQty):
                highestQty = qty
                highestDie = i
        return [highestQty, highestDie]
