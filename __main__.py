from game.game import Game

from players.Template import Template
#from players.MiloRoll import MiloRoll
from players.Felix import Felix, Felix0
from players.Papa import Papa

players = [
    Template,
#    MiloRoll,
    Felix,
    Felix0,
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
