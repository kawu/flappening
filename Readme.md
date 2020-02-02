# Flappening

## Installation *(from source)*

Common (only install `typing` for Python <3.5)
```bash
# bash, powershell:
pip3 install pygame pytorch typing
# or:
pip3 install -r requirements.txt
```

## Getting Started
Run game through command line:
```bash
python3 main.py
```
or create an custom *main.py*-file:
```python
# import the game
from game import Game

def main():
    
    # create new Game Object
    # gameMode = 0 : human player
    # gameMode = 1 : single simple machine player
    myGame = Game(gameMode=1)

    # run the game
    myGame.run()

# run iff file is main
if __name__ == '__main__':
    main()
```

## Releases
* initial commit
* added bird object *(player character)*
* bird in bound detection
* added score object

## Roadmap
* collision detection *(http://www.jeffreythompson.org/collision-detection/rect-rect.php)*
* tubes object class
* sprites for bird, tubes, background
* neural net *(Linear MLP)*
* genetic optimization through evolution and mutation