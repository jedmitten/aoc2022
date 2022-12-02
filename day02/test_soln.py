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
    
    
def test_parse_pt1(sample_input):
    expected = [
        (soln.THEY_PLAY["A"], soln.I_PLAY["Y"]),
        (soln.THEY_PLAY["B"], soln.I_PLAY["X"]),
        (soln.THEY_PLAY["C"], soln.I_PLAY["Z"]),
    ]
    found = list(soln.parse_pt1(sample_input))
    assert found == expected
 
 
def test_parse_pt2(sample_input):
    expected = [
        (soln.THEY_PLAY["A"], soln.RESULT["Y"]),
        (soln.THEY_PLAY["B"], soln.RESULT["X"]),
        (soln.THEY_PLAY["C"], soln.RESULT["Z"]),
    ]
    found = list(soln.parse_pt2(sample_input))
    assert found == expected
   
    
def test_score_pt1(sample_input):
    expected = 8
    found = soln.score_pt1(they_play=soln.ROCK, i_play=soln.PAPER)
    assert expected == found
    
    expected = 1
    found = soln.score_pt1(they_play=soln.PAPER, i_play=soln.ROCK)
    assert found == expected
    
    expected = 6
    found = soln.score_pt1(they_play=soln.SCISSORS, i_play=soln.SCISSORS)
    assert found == expected
    
    
def test_score_pt2(sample_input):
    assert soln.score_pt2(soln.ROCK, soln.DRAW) == 4
    assert soln.score_pt2(soln.PAPER, soln.LOSE) == 1
    assert soln.score_pt2(soln.SCISSORS, soln.WIN) == 7


def test_solve_pt1(sample_input):
    expected_score = 15
    assert soln.solve_pt1(sample_input) == expected_score
    
    
def test_solve_pt2(sample_input):
    expected_score = 12
    assert soln.solve_pt2(sample_input) == expected_score
    