from game.player import Player
from util.probability import atleast
import numpy as numpy

class Papa4(Player):
    """
        I'm a Liar's Dice player
    """
    safeOddsToBet = .8 # Probability above which I will place a bet
    oddsToAcceptBet = .3 # Probability above which I will accept others' bets
    name = "Papa 4" # Name of this player

    def play(self, input):
        """
            Make a bet
        """
        # get previous player's bet
        prevQty, prevDie = input.getPrevBet()

        # get my die with highest quantity
        myHighestDie = numpy.argmax(input.getYourDice())
        myHighestQty = input.getYourDice()[myHighestDie]

        # what's my highest safe bet?
        myHighestSafeQty = myHighestQty
        while self.getOdds(myHighestSafeQty + 1, myHighestQty, input.getYourTotalDice(), input.getTotalDice()) > self.safeOddsToBet:
            myHighestSafeQty += 1

        # if my highest safe bet is higher than previous qty, bet it
        if (myHighestSafeQty > prevQty):
            return [myHighestSafeQty, myHighestDie]
        # if my highest safe qty is the same as the previous qty but mine is a higher die, bet it
        elif (myHighestSafeQty == prevQty and myHighestDie > prevDie):
            return [myHighestQty, myHighestDie]
        # if I can go up to 6 and bet same quantity, do that
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
        odds = self.getOdds(prevQty, myQty, totalDiceInGame, myTotalDice)

        # accept bet if it's over 50% likely to be true
        acceptBet = odds > self.oddsToAcceptBet
        #acceptOrReject = "accept" if acceptBet else "reject"
        #print(f"{self.name} will {acceptOrReject} last bet of {prevQty} {prevDie+1}'s because it's {round(odds*100)}% likely given that there's {input.getTotalDice()} total dice and I have {myQty} {prevDie+1}'s.")
        return acceptBet

    def getOdds(self, betQty, myQty, totalDiceInGame, myTotalDice):
        """
            Return the probability that there's at least betQty of a die out of totalDice dice
            -------
            float (0-1)
        """
        qty = betQty - myQty
        total = totalDiceInGame - myTotalDice
        return atleast(qty, total)
