from game.player import Player
from util.probability import atleast
import numpy as np


'''class Felix0(Player):
    name = "Felix"

    def __init__(this):
        this.minProb = tf.Variable(.5)
        this.sess = tf.Session()
        this.sess.run(this.minProb.initializer)
        #this.train_op = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

    def play(this, input):
        prevNum = input.getBetHistory()[-1, 0]
        prevDie = input.getBetHistory()[-1, 1]

        if prevDie >= 5:
            return [prevNum + 1, 0]
        else:
            return [prevNum, prevDie + 1]

    def verify(this, input):
        return atleast(input.getBetHistory()[-1, 0], input.getTotalDice()) > this.sess.run(this.minProb)

    def onVerify(this, a, b, input):
        if a == b:
            loss = 1
        else:
            loss = -1
        print("LOSS",loss)
        if loss > 0:
            this.minProb.assign_add(.01)
            print("minProb", this.sess.run(this.minProb))
        elif loss < 0:
            this.minProb.assign_add(-.01)
            print("minProb", this.sess.run(this.minProb))

    def onWin(this, win):
        print(this.sess.run(this.minProb))'''

class Felix(Player):
    name = "FelixBot_alpha"

    prob = .2
    safe = .8

    def play(this, input):
        qty = input.getBetHistory()[-1, 0]
        die = np.argmax(this.dice)

        if qty < this.dice[die]:
            qty = this.dice[die]
        elif input.getBetHistory()[-1, 1] >= die:
            qty += 1

        while this.getOdds([qty + 1, die], input) > this.safe:
            qty += 1

        return [qty, die]

    def verify(this, input):
        return this.getOdds(input.getBetHistory()[-1], input) > this.prob

    def getOdds(this, move, input):
        return atleast(
            move[0] - input.getYourDice()[move[1]],
            input.getTotalDice() - input.getYourTotalDice()
        )

class Felix0(Player):
    name = "FelixBot_beta"

    prob = .2
    safe = .8

    def play(this, input):
        qty = input.getBetHistory()[-1, 0]
        die = np.argmax(this.dice)

        if qty < this.dice[die]:
            qty = this.dice[die]
        elif input.getBetHistory()[-1, 1] >= die:
            qty += 1

        while this.getOdds([qty + 1, die], input) > this.safe:
            qty += 1

        return [qty, die]

    def verify(this, input):
        return this.getOdds(input.getBetHistory()[-1], input) > this.prob

    def getOdds(this, move, input):
        return atleast(
            move[0] - input.getYourDice()[move[1]],
            input.getTotalDice() - input.getYourTotalDice()
        )
