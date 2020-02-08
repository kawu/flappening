from lib.player import Machine
from lib.neural import Brain


class Neural(Machine):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, screen, score):
        super().__init__(
            screen,
            score,
        )

        self.brain = Brain(16)

    #
    #
    #  -------- Interact -----------
    #
    def interact(self, event) -> bool:

        if (self.brain.think(
            [self.getInBirdPosition(),
             self.getInTubesPosition()])):
            return True

        return False

    #  -------- draw -----------
    #
    def draw(self):
        super().draw()
