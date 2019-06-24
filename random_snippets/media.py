import argparse
import os
import sys
from pathlib import Path, PurePath
import shutil

GREEN = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
RED = "\033[0;32m"
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
    files = (f for f in Path(".").iterdir())
    for f in files:
        filename = str(f.name)
        if "tamilrock" in filename.lower():
            new_filename = "".join(filename.split("-")[1:]).strip()
            target = Path(PurePath(new_filename))
            print(filename)
            f.rename(target)
            success(f"Renamed {filename} ==> {new_filename}")


def get_or_create_directories(path, languages):
    os.chdir(path)
    for lang_dir in languages:
        path = Path(lang_dir)
        if not path.exists():
            path.mkdir()


def organize(path):
    languages = ["tamil", "telugu", "malayalam",
                 "kannada", "others", "hindi", "english"]
    series = {
        'season': 'series'
    }
    get_or_create_directories(path, languages)
    os.chdir(path)

    files = (f for f in Path(".").iterdir())
    for f in files:
        if not f.is_dir():
            for lang in languages:
                fname = str(f.name)
                if lang in fname.lower():
                    print(f"{fname} moved to => {lang}")
                    shutil.move(fname, lang)
                    break


def main():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("path", help="path to movie folder")
    args = arg_parser.parse_args()
    try:
        path = args.path
        path = os.path.expanduser(path)
        rename_files(path)
        organize(path)
    except BaseException:
        alert(msg="path not found")
        raise


if __name__ == "__main__":
    main()
