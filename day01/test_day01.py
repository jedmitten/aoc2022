from pathlib import Path
from typing import List
from pytest import fixture
# from click.testing import CliRunner

from .solution import elves_from_strs, most_calories_carried


@fixture
def sample_input() -> List[int]:
    path = Path("./aoc2022/day01/test_input.py").absolute()
    try:
        with open(path) as f:
            return f.readlines()
    except FileNotFoundError as e:
        raise FileNotFoundError(e, "full_path: ", str(path))


def test_solution(sample_input):
    elves = elves_from_strs(sample_input)
    
    expected = [
        [1000, 2000, 3000],
        [4000],
        [5000, 6000],
        [7000, 8000, 9000],
        [10000],
    ]
    
    assert len(elves) == len(expected)
    
    for i in range(len(elves)):
        elf_food = [f.calories for f in elves[i].food]
        assert values_as_expected(elf_food, expected[i])
        assert elves[i].total_calories == sum(expected[i])
    
    assert most_calories_carried(elves=elves) == 24000


def values_as_expected(vals: List[int], expected: List[int]) -> bool:
    """Check that each step of the validation is true"""
    valid = True
    if len(vals) != len(expected):
        valid = False
    for v in vals:
        if v not in expected:
            valid = False
    if sum(vals) != sum(expected):
        valid = False
    return valid
    