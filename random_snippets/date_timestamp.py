from datetime import datetime, timedelta
from argparse import ArgumentParser


def day_to_timestamp(days=0):
    dt = datetime.now() + timedelta(days=days)
    return str(dt.timestamp()).split(".")[0]


def main():
    parser = ArgumentParser(
        "Return a day relative to current time as timestamp.")
    parser.add_argument(
        "-d", type=int, help="Days relative to today for which timestamp is required.", required=True)
    args = parser.parse_args()
    if args.d:
        print(day_to_timestamp(days=args.d))


if __name__ == "__main__":
    main()
