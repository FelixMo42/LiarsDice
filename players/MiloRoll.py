import random
import numpy as np
from util.probability import atleast

class MiloRoll:
    name = "Milo"
    maxName = ""
    numDice = 5

    def __init__(self):
        self.FullIn = tf.zeros([15],dtype=tf.float32)
        self.L1 = tf.layers.dense(inputs=self.FullIn,units=20)
        self.L2 = tf.layers.dense(inputs=self.L1,units=20)
        self.L3 = tf.layers.dense(inputs=self.L2,units=20)
        self.L4 = tf.layers.dense(inputs=self.L3,units=10)
        self.out = tf.layers.dense(inputs=self.L4,units=1)
        self.init = tf.global_variables_initializer()
        self.sess = tf.Session()
        self.sess.run(self.init)

    def setup(self,input):
         Maxs = [0,0,0,0,0,0]
        for play in self.getBetHistory():
            if Maxs[play[0]-1] < play[1]:
                Maxs[play[0]-1] = play[1]
        dicelist = []
        for i in range(6):
            dicelist.append(self.getYourDice()[i][1])
        self.FullIn = tf.Tensor(Maxs + [len(self.players()),self.getTotalDice(),atleast(input.getBetHistory()[-1, 0], input.getTotalDice())] + dicelist + )

    def roll(self):
        '''Rolls your dice (do not override!)
        '''

        self.dice = np.array([0] * 6)
        for i in range(self.numDice):
            self.dice[random.randint(0, 5)] += 1

    def lose(self):
        '''Lowers your dice total by one (do not override!)
        '''

        self.numDice -= 1

    def play(self, input):
        prevNum = input.getBetHistory()[-1, 0]
        prevDie = input.getBetHistory()[-1, 1]

        if prevDie >= 5:
            return [prevNum + 1, 0]
        else:
            return [prevNum, prevDie + 1]

    def onPlay(self, correct, belived, input):
        '''Called after you make a claim when game is in training mode (implement me!)

            Parameters
            ----------
                input: PlayInput
                correct: bool (did you tell the truth)
                belived: bool (wether you were called out)
        '''

        pass

    def verify(self, input):
        self.setup(input)
        if sess.run(out) > .5:
            return True
        else:
            return False
    def onVerify(self, correct, belived, input):
        '''Called after you verify a claim when game in training mode (implement me!)

            Parameters
            ----------
                input: PlayInput
                correct: bool (did they tell the truth)
                belived: bool (wether you called them out)
        '''

        pass
        self.setup(input)
        optimizer = tf.train.GradientDescentOptimizer(0.01)

        if correct != belived:
            if sess.run(out) > .5:
                loss = (out - 1) ** 2
            else:
                loss = out ** 2
        else:
            if sess.run(out) > .5:
                loss = out ** 2
            else:
                loss = (out - 1) ** 2

    def onIllegalMove(self, input):
        '''Called after you make an illegal claim when game in training mode (implement me!)

            Parameters
            ----------
                input: PlayInput
        '''

        pass
