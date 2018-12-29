class PlayInput:
    def __init__(this, history, players, turn):
        this.history = history
        this.players = players
        this.player_index = turn % len(players)
        this.player = players[this.player_index]

    '''
        History of bets
        [[quantity from 1-infinite, die 0-5]]
    '''
    def getBetHistory(this):
        return this.history

    '''
        Quantity of dice each player has, excluding yourself
        [numDice 1-infinite]
    '''
    def getAllPlayersDice(this):
        dice = []

        for i in range(this.player_index + 1, len(this.players)):
            dice.append(this.players[i].numDice)

        for i in range(this.player_index):
            dice.append(this.players[i].numDice)

        return dice

    '''
        Total quantity of dice across all players, including yourself
        integer
    '''
    def getTotalDice(this):
        total = 0

        for player in this.players:
            total += player.numDice

        return total

    '''
        Quantity of dice that you have
        [numDice 1-5] arr length 6
    '''
    def getYourDice(this):
        return this.player.dice

    '''
        Total quantity of dice you have
        integer 0-4
    '''
    def getYourTotalDice(this):
        return sum(this.player.dice)
