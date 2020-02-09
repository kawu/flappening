from lib.entities import Bird


class Player():

    #
    #
    #  -------- Init -----------
    #
    def __init__(self):

        self.bird = Bird()
        self.score: int = 0

    #
    #
    #  -------- Turn -----------
    #
    def turn(self, event):

        flapped = False

        # --- Check if game is lost:
        if (not (self.bird.inBound())):
            return False

        # --- Handle player interaction
        flapped = self.interact(event)

        self.bird.move(flapped=flapped)
        self.score += 1

        return True

    #  -------- interact -----------
    #  --- ABSTRACT METHOD
    def interact(self, event=None):
        pass

    #  -------- draw -----------
    def draw(self):
        self.bird.draw()

    #  -------- getScore -----------
    def getScore(self):
        return self.score
