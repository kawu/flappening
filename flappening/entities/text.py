import pygame


class Text():

    #
    #
    #  -------- Init -----------
    #
    def __init__(
            self,
            content: str = '',
            size: int = 24,
            position: list = [600, 25],
            color=pygame.Color('BlACK'),
    ):

        # get corresponding screen object
        self.screen = pygame.display.get_surface()

        self.content: str = content
        self.size: int = size
        self.position: list = position
        self.color: list = color

        # font.font(typeface[string], size[px])
        # https://www.pygame.org/docs/ref/font.html#pygame.font.Font
        self.font = pygame.font.Font(None, self.size)

    #  -------- draw -----------
    #
    def draw(self) -> None:

        # font.render(text[font.obj], antialias[bool], color[tuple])
        # src: https://www.pygame.org/docs/ref/font.html#pygame.font.Font.render
        text = self.font.render(self.content, True, self.color)

        # surface.blit(content[pygame.obj], position[tuple])
        # src: https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
        self.screen.blit(text, self.position)
