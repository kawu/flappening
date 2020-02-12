import pygame

from config import game

# create default boundary object
BOUND = pygame.Rect((0, 0), game['size'])


# default particle class (rect):
class Particle(pygame.Rect):

    #
    #
    #  -------- Init -----------
    #
    def __init__(
            self,
            position: list = [0, 0],
            size: list = [0, 0],
            color=pygame.Color('BlACK'),
    ):

        super().__init__(position, size)

        # get corresponding screen object
        self.screen = pygame.display.get_surface()

        # save color
        self.color = color

    #  -------- inBound -----------
    #
    def inBound(self) -> bool:

        # Rect.contains(Rect)
        # https://www.pygame.org/docs/ref/rect.html#pygame.Rect.contains
        if (BOUND.contains(self)):
            return True

        return False

    #  -------- collision -----------
    #
    def collision(self, particle) -> bool:

        # Rect.colliderect(Rect)
        # https://www.pygame.org/docs/ref/rect.html#pygame.Rect.colliderect
        if (self.colliderect(particle)):
            return True

        return False

    #  -------- visible -----------
    #
    def visible(self) -> bool:

        if (self.collision(BOUND)):
            return True

        return False

    #  -------- draw -----------
    #
    def draw(self) -> None:

        # draw.rect(Surface[display.obj], Color[tuple], Particle[rect.object])
        # src: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
        pygame.draw.rect(self.screen, self.color, self)
