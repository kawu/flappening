import pygame

from entities.particle import Particle

from config.util import colors


class Score(Particle):
    def __init__(self, screen, value: int = 0, increment: int = 1):

        super().__init__(
            screen,
            size=24,
            position=[600, 25],
            color=colors['black'],
        )

        self.value = value
        self.increment = increment

        # font.font(typeface[string], size[px])
        # https://www.pygame.org/docs/ref/font.html#pygame.font.Font
        self.font = pygame.font.Font(None, self.size)

    def increase(self):
        self.value += self.increment

    def draw(self):

        # font.render(text[font.obj], antialias[bool], color[tuple])
        # src: https://www.pygame.org/docs/ref/font.html#pygame.font.Font.render
        text = self.font.render('Score: ' + str(self.value), True, self.color)

        # surface.blit(content[pygame.obj], position[tuple])
        # src: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
        self.screen.blit(text, self.position)

    def getValue(self):
        return self.value
