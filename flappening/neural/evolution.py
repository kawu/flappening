import random


def evolve(players) -> list:

    newPlayers: list = []

    for i in range(int(len(players) / 4)):

        # TODO: improve bird selection, fitness evalutation
        newPlayers.append(mutate(players[-1]))
        newPlayers.append(mutate(players[-2]))
        newPlayers.append(mutate(players[-3]))
        newPlayers.append(mutate(players[-4]))

    return newPlayers


def mutate(player, rate: float = 0.02):

    newPlayer = player.copy()

    # TODO: improve mutation with fitness

    for param in player.brain.parameters():

        # mutate weights of linear layer
        if (len(param.shape) == 2):
            for i0 in range(param.shape[0]):
                for i1 in range(param.shape[1]):
                    param[i0][i1] += rate * random.randint(-1, 1)

        # mutate biases of linear layer
        if (len(param.shape) == 1):
            for i0 in range(param.shape[0]):
                param[i0] += rate * random.randint(-1, 1)

    return newPlayer
