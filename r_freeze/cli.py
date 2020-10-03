"""Console script for r_freeze."""
import argparse
import sys
from r_freeze.r_freeze import get_packages, write_package_file


def main():
    """Console script for r_freeze."""
    parser = argparse.ArgumentParser()
    parser.add_argument("dir", type=str, help="Directory to look for")
    parser.add_argument(
        "-o", type=str, help="Name of outfile if you want to craete one"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        default=False,
        help="Over write output file if it already exists",
    )

    args = parser.parse_args()
    if not isinstance(args.dir, str):
        raise TypeError('Directory should be string or "."')
    if args.o and args.dir:
        if not isinstance(args.o, str):
            raise TypeError('Outfile should be string or "."')

    if args.dir and args.o:
        packages = get_packages(args.dir)
        write_package_file(packages, args.o, args.overwrite)

    elif args.dir:
        print(get_packages(args.dir))


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
