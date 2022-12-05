from pathlib import Path
from typing import List
from pytest import fixture

from . import solution as soln


@fixture
def sample_input() -> List[int]:
    path = Path("~/GitRepos/aoc2022/day04/test_input.txt").expanduser().absolute()
    try:
        with open(path) as f:
            return [l.strip() for l in f.readlines()]
    except FileNotFoundError as e:
        raise FileNotFoundError(e, "full_path: ", str(path))
    
    
def test_parse(sample_input):
    parsed = soln.parse(sample_input)
    assert len(parsed) == 6
    print("parsed", parsed)
    assert all([len(g) == 2 for g in parsed])
    group = parsed[0]
    assert group[0] == {2, 3, 4}
    assert group[1] == {6, 7, 8}
    group = parsed[5]
    assert group[0] == set([int(i) for i in list("23456")])
    assert group[1] == set([int(i) for i in list("45678")])
    

def test_get_assignments():
    assert soln.get_assignments("2-4") == {2, 3, 4}
    

def test_solve_pt1(sample_input):
    assert soln.solve_pt1(sample_input) == 2
    
    
def test_solve_pt2(sample_input):
    assert soln.solve_pt2(sample_input) == 4
