import pygame

from flappening.player import Player


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
        if event.type == pygame.KEYDOWN:

            # UP KEY
            if (event.key == pygame.K_UP or event.key == pygame.K_SPACE):
                return True

        return False

    #  -------- isMachine -----------
    #
    def isMachine(self) -> bool:
        return False
