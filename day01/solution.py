from attrs import define
from itertools import chain
from pathlib import Path
from typing import Any, List, Optional


@define
class Food:
    calories: int


@define
class Elf:
    food: Optional[List[Food]]

    @property
    def total_calories(self):
        return sum([f.calories for f in self.food])


def read_input(filepath: str) -> List[Any]:
    """Read input file and return a list of something"""
    filepath = Path(filepath)  # type: Path
    if filepath.exists:
        raise ValueError(f"The path {filepath.expanduser} could not be found")
    with open(filepath) as f:
        lines = f.readlines()
    return lines


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


def calores_sorted(elves: List[Elf]) -> List[int]:
    """Provide a sorted list of total calories carried by all elves"""
    return  sorted([e.total_calories for e in elves], reverse=True)


def most_calories_carried(elves: List[Elf]) -> int:
    """Get the index of the elf carrying the most calories"""
    highest = max([e.total_calories for e in elves])
    return highest
