from game.game import Game

from players.Template import Template
#from players.MiloRoll import MiloRoll
from players.Felix import Felix, Felix0
from players.Papa1 import Papa1
from players.Papa2 import Papa2
from players.Papa3 import Papa3

players = [
    Template,
    #MiloRoll,
    Felix,
    #Felix0,
    Papa1,
    Papa2,
    Papa3
]

verbose = 0
training = True

game = Game(
    players,
    verbose,
    training
)

game.play(500)
