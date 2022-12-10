# AOC 2022 Day 9 https://adventofcode.com/2022/day/0
import math
from pathlib import Path
from typing import List, Tuple


DAY = 9
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


def parse(lines: List[str]) -> List[Tuple[int, int, int]]:
    """Given the input, parse into instructions
    R 4 = Right 4, so use add 4 to the head x-axis
    That means return (1, 0, 4) for x-axis multiplier, y-axis multiplier, 4 units
    """
    for line in lines:
        x = y = 0
        direction, count = line.split(" ")
        if direction == "R":
            x = Direction.Right
        elif direction == "L":
            x = Direction.Left
        elif direction == "U":
            y = Direction.Up
        else:
            y = Direction.Down
        yield (x, y, int(count))


def distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    """Distance between 2 points on a plane"""
    x1 = p1[0]
    x2 = p2[0]
    y1 = p1[1]
    y2 = p2[1]

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def move_tail_toward_head(head: Tuple[int, int], tail: Tuple[int, int]) -> Tuple[int, int]:
    """
    If p1 is left of p2, return (-1, 0)
       p1 is left and above p2, return (-1, 1)
       ...
    """
    x = y = 0
    if distance(head, tail) > math.sqrt(2):
        if head[0] < tail[0]:  #left
            x = Direction.Left
        if head[0] > tail[0]:  # right
            x = Direction.Right
        if head[1] < tail[1]:
            y = Direction.Down
        if head[1] > tail[1]:
            y = Direction.Up
    return (tail[0] + x, tail[1] + y)


def move_head(
    from_coord: Tuple[int, int], coord_update: Tuple[int, int]
) -> Tuple[int, int]:
    """Move a point in the direction(s) indicated by coord_update"""
    return (
        from_coord[0] + (1 * coord_update[0]),
        from_coord[1] + (1 * coord_update[1]),
    )


def solve_pt1(lines: List[str]) -> int:
    h = t = (0, 0)
    tail_spaces = set(list())
    for x, y, count in parse(lines):
        update = (x, y)
        # move in the direction, count spaces, one at a time
        for _ in range(count):
            tail_spaces.add(t)
            h = move_head(h, update)
            t = move_tail_toward_head(h, t)
    tail_spaces.add(t)
    return len(tail_spaces)


def solve_pt2(lines: List[str]) -> int:
    return ""
