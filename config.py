# game configuration
game = {
    # the screen [width, height]p
    'size': (700, 500),
    # fresh rate in fps,
    'speed': 30,
}
# player: configuration
player = {
    'size': (30, 30),
    'startPosition': (100, 200),
    'velocity': 0,
    'stepSize': 25
}

# default color set
colors = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255)
}

event = {
    'QUIT': 0,  # : {'none'}
    'ACTIVEEVENT': 1,  # : {'gain', 'state'}
    'KEYDOWN': 2,  # : {'key', 'mod', 'unicode', 'scancode'}
    'KEYUP': 3,  # : {'key', 'mod'}
}

key = {
    'up': 273,
    'down': 274,
    'right': 275,
    'left': 276,
}
