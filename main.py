import pygame

from entities import Player
import config


class Game:
    def __init__(self):
        super().__init__()

        self.screen = None
        self.clock = None

        self.player = None

        self.setup()
        self.run()

    # -------- Setup -----------
    def setup(self):

        # init pygame
        pygame.init()

        # set & save screen
        self.screen = pygame.display.set_mode(config.game['size'])

        # add screen title
        pygame.display.set_caption("Flappy Bird")

        # initiate & save game clock
        self.clock = pygame.time.Clock()

        # initiate player
        self.player = Player(self.screen)

    # -------- Game Loop -----------
    def run(self):

        while True:

            # --- Main event loop
            for event in pygame.event.get():

                # window close handler
                if event.type == pygame.QUIT:

                    # Close the window and quit.
                    pygame.quit()

                # game logic for keydown presses
                if event.type == config.event['KEYDOWN']:

                    # UP KEY
                    if (event.key == config.key['up']):
                        self.player.move((0, -1))

                    # DOWN KEY
                    elif (event.key == config.key['down']):
                        self.player.move((0, 1))

                    # LEFT KEY
                    elif (event.key == config.key['right']):
                        self.player.move((1, 0))

                    # RIGHT KEY
                    elif (event.key == config.key['left']):
                        self.player.move((-1, 0))

            # --- Screen-clearing code goes here
            # If you want a background image, replace this clear with blit'ing
            # background image.
            self.screen.fill(config.colors['white'])

            # --- Drawing code should go here
            self.player.draw()

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()

            # --- Limit to 60 frames per second
            self.clock.tick(config.game['speed'])


def main():
    Game()


main()
