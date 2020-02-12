# import the game
from flappening import Game

# import training
from flappening.neural import training


def test__training():

    print('test running: machine training game play')

    myGame = Game(gameMode=2, playerCount=200)

    training(myGame, epochs=30)
