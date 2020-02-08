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

        self.brain = Brain(3)

    #
    #
    #  -------- Interact -----------
    #
    def interact(self, event=None) -> bool:

        if (self.brain.think(
            [self.getInBirdPosition(),
             self.getInTubesPosition()])):
            return True

        return False
