from typing import List
from pytest import fixture

from . import solution as soln


@fixture
def sample_input() -> List[str]:
    return soln.read_input(f"~/GitRepos/aoc2022/day{soln.DAY_STR}/test_input.txt")


def test_parse(sample_input):
    monkeys = soln.parse(sample_input)
    pass

def test_solve_pt1(sample_input):
    assert soln.solve_pt1(sample_input) == 13140


def test_solve_pt2(sample_input):
    assert soln.solve_pt2(sample_input) == 1
