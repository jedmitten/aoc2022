from pathlib import Path
from typing import List
from pytest import fixture

from . import solution as soln


P1 = (0, 0)
P2 = (1, 0)
P3 = (1, 1)


@fixture
def sample_input() -> List[int]:
    return soln.read_input(f"~/GitRepos/aoc2022/day{soln.DAY_STR}/test_input.txt")

@fixture
def sample_input_small() -> List[int]:
    return soln.read_input(f"~/GitRepos/aoc2022/day{soln.DAY_STR}/test_input_small.txt")


def test_cpu(sample_input):
    cpu = soln.Cpu(instructions=sample_input)


# def test_parse(sample_input_small):
#     expected_instructions = ["noop", "addx 3", "addx -5"]
#     expected_executions = [(1, 0), (3, 3), (4, -5)]
#     found_cpu = soln.parse(sample_input_small)
#     assert found_cpu._instructions == expected_instructions
#     found_cpu.run()
#     assert found_cpu._executions == expected_executions


# def test_cpu_x_val_small(sample_input_small):
#     cpu = soln.parse(sample_input_small)
#     cpu.run_cycles()
#     assert cpu._X == -1


# def test_cpu_x_val(sample_input):
#     cpu = soln.parse(sample_input)
#     cpu.run_cycles()
#     pass


def test_solve_pt1(sample_input):
    assert soln.solve_pt1(sample_input) == 13140


# def test_solve_pt2(sample_input):
#     assert soln.solve_pt2(sample_input) == 1


# def test_solve_pt2_2(sample_input2):
#     assert soln.solve_pt2(sample_input2) == 36
