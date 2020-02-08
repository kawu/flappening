# Flappening 0.1.4

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
or create a custom `main.py`:
```python
# import the game
from lib import Game

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
* 0.0.0: initial commit
* 0.0.1: added bird object *(player character)*
* 0.0.4: bird in bound detection
* 0.0.5: added score object
* 0.1.1: collision detection *(http://www.jeffreythompson.org/collision-detection/rect-rect.php)*
* 0.1.4: tubes object class
* 0.1.5: human and dummy machine player
* 0.1.6: game recording

## Roadmap
* neural net *(Single Linear / Linear MLP / RNN(LSTM))*
* statistic output
* genetic optimization through evolution and mutation
* sprites for bird, tubes, background
* sounds for bird, tubes, background
