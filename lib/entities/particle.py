import pygame

from config import game, colors


# default particle class (rect):
class Particle(pygame.Rect):

    # create default boundary object
    BOUND = pygame.Rect((0, 0), game['size'])

    #
    #
    #  -------- Init -----------
    #
    def __init__(self,
                 position: list = [0, 0],
                 size: list = [0, 0],
                 color: tuple = colors['black']):

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
        if (self.BOUND.contains(self)):
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

        if (self.collision(self.BOUND)):
            return True

        return False

    #  -------- draw -----------
    #
    def draw(self) -> None:

        # draw.rect(Surface[display.obj], Color[tuple], Particle[rect.object])
        # src: https://www.pygame.org/docs/ref/draw.html#pygame.draw.rect
        pygame.draw.rect(self.screen, self.color, self)
