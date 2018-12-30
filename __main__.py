from game.game import Game

from players.Template import Template
#from players.MiloRoll import MiloRoll
from players.Felix import Felix
from players.Papa import Papa

players = [
    Template,
    #MiloRoll,
    Felix,
    Papa
]

verbose = 2
training = True

game = Game(
    players,
    verbose,
    training
)

game.play(100)
