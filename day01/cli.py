import click

from solution import elves_from_strs, most_calories_carried, calores_sorted


@click.command()
@click.option("-i", "--infile", type=click.Path(exists=True), help="The file containing input for this day")
def main(infile):
    # read input
    with open(infile) as f:
        lines = f.readlines()
        
    # process input
    elves = elves_from_strs(lines)
    # find the elf carrying the most calories
    most_cals = most_calories_carried(elves=elves)
    print(f"The elf carrying the most is {most_cals}")
    top_3 = calores_sorted(elves=elves)[:3]
    assert len(top_3) == 3
    print(f"Part 2 answer: {sum(top_3)}")


if __name__ == "__main__":
    main()
