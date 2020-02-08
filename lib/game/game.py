import pygame

from lib.player import Human, Machine, Neural

from lib.entities import Tubes

from config import game


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

        #
        # --- Initiate & Save player(s)

        # human
        if (self.gameMode == 0):
            self.players: list = [Human(self.screen, 0)]

        # machine single
        elif (self.gameMode == 1):
            self.players: list = [Machine(self.screen, 0)]

        # machine array
        elif (self.gameMode == 2):
            # TODO: evolving array of machine players
            self.players: list = [Neural(self.screen, 0)]

        #
        # --- Initiate & Save Tubes'/obstacles
        self.tubes: list = [Tubes(self.screen)]

    #
    #
    # -------- Game Loop -----------
    #
    def run(self):

        gameOn: bool = True

        while gameOn:

            # --- Player(s) turn(s)
            for player in self.players:

                # machine observes game
                if (player.isMachine()):
                    player.observe(self.tubes)

                # player takes action
                player.turn()

            # --- Tubes' moving
            for tubes in self.tubes:
                tubes.move()

                # check tubes collide with Player(s)
                for player in self.players:
                    if (tubes.collision(player.bird)
                            or not player.bird.inBound()):
                        gameOn = False
                        continue

                # remove not visible tubes
                if (not tubes.visible()):
                    self.tubes.remove(tubes)

            # --- Add new tubes if necessary
            tubleWallDistance = game['size'][1] - self.tubes[-1].getXCenter()

            if (tubleWallDistance > game['tubeGap']):
                self.tubes.append(Tubes(self.screen))

            # --- Screen-clearing
            self.screen.fill(game['color'])

            # --- Draw tubes'
            for tubes in self.tubes:
                tubes.draw()

            # --- Draw player(s)
            for player in self.players:
                player.draw()

            # --- Update the screen
            pygame.display.flip()

            # --- Update clock with game fps
            self.clock.tick(game['fps'])
