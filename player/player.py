from entities.bird import Bird
from entities.util import Score


class Player():
    def __init__(self, screen, score):

        self.bird = Bird(screen)
        self.score = Score(screen, score)

    # ABSTRACT METHOD
    def turn(self):
        pass

    def draw(self):
        self.bird.draw()
        self.score.draw()