from pathlib import Path
from typing import List
from pytest import fixture

from . import solution as soln
#
#
# @fixture
# def sample_input() -> List[int]:
#     path = Path("~/GitRepos/aoc2022/day05/test_input.txt").expanduser().absolute()
#     try:
#         with open(path) as f:
#             return [l for l in f.readlines()]
#     except FileNotFoundError as e:
#         raise FileNotFoundError(e, "full_path: ", str(path))


def test_find_signal_start():
    tests = [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10)
    ]
    for t in tests:
        stream, expected = t
        found = soln.find_signal_start(stream)
        assert found == expected


def test_find_message_start():
    tests = [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29)
    ]
    for t in tests:
        stream, expected = t
        found = soln.find_message_start(stream)
        assert found == expected
