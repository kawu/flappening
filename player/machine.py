from player.player import Player

from config import game  # , events


class Machine(Player):
    def __init__(self, screen, score):
        super().__init__(
            screen,
            score,
        )

        self.inBirdPosition: list = []
        self.inTubesPosition: list = []

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

    # DUMMY:
    def interact(self, event):

        if (True):  # event.type == events['USEREVENT']

            print(self.inBirdPosition)
            print(self.inTubesPosition)

            if (self.inBirdPosition[1] > .4):
                return True

        return False

    def draw(self):
        super().draw()

    def isMachine(self):
        return True
