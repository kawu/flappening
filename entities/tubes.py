import random

from entities import Particle

from config import tubes
from config import game


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

        self.yCenter: float = self.rndYCenter()
        self.xCenter: float = game['size'][0] - self.width

        # TODO solve this elegant
        self.upper = Particle(self.screen,
                              size=[self.width, self.yCenter - self.gap / 2],
                              position=[self.xCenter, 0],
                              color=tubes['color'])

        # TODO solve this elegant
        self.lower = Particle(
            self.screen,
            size=[self.width, game['size'][1] - self.yCenter + self.gap / 2],
            position=[self.xCenter, self.yCenter + self.gap / 2],
            color=tubes['color'])

    def draw(self) -> None:
        self.upper.draw()
        self.lower.draw()

    def move(self) -> None:
        # move self center
        self.xCenter -= self.speed

        # move particles
        self.upper.position[0] -= self.speed
        self.lower.position[0] -= self.speed

    def rndYCenter(self) -> float:

        minY: int = self.padding + self.gap / 2
        maxY: int = game['size'][1] - self.padding - self.gap / 2

        # random.randint(min[px], max[px])
        # src: https://docs.python.org/2/library/random.html#random.randint
        return random.randint(minY, maxY)

    def inBound(self) -> bool:
        # check if both pipes are inBound:
        if (self.upper.inBound() or self.lower.inBound()):
            return True

        # default False:
        return False

    def collision(self, particle) -> bool:
        # check if on of the pipes are colliding:
        if (self.upper.collision(particle) or self.lower.collision(particle)):
            return True

        return False

    def getYCenter(self) -> float:
        return self.yCenter

    def getXCenter(self) -> float:
        return self.xCenter
