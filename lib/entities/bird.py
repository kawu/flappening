from lib.entities import Particle

from config import bird


class Bird(Particle):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self,
                 screen,
                 velocity: float = bird['startVelocity'],
                 maxVelocity: float = bird['maxVelocity'],
                 lift: float = bird['lift']):

        super().__init__(
            screen,
            size=bird['size'],
            position=bird['startPosition'],
            color=bird['color'],
        )

        self.startVelocity: float = velocity
        self.velocity: float = velocity
        self.maxVelocity: float = maxVelocity
        self.lift: float = lift

    #
    #
    #  -------- Move -----------
    #
    def move(self, flapped: bool = False) -> None:

        if flapped:
            # lift in y position
            self.position[1] -= self.lift
            self.velocity = self.startVelocity

        else:
            # drop in y position
            self.position[1] += self.velocity

            # increase fall rate
            if (self.velocity < self.maxVelocity):
                self.velocity *= bird['attraction']
