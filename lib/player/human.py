from lib.player import Player

from config import events, keys


class Human(Player):
    def __init__(self, screen, score):
        super().__init__(
            screen,
            score,
        )

    def interact(self, event):

        # --- Check for keypress
        if event.type == events['KEYDOWN']:

            # UP KEY
            if (event.key == keys['up'] or event.key == keys['space']):
                return True

        return False

    def draw(self):
        super().draw()
