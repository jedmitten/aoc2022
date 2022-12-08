from pathlib import Path
from typing import List
from pytest import fixture

from . import solution as soln


@fixture
def sample_input() -> List[int]:
    return soln.read_input("~/GitRepos/aoc2022/day07/test_input.txt")


def test_file():
    name = "a.txt"
    size = 10
    f = soln.File(name=name, size=size)
    assert f.name == name
    assert f.size == size


def test_directory():
    files = [soln.File("a.txt", 10), soln.File("b.txt", 100)]
    d = soln.Directory()
    for f in files:
        d.add_child(child=f)
    assert d.size == 110

    d2 = soln.Directory(name="sub1")
    for f in files:
        d2.add_child(f)
    d.add_child(d2)
    assert d2.parent == d
    assert len(d2) == 2
    assert d.size == 220
    
    
def test_get_nested_dir_list(sample_input):
    fs = soln.parse(sample_input)
    arr = soln.get_nested_dir_list(fs.root_directory)
    assert len(arr) == 4
    

def test_parse(sample_input):
    fs = soln.parse(sample_input)
    
    assert "a" in [c for c in fs.root_directory.children]
    assert "d" in [c for c in fs.root_directory.children]
    

def test_solve_pt1(sample_input):
    answer = soln.solve_pt1(sample_input)
    assert answer == 95437    
        

def test_solve_pt2(sample_input):
    answer = soln.solve_pt2(sample_input)
    assert answer == 24933642    
