def training(game, epochs: int = 10, players: int = 10):

    for n in range(epochs):
        game.setup()
        game.run()
