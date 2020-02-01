import pygame

from entities.bird import Bird
from entities.util import Score

from config.game import game
from config.util import colors, events, keys


class Game:

    #
    #
    #  -------- Init -----------
    #
    def __init__(self):
        super().__init__()

        self.setup()
        self.run()

    #
    #
    # -------- Setup -----------
    #
    def setup(self):

        # init pygame
        pygame.init()

        # set & save screen
        self.screen = pygame.display.set_mode(game['size'])

        # add screen title
        pygame.display.set_caption(game['title'])

        # initiate & save game clock
        self.clock = pygame.time.Clock()

        # initiate player, score
        self.bird = Bird(self.screen)
        self.score = Score(self.screen, 0)

    #
    #
    # -------- Game Loop -----------
    #
    def run(self):

        while True:

            # --- Main event loop
            for event in pygame.event.get():

                flapped = False

                # window close handler
                if event.type == pygame.QUIT:

                    # Close the window and quit.
                    pygame.quit()

                # game logic for keydown presses
                if event.type == events['KEYDOWN']:

                    # UP KEY
                    if (event.key == keys['up']):
                        flapped = True

            self.bird.move(flapped=flapped)

            self.score.increase()

            # --- Screen-clearing code goes here
            # If you want a background image, replace this clear with blit'ing
            # background image.
            self.screen.fill(colors['white'])

            # --- Drawing code should go here
            self.bird.draw()
            self.score.draw()

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            if (not (self.bird.inBound())):
                exit()

            # --- Limit to 60 frames per second
            self.clock.tick(game['speed'])


def main():
    Game()


main()
