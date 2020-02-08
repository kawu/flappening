import argparse

from tests import test__training, test__playing

parser = argparse.ArgumentParser(description='play or train flappening')
parser.add_argument('gameMode',
                    metavar='gameMode',
                    help='choose the gameMode. 0 : playing, 1 : training',
                    type=int,
                    nargs='?',
                    const=1)

# run iff file is main
if __name__ == '__main__':
    args = parser.parse_args()

    if (args.gameMode == 0):
        test__playing()

    elif (args.gameMode == 1):
        test__training()

    else:
        test__training()
