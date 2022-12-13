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
    found = m.get_monkey_and_worry(worry_divider=3)
    assert expected == found


def test_process_round(sample_input):
    monkeys = soln.parse(sample_input)
    monkeys = soln.process_round(monkeys=monkeys, worry_divider=3)
    m = monkeys[0]
    assert m.items == [20, 23, 27, 26]
    m = monkeys[1]
    assert m.items == [2080, 25, 167, 207, 401, 1046]
    m = monkeys[2]
    assert m.items == []
    m = monkeys[3]
    assert m.items == []

    # reset
    monkeys = soln.parse(sample_input)
    monkeys = soln.process_round(monkeys=monkeys, worry_divider=1)
    m = monkeys[0]
    assert m.count_inspected_items == 2
    m = monkeys[1]
    assert m.count_inspected_items == 4
    m = monkeys[2]
    assert m.count_inspected_items == 3
    m = monkeys[3]
    assert m.count_inspected_items == 6

    # go to 20 so 19 more rounds
    for i in range(20):
        monkeys = soln.process_round(monkeys=monkeys, worry_divider=1)
    m = monkeys[0]
    assert m.count_inspected_items == 99
    m = monkeys[1]
    assert m.count_inspected_items == 97
    m = monkeys[2]
    assert m.count_inspected_items == 8
    m = monkeys[3]
    assert m.count_inspected_items == 103

    # reset
    monkeys = soln.parse(sample_input)
    for i in range(1000):
        monkeys = soln.process_round(monkeys=monkeys, worry_divider=1)
    m = monkeys[0]
    assert m.count_inspected_items == 99
    m = monkeys[1]
    assert m.count_inspected_items == 97
    m = monkeys[2]
    assert m.count_inspected_items == 8
    m = monkeys[3]
    assert m.count_inspected_items == 103


def test_solve_pt1(sample_input):
    assert soln.solve_pt1(sample_input) == 10605


def test_solve_pt2(sample_input):
    assert soln.solve_pt2(sample_input) == 2713310158
