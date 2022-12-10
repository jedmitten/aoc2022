# AOC 2022 Day 9 https://adventofcode.com/2022/day/0
import math
from pathlib import Path
from typing import Dict, List, Tuple


DAY = 10
DAY_STR = f"{DAY:02d}"


class Direction:
    Left = -1
    Right = 1
    Up = 1
    Down = -1


def read_input(filepath: str) -> List[str]:
    """Read input file and return a list of something"""
    filepath = Path(filepath).expanduser().absolute()  # type: Path
    if not filepath.exists:
        raise ValueError(
            f"The path {filepath.expanduser().absolute()} could not be found"
        )
    with open(filepath) as f:
        lines = f.readlines()
    return [_l.strip() for _l in lines if _l]


def solve_pt1(lines: List[str]) -> int:
    return ""


def solve_pt2(lines: List[str]) -> int:
    return ""
