from game.playInput import PlayInput
import numpy as np
import random

class Game:
    def __init__(this, players, verbose, training):
        this.players = []
        this.verbose = verbose
        this.training = training
        this.states = {}
        for player in players:
            p = player()
            this.players.append(p)
            this.states[p] = 0

        this.configureNames()

    def configureNames(this):
        maxLeng = len(this.players[0].name)
        for player in this.players:
            if len(player.name) > maxLeng:
                maxLeng = len(player.name)

        for player in this.players:
            player.maxName = player.name + " " * (maxLeng - len(player.name))


    def play(this, rounds=1):
        for i in range(rounds):
            this.states[Match(this).play()] += 1

        if rounds > 1:
            for dict in sorted(this.states.items(), key=lambda kv: -kv[1]):
                print('\033[37m' + dict[0].maxName + '\033[0m' + " │ " + '\033[37m' + str(dict[1] / rounds * 100) + "%" + '\033[0m')


class Match:
    turn = 0

    def __init__(this, game):
        this.game = game
        this.verbose = game.verbose

        this.players = []
        for player in game.players:
            player.reset()
            this.players.append(player)


    def play(this, round=1):
        while True:
            this.history = np.array([[0,5]])
            this.prevPlayer = False

            winner = this.cheakIfWinner()
            if winner:
                return winner

            this.setTotalDice()

            loser = this.round()
            loser.lose()
            if this.game.training:
                for player in this.players:
                    if player == loser:
                        loser.onWin(False)
                    else:
                        loser.onWin(True)

            if this.verbose == 2:
                print('\033[1m' + '\033[95m' + "round over!" + '\033[0m' + '\033[0m')
            elif this.verbose == 1:
                print("-------------------------------------")

    def cheakIfWinner(this):
        for player in this.players:
            if player.numDice == 0:
                this.players.remove(player)
                break

        if len(this.players) == 1:
            if this.verbose > 0:
                print('\033[1m' + '\033[95m' + this.players[0].name + " wins!" + '\033[0m' + '\033[0m' + u' \U0001F389')
            return this.players[0]

    def setTotalDice(this):
        random.shuffle(this.players)

        this.total = [0] * 6
        this.playersDice = []
        for player in this.players:
            player.roll()
            if this.verbose > 0:
                dice = ""
                for i in range(len(player.dice)):
                    dice = str(i + 1) * player.dice[i] + dice
                print('\033[37m' + player.maxName + '\033[0m' + " │ " + '\033[37m' + dice + '\033[0m')
            this.total += player.dice
            this.playersDice.append(player.numDice)

        this.totalDice = sum(this.total)

    def round(this):
        while True:
            # set up input and player
            this.input = PlayInput(this.history, this.players, this.turn)
            this.player = this.players[this.turn % len(this.players)]
            # did player call out previus player
            if this.prevPlayer:
                belived = this.player.verify(this.input)
                correct = this.total[this.history[-1][1]] >= this.history[-1][0]

                if this.game.training:
                    this.player.onVerify(correct, belived, this.input)
                    this.prevPlayer.onPlay(correct, belived, this.input)

                if not belived:
                    if correct:
                        if this.verbose == 2:
                            print('\033[37m' + this.player.maxName + " falsely called out " + this.prevPlayer.name + '\033[0m')

                        return this.player
                    elif not correct:
                        if this.verbose == 2:
                            print('\033[37m' + this.player.maxName + " correctly called out " + this.prevPlayer.name + '\033[0m')

                        return this.prevPlayer

            # what is the player saying
            move = this.player.play(this.input)
            if this.verbose:
                print('\033[37m' + this.player.maxName + " said " + str(move[0]) + " " + str(move[1] + 1) + "'s" + '\033[0m')

            try:
                # is the move legal?
                this.moveIsLegal(move)
            except Exception as err:
                # if its not legal
                if this.game.training:
                    this.player.onIllegalMove(this.input)

                print(this.player.name + " didn\'t give a proper result: " + str(err))
                return this.player

            # add the move to the history of all bets
            this.history = np.append(this.history, [move], axis=0)

            this.turn += 1
            this.prevPlayer = this.player

    def moveIsLegal(this, move):
        if move[1] > 5 or move[1] < 0:
            raise Exception('die must be 0-5. It was: {}'.format(move[1]))
        elif move[0] < 1:
            raise Exception('quantity must be 1 or more. It was: {}'.format(move[0]))
        elif move[0] < this.history[-1, 0]:
            raise Exception('quantity {} is lower than the previous bet\'s quantity of {}'.format(move[0], this.history[-1, 0]))
        elif move[0] == this.history[-1, 0] and move[1] <= this.history[-1, 1]:
            raise Exception('{} {}\'s isn\'t higher than the previous bet, {} {}\'s'.format(move[0], move[1], this.history[-1, 0], this.history[-1, 1]))
