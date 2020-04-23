"""cli to call stack assembler"""

import fire

from stacker.assembler import generate_all_dockerfiles

#from assembler import generate_all_dockerfiles

# TODO implement opts --build, --lint, --dry-run, --tag
# TODO implement opts --var = variable to add to the global spec dictionary
# TODO implement --singularity = generate singularity recipe files
def stacker(generate, build=False):
    """Tool to generate dockerfiles and build dockerimages for stacks\n
       --generate to generte dockerfiles eg. python cli.py --generate
       --build to build dockerimages from generated files eg. python cli.py --generate --build
    """
    generate_all_dockerfiles(generate, build)


def main():
    fire.Fire(stacker)


if __name__ == "__main__":
    fire.Fire(stacker)
