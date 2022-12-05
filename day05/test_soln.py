from pathlib import Path
from typing import List
from pytest import fixture

from . import solution as soln


@fixture
def sample_input() -> List[int]:
    path = Path("~/GitRepos/aoc2022/day05/test_input.txt").expanduser().absolute()
    try:
        with open(path) as f:
            return [l for l in f.readlines()]
    except FileNotFoundError as e:
        raise FileNotFoundError(e, "full_path: ", str(path))
    
    
def test_stack():
    stack = soln.Stack()
    stack.add('a')
    assert stack.containers == ['a']
    stack.remove()
    assert stack.containers == []
    
    
def test_warehouse():
    tstr = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """
    wh = soln.Warehouse()
    wh._initialize(initialization=tstr)
    assert isinstance(wh, soln.Warehouse)
    assert wh.stack_count == 3
    assert len(wh.stacks[0]) == 2
    assert len(wh.stacks[1]) == 3
    assert len(wh.stacks[2]) == 1
    
    
def test_parse(sample_input):
    expected = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 """
    found_init, found_instr = soln.parse(sample_input)
    assert isinstance(found_init, soln.Warehouse)
    assert isinstance(found_instr, list)
    assert len(found_init) == 3
    assert len(found_init.stacks[0]) == 2
    assert len(found_init.stacks[1]) == 3
    assert len(found_init.stacks[2]) == 1
    assert len(found_instr) == 4
    
    
def test_solve_pt1(sample_input):
    found = soln.solve_pt1(sample_input)
    expected = "CMZ"
    assert found == expected
