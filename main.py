# import the game
from game import Game


def main():

    # create new Game Object
    # gameMode = 0 : human player
    # gameMode = 1 : single simple machine player
    myGame = Game(gameMode=1)

    # run the game
    myGame.run()


# run iff file is main
if __name__ == '__main__':
    main()
