from pathlib import Path
from typing import List
from pytest import fixture

from . import solution as soln


@fixture
def sample_input() -> List[int]:
    path = Path("./day03/test_input.txt").absolute()
    try:
        with open(path) as f:
            return f.readlines()
    except FileNotFoundError as e:
        raise FileNotFoundError(e, "full_path: ", str(path))
    
    
def test_priority():
    assert soln.priority('a') == 1
    assert soln.priority('z') == 26
    assert soln.priority('A') == 27
    assert soln.priority('Z') == 52
    
    
def test_split_string():
    line = "vJrwpWtwJgWrhcsFMMfFFhFp"
    pt1, pt2 = soln.split_string(line)
    assert pt1 == "vJrwpWtwJgWr"
    assert pt2 == "hcsFMMfFFhFp"
 
    
def test_find_shared(sample_input):
    c1 = "jqHRNqRjqzjGDLGL"
    c2 = "rsFMfFZSrLrFZsSL"
    assert soln.find_shared(c1, c2) == "L"
    

def test_solve_pt1(sample_input):
    expected = [
       "p",
       "L",
       "P",
       "v",
       "t",
       "s"
    ]

    found_shared = []
    for i in range(len(sample_input)):
        found = soln.find_shared(*soln.split_string(sample_input[i]))
        assert found == expected[i]
        found_shared.append(found)
    assert sum([soln.priority(c) for c in found_shared]) == 157
    assert soln.solve_pt1(sample_input) == 157
    
    
#     expected = 1
#     found = soln.score_pt1(they_play=soln.PAPER, i_play=soln.ROCK)
#     assert found == expected
    
#     expected = 6
#     found = soln.score_pt1(they_play=soln.SCISSORS, i_play=soln.SCISSORS)
#     assert found == expected
    
 
# def test_solve_pt1(sample_input):
#     expected_score = 15
#     assert soln.solve_pt1(sample_input) == expected_score
    
    
# def test_parse_pt2(sample_input):
#     expected = [
#         (soln.THEY_PLAY["A"], soln.RESULT["Y"]),
#         (soln.THEY_PLAY["B"], soln.RESULT["X"]),
#         (soln.THEY_PLAY["C"], soln.RESULT["Z"]),
#     ]
#     found = list(soln.parse_pt2(sample_input))
#     assert found == expected
   
    
# def test_score_pt2(sample_input):
#     assert soln.score_pt2(soln.ROCK, soln.DRAW) == 4
#     assert soln.score_pt2(soln.PAPER, soln.LOSE) == 1
#     assert soln.score_pt2(soln.SCISSORS, soln.WIN) == 7


# def test_solve_pt2(sample_input):
#     expected_score = 12
#     assert soln.solve_pt2(sample_input) == expected_score
    