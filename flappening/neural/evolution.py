import random

from flappening.utils import avgScore

# ensure mutation is identically every run
random.seed(42)


class Evolution():

    #
    #
    #  -------- Init -----------
    #
    def __init__(
            self,
            mutationRate: float = 0.02,
            toSurvive: int = 20,
    ):

        super().__init__()

        self.mutationRate = mutationRate
        self.toSurvive = toSurvive

        self.bestPlayerHistory: list = []

    #
    #
    #  -------- createNextGen -----------
    #
    def createNextGen(self, players: list) -> list:

        nextPlayers: list = []

        # elitism selection
        playerSelection: list = self.selectElite(players, self.toSurvive)

        # use elite players from last generation if they perform better
        if (avgScore(playerSelection) <= avgScore(self.bestPlayerHistory[-1])):
            playerSelection = self.bestPlayerHistory[-1]

        # generate new players
        for i in range(len(players)):

            # select random player from selection
            randomSelected = playerSelection[random.randint(
                0, self.toSurvive - 1)]

            # mutate and append it
            nextPlayers.append(self.mutate(randomSelected))

        return nextPlayers

    #
    #
    #  -------- mutate -----------
    #
    def mutate(self, player):

        newPlayer = player.copy()

        for param in player.brain.parameters():

            # mutate weights of linear layer
            if (len(param.shape) == 2):
                for i0 in range(param.shape[0]):
                    for i1 in range(param.shape[1]):
                        param[i0][i1] += self.mutationRate * random.randint(
                            -1, 1)

            # mutate biases of linear layer
            if (len(param.shape) == 1):
                for i0 in range(param.shape[0]):
                    param[i0] += self.mutationRate * random.randint(-1, 1)

        return newPlayer

    #  -------- selectElite -----------
    #
    def selectElite(self, players: list, n: int):

        ranking: list = sorted(players, key=lambda player: player.getScore())

        elite: list = ranking[len(ranking) - n:]

        self.bestPlayerHistory.append(elite)

        return elite
