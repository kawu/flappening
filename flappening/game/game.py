import pygame

from flappening.game import Statistics
from flappening.player import Human, Neural
from flappening.entities import Tubes


class Game:

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, config: dict):
        super().__init__()

        self.config = config

        # keep track of game iterations
        self.iteration: int = 0

        self.setup()

    #
    #
    # -------- Setup -----------
    #
    def setup(self):

        # initiate pygame
        pygame.init()

        # initiate & save screen
        self.screen = pygame.display.set_mode(self.config['game']['size'])

        # add screen title
        pygame.display.set_caption(self.config['meta']['title'])

        # initiate & save game clock
        self.clock = pygame.time.Clock()

        # initiate & save Statistics
        self.statistics = Statistics()

        # reset game
        self.reset()

    #
    #
    # -------- Reset -----------
    #
    def reset(self):

        # --- Initiate & Save player(s)
        self.players: list = [Human(self.config)]

        # players garbage
        self.playersGarbage: list = []

        #
        # --- Initiate & Save Tubes'/obstacles
        self.tubes: list = [Tubes(self.config)]

        # raise game iteration count
        self.iteration += 1

    #
    #
    # -------- Game Loop -----------
    #
    def run(self):

        gameOn: bool = True

        while gameOn:

            # --- Main event loop
            for event in pygame.event.get():

                # --- handle window close
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                # --- Handle User interaction
                if isinstance(self.players[0], Human):
                    self.handleUserInteraction(event)

            # --- Handle Network interaction
            if isinstance(self.players[0], Neural):
                self.handleNetworkInteraction()

            self.handleInGameInteraction()
            self.updateScreen()

            # --- End game if no active players exists
            if (len(self.players) == 0):
                gameOn = False

    #
    #
    # -------- handleUserInteraction -----------
    #
    def handleUserInteraction(self, event):

        # --- Player(s) turn(s)
        for player in self.players:
            player.turn(event)

    #
    #
    # -------- handleUserInteraction -----------
    #
    def handleNetworkInteraction(self):

        # --- Player(s) turn(s)
        for player in self.players:

            # player observers and takes action
            player.observe(self.tubes)
            player.turn(event=None)

    #
    #
    # -------- handleInGameInteraction -----------
    #
    def handleInGameInteraction(self):

        # --- Save vars for more readability
        maxScore: int = self.config['game']['max_score']
        gameWidth: int = self.config['game']['size'][1]
        tubeDistance: int = self.config['game']['tube_distance']

        # --- Apply game interaction on each player
        for player in self.players:

            # --- Apply gravity
            player.applyGravity()

            # --- Check if player is inbound and has not reached the max score
            if (not player.bird.inBound() or player.getScore() >= maxScore):
                self.withdrawPlayer(player)

        # --- Handle each Tubes'
        for tubes in self.tubes:

            # --- Tubes' moving
            tubes.move()

            # --- Remove not visible Tubes'
            if (not tubes.visible()):
                self.tubes.remove(tubes)

            # --- Check Tubes' Player collision
            for player in self.players:
                if (tubes.collision(player.bird)):
                    self.withdrawPlayer(player)

        # --- Get game width and last tube distance
        tubleWallDistance = gameWidth - self.tubes[-1].getXCenter()

        # --- Add new Tubes if necessary
        if (tubleWallDistance > tubeDistance):
            self.tubes.append(Tubes(self.config))

        # --- Update Statistics
        self.statistics.update(
            self.players,
            self.playersGarbage,
            self.iteration,
        )

    #
    #
    # -------- updateScreen -----------
    #
    def updateScreen(self):

        # --- Screen-clearing
        self.screen.fill(pygame.Color('WHITE'))

        # --- Draw tubes'
        for tubes in self.tubes:
            tubes.draw()

        # --- Draw player(s)
        for player in self.players:
            player.draw()

        # --- Draw Statistics
        self.statistics.draw()

        # --- Update the screen
        pygame.display.flip()

        # --- Update clock with game fps
        self.clock.tick(self.config['game']['fps'])

    # -------- withdrawPlayer -----------
    #
    def withdrawPlayer(self, player):
        try:
            self.players.remove(player)
            self.playersGarbage.append(player)

        except ValueError:
            pass  # Player is already dead and cannot be removed.

    # -------- generatePlayers -----------
    #
    def generatePlayers(self, n: int):
        self.players = [Neural(self.config) for i in range(n)]

    # -------- loadPlayers -----------
    #
    def loadPlayers(self, players):
        self.players = players

    # -------- getPlayer -----------
    #
    def getPlayers(self):
        return self.players

    # -------- getPlayersGarbage -----------
    #
    def getPlayersGarbage(self):
        return self.playersGarbage
