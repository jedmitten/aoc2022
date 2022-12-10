# AOC 2022 Day 10 https://adventofcode.com/2022/day/10
import math
from pathlib import Path
from typing import Dict, List, Tuple


DAY = 10
DAY_STR = f"{DAY:02d}"


class Cpu:
    def __init__(self, instructions) -> None:
        self._X = 1
        self._clock = 0
        self._instructions = instructions
        self._instruction_pointer = 0
        self._executions = []
        self._execution_pointer = 0
        self._proceed = True
        self._cycles = []  # this will hold the (addx, X) pairs
        
    @property
    def has_instructions(self) -> bool:
        return self._instruction_pointer < len(self._instructions)
    
    @property
    def has_executions(self) -> bool:
        return self._execution_pointer < len(self._executions)
    
    def read_instruction(self) -> Tuple[int, int]:
        ret = self._instructions[self._instruction_pointer]
        self._instruction_pointer += 1
        return ret
        
    def execute_instruction(self) -> Tuple[int, int]:
        ret = self._executions[self._execution_pointer]
        self._execution_pointer += 1
        return ret
    
    def load_instruction(self, v) -> None:
        self._executions.append(v)
    
    def peek_next_execution(self) -> Tuple[int, int]:
        return self._executions[self._execution_pointer]
     
    def run_cycles(self):
        while self.has_instructions or self.has_executions:
            if self.has_instructions and self._proceed:
                # 1. Read instruction. Either ["noop"] or ["addx", "val"]
                parts = self.read_instruction().split(' ')
                # 2. Process instruction
                if parts[0] == "addx":
                    # set the time this should be executed. addx takes 2 clock cycles
                    exec_at = self._clock + 1
                    val = int(parts[1])
                else:  # noop
                    exec_at = self._clock + 0
                    val = 0
                # set the value X should be incremented by
                self.load_instruction((exec_at, val))
                self._proceed = False  # do not process more instructions until the clock is free
                # 3. increment clock
            # keep track of the value of X mid-cycle
            self._cycles.append(self._X)
            # 4. execute instructions at the right time
            if self.has_executions:
                while self.has_executions and self.peek_next_execution()[0] == self._clock:
                    # addx
                    _, val = self.execute_instruction()
                    self._X += val
                    self._proceed = True
            self._clock += 1

                    
    @property
    def interesting_signals(self) -> List[int]:
        cycle_index = 19  # start at 20th cycle
        interesting = []
        while cycle_index < len(self._cycles):
            # grab the addx value from the pair of (cycle, X)
            # during the 20th cycle the value is 21 so the strength is 20 * 21
            signal = (cycle_index + 1) * self._cycles[cycle_index]
            interesting.append(signal)
            cycle_index += 40
        return interesting
        
        

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


def parse(lines: List[str]) -> Cpu:
    return Cpu(instructions=lines)


def solve_pt1(lines: List[str]) -> int:
    cpu = parse(lines)
    cpu.run_cycles()
    return sum(cpu.interesting_signals)
    

def solve_pt2(lines: List[str]) -> int:
    return ""
