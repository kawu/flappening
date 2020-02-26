from flappening.neural import Evolution
from flappening.utils import avgScore


#
#  -------- training -----------
#
def training(
        game,
        players: int = 200,
        epochs: int = 10,
        mutationRate: float = 0.02,
        toSurvive: int = 20,
        config: dict = None,
):

    if (config):
        players = config['player_num']
        toSurvive = config['survivor_num']
        epochs = config['epoch_num']
        mutationRate = config['mutation_rate']

    evolution = Evolution(
        mutationRate=mutationRate,
        toSurvive=toSurvive,
    )

    print('''
        [-- training configuration --]
         -- players: %d
         -- epochs: %d
         -- mutation rate: %4f
         -- to surive: %d

        [-- training begin --]
        ''' % (players, epochs, mutationRate, toSurvive))

    # initialize our starting players:
    game.generatePlayers(players)

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
