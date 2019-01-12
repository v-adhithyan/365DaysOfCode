import argparse
import os
import sys
from pathlib import Path, PurePath

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"


def success(msg):
    sys.stdout.write(RED)
    print(msg)


def alert(msg):
    sys.stdout.write(GREEN)
    print(msg)


def rename_files(path):
    os.chdir(path)
    files = (f for f in Path(".").iterdir() if not f.is_dir())
    for f in files:
        filename = str(f.name)
        if "tamilrockers" in filename.lower():
            new_filename = "".join(filename.split("-")[1:]).strip()
            target = Path(PurePath(new_filename))
            print(filename)
            f.rename(target)
            success(msg="Renamed {} ==> {}".format(filename, new_filename))


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("path", help="path to movie folder")
    args = arg_parser.parse_args()
    try:
        path = args.path
        path = os.path.expanduser(path)
        rename_files(path)
    except BaseException:
        alert(msg="path not found")
        raise


if __name__ == "__main__":
    main()
