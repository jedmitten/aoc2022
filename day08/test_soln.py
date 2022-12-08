from pathlib import Path
from typing import List
from pytest import fixture

from . import solution as soln
from . import DAY_STR


@fixture
def sample_input() -> List[int]:
    return soln.read_input(f"~/GitRepos/aoc2022/{DAY_STR}/test_input.txt")


def test_map():
    """
    expecting
     0  1  2  3  4
  0   0  1  2  3  4
  1   5  6  7  8  9
  2  10 11 12 13 14
  3  15 16 17 18 19
  4  20 21 22 23 24
    """
    map = soln.Map(5, 5)
    assert map.max_x == 4
    assert map.max_y == 4
    
    assert map.get_tree(2, 2) == 12
    assert map.get_tree(0, 0) == 0
    assert map.get_tree(4, 4) == 24
    
    map.add_tree(1, 2, 1000)
    map.add_tree(2, 3, 0)
    
    assert map.get_tree(1, 2) == 1000
    assert map.get_tree(2, 3) == 0
