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

def test_file():
    name = "a.txt"
    size = 10
    f = soln.File(name=name, size=size)
    assert f.name == name
    assert f.size == size
    

def test_directory():
    files = [
        soln.File("a.txt", 10),
        soln.File("b.txt", 100)
    ]
    d = soln.Directory()
    for f in files:
        d.add_child(child=f)
    assert d.size == 110
    