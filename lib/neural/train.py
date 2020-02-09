from .evolution import evolve


def training(game, epochs: int = 10):

    generation: list = []
    nextGeneration: list = []

    for n in range(epochs):

        # run game
        game.run()

        # save current generation, evolve the next
        generation = game.getPlayersGarbage()
        nextGeneration = evolve(generation)

        # reset, preload game
        game.reset()
        game.loadPlayers(nextGeneration)

        # reporting
        print('[Gen: %3d] \t avg: %4d \t best: %4d' %
              (n + 1, avgScore(generation), generation[-1].getScore()))


def avgScore(players):

    SUM = 0

    for item in [player.getScore() for player in players]:
        SUM = SUM + item

    AVG = SUM / len(players)

    return AVG
