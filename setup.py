import os
import json

from setuptools import find_packages, setup

DIR = os.path.dirname(__file__)
REQUIREMENTS = os.path.join(DIR, "requirements.txt")

with open(REQUIREMENTS) as f:
    reqs = f.read()

# load JSON config
with open("config.json") as json_file:
    config = json.load(json_file)

setup(
    name=config['meta']['title'],
    version=config['meta']['version'],
    author=config['meta']["author"],
    url=config['meta']['url'],
    description=config['meta']['description'],
    packages=find_packages(exclude=("config", "tests")),
    install_requires=reqs.strip().split("\n"),
    entry_points={"console_scripts": ["flappening = main:main"]},
)
