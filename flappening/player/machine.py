from flappening.player import Player


class Machine(Player):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, config):
        super().__init__(config)

        self.inBirdPosition: list = []
        self.inTubesPosition: list = []

    #
    #
    #  -------- Observe -----------
    #
    def observe(self, tubes):

        self.inBirdPosition = [
            self.bird.x / self.config['game']['size'][0],
            self.bird.y / self.config['game']['size'][1]
        ]

        # empty positions
        self.inTubesPosition = list()

        for tube in tubes:

            tubeXEnd = (tube.getXCenter() + tube.width / 2)

            self.inTubesPosition.append([
                tubeXEnd / self.config['game']['size'][0],
                tube.getYCenter() / self.config['game']['size'][1]
            ])

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
