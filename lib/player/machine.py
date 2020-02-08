from lib.logger import Logger

from lib.player import Player

from config import game


class Machine(Player):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, screen, score):
        super().__init__(
            screen,
            score,
        )

        self.logger = Logger(gameMode=1)

        self.inBirdPosition: list = []
        self.inTubesPosition: list = []

    #
    #
    #  -------- Observe -----------
    #
    def observe(self, tubes):

        self.inBirdPosition = [
            self.bird.position[0] / game['size'][0],
            self.bird.position[1] / game['size'][1]
        ]

        for tube in tubes:
            self.inTubesPosition.append([
                tube.getXCenter() / game['size'][0],
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

        self.logger.update({'score': self.score.getValue()})

    #
    #
    #  -------- Interact (dummy) -----------
    #
    def interact(self, event) -> bool:

        if (self.inBirdPosition[1] > .4):
            return True

        return False

    #  -------- draw -----------
    #
    def draw(self):
        super().draw()

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
