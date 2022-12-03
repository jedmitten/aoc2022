from pathlib import Path
from typing import List
from pytest import fixture

from . import solution as soln


@fixture
def sample_input() -> List[int]:
    path = Path("./day03/test_input.txt").absolute()
    try:
        with open(path) as f:
            return [l.strip() for l in f.readlines()]
    except FileNotFoundError as e:
        raise FileNotFoundError(e, "full_path: ", str(path))


def test_priority():
    assert soln.priority("a") == 1
    assert soln.priority("z") == 26
    assert soln.priority("A") == 27
    assert soln.priority("Z") == 52


def test_split_string():
    line = "vJrwpWtwJgWrhcsFMMfFFhFp"
    pt1, pt2 = soln.split_string(line)
    assert pt1 == "vJrwpWtwJgWr"
    assert pt2 == "hcsFMMfFFhFp"


def test_find_shared(sample_input):
    c1 = "jqHRNqRjqzjGDLGL"
    c2 = "rsFMfFZSrLrFZsSL"
    assert soln.find_shared(c1, c2) == "L"


def test_make_groups_of_three(sample_input):
    expected1 = [
        "vJrwpWtwJgWrhcsFMMfFFhFp",
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
    ]

    expected2 = [
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw",
    ]

    found_groups = list(soln.make_groups_of_three(sample_input))
    print(found_groups[0], "|", expected1)
    assert found_groups[0] == expected1
    print(found_groups[1], "|",  expected2)
    assert found_groups[1] == expected2


def test_find_group_badge(sample_input):
    groups = list(soln.make_groups_of_three(sample_input))
    assert soln.find_group_badge(groups[0]) == "r"
    assert soln.find_group_badge(groups[1]) == "Z"


def test_solve_pt1(sample_input):
    expected = ["p", "L", "P", "v", "t", "s"]

    found_shared = []
    for i in range(len(sample_input)):
        found = soln.find_shared(*soln.split_string(sample_input[i]))
        assert found == expected[i]
        found_shared.append(found)
    assert sum([soln.priority(c) for c in found_shared]) == 157
    assert soln.solve_pt1(sample_input) == 157


def test_solve_pt1(sample_input):
    assert soln.solve_pt2(sample_input) == 70
