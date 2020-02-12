from flappening.entities import Text


class Statistics:

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, gameMode: int = 0):
        super().__init__()

        self.gameMode = gameMode

        self.bestScore = Text('', position=[550, 25])
        self.avgScore = Text('', position=[550, 50])
        self.playersAlive = Text('', position=[550, 75])
        self.generation = Text('', position=[550, 100])

    #
    #
    #  -------- update -----------
    #
    def update(self, players, playersGarbage, gameIteration) -> None:

        # human player score:
        if (len(players) >= 1 and self.gameMode == 0):
            self.bestScore.setContent('score: ' + str(players[-1].getScore()))

        # machine statistics:
        elif (len(players) >= 1 and self.gameMode == 1):

            self.playersAlive.setContent('bird alive: ' + str(len(players)))

            self.bestScore.setContent('best score: ' +
                                      str(players[-1].getScore()))

            self.avgScore.setContent('avg score: ' + 'TODO')

            self.generation.setContent('generation: ' + str(gameIteration))

    #  -------- draw -----------
    #
    def draw(self) -> None:
        self.playersAlive.draw()
        self.bestScore.draw()
        self.avgScore.draw()
        self.generation.draw()
