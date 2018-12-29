from game.playInput import PlayInput
import numpy as np
import random

class Game:
    def __init__(this, players, verbose):
        this.players = players
        this.verbose = verbose
        this.states = {}
        this.configureNames()
        for player in players:
            this.states[player.name] = 0

    def configureNames(this):
        maxLeng = len(this.players[0].name)
        for player in this.players:
            if len(player.name) > maxLeng:
                maxLeng = len(player.name)

        for player in this.players:
            player.name = player.name + " " * (maxLeng - len(player.name))


    def play(this, rounds=1):
        for i in range(rounds):
            this.states[Match(this).play().name] += 1

        if rounds > 1:
            for dict in sorted(this.states.items(), key=lambda kv: -kv[1]):
                print(dict[0] + " | " + str(dict[1] / rounds * 100) + "%")


class Match:
    turn = 0

    def __init__(this, game):
        this.game = game
        this.verbose = game.verbose

        this.players = []
        for player in game.players:
            this.players.append(player())


    def play(this, round=1):
        while True:
            this.history = np.array([[0,5]])
            this.prevPlayer = False

            winner = this.cheakIfWinner()
            if winner:
                return winner

            this.getTotalDice()

            this.round().lose()

            if this.verbose == 2:
                print("round over!")
            elif this.verbose == 1:
                print("-------------------------------------")

    def cheakIfWinner(this):
        for player in this.players:
            if player.numDice == 0:
                this.players.remove(player)
                break

        if len(this.players) == 1:
            if this.verbose > 0:
                print(this.players[0].name + " wins!")
            return this.players[0]

    def getTotalDice(this):
        random.shuffle(this.players)

        this.total = [0] * 6
        this.playersDice = []
        for player in this.players:
            if this.verbose > 0:
                print(player.name + " | " + "*" * player.numDice)
            player.roll()
            this.total += player.dice
            this.playersDice.append(player.numDice)

        this.totalDice = sum(this.total)

    def round(this):
        while True:
            # set up input and player
            this.input = PlayInput(this.history, this.players, this.turn)
            this.player = this.players[this.turn % len(this.players)]
            # did player call out previus player
            if this.prevPlayer and not this.player.verify(this.input):
                # if he right
                if this.total[this.history[-1][1]] >= this.history[-1][0]:
                    if this.verbose == 2:
                        print(this.player.name + " falsely called out " + this.prevPlayer.name)
                    return this.player
                # if he was wrong
                else:
                    if this.verbose == 2:
                        print(this.player.name + " correctly called out " + this.prevPlayer.name)
                    return this.prevPlayer
            # what is the player saying
            move = this.player.play(this.input)
            if this.verbose:
                print(this.player.name + " said " + str(move[0]) + " " + str(move[1] + 1) + "'s")
            # if its not legal
            if not this.moveIsLegal(move):
                print(this.player.name + " didnt give a proper result")
                return this.player
            # add the move to the history of all bets
            this.history = np.append(this.history, [move], axis=0)

            this.turn += 1
            this.prevPlayer = this.player

    def moveIsLegal(this, move):
        if move[1] > 5:
            return False
        if move[0] >= this.history[-1, 0]:
            return True
        if move[0] == this.history[-1, 0] and move[1] <= this.history[-1, 1]:
            return True
        else:
            return False
