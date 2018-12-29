###########
# OPTIONS #
###########

verbose = False

########
# CODE #
########

from player import Player
import numpy as np

from players.Template import Template

players = [
    Template(),
    Player()
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
        player = players[turn % len(players)]
        if prevPlayer and not player.verify(
            history=history,
            players=playersDice,
            totalDice=totalDice,
            numDice=player.numDice,
            dice=player.dice
        ):
            if total[history[-1][1]] >= history[-1][0]:
                if verbose:
                    print(player.name + " falsely called out " + prevPlayer.name)
                player.loose()
                break
            else:
                if verbose:
                    print(player.name + " correctly called out " + prevPlayer.name)
                prevPlayer.loose()
                break

        move = player.play(
            history=history,
            players=playersDice,
            totalDice=totalDice,
            numDice=player.numDice,
            dice=player.dice
        )
        if verbose:
            print(player.name + " said " + str(move[0]) + " " + str(move[1] + 1) + "'s")
        if move[0] < history[-1, 0] or move[1] > 5 or (move[0] == history[-1, 0] and move[1] <= history[-1, 1]):
            print(player.name + " didnt give a proper result")
            player.loose()
            break
        history = np.append(history, [move], axis=0)

        turn += 1
        prevPlayer = player

    if verbose:
        print("round over!")
    else:
        print("-------------------------------------")
