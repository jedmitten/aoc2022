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


@fixture
def sample_input2() -> List[int]:
    return soln.read_input(f"~/GitRepos/aoc2022/day{soln.DAY_STR}/test_input_2.txt")


def test_distance():
    assert soln.distance(P1, P2) == 1
    assert soln.distance(P2, P3) == 1
    assert soln.distance(P1, P3) > 1


def test_move_head():
    assert soln.move_head(P1, (1, 0)) == (1, 0)
    assert soln.move_head(P2, (1, 1)) == (2, 1)


def test_move_tail_toward_head():
    head = (3, 3)
    tail = (2, 3)
    assert soln.move_tail_toward_head(head, tail) == tail
    head = (3, 4)
    assert soln.move_tail_toward_head(head, tail) == tail
    head = (3, 5)
    assert soln.move_tail_toward_head(head, tail) == (3, 4)


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
