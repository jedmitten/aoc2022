from pathlib import Path
import click

from solution import read_input, parse_pt1, solve_pt1


@click.command()
@click.option("-i", "--infile", default=Path("./day02/input.txt"), type=click.Path(exists=True), help="The file containing input for this day")
def main(infile):
    # read input
    lines = read_input(infile)
    answer_pt1 = solve_pt1(lines=lines)
    print(f"Part 1 answer: {answer_pt1}")


if __name__ == "__main__":
    main()
