# AOC 2022 Day 5
from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Tuple


EMPTY_LIST_FIELD = field(default_factory=lambda: [])


@dataclass
class Stack:
    containers: List[str] = EMPTY_LIST_FIELD
    
    def __len__(self) -> int:
        return len(self.containers)

    def add(self, v: str) -> None:
        self.containers.append(v)

    def remove(self) -> str:
        return self.containers.pop()
    
    def top(self) -> str:
        """Return the last-in value"""
        return self.containers[-1]


@dataclass
class Warehouse:
    stacks: List[Stack] = EMPTY_LIST_FIELD
    
    def __len__(self) -> int:
        return len(self.stacks)

    def _initialize(self, initialization: str) -> None:
        self.lines = initialization.split("\n")
        self.stack_count = self._get_stack_count()
        self._init_stacks()

    def _get_stacks_line(self) -> int:
        """Retrieve the line that contains stack count from input"""
        for i in range(len(self.lines)):
            line = self.lines[i]
            # remove all spaces
            line = line.replace(" ", "")
            # find the first line that starts with an int
            try:
                int(line[0])
                return i
            except ValueError:
                continue

    def _get_stack_count(self):
        """Find the line and return the last number"""
        idx = self._get_stacks_line()
        count_line = self.lines[idx]
        stack_count_str = count_line.strip()[-1]
        return int(stack_count_str)

    def _build_row(self, line) -> List[Stack]:
        """
        These are sample inputs
            [D]
        [N] [C]
        [Z] [M] [P]

        Given an input, build the stacks by grabbing 4 characters at
        a time and appending to the stack as it comes
        """
        assert "[" in line  # make sure this is a container row
        grab_len = 4
        i = 0
        for j in range(self.stack_count):
            if not self.stacks[j]:
                stack = Stack()
            else:
                stack = self.stacks[j]
            part = line[i:i + grab_len]
            # replace all non-character possibilities
            char = part.strip().replace("[", "").replace("]", "")
            # if empty, then don't add anything to stack
            if char:
                stack.add(char)
            self.stacks[j] = stack
            i += grab_len

    def _init_stacks(self):
        """Starting from the stack count line, move up to build the stacks"""
        self.stacks = [Stack() for i in range(self.stack_count)]
        idx = self._get_stacks_line()
        while idx > 0:
            # move up one from the stack number line
            idx -= 1
            self._build_row(self.lines[idx])
            
    def execute_moves(self, instructions: List[str]) -> None:
        """Rearrange stacks based on input
        
        move 2 from 1 to 2 means "move 2 containers from stack 1 to stack 2"
        """
        for inst in instructions:
            _, count, _, _from, _, _to = inst.split(" ")
            _from = int(_from) - 1  # adjust for 0-index
            _to = int(_to) - 1  # adjust for 0-index
            self.move_n_from_to(n=int(count), _from=_from, _to=_to)

    def move_from_to(self, _from, _to) -> None:
        """1-based index of stacks"""
        container = self.stacks[_from].remove()
        self.stacks[_to].add(container)

    def move_n_from_to(self, n, _from, _to) -> None:
        for i in range(n):
            self.move_from_to(_from, _to)
            
    def top(self) -> str:
        return "".join([s.top() for s in self.stacks])


def read_input(filepath: str) -> List[str]:
    """Read input file and return a list of something"""
    filepath = Path(filepath)  # type: Path
    if not filepath.exists:
        raise ValueError(
            f"The path {filepath.expanduser().absolute()} could not be found"
        )
    with open(filepath) as f:
        lines = f.readlines()
    return [l for l in lines]


def parse(lines: List[str]) -> Tuple[Warehouse, List[str]]:
    """There is an empty line between initalization and instructions"""
    # find blank line
    for i in range(len(lines)):
        if not lines[i].strip():
            break
        i += 1
    initialization = "".join(lines[:i])
    instruction = [l.strip() for l in lines[i + 1:]]
    wh = Warehouse()
    wh._initialize(initialization=initialization)
    return wh, instruction


def solve_pt1(lines: List[str]) -> str:
    # 1. initialize from input
    warehouse, instr = parse(lines)
    # 2. execute the instructions
    warehouse.execute_moves(instr)
    # 3. Which container is at the top of each stack
    return warehouse.top()


def solve_pt2(lines: List[str]) -> int:
    return ""
