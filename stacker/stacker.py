"""Docker assembler and formatting tool for stacks

- parse spec file - DONE
- parse slices of dockerfiles per app - DONE
- update dockerfile based on the yaml file values

- assemble dockerfiles from slices
- lint dockerfiles

- build images
- resize images
- convert dockerfiles to singularity recepies
"""
import collections
import copy
import errno
import itertools
import json
import multiprocessing
import os
import platform
import re
import shutil
import sys

from absl import app
import yaml

from cli import FLAGS

def read_template_slices(slices_path="."):
    """read all partial dockerfiles.
    Args:
        slices_path (string): read partials from this path

    Returns:
        Dict[string, string] of partials
        eg: Dict["clear/python: <dockerfile text]

    """
    slice = {}
    # change with Pathlib
    for path, _, files in os.walk(slices_path):
        print(path, files)
        for name in files:
            fullpath = os.path.join(path, name)
            try:
                slice_name = name
                print(slice_name)
            except Exception as e:
                print(e)
            with open(fullpath, "r") as f:
                contents = f.read()
                slice[name] = contents
    return slice


def main(argv):
    with open(FLAGS.spec_file, "r") as spec_file:
        # parse spec file
        tag_spec = yaml.safe_load(spec_file)
        print(tag_spec)

        # parse and save and save dockerfile slices as a dict
        dockerfile_slices = read_template_slices(FLAGS.slices_path)
        print(dockerfile_slices)

        # update dockerfile vars with values from spec file
        # concat slices according to stacker cli


if __name__ == "__main__":
    app.run(main)
