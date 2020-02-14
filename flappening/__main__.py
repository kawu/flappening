import argparse

from flappening import Game
from flappening.neural import training

parser = argparse.ArgumentParser(description='play or train flappening')

# argument: gameMode
parser.add_argument(
    '-m',
    metavar='gameMode',
    help='choose the game mode (0 : human playing, 1 : machine evolution)',
    type=int,
    nargs='?',
    default=1,
)

# argument: playerCount
parser.add_argument(
    '-p',
    metavar='playerCount',
    help='choose the number of players (only for machine evolution)',
    type=int,
    nargs='?',
    default=200,
)

# argument: trainEpochs
parser.add_argument(
    '-e',
    metavar='trainEpochs',
    help='choose the number train epochs (only for machine evolution)',
    type=int,
    nargs='?',
    default=10,
)

# argument: mutationRate
parser.add_argument(
    '-r',
    metavar='mutationRate',
    help='choose the mutation rate (only for machine evolution)',
    type=float,
    nargs='?',
    default=0.02,
)

# argument: toSurvive
parser.add_argument(
    '-s',
    metavar='toSurvive',
    help='choose how many players survive (only for machine evolution)',
    type=int,
    nargs='?',
    default=10,
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
