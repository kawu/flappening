from entities.particle import Particle

from config.bird import bird
from config.util import colors
from config.game import game


class Bird(Particle):
    def __init__(self,
                 screen,
                 velocity: float = bird['startVelocity'],
                 maxVelocity: float = bird['maxVelocity'],
                 lift: float = bird['lift']):

        super().__init__(
            screen,
            size=bird['size'],
            position=bird['startPosition'],
            color=colors['red'],
        )

        self.startVelocity: float = velocity
        self.velocity: float = velocity
        self.maxVelocity: float = maxVelocity
        self.lift: float = lift

    def draw(self):
        super().draw()

    def move(self, flapped: bool = False):

        if flapped:
            # lift in y position
            self.position[1] -= self.lift
            self.velocity = self.startVelocity

        else:
            # drop in y position
            self.position[1] += self.velocity

            # increase fall rate
            if (self.velocity < self.maxVelocity):
                self.velocity *= game['gravity']

    def inBound(self):

        boxModel = super().getBoxModel()

        # check border collision for each point in box model
        for point in boxModel:

            # check if x is out of bound
            if (point[0] < 0 or point[0] > game['size'][0]):
                return False

            # check if y out of bound
            if (point[1] < 0 or point[1] > game['size'][1]):
                return False

        return True