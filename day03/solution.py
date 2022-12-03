# AOC 2022 Day 3
from pathlib import Path
from typing import List, Tuple


def read_input(filepath: str) -> List[Tuple[str, str]]:
    """Read input file and return a list of something"""
    filepath = Path(filepath)  # type: Path
    if not filepath.exists:
        raise ValueError(
            f"The path {filepath.expanduser().absolute()} could not be found"
        )
    with open(filepath) as f:
        lines = f.readlines()
    return [l.strip() for l in lines]


def make_groups_of_three(lines: List[str]) -> List[List[str]]:
    """Split the file in groups of 3 consecutive lines"""
    idx = 0
    while idx < len(lines):
        yield lines[idx:idx+3]
        idx += 3
        
        
def find_group_badge(group: List[str]) -> str:
    """Given a group of 3 lines find the character shared among those lines"""
    for c in list(group[0]):
        if c not in group[1]:
            continue
        if c not in group[2]:
            continue
        return c


def is_upper(c: str) -> bool:
    if ord(c) >= 65 and ord(c) < 97:
        return True
    return False


def is_lower(c: str) -> bool:
    if ord(c) >= 97 and ord(c) < 123:
        return True
    return False


def priority(c: str) -> int:
    """Convert a=1, z=26, A=27, Z=52"""
    # ord(A) == 65
    # ord(z) == 122
    if len(c) > 1 or not c:
        raise ValueError("input must be a single character")
    if ord(c) < 65 or ord(c) > 122:
        raise ValueError("input must be a-zA-Z")
    if is_lower(c):
        return ord(c) - 96  # ord(a) = 97 - 96 = 1
    if is_upper(c):
        return ord(c) - 65 + 27


def split_string(s: str) -> Tuple[str, str]:
    """Read the input line and split in 2"""
    idx = int(len(s) / 2)
    part1 = s[:idx]
    part2 = s[idx:]
    return part1, part2


def find_shared(compartment1: str, compartment2: str) -> str:
    """Find the letter shared between two compartments"""
    set1 = set(list(compartment1))
    set2 = set(list(compartment2))
    shared = set1.intersection(set2)
    if not len(shared) == 1:
        raise RuntimeError(f"find_shared is supposed to return a single character")
    return list(shared)[0]
        
        
def solve_pt1(lines: List[str]) -> int:
    """Read input, parse, calculate score"""
    shared = []
    for i in range(len(lines)):
        found = find_shared(*split_string(lines[i]))
        shared.append(found)
    return sum([priority(c) for c in shared])
        
        
def solve_pt2(lines: List[str]) -> int:
    """Read input, parse, calculate score"""
    groups = make_groups_of_three(lines)
    badges = [find_group_badge(g) for g in groups]
    return sum([priority(b) for b in badges])
