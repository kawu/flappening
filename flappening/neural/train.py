from flappening.neural.evolution import Evolution

from flappening.utils import avgScore


def training(
        game,
        epochs: int = 10,
        mutationRate: float = 0.02,
        toSurvive: int = 20,
):

    evolution = Evolution(
        mutationRate=mutationRate,
        toSurvive=toSurvive,
    )

    print('''
        [-- training configuration --]
         -- epochs: %d
         -- mutation rate: %4f
         -- to surive: %d

        [-- training begin --]
        ''' % (epochs, mutationRate, toSurvive))

    for n in range(epochs):

        # run game
        game.run()

        # save current generation
        generation: list = game.getPlayersGarbage()

        # reset, preload game with next generation
        game.reset()
        game.loadPlayers(evolution.createNextGen(generation))

        # reporting
        print('[Gen: %3d] \t avg: %4d \t best: %4d' %
              (n + 1, avgScore(generation), generation[-1].getScore()))
