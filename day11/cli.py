from pathlib import Path
import logging
import click


logging.basicConfig()
LOG = logging.getLogger(__name__)

from solution import read_input, solve_pt1, solve_pt2, DAY_STR


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
    LOG.info(f"reading {infile}")
    lines = read_input(infile)
    answer_pt1 = solve_pt1(lines=lines)
    print(f"Part 1 answer: {answer_pt1}")
    answer_pt2 = solve_pt2(lines=lines)
    print(f"Part 2 answer: {answer_pt2}")


if __name__ == "__main__":
    main()
