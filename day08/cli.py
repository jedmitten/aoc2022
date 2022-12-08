from pathlib import Path
import click

from solution import read_input, solve_pt1, solve_pt2
from . import DAY_STR


@click.command()
@click.option(
    "-i",
    "--infile",
    default=Path(f"./day{DAY_STR}/input.txt"),
    type=click.Path(exists=True),
    help="The file containing input for this day",
)
def main(infile):
    # read input
    lines = read_input(infile)
    answer_pt1 = solve_pt1(lines=lines)
    print(f"Part 1 answer: {answer_pt1}")
    answer_pt2 = solve_pt2(lines=lines)
    print(f"Part 2 answer: {answer_pt2}")


if __name__ == "__main__":
    main()
