# The binary to build (basename).
MODULE := flappening

BLUE='\033[0;34m'
NC='\033[0m' # No Color

run:
	@python -m $(MODULE) $(gameMode) $(playerCount) $(trainEpochs)

test:
	@echo "\n${BLUE}Running PyTest against source and test files...${NC}\n"
	@pytest

lint:
	@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
	@flake8

clean:
	rm -rf logs cache