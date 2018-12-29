###########
# OPTIONS #
###########

verbose = False

########
# CODE #
########

from player import Player
from playInput import PlayInput
import numpy as np

from players.Template import Template
from players.MiloRoll import MiloRoll

players = [
    Template(),
    MiloRoll()
]

#print(players)

turn = 0
while True:
    history = np.array([[0,5]])
    prevPlayer = False

    for player in players:
        if player.numDice == 0:
            players.remove(player)
            break

    if len(players) == 1:
        print(players[0].name + " wins!")
        break

    total = [0] * 6
    playersDice = []
    for player in players:
        print(player.name + " | " + "*" * player.numDice)
        player.roll()
        total += player.dice
        playersDice.append(player.numDice)

    totalDice = sum(total)

    while True:
        input = PlayInput(history, players, turn)

        player = players[turn % len(players)]
        if prevPlayer and not player.verify(input):
            if total[history[-1][1]] >= history[-1][0]:
                if verbose:
                    print(player.name + " falsely called out " + prevPlayer.name)
                player.lose()
                break
            else:
                if verbose:
                    print(player.name + " correctly called out " + prevPlayer.name)
                prevPlayer.lose()
                break

        move = player.play(input)
        if verbose:
            print(player.name + " said " + str(move[0]) + " " + str(move[1] + 1) + "'s")
        if move[0] < history[-1, 0] or move[1] > 5 or (move[0] == history[-1, 0] and move[1] <= history[-1, 1]):
            print(player.name + " didnt give a proper result")
            player.lose()
            break
        history = np.append(history, [move], axis=0)

        turn += 1
        prevPlayer = player

    if verbose:
        print("round over!")
    else:
        print("-------------------------------------")
