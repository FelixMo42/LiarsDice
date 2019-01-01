from game.player import Player
from util.probability import atleast

class Papa3(Player):
    """
        I'm a Liar's Dice player
    """
    o = .3
    name = "Papa3 " + str(o) # Name of this player

    def play(self, input):
        """
            Make a bet
        """
        # get previous player's bet
        prevQty = input.getBetHistory()[-1, 0]
        prevDie = input.getBetHistory()[-1, 1]

        # find my die with highest quantity
        myHighest = self.getMyHighestDie(input.getYourDice())
        myHighestQty = myHighest[0]
        myHighestDie = myHighest[1]

        # if my highest qty is higher than previous qty, bet it
        if (myHighestQty > prevQty):
            return myHighest
        # if my highest qty is the same as the previous qty but is a higher die, bet it
        elif (myHighestQty == prevQty and myHighestDie > prevDie):
            return myHighest
        # if I can go up to 6 and bet same quantity
        elif (prevDie < 5):
            return [prevQty, 5]
        # if my highest qty + 1 is higher than previous qty, bet it
        elif ((myHighestQty + 1) > prevQty):
            return [myHighestQty + 1, myHighestDie]       
        # else stay at same die and increase quantity
        else:
            return [prevQty + 1, prevDie]

    def verify(self, input):
        """
            Accept or reject the previous person's bet
        """
        prevBet = input.getPrevBet()
        prevQty = prevBet[0]
        prevDie = prevBet[1]
        myQty = input.getYourDice()[prevDie]
        totalDiceInGame = input.getTotalDice()
        myTotalDice = input.getYourTotalDice()
        odds = self.getOdds(prevQty, prevDie, myQty, totalDiceInGame, myTotalDice)

        # accept bet if it's over 50% likely to be true
        acceptBet = odds > self.o
        #acceptOrReject = "accept" if acceptBet else "reject"
        #print(f"{self.name} will {acceptOrReject} last bet of {prevQty} {prevDie+1}'s because it's {round(odds*100)}% likely given that there's {input.getTotalDice()} total dice and I have {myQty} {prevDie+1}'s.")
        return acceptBet

    def getMyHighestDie(self, myDice):
        """
            Get my die with the highest quantity
        """
        higestQty = 0
        highestDie = -1
        for i, qty in enumerate(myDice):
            if (qty > higestQty):
                highestQty = qty
                highestDie = i
        return [highestQty, highestDie]

    def getOdds(self, betQty, betDie, myQty, totalDiceInGame, myTotalDice):
        """
            Return the probability that there's at least betQty of a die out of totalDice dice
            -------
            float (0-1)
        """
        qty = betQty - myQty
        total = totalDiceInGame - myTotalDice
        return atleast(qty, total)
