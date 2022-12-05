# AOC 2022 Day 4
from pathlib import Path
from typing import List, FrozenSet, Tuple


def read_input(filepath: str) -> List[str]:
    """Read input file and return a list of something"""
    filepath = Path(filepath)  # type: Path
    if not filepath.exists:
        raise ValueError(
            f"The path {filepath.expanduser().absolute()} could not be found"
        )
    with open(filepath) as f:
        lines = f.readlines()
    return [l.strip() for l in lines]


def parse(lines: List[str]) -> List[Tuple[int, int]]:
    """From a line, split into groups separated by a blank line
    Each group has 2 elves
    For each elf, identify the start and stop of each line
    e.g.
    2-4,6-8
    2-3,4-5

    Return [([2, 3, 4], [6, 7, 8]), ([2, 3], [4, 5])]
    That represents 2 groups of 2 elves. The assignments for each elf are
    represented as a list of a range.
    """
    groups = []
    for line in [l for l in lines if l]:
        elf1, elf2 = line.split(",")
        elf1_assignment = get_assignments(elf1)
        elf2_assignment = get_assignments(elf2)
        groups.append((elf1_assignment, elf2_assignment))
    return groups


def get_assignments(assign: str) -> FrozenSet[int]:
    """Turn input like 2-4 into a list of [2, 3, 4]"""
    start, stop = assign.split("-")
    start = int(start)
    stop = int(stop)
    return set(range(start, stop + 1))


def solve_pt1(lines: List[str]) -> int:
    """How many groups have one elf sections fully-contained by another's
    e.g.,
    elf1 has section 2, 3
    elf2 has sections 1, 2, 3, 4, 5

    elf2 fully contains elf1
    """
    overlapping_group_count = 0
    groups = parse(lines=lines)
    for g in groups:
        g0 = set(g[0])
        g1 = set(g[1])
        if g1.issubset(g0) or g0.issubset(g1):
            overlapping_group_count += 1
    return overlapping_group_count


def solve_pt2(lines: List[str]) -> int:
    """How many groups have one elf sections overlapped by another's
    e.g.,
    elf1 has section 2, 3
    elf2 has sections 3, 4, 5

    elf2 overlaps elf1
    """
    overlapping_group_count = 0
    groups = parse(lines=lines)
    for g in groups:
        if g[0].intersection(g[1]):
            overlapping_group_count += 1
    return overlapping_group_count
