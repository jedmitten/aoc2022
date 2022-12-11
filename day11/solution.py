# AOC 2022 Day 11 https://adventofcode.com/2022/day/11
from pathlib import Path
from typing import Dict, List, Tuple


DAY = 11
DAY_STR = f"{DAY:02d}"


class Monkey:
    def __init__(self):
        self.starting_items = None
        self.operation = None
        self.test = None
        self.throw_true = None
        self.throw_false = None

    def inspect(self, item):
        raise NotImplementedError()

    def test_worry(self, worry):
        raise NotImplementedError()

    def throw_to(self, other_monkey, val):
        raise NotImplementedError()


def read_input(filepath: str) -> List[str]:
    """Read input file and return a list of something"""
    filepath = Path(filepath).expanduser().absolute()  # type: Path
    if not filepath.exists:
        raise ValueError(
            f"The path {filepath.expanduser().absolute()} could not be found"
        )
    with open(filepath) as f:
        lines = f.readlines()
    return [_l.strip() for _l in lines if _l]


def parse(lines: List[str]) -> List[Monkey]:
    monkey_inits = []
    i = 0
    fwd = 6
    while i < len(lines):
        line = lines[i]
        if line.startswith("Monkey"):
            monkey_inits.append(lines[i:i+fwd])
            i += fwd
        else:
            i += 1

    monkeys = []
    for init in monkey_inits:
        m = Monkey()
        _, items = init[1].split(":")
        m.starting_items = [int(i.strip()) for i in items.split(",")]
        _, op = init[2].split(":")
        m.operation = op.strip()
        _, div_init = init[3].split(":")
        m.test = int(div_init.replace(" divisible by ", "").strip())
        _, if_true = init[4].split(":")
        m.throw_true = int(if_true.replace(" throw to monkey ", "").strip())
        _, if_false = init[5].split(":")
        m.throw_false = int(if_false.replace(" throw to monkey ", "").strip())
        monkeys.append(m)

    return monkeys


def solve_pt1(lines: List[str]) -> int:
    return ""


def solve_pt2(lines: List[str]) -> int:
    return ""
