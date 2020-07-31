from abc import ABC, abstractmethod

from flappening.entities import Bird


class Player(ABC):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, config):

        self.config = config

        self.bird = Bird(self.config)
        self.score: int = 0

    #
    #
    #  -------- Turn -----------
    #
    def turn(self, event):

        # --- Handle player interaction
        if (self.interact(event)):
            self.bird.flap()

        self.score += 1

    #
    #
    #  -------- interact -----------
    #
    @abstractmethod
    def interact(self, event=None):
        return NotImplementedError

    #
    #
    #  -------- draw -----------
    #
    def draw(self):
        self.bird.draw()

    #
    #
    #  -------- applyGravity -----------
    #
    def applyGravity(self):
        self.bird.applyGravity()

    #
    #
    #  -------- getScore -----------
    #
    def getScore(self):
        return self.score

    #
    #
    #  -------- getFitness -----------
    #
    def getFitness(self):
        return self.score / self.config['game']['max_score']
