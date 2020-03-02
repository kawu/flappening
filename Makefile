# The binary to build (basename).
MODULE := flappening

BLUE='\033[0;34m'
NC='\033[0m' # No Color

# default run config
gameMode=1
playerCount=200
trainEpochs=10
mutationRate=0.02
toSurvive=20

run:
	@python -m $(MODULE) $(gameMode) $(playerCount) $(trainEpochs) $(mutationRate) $(toSurvive) >> ./results/test/Log.tmp.txt

test:
	@echo "\n${BLUE}Running PyTest against source and test files...${NC}\n"
	@python3 -m pytest -s

lint:
	@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
	@flake8

clean:
	rm -rf logs cache .pytest_cache results/test