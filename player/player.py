import pygame

from entities import Bird
from entities import Score


class Player():
    def __init__(self, screen, score):

        self.bird = Bird(screen)
        self.score = Score(screen, score)

    def turn(self):

        flapped = False

        # --- Create & Post syntetic user event
        event = pygame.event.Event(pygame.USEREVENT)
        pygame.event.post(event)

        # --- Main event loop
        for event in pygame.event.get():

            # --- Handle window close
            if event.type == pygame.QUIT:
                pygame.quit()

            # --- Check if game is lost:
            if (not (self.bird.inBound())):
                return False

            # --- Handle player interaction
            flapped = self.interact(event)

        self.bird.move(flapped=flapped)
        self.score.increase()

        return True

    # ABSTRACT METHOD
    def interact(self):
        pass

    def draw(self):
        self.bird.draw()
        self.score.draw()
