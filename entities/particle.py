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

    # TODO: solve this elegant:
    def getBoxModel(self):

        # p(x,y)px
        p1 = tuple(self.position)  # top left
        p3 = (self.position[0], self.position[1] + self.size[1])  # top right
        p2 = (self.position[0] + self.size[0], self.position[1])  # bottom left
        p4 = (self.position[0] + self.size[0], self.position[1] + self.size[1]
              )  # bottom right

        # debug printing
        if (self.debug):
            print([p1, p2, p3, p4])

        return [p1, p2, p3, p4]

    def draw(self):
        # draw rect(surface[screen], color, (left[y], top[x], width, height))
        # src: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
        pygame.draw.rect(self.screen, self.color, (self.position, self.size))
