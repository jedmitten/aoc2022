from pathlib import Path
from typing import List
from pytest import fixture

from . import solution as soln


P1 = (0, 0)
P2 = (1, 0)
P3 = (1, 1)


@fixture
def sample_input() -> List[int]:
    return soln.read_input(f"~/GitRepos/aoc2022/day{soln.DAY_STR}/test_input.txt")


def test_parse(sample_input):
    moves = list(soln.parse(sample_input))
    for x, y, count in moves:
        assert isinstance(x, int)
        assert isinstance(y, int)
        assert isinstance(count, int)
    assert moves[0] == (1, 0, 4)


def test_solve_pt1(sample_input):
    assert soln.solve_pt1(sample_input) == 13


def test_solve_pt2(sample_input):
    assert soln.solve_pt2(sample_input) == 1


def test_solve_pt2_2(sample_input2):
    assert soln.solve_pt2(sample_input2) == 36
