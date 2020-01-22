"""parse the spec file and convert to python dicts."""
import sys

from ruamel.yaml import YAML


def init(specfile="specs/dlrs.yaml"):
    global spec
    yaml = YAML()
    with open(specfile) as fh:
        spec = yaml.load(fh.read())


if __name__ == "__main__":
    init()
    print(spec["version"])
    print(spec["license"])
    print(spec["stack"]["dlrs"]["ubuntu"]["apt"])
