import pygame

from player.human import Human
from player.machine import Machine

from config.game import game
from config.util import colors


class Game:

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, gameMode: int = 0):
        super().__init__()

        # 0 : human player
        # 1 : single simple machine player
        # 2 : evolving array of machine players
        self.gameMode = gameMode

        self.setup()

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

        # --- Initiate & Save player(s)
        # human
        if (self.gameMode == 0):
            self.player = Human(self.screen, 0)

        # machine single
        elif (self.gameMode == 1):
            self.player = Machine(self.screen, 0)

        # machine array
        elif (self.gameMode == 2):
            # TODO: evolving array of machine players
            pass

    #
    #
    # -------- Game Loop -----------
    #
    def run(self):

        gameOn: bool = True

        while gameOn:

            # --- Player turn(s)
            if (self.player.turn() is False):
                gameOn = False

            # --- Screen-clearing
            self.screen.fill(colors['white'])

            # --- Draw player(s)
            self.player.draw()

            # --- Update the screen
            pygame.display.flip()

            # --- Update clock with game speed
            self.clock.tick(game['speed'])
