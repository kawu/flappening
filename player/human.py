import pygame

from player.player import Player

from config.util import events, keys


class Human(Player):
    def __init__(self, screen, score):
        super().__init__(
            screen,
            score,
        )

    def turn(self):

        flapped = False

        # --- Main event loop
        for event in pygame.event.get():

            # --- Handle window close
            if event.type == pygame.QUIT:
                pygame.quit()

            # --- Check if game is lost:
            if (not (self.bird.inBound())):
                return False

            # --- Handle user interaction
            if event.type == events['KEYDOWN']:

                # UP KEY
                if (event.key == keys['up']):
                    flapped = True

        self.bird.move(flapped=flapped)
        self.score.increase()

        return True

    def draw(self):
        super().draw()