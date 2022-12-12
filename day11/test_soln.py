from typing import List
from pytest import fixture

from . import solution as soln


@fixture
def sample_input() -> List[str]:
    return soln.read_input(f"~/GitRepos/aoc2022/day{soln.DAY_STR}/test_input.txt")


def test_parse(sample_input):
    monkeys = soln.parse(sample_input)
    m = monkeys[0]
    assert m.test == 23
    assert m.operation == "old * 19"
    assert m.items == [79, 98]
    assert m.throw_true == 2
    assert m.throw_false == 3


def test_monkey(sample_input):
    monkeys = soln.parse(sample_input)
    m = monkeys[0]
    expected = (500, 3)
    found = m.get_monkey_and_worry()
    assert expected == found


def test_solve_pt1(sample_input):
    assert soln.solve_pt1(sample_input) == 13140


def test_solve_pt2(sample_input):
    assert soln.solve_pt2(sample_input) == 1
