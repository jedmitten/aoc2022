# AOC 2022 Day 8
import attrs
from pathlib import Path
from typing import List, Tuple


@attrs.define
class Tree:
    x: int
    y: int
    
    def is_inside(self, x, y):
        return self.x 
    
    def is_blocked_by(self, other_tree) -> bool:
        pass
        
class Map:
    def __init__(self, max_x: int, max_y: int) -> None:
        self.trees = list(range(max_x + (max_y * max_x)))
        self.max_x = max_x - 1
        self.max_y = max_y - 1
            
    def _get_index_of(self, x, y):
        """
        0, 0 = 0 + 0*5 = 0th index
        0, 1 = 0 + 1*5 = 5th index 
        1, 0 = 1 + 0*5 = 1st index
        2, 2 = 2 + 2*5 = 12th index
        """
        index = x + (y * (self.max_x + 1))
        return index
    
    def get_tree(self, x, y):
        index = self._get_index_of(x, y)
        return self.trees[index]
    
    def add_tree(self, x, y, val):
        self.trees[self._get_index_of(x, y)] = val
    
    def is_edge(self, x, y):
        return x > 0 and x < self.max_x and y > 0 and y < self.max_y
    
    def get_surrounding(self, x, y):
        """Get the trees that are
        1. above
        2. below
        3. left
        4. right
        of current tree

        Args:
            x (_type_): _description_
            y (_type_): _description_
        """
        raise NotImplementedError("This method has not yet been implemented")



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


def parse(lines: List[str]) -> Map:
    y =len(lines)
    x = len(lines[0])
    
    map = Map(max_x=x, max_y=y)
    


def solve_pt1(lines: List[str]) -> int:
    return ""

def solve_pt2(lines: List[str]) -> int:
    return ""    
