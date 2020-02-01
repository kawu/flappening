import pygame

from player.human import Human

from config.game import game
from config.util import colors


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

        # initiate pygame
        pygame.init()

        # initiate & save screen
        self.screen = pygame.display.set_mode(game['size'])

        # add screen title
        pygame.display.set_caption(game['title'])

        # initiate & save game clock
        self.clock = pygame.time.Clock()

        # initiate & save player
        self.player = Human(self.screen, 0)

    #
    #
    # -------- Game Loop -----------
    #
    def run(self):

        gameOn: bool = True

        while gameOn:

            # --- Player turn
            if (self.player.turn() is False):
                gameOn = False

            # --- Screen-clearing
            self.screen.fill(colors['white'])

            # --- Draw player
            self.player.draw()

            # --- Update the screen
            pygame.display.flip()

            # --- Update clock with game speed
            self.clock.tick(game['speed'])


def main():
    Game()


main()
