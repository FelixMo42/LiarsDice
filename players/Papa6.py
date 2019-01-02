from game.player import Player
from util.probability import atleast
import numpy as numpy

class Papa6(Player):
    """
        I'm a Liar's Dice player
    """
    safeOddsToBet = .7 # Probability above which I will place a bet
    name = "Papa 6 " + str(safeOddsToBet) # Name of this player

    def play(self, input):
        """
            Make a bet with the game's standard input
        """
        return self.bet(input.getPrevBet(), input.getYourHighestDice(), input.getTotalDice(), input.getYourTotalDice())

    def bet(self, prevBet, myHighestDice, totalDice, myTotalDice):
        """
            Make a bet with the parameters exploded
        """
        # get previous player's bet
        prevQty, prevDie = prevBet

        # get my die with highest quantity
        myHighestQty, myHighestDie = myHighestDice

        # what's my highest safe bet?
        myHighestSafeQty = myHighestQty
        while atleast((myHighestSafeQty - myHighestQty) + 1, totalDice - myTotalDice) > self.safeOddsToBet:
            myHighestSafeQty += 1

        # if my highest safe bet is higher than previous qty, bet it
        if (myHighestSafeQty > prevQty):
            return [myHighestSafeQty, myHighestDie]
        # if my highest safe qty is the same as the previous qty but mine is a higher die, bet it
        elif (myHighestSafeQty == prevQty and myHighestDie > prevDie):
            return [myHighestSafeQty, myHighestDie]
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
            Accept or reject the previous player's bet
        """
        prevBet = input.getPrevBet()
        prevQty = prevBet[0]
        prevDie = prevBet[1]
        myQty = input.getYourDice()[prevDie]
        totalDiceInGame = input.getTotalDice()
        myTotalDice = input.getYourTotalDice()

        # calculate odds of bet
        odds = atleast(prevQty - myQty, totalDiceInGame - myTotalDice)
        # what would be my next bet?
        myNextBetQty, myNextBetDie = self.bet(input.getPrevBet(), input.getYourHighestDice(), input.getTotalDice(), input.getYourTotalDice())
        # calculate odds of my next bet
        myNextBetDiceQty = input.getYourDice()[myNextBetDie]
        oddsOfMyNextBet = atleast(myNextBetQty - myNextBetDiceQty, totalDiceInGame - myTotalDice)
        # if my future odds are less likely than challenging this bet, challenge it
        oddsOfMeWinningIfIChallenge = 1 - odds
        acceptBet = oddsOfMeWinningIfIChallenge < oddsOfMyNextBet

        #acceptOrReject = "accept" if acceptBet else "reject"
        #print(f"{self.name} will {acceptOrReject} last bet of {prevQty} {prevDie+1}'s because it's {round(odds*100)}% likely given that there's {input.getTotalDice()} total dice and I have {myQty} {prevDie+1}'s.")

        return acceptBet
