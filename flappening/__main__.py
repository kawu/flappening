import torch
import random

import argparse

from flappening import Game
from flappening.neural import training

# ensure that each run is somewhat identically
torch.manual_seed(42)
random.seed(42)

#
#
#  -------- ARGPARSER -----------
#
parser = argparse.ArgumentParser(description='play or train flappening')

# argument: gameMode
parser.add_argument(
    'gameMode',
    metavar='gameMode',
    help='choose the game mode (0 : human playing, 1 : machine evolution)',
    type=int,
    nargs='?',
    default=1,
)

# argument: playerCount
parser.add_argument(
    'playerCount',
    metavar='playerCount',
    help='choose the number of players (only for machine evolution)',
    type=int,
    nargs='?',
    default=200,
)

# argument: trainEpochs
parser.add_argument(
    'trainEpochs',
    metavar='trainEpochs',
    help='choose the number train epochs (only for machine evolution)',
    type=int,
    nargs='?',
    default=10,
)

# argument: mutationRate
parser.add_argument(
    'mutationRate',
    metavar='mutationRate',
    help='choose the mutation rate (only for machine evolution)',
    type=float,
    nargs='?',
    default=0.02,
)

# argument: toSurvive
parser.add_argument(
    'toSurvive',
    metavar='toSurvive',
    help='choose how many players survive (only for machine evolution)',
    type=int,
    nargs='?',
    default=20,
)

# run iff file is main
if __name__ == '__main__':
    args = parser.parse_args()

    # initialize game with console parameters
    game = Game(
        gameMode=args.gameMode,
        playerCount=1 if args.gameMode == 0 else args.playerCount,
    )

    # run game for human
    if (args.gameMode == 0):

        print('game mode 0: human playing')
        game.run()

    # run game for machine training
    elif (args.gameMode == 1):

        print('game mode 1: machine training/evolution')
        training(
            game,
            players=args.playerCount,
            epochs=args.trainEpochs,
            mutationRate=args.mutationRate,
            toSurvive=args.toSurvive,
        )
