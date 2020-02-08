from player.player import Player

from config import game  # , events


class Machine(Player):
    def __init__(self, screen, score):
        super().__init__(
            screen,
            score,
        )

    # DUMMY:
    def interact(self, event):

        if (True):  # event.type == events['USEREVENT']

            y = self.bird.position[1] / game['size'][1]

            if (y > .4):
                return True

        return False

    def draw(self):
        super().draw()
