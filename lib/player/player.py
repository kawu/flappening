from lib.entities import Bird, Score


class Player():

    #
    #
    #  -------- Init -----------
    #
    def __init__(self, screen, score):

        self.bird = Bird(screen)
        self.score = Score(screen, score)

        # FIMXE: bird starting position
        self.bird.position = [120, 160]

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
        self.score.increase()

        return True

    #  -------- interact -----------
    #  --- ABSTRACT METHOD
    def interact(self, event=None):
        pass

    #  -------- draw -----------
    def draw(self):
        self.bird.draw()
        self.score.draw()
