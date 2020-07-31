# flappening

## Installation _(from source)_

Common (only install `typing` for Python <3.5)

```bash
# bash, powershell:
pip3 install pygame pytorch pytest numpy pandas matplotlib typing
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
# mutationRate -> FLOAT | (default: 0.02, only for machine evolution)
# toSurvive -> INT | (default: 20, only for machine evolution)

# using python interpreter directly:
python3 -m flappening [gameMode] [playerCount] [trainEpochs] [mutationRate] [toSurvive]

# or the Makefile:
make run [gameMode=VAL] [playerCount=VAL] [trainEpochs=VAL] [mutationRate=VAL] [toSurvive=VAL]

# play as a human:
make play

# evolve using the genetic algorithm
make evolve

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

- 0.0.0: Initial Commit
- 0.0.1: added bird object _(player character)_
- 0.0.4: bird in bound detection
- 0.0.5: added score object
- 0.1.1: collision detection
- 0.1.4: tubes object class
- 0.1.5: human and dummy machine player
- 0.1.6: game recording
- 0.2.0: tests, argparse includes
- 0.3.0: optimization through evolution and mutation
- 0.3.5: integrate statistic output
- 0.4.0: Improve Evolution and Mutation

## Roadmap [None]
