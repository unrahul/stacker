"""parse the spec file and convert to python dicts."""
import sys

from ruamel.yaml import YAML


def init(specfile: str = "configs/dlrs.yaml") -> None:
    """initializer, read in specification file and assign to variable spec.
    >>> init()
    >>> print(spec["version"])
    0.6.0
    """
    global spec
    yaml = YAML()
    with open(specfile) as fh:
        spec = yaml.load(fh.read())


if __name__ == "__main__":
    """trivial examples"""
    init()
    print(spec["version"])
    print(spec["license"])
    print(spec["stack"]["dlrs"]["ubuntu"]["apt"])
