def training(game, epochs: int = 10):

    for n in range(epochs):

        game.run()

        players = game.getPlayersGarbage()

        freq = {}

        for item in [player.getScore() for player in players]:

            if (item in freq):
                freq[item] += 1

            else:
                freq[item] = 1

        print('Scores for epoch: \t' + str(n) + ' : ' + str(freq))

        game.reset()
