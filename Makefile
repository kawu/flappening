# The binary to build (basename).
MODULE := flappening

BLUE='\033[0;34m'
NC='\033[0m' # No Color

run:
	@python -m $(MODULE)

test:
	@pytest

lint:
	@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
	@flake8

clean:
	rm -rf .pytest_cache .coverage .pytest_cache