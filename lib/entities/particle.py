import pygame

from config import game, colors


# default particle class (rectangular box):
class Particle:

    #
    #
    #  -------- Init -----------
    #
    def __init__(self,
                 screen,
                 size: list = [0, 0],
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

    #
    #
    #  -------- GetBoxModel -----------
    # TODO: solve this elegant:
    def getBoxModel(self) -> list:

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

    #
    #
    #  -------- inBound -----------
    #
    def inBound(self) -> bool:

        # check border collision for each point in box model
        for point in self.getBoxModel():

            # check if x is out of bound
            if (point[0] < 0 or point[0] > game['size'][0]):
                return False

            # check if y out of bound
            if (point[1] < 0 or point[1] > game['size'][1]):
                return False

        return True

    #
    #
    #  -------- Visible -----------
    #
    def visible(self) -> bool:

        # check if each point in box model is out of bound
        for point in self.getBoxModel():

            # check if x is out of bound
            if (not point[0] < 0 or not point[0] > game['size'][0]):
                return True

            # check if y out of bound
            if (not point[1] < 0 or not point[1] > game['size'][1]):
                return True

        return False

    #
    #
    #  -------- collision -----------
    #
    def collision(self, particle) -> bool:

        # Rectangle/Rectangle collision
        # src: http://www.jeffreythompson.org/collision-detection/rect-rect.php
        if (self.position[0] + self.size[0] >= particle.position[0]
                and self.position[0] <= particle.position[0] + particle.size[0]
                and self.position[1] + self.size[1] >= particle.position[1] and
                self.position[1] <= particle.position[1] + particle.size[1]):
            return True

        return False

    #  -------- draw -----------
    #
    def draw(self) -> None:
        # draw.rect(surface[display.obj], color[tuple], rect[left[px], top[px], width[px], height[px]])
        # src: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
        pygame.draw.rect(self.screen, self.color, (self.position, self.size))

    #  -------- getSize -----------
    #
    def getSize(self) -> list:

        # debug printing
        if (self.debug):
            print(self.size)

        return self.size

    #  -------- getPosition -----------
    #
    def getPosition(self) -> list:

        # debug printing
        if (self.debug):
            print(self.position)

        return self.position
