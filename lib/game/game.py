import pygame

from lib.player import Human, Machine, Neural

from lib.entities import Tubes

from config import game


class Game:

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, gameMode: int = 0, playerCount: int = 1):
        super().__init__()

        # 0 : human player
        # 1 : single simple machine player
        # 2 : evolving array of machine players
        self.gameMode = gameMode

        self.playerCount = playerCount

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

        # reset game
        self.reset()

    #
    #
    # -------- Reset -----------
    #
    def reset(self):

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

            self.players: list = [
                Neural(self.screen, 0) for i in range(self.playerCount)
            ]

        # players garbage
        self.playersGarbage: list = []

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

            if (len(self.players) == 0):
                gameOn = False

            # --- Create & Post syntetic user event (for fair machine interaction)
            event = pygame.event.Event(pygame.USEREVENT)
            pygame.event.post(event)

            # --- Main event loop
            for event in pygame.event.get():
                self.handleUserInteraction(event)

            self.handleInGameInteraction()
            self.updateScreen()

    #
    #
    # -------- handleUserInteraction -----------
    #
    def handleUserInteraction(self, event):

        # --- Handle window close
        if event.type == pygame.QUIT:
            pygame.quit()

        # --- Player(s) turn(s)
        for player in self.players:

            # machine observes game
            if (player.isMachine()):
                player.observe(self.tubes)

            # player takes action
            player.turn(event)

    #
    #
    # -------- handleInGameInteraction -----------
    #
    def handleInGameInteraction(self):

        # --- Tubes' moving
        for tubes in self.tubes:
            tubes.move()

            # check tubes collide with Player(s)
            for player in self.players:
                if (tubes.collision(player.bird) or not player.bird.inBound()):

                    if (hasattr(player, 'logger')):
                        player.logger.write()

                    self.players.remove(player)
                    self.playersGarbage.append(player)

            # remove not visible tubes
            if (not tubes.visible()):
                self.tubes.remove(tubes)

        # --- Add new tubes if necessary
        tubleWallDistance = game['size'][1] - self.tubes[-1].getXCenter()

        if (tubleWallDistance > game['tubeGap']):
            self.tubes.append(Tubes(self.screen))

    #
    #
    # -------- updateScreen -----------
    #
    def updateScreen(self):
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

    # -------- getPlayer -----------
    #
    def getPlayers(self):
        return self.players

    # -------- getPlayersGarbage -----------
    #
    def getPlayersGarbage(self):
        return self.playersGarbage
