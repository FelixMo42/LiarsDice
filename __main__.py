from game.game import Game

from players.Template import Template
from players.MiloRoll import MiloRoll
from players.Felix import Felix

players = [
    Template,
    MiloRoll,
    Felix
]

verbose = 0

game = Game(
    players,
    verbose
)

game.play(100)
