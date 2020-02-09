from lib.logger import Logger

from lib.player import Player

from config import game


class Machine(Player):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self):
        super().__init__()

        self.logger = Logger(muted=True)

        self.inBirdPosition: list = []
        self.inTubesPosition: list = []

    #
    #
    #  -------- Observe -----------
    #
    def observe(self, tubes):

        self.inBirdPosition = [
            self.bird.x / game['size'][0], self.bird.y / game['size'][1]
        ]

        # empty positions
        self.inTubesPosition = list()

        for tube in tubes:

            tubeXEnd = (tube.getXCenter() + tube.width / 2)

            self.inTubesPosition.append([
                tubeXEnd / game['size'][0],
                tube.getYCenter() / game['size'][1]
            ])

        self.log()

    #
    #
    #  -------- Log -----------
    #
    def log(self):
        self.logger.addSnapshot({
            'inBirdPosition': self.inBirdPosition,
            'inTubesPosition': self.inTubesPosition
        })

        self.logger.update({'score': self.getScore()})

    #
    #
    #  -------- Interact (dummy) -----------
    #
    def interact(self, event=None) -> bool:

        if (self.inBirdPosition[1] > .4):
            return True

        return False

    #  -------- isMachine -----------
    #
    def isMachine(self) -> bool:
        return True

    #  -------- getInBirdPosition -----------
    #
    def getInBirdPosition(self) -> list:
        return self.inBirdPosition

    #  -------- getInTubesPosition -----------
    #
    def getInTubesPosition(self) -> list:
        return self.inTubesPosition
