import random


def evolve(players: list, toSurvive: int = 4) -> list:

    nextPlayers: list = []

    # elitism selection
    playerSelection: list = selectElite(players, toSurvive)

    # keep playerSelection
    nextPlayers.extend(playerSelection)

    # generate new players
    for i in range(len(players) - toSurvive):

        # select random player from selection
        randomSelected = playerSelection[random.randint(0, toSurvive - 1)]

        # mutate and append it
        nextPlayers.append(mutate(randomSelected))

    return nextPlayers


def mutate(player, rate: float = 0.005):

    newPlayer = player.copy()

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


def selectElite(players: list, n: int):

    ranking: list = sorted(players, key=lambda player: player.getScore())

    return ranking[len(ranking) - n:]
