import os

from setuptools import find_packages, setup

from config import game

DIR = os.path.dirname(__file__)
REQUIREMENTS = os.path.join(DIR, "requirements.txt")

with open(REQUIREMENTS) as f:
    reqs = f.read()

setup(
    name=game['title'],
    version=game['version'],
    author="smnmnkr",
    url=game['url'],
    description=game['description'],
    packages=find_packages(exclude=("config", "tests")),
    install_requires=reqs.strip().split("\n"),
    entry_points={"console_scripts": ["flappening = main:main"]},
)
