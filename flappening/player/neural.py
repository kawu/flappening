import copy
import pygame

from flappening.player import Machine
from flappening.neural import Brain


class Neural(Machine):

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, config, brain=None):
        super().__init__(config)

        # use given brain
        if (brain):
            self.brain = brain

        # create new brain
        else:
            self.brain = Brain(3)

    #
    #
    #  -------- Interact -----------
    #
    def interact(self, event=None) -> bool:

        # only interact on syntetic machine event
        if (event.type != pygame.USEREVENT):
            return

        dataBird = self.getInBirdPosition()
        dataTubes = self.getInTubesPosition()

        # get id of the next tubes object
        # bird X > pipes.index(0) X use
        nTubesID: int = 0
        if (dataBird[0] > dataTubes[0][0]):
            nTubesID = 1

        x1 = dataBird[1]  # bird Y
        x2 = dataTubes[nTubesID][0]  # pipes.index(nTubesID) X
        x3 = dataTubes[nTubesID][1]  # pipes.index(nTubesID) Y

        if (self.brain.think([x1, x2, x3])):
            return True

        return False

    #  -------- copy -----------
    #
    def copy(self):
        return Neural(self.config, brain=copy.deepcopy(self.brain))
