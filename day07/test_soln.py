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

def test_directory_size():
    inputs = [
        ("a.txt", 1000),
        ("b.txt", 150),
        ("c.txt", 20)
    ]
    d = soln.Directory
    for i in inputs:
        