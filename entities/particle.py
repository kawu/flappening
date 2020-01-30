import pygame

from config.util import colors


# default particle class (rectangular box):
class Particle:
    def __init__(self,
                 screen,
                 size: int = 0,
                 position: list = [0, 0],
                 color: set = colors['black'],
                 debug: bool = False):
        super().__init__()

        # enables additional printing
        self.debug: bool = debug

        # saves corresponding screen object
        self.screen = screen

        self.size: int = size
        self.position: list = position
        self.color: set = color

    def getSize(self):

        # debug printing
        if (self.debug):
            print(self.size)

        return self.size

    def getPosition(self):

        # debug printing
        if (self.debug):
            print(self.position)

        return self.position

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.position, self.size))
