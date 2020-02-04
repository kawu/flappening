from entities.particle import Particle

from config.tubes import tubes


class Tubes():
    def __init__(self,
                 screen,
                 width: float = tubes['width'],
                 gap: float = tubes['gap'],
                 speed: float = tubes['speed']):

        super().__init__()

        self.screen = screen

        self.width: float = width
        self.gap: float = gap
        self.speed: float = speed

        self.upper = Particle(self.screen, color=tubes['color'])
        self.lower = Particle(self.screen, color=tubes['color'])

    def draw(self):
        self.upper.draw()
        self.lower.draw()

    # TODO implement
    def move(self):
        pass
