# import the game
from lib import Game

# import training
from lib.neural import training


def test__training():

    print('test running: machine training game play')

    myGame = Game(gameMode=2, playerCount=70)

    training(myGame, epochs=15)
