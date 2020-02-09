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
    'startVelocity': 1.25,
    'maxVelocity': 15.0,
    'lift': 25.0,
    'attraction': 1.15,
}
