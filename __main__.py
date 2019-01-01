from game.game import Game

from players.Template import Template
#from players.MiloRoll import MiloRoll
from players.Felix import Felix, Felix0
from players.Papa1 import Papa1
from players.Papa2 import Papa2
from players.Papa3 import Papa3
from players.Papa4 import Papa4
from players.Papa5 import Papa5
from players.Papa6 import Papa6

players = [
    #Template,
    #MiloRoll,
    Felix,
    #Felix0,
    #Papa1,
    #Papa2,
    #Papa3,
    Papa4,
    Papa5,
    Papa6
]

verbose = 0
training = True

game = Game(
    players,
    verbose,
    training
)

game.play(500)
