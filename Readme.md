# flappening

## Installation *(from source)*

Common (only install `typing` for Python <3.5)
```bash
# bash, powershell:
pip3 install pygame pytorch typing
# or:
pip3 install -r requirements.txt
```

## Getting Started

### Running

Run game through command line with following options:
```bash
# options: 
# gameMode -> 0 : playing human, 1 : neural evolution | (default: 1)
# playerCount -> INT | (default: 200, only for machine evolution)
# trainEpochs -> INT | (default: 50, only for machine evolution)

# using python interpreter directly:
python3 -m flappening [gameMode] [playerCount] [trainEpochs]

# or the Makefile:
make run [gameMode=VAL] [playerCount=VAL] [trainEpochs=VAL]

# getting help:
python3 -m flappening --help 
```

### Linting, Cleaning

```bash
# lint: flake8
make lint

# clean: cache/tmp files
make clean
```

## Releases
* 0.0.0: Initial Commit
* 0.0.1: added bird object *(player character)*
* 0.0.4: bird in bound detection
* 0.0.5: added score object
* 0.1.1: collision detection
* 0.1.4: tubes object class
* 0.1.5: human and dummy machine player
* 0.1.6: game recording
* 0.2.0: tests, argparse includes
* 0.3.0: optimization through evolution and mutation
* 0.3.5: integrate statistic output
* 0.4.0: Improve Evolution and Mutation

## Roadmap [None]

