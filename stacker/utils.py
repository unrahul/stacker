"""utils for the project"""
import pathlib
import sys


def eprint(*args, **kwargs) -> None:
    """print all error to standard error"""
    print(*args, file=sys.stderr, **kwargs)


def mkdir_p(path: str) -> str:
    """mkdir even if the directory is present recurisvely"""
    try:
        path = pathlib.Path(path)
        path.mkdir(parents=True, exist_ok=True)
        return str(path)
    except Exception as e:
        eprint(
            "shouldn't do this, but yeah the house is on fire, {} to do its job!".format(
                mkdir_p.__name__
            )
        )
        eprint(e)


def write_to_file(path: str, content: str):
    """write to file, da!"""
    try:
        pathlib.Path(path).write_text(content)
    except Exception as e:
        eprint(
            "shouldn't do this, but yeah the house is on fire, {} to do its job!".format(
                write_to_file.__name__
            )
        )
        eprint(e)
