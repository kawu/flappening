import pygame

#
#
# bird configuration:
#
bird = {
    #
    # size, position, color:
    'size': [30, 30],  # px
    'startPosition': [120, 160],  # px
    'color': pygame.Color('RED'),
    #
    # physics:
    'startVelocity': 2.50,
    'maxVelocity': 20.0,
    'lift': 25.0,
    'attraction': 1.15,
}
