from attrs import define
from pathlib import Path
from typing import Any, List, Optional


@define
class Food:
    calories: int
    
    
@define
class Elf:
    food: Optional[List[Food]]
    
    def total_calories(self):
        return sum(self.food.calories)


def read_input(filepath: str) -> List[Any]:
    """Read input file and return a list of something"""
    filepath = Path(filepath)  # type: Path
    if filepath.exists:
        raise ValueError(f"The path {filepath.expanduser} could not be found")
    with open(filepath) as f:
        lines = f.readlines()
    return lines
