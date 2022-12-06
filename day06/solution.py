# AOC 2022 Day 5
from pathlib import Path
from typing import List


def read_input(filepath: str) -> List[str]:
    """Read input file and return a list of something"""
    filepath = Path(filepath)  # type: Path
    if not filepath.exists:
        raise ValueError(
            f"The path {filepath.expanduser().absolute()} could not be found"
        )
    with open(filepath) as f:
        lines = f.readlines()
    return [_l for _l in lines]


def find_start(stream: str, start_size: int = 4) -> int:
    for i in range(start_size, len(stream)):
        block = stream[i - start_size:i]
        if len(set(list(block))) == start_size:
            return i


def find_signal_start(stream: str) -> int:
    """Find the index of the first character in the start sequence

    The signal start sequence is the end of the first non-repeating 4-tuple in signal
    """
    return find_start(stream, 4)


def find_message_start(stream: str) -> int:
    """
    Find the index of the first of a string with 14 distinct characters
    """
    return find_start(stream, 14)


def solve_pt1(lines: List[str]) -> int:
    return find_signal_start(lines[0])


def solve_pt2(lines: List[str]) -> int:
    return find_message_start(lines[0])
