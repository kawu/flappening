import random

from entities.particle import Particle

from config.tubes import tubes
from config.game import game


class Tubes():
    def __init__(self,
                 screen,
                 width: int = tubes['width'],
                 padding: int = tubes['padding'],
                 gap: int = tubes['gap'],
                 speed: float = tubes['speed']):

        super().__init__()

        self.screen = screen

        self.width: int = width
        self.padding: int = padding
        self.gap: int = gap
        self.speed: float = speed

        self.yCenter = self.rndYCenter()

        # TODO cleaning
        self.upper = Particle(self.screen,
                              size=[self.width, self.yCenter - self.gap / 2],
                              position=[600, 0],
                              color=tubes['color'])

        # TODO cleaning
        self.lower = Particle(
            self.screen,
            size=[self.width, game['size'][1] - self.yCenter + self.gap / 2],
            position=[600, self.yCenter + self.gap / 2],
            color=tubes['color'])

    def draw(self):
        self.upper.draw()
        self.lower.draw()

    def move(self):
        self.upper.position[0] -= self.speed
        self.lower.position[0] -= self.speed

    def rndYCenter(self):

        minY: int = self.padding + self.gap / 2
        maxY: int = game['size'][1] - self.padding - self.gap / 2

        # random.randint(min[px], max[px])
        # src: https://docs.python.org/2/library/random.html#random.randint
        return random.randint(minY, maxY)

    def getYCenter(self):
        return self.yCenter
