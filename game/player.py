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
        '''(implement me!)

            Parameters
            ----------
                input: PlayInput

            Raises
            ------
                NotImplementedError

            Returns
            -------
                [int (how many dice, 1-inifinity), int (what die, 0-5)]
        '''

        raise NotImplementedError("Player classes must override the play method!")

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
        '''(implement me!)

            Parameters
            ----------
                input: PlayInput

            Raises
            ------
                NotImplementedError

            Returns
            -------
                bool (wether you belive them or not)
        '''

        raise NotImplementedError("Player classes must override the verify method!")

    def onVerify(self, correct, belived, input):
        '''Called after you verify a claim when game in training mode (implement me!)

            Parameters
            ----------
                input: PlayInput
                correct: bool (did they tell the truth)
                belived: bool (wether you called them out)
        '''

        pass

    def onIllegalMove(self, input):
        '''Called after you make an illegal claim when game in training mode (implement me!)

            Parameters
            ----------
                input: PlayInput
        '''

        pass

    def onWin(self, didWin):
        '''Called after the round ends (implement me!)

            Parameters
            ----------
                didWin: bool (did I win)
        '''

        pass
