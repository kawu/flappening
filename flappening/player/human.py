from flappening.player import Player

from config import events, keys


class Human(Player):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self):
        super().__init__()

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

    #  -------- isMachine -----------
    #
    def isMachine(self) -> bool:
        return False
