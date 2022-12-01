from typing import List

from ..common import read_input, Elf, Food


def elves_from_strs(strs: List[str]) -> List[Elf]:
    elves = []
    # Iterate list of calories looking for empty string as indicator of new elf food
    elf = Elf(food=[])
    for v in strs:
        if not v or v == "\n":
            elves.append(elf)
            elf = Elf(food=[])
            continue
        try:
            elf.food.append(Food(calories=int(v)))
        except ValueError:
            raise ValueError(f'Could not convert "{v}" to an int')
    # account for final elf created from invals
    elves.append(elf)
    return elves


def most_calories_carried(elves: List[Elf]) -> int:
    """Get the index of the elf carrying the most calories"""
    highest = max([e.total_calories for e in elves])
    return highest
