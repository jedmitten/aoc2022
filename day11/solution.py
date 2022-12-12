# AOC 2022 Day 11 https://adventofcode.com/2022/day/11
import math
from pathlib import Path
from typing import List, Tuple


DAY = 11
DAY_STR = f"{DAY:02d}"


class Monkey:
    def __init__(self):
        self.items = None
        self.operation = None
        self.test = None
        self.throw_true = None
        self.throw_false = None

    def inspect_next(self) -> int:
        # get the next item
        worry = self.items.pop(0)
        return self.perform_operation(worry)

    def perform_operation(self, item) -> int:
        """Use the self.operation string to eval math"""
        operation = self.operation.replace("old", "item")
        new_worry = eval(operation)
        return new_worry

    def test_worry(self, worry) -> bool:
        # check if number is divisible by self.test
        return not worry % self.test

    def get_monkey_and_worry(self) -> Tuple[int, int]:
        # 1. Inspect
        worry = self.inspect_next()
        # 2. I settle down
        # Monkey gets bored with item. Worry level is divided by 3 to 500.
        worry = math.floor(worry / 3)
        # 3. Perform operation
        test_true = self.test_worry(worry)
        # 4. Perform throw based on test_true
        next_monkey_idx = self.throw_true if test_true else self.throw_false
        return worry, next_monkey_idx


def read_input(filepath: str) -> List[str]:
    """Read input file and return a list of string inputs"""
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
            monkey_inits.append(lines[i : i + fwd])
            i += fwd
        else:
            i += 1

    monkeys = []
    for init in monkey_inits:
        m = Monkey()
        _, items = init[1].split(":")
        m.items = [int(i.strip()) for i in items.split(",")]
        _, op = init[2].split(":")
        op = op.split("=")[1].strip()
        m.operation = op
        _, div_init = init[3].split(":")
        m.test = int(div_init.replace(" divisible by ", "").strip())
        _, if_true = init[4].split(":")
        m.throw_true = int(if_true.replace(" throw to monkey ", "").strip())
        _, if_false = init[5].split(":")
        m.throw_false = int(if_false.replace(" throw to monkey ", "").strip())
        monkeys.append(m)

    return monkeys


def solve_pt1(lines: List[str]) -> int:
    monkeys = parse(lines)
    # The monkeys take turns inspecting and throwing items
    i = 0
    while True:
        worry, target_monkey_idx = monkeys[0].get_monkey_and_worry()
        # throw the item
        target_monkey = monkeys[target_monkey_idx]
        target_monkey.items.append(worry)
        # go to next monkey
        i = (i + 1) % len(monkeys)

    """
    After each monkey inspects an item but before it tests your worry level,
 x  your relief that the monkey's inspection didn't damage the item causes
    your worry level to be divided by three and rounded down to the nearest
    integer.
    """


def solve_pt2(lines: List[str]) -> int:
    return ""
