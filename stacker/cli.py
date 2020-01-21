#!/usr/bin/env python3
"""Console script for stacker."""
import argparse
import sys

from absl import flags


FLAGS = flags.FLAGS

# sort of like opt parse
flags.DEFINE_string(
    "dockerfile_dir",
    "./dockerfiles",
    "save dockerfiles to this directory",
    short_name="o",
)

flags.DEFINE_string(
    "slices_path",
    "./slices/",
    "path to a directory containing slices of dockerfiles",
    short_name="p",
)
flags.DEFINE_string(
    "spec_file", "./specs/dlrs.yml", "Path to the YAML specification file", short_name="s"
)
