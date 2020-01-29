import pygame

import config


class Player:
    def __init__(self,
                 screen,
                 size: int = config.player['size'],
                 position: set = config.player['startPosition'],
                 velocity: float = config.player['velocity'],
                 stepSize: int = config.player['stepSize'],
                 color: set = config.colors['red'],
                 debug: bool = False):

        super().__init__()

        # enables additional printing
        self.debug: bool = debug

        # saves corresponding screen object
        self.screen = screen

        self.alive: bool = True
        self.score: int = 0

        self.size: int = size
        self.position: set = position
        self.velocity: float = velocity
        self.stepSize: int = stepSize

        self.color: set = color

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.position, self.size))

    def move(self, direction):

        self.position = (self.position[0] + self.stepSize * direction[0],
                         self.position[1] + self.stepSize * direction[1])

        if (self.debug):
            print(self.position)
