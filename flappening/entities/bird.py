import pygame

from flappening.entities import Particle


class Bird(Particle):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, config: dict):

        # save shared config
        self.config = config['game']['bird']

        # deepcopying the inputs:
        self.startVelocity = float(self.config['startVelocity'])
        self.velocity = float(self.config['startVelocity'])
        self.maxVelocity = float(self.config['maxVelocity'])

        self.lift = float(self.config['lift'])
        self.attraction = float(self.config['attraction'])

        # call particle constructor
        super().__init__(
            size=self.config['size'],
            position=self.config['startPosition'],
            color=pygame.Color('RED'),
        )

    #
    #
    #  -------- Move -----------
    #
    def move(self, flapped: bool = False) -> None:

        if flapped:
            # lift in y position
            self.y -= self.lift
            self.velocity = self.startVelocity

        else:
            # drop in y position
            self.y += self.velocity

            # increase fall rate
            if (self.velocity < self.maxVelocity):
                self.velocity *= self.attraction
