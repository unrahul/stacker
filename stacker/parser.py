"""parse the spec file and convert to python dicts."""
import sys

from ruamel.yaml import YAML

yaml = YAML()
specfile = "specs/dlrs.yaml"
spec = ""
with open(specfile) as fh:
    spec = yaml.load(fh.read())

print(spec["version"])
print(spec["stack"]["dlrs"]["ubuntu"]["apt"])
