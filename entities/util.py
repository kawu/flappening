import pygame

from entities.particle import Particle

from config.util import colors


class Score(Particle):
    def __init__(self, screen, value):

        super().__init__(
            screen,
            size=24,
            position=[600, 25],
            color=colors['black'],
        )

        self.value = value

        self.font = pygame.font.Font(None, self.size)

    def increase(self):
        self.value += 1

    def draw(self):
        text = self.font.render('Score: ' + str(self.value), False, self.color)
        self.screen.blit(text, self.position)
