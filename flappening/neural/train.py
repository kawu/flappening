from datetime import datetime

from flappening.neural import Evolution
from flappening.utils import avgScore, plotHistory


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

    print('''
        [-- begin training: %s --]
    ''' % datetime.now())

    # history data collector
    train_history: list = []

    # load config if given
    if (config):
        players = config['player_num']
        toSurvive = config['survivor_num']
        epochs = config['epoch_num']
        mutationRate = config['mutation_rate']

    # create evolution object
    evolution = Evolution(
        mutationRate=mutationRate,
        toSurvive=toSurvive,
    )

    # initialize our starting players
    game.generatePlayers(players)

    print('''
        [-- training configuration --]
         -- players: %d
         -- epochs: %d
         -- mutation rate: %4f
         -- to surive: %d

        [-- training begin --]
        ''' % (players, epochs, mutationRate, toSurvive))

    for n in range(epochs):

        # run game
        game.run()

        # save current generation
        generation: list = game.getPlayersGarbage()

        # reset, preload game with next generation
        game.reset()
        game.loadPlayers(evolution.createNextGen(generation))

        # get results and append them, reuse for printing
        train_results: dict = {
            'epoch': n + 1,
            'avg_score': avgScore(generation),
            'best_score': generation[-1].getScore(),
        }
        train_history.append(train_results)

        # reporting
        print('[Gen: %3d] \t avg: %4d \t best: %4d' %
              (train_results['epoch'], train_results['avg_score'],
               train_results['best_score']))

    # plot graph
    plotHistory(train_history, config)

    print('''
        [-- finished training: %s --]
    ''' % datetime.now())
