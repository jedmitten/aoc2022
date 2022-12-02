from pathlib import Path
from typing import List
from pytest import fixture

from . import solution as soln


@fixture
def sample_input() -> List[int]:
    path = Path("./day02/test_input.txt").absolute()
    try:
        with open(path) as f:
            return f.readlines()
    except FileNotFoundError as e:
        raise FileNotFoundError(e, "full_path: ", str(path))
    
    
def test_parse(sample_input):
    expected = [
        (soln.THEY_PLAY["A"], soln.I_PLAY["Y"]),
        (soln.THEY_PLAY["B"], soln.I_PLAY["X"]),
        (soln.THEY_PLAY["C"], soln.I_PLAY["Z"]),
    ]
    found = list(soln.parse(sample_input))
    assert found == expected
    
    
def test_score(sample_input):
    expected = 8
    found = soln.score(they_play=soln.ROCK, i_play=soln.PAPER)
    assert expected == found
    
    expected = 1
    found = soln.score(they_play=soln.PAPER, i_play=soln.ROCK)
    assert found == expected
    
    expected = 6
    found = soln.score(they_play=soln.SCISSORS, i_play=soln.SCISSORS)
    assert found == expected


def test_solve(sample_input):
    expected_score = 15
    assert soln.solve_pt1(sample_input) == expected_score
    