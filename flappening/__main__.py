import argparse

from . import Game
from .neural import training

parser = argparse.ArgumentParser(description='play or train flappening')
parser.add_argument(
    'gameMode',
    metavar='gameMode',
    help='choose the gameMode. 0 : human playing, 1 : machine evolution',
    type=int,
    nargs='?',
    const=1,
)

# run iff file is main
if __name__ == '__main__':
    args = parser.parse_args()

    # initialize game with console parameters
    game = Game(
        gameMode=args.gameMode,
        playerCount=1 if args.gameMode == 0 else 200,
    )

    # run game for human
    if (args.gameMode == 0):

        print('game mode 0: human playing')
        game.run()

    # run game for machine training
    elif (args.gameMode == 1):

        print('game mode 1: machine training/evolution')
        training(game, epochs=30)
