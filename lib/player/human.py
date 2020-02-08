from lib.player import Player

from config import events, keys


class Human(Player):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, screen, score):
        super().__init__(
            screen,
            score,
        )

    #
    #
    #  -------- Interact -----------
    #
    def interact(self, event):

        # --- Check for keypress
        if event.type == events['KEYDOWN']:

            # UP KEY
            if (event.key == keys['up'] or event.key == keys['space']):
                return True

        return False

    #  -------- draw -----------
    #
    def draw(self):
        super().draw()
