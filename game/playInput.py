class PlayInput:
    def __init__(this, history, players, turn):
        this.history = history
        this.players = players
        this.player_index = turn % len(players)
        this.player = players[this.player_index]

    def getBetHistory(this):
        '''
            Returns
            -------
            [[int (how many dice, 1-infinite), int (what die, 0-5)]]
        '''
        
        return this.history

    def getAllPlayersDice(this):
        '''
            Returns
            -------
            [int (how many dice player has, 1-infinite)]
                Quantity of dice each player has, excluding yourself
        '''

        dice = []

        for i in range(this.player_index + 1, len(this.players)):
            dice.append(this.players[i].numDice)

        for i in range(this.player_index):
            dice.append(this.players[i].numDice)

        return dice

    def getTotalDice(this):
        '''
            Returns
            -------
            int (total numer of dice in the game)
        '''
        total = 0

        for player in this.players:
            total += player.numDice

        return total

    def getYourDice(this):
        '''
            Returns
            -------
            [int (how many of the die you rolled)]
                ex: [0,0,1,1,0,2]
                In this case you rolled one three, one four, two sixes, and zero
                of every thing else.
        '''

        return this.player.dice

    def getYourTotalDice(this):
        '''
            Returns
            -------
            int (how many dice you have)
        '''

        return sum(this.player.dice)
