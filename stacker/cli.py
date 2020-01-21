"""Console script for stacker."""
import argparse
import sys


def main():
    """Console script for stacker."""
    parser = argparse.ArgumentParser()
    parser.add_argument('generate', nargs='*')
    parser.add_argument('os', nargs='*')
    parser.add_argument('py', nargs='*')
    parser.add_argument('stack', nargs='*')
    args = parser.parse_args()

    print("Arguments: " + str(args.generate))
    print("Arguments: " + str(args.os))
    print("Arguments: " + str(args.py))
    print("Arguments: " + str(args.py))
    print("Replace this message by putting your code into "
          "stacker.cli.main")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
