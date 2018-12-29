import random
import numpy as np

class Player:
    name = "default"
    numDice = 5

    def roll(self):
        self.dice = np.array([0] * 6)
        for i in range(self.numDice):
            self.dice[random.randint(0, 5)] += 1

    def loose(self):
        self.numDice -= 1

    def play(self, input):
        error("You must override the play method")

    def verify(self, input):
        error("You must override the verify method")
