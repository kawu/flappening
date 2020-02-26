from flappening.entities import Text

from flappening.utils import avgScore


class Statistics:

    #
    #
    #  -------- Init -----------
    #
    def __init__(self):
        super().__init__()

        self.bestScore = Text('', position=[550, 25])
        self.avgScore = Text('', position=[550, 50])
        self.playersAlive = Text('', position=[550, 75])
        self.generation = Text('', position=[550, 100])

    #
    #
    #  -------- update -----------
    #
    def update(self, players, playersGarbage, gameIteration) -> None:

        if (len(players) >= 1):

            self.playersAlive.setContent('bird alive: ' + str(len(players)))

            self.bestScore.setContent('best score: ' +
                                      str(players[-1].getScore()))

            self.avgScore.setContent(
                'avg score: ' + str(avgScore([*players, *playersGarbage])))

            self.generation.setContent('generation: ' + str(gameIteration))

    #  -------- draw -----------
    #
    def draw(self) -> None:
        self.playersAlive.draw()
        self.bestScore.draw()
        self.avgScore.draw()
        self.generation.draw()
