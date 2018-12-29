import random
import numpy as np

class Player:
    name = "default"
    maxName = ""
    numDice = 5

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
        '''
            Raises
            ------
                NotImplementedError

            Returns
            -------
                [int (how many dice, 1-inifinity), int (what die, 0-5)]
        '''

        raise NotImplementedError("Player classes must override the play method!")


    def verify(self, input):
        '''
            Raises
            ------
                NotImplementedError

            Returns
            -------
                bool (wether you belive them or not)
        '''

        raise NotImplementedError("Player classes must override the verify method!")
