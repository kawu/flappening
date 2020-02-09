import random

from lib.entities import Particle

from config import tubes, game


class Tubes():

    #
    #
    #  -------- Init -----------
    #
    def __init__(
            self,
            width: int = tubes['width'],
            padding: int = tubes['padding'],
            gap: int = tubes['gap'],
            speed: float = tubes['speed'],
    ):

        super().__init__()

        self.width: int = width
        self.padding: int = padding
        self.gap: int = gap
        self.speed: float = speed

        self.yCenter: float = self.rndYCenter()
        self.xCenter: float = game['size'][0]

        # TODO solve this elegant
        self.upper = Particle(
            position=[self.xCenter, 0],
            size=[self.width, self.yCenter - self.gap / 2],
            color=tubes['color'],
        )

        # TODO solve this elegant
        self.lower = Particle(
            position=[self.xCenter, self.yCenter + self.gap / 2],
            size=[self.width, game['size'][1] - self.yCenter + self.gap / 2],
            color=tubes['color'],
        )

    #
    #
    #  -------- Visible -----------
    #
    def visible(self) -> bool:
        # check if both pipes are inBound:
        if (self.upper.visible() or self.lower.visible()):
            return True

        # default False:
        return False

    #
    #
    #  -------- Collision -----------
    #
    def collision(self, particle) -> bool:
        # check if on of the pipes are colliding:
        if (self.upper.collision(particle) or self.lower.collision(particle)):
            return True

        # default False:
        return False

    #
    #
    #  -------- Move -----------
    #
    def move(self) -> None:
        # move self center
        self.xCenter -= self.speed

        # move particles
        self.upper.x -= self.speed
        self.lower.x -= self.speed

    #
    #
    #  -------- rndYCenter -----------
    #
    def rndYCenter(self) -> float:

        minY: int = self.padding + self.gap / 2
        maxY: int = game['size'][1] - self.padding - self.gap / 2

        # random.randint(min[px], max[px])
        # src: https://docs.python.org/2/library/random.html#random.randint
        return random.randint(minY, maxY)

    #  -------- draw -----------
    #
    def draw(self) -> None:
        self.upper.draw()
        self.lower.draw()

    #  -------- getYCenter -----------
    #
    def getYCenter(self) -> float:
        return self.yCenter

    #  -------- getXCenter -----------
    #
    def getXCenter(self) -> float:
        return self.xCenter
