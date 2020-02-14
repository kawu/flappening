from flappening.entities import Bird


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

        # --- Handle player interaction
        flapped = self.interact(event)

        self.bird.move(flapped=flapped)
        self.score += 1

    #  -------- interact -----------
    #  --- ABSTRACT METHOD
    def interact(self, event=None):
        return False

    #  -------- draw -----------
    def draw(self):
        self.bird.draw()

    #  -------- getScore -----------
    def getScore(self):
        return self.score
