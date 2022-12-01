from pathlib import Path
from typing import List
from pytest import fixture
# from click.testing import CliRunner

from .solution import elves_from_strs


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
    
    assert len(elves) == 5, "there must be 5 elves"
    
    elf1_calories = [food.calories for food in elves[0].food]
    elf2_calories = [food.calories for food in elves[1].food]
    elf3_calories = [food.calories for food in elves[2].food]
    elf4_calories = [food.calories for food in elves[3].food]
    elf5_calories = [food.calories for food in elves[4].food]
    
    expected = [1000, 2000, 3000]
    assert values_as_expected(elf1_calories, expected), "must be equal"
        
    expected = [4000]
    assert values_as_expected(elf2_calories, expected), "must be equal"
        
    expected = [5000, 6000]
    assert values_as_expected(elf3_calories, expected), "must be equal"
        
    expected = [7000, 8000, 9000]
    assert values_as_expected(elf4_calories, expected), "must be equal"
        
    expected = [10000]
    assert values_as_expected(elf5_calories, expected), "must be equal"


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
    