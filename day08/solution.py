# AOC 2022 Day 8 https://adventofcode.com/2022/day/8
import attrs
from pathlib import Path
from typing import List, Tuple


DAY = 8
DAY_STR = f"{DAY:02d}"


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
        self.trees = list(range(max_y * max_x))
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
        if isinstance(val, str):
            val = int(val)
        self.trees[self._get_index_of(x, y)] = val

    def get_above(self, x, y) -> List[int]:
        """Get the tress 'north' of this one"""
        above = []
        y = y - 1
        while y >= 0:
            above.append(self.get_tree(x, y))
            y -= 1
        return above

    def get_below(self, x, y) -> List[int]:
        below = []
        y = y + 1
        while y <= self.max_y:
            below.append(self.get_tree(x, y))
            y += 1
        return below

    def get_left(self, x, y) -> List[int]:
        left = []
        x = x - 1
        while x >= 0:
            left.append(self.get_tree(x, y))
            x -= 1
        return left

    def get_right(self, x, y) -> List[int]:
        right = []
        x = x + 1
        while x <= self.max_x:
            right.append(self.get_tree(x, y))
            x += 1
        return right

    def visible_from_above(self, x, y) -> bool:
        """Get a list of all above and see if any are taller than this one"""
        trees = self.get_above(x, y)
        if not trees:
            return True
        return all([t < self.get_tree(x, y) for t in trees])

    def visible_from_below(self, x, y) -> bool:
        trees = self.get_below(x, y)
        if not trees:
            return True
        return all([t < self.get_tree(x, y) for t in trees])

    def visible_from_left(self, x, y) -> bool:
        trees = self.get_left(x, y)
        if not trees:
            return True
        return all([t < self.get_tree(x, y) for t in trees])

    def visible_from_right(self, x, y) -> bool:
        trees = self.get_right(x, y)
        if not trees:
            return True
        return all([t < self.get_tree(x, y) for t in trees])

    def is_visible(self, x, y) -> bool:
        from_above = self.visible_from_above(x, y)
        from_below = self.visible_from_below(x, y)
        from_left = self.visible_from_left(x, y)
        from_right = self.visible_from_right(x, y)
        return any([from_above, from_below, from_left, from_right])
    
    def viewing_score(self, x, y) -> int:
        # how far can each tree see in all directions
        left_score = 0
        this_tree = self.get_tree(x, y)
        for i in range(x - 1, -1, -1):
            other_tree = self.get_tree(i, y)
            if other_tree < this_tree:
                left_score += 1
            else:
                left_score += 1
                break
        right_score = 0
        for i in range(x + 1, self.max_x + 1, 1):
            other_tree = self.get_tree(i, y)
            if other_tree < this_tree:
                right_score += 1
            else:
                right_score += 1
                break
        above_score = 0
        for j in range(y - 1, -1, -1):
            other_tree = self.get_tree(x, j)
            if other_tree < this_tree:
                above_score += 1
            else:
                above_score += 1
                break
        below_score = 0
        for j in range(y + 1, self.max_y + 1, 1):
            other_tree = self.get_tree(x, j)
            if other_tree < this_tree:
                below_score += 1
            else:
                below_score += 1
                break
            
        return left_score * right_score * above_score * below_score

    @property
    def visible_trees(self) -> List[int]:
        trees = []
        for i in range(self.max_x + 1):
            for j in range(self.max_y + 1):
                if self.is_visible(i, j):
                    trees.append((i, j, self.get_tree(i, j)))
        return trees


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
    y = len(lines)
    x = len(lines[0])

    map = Map(max_x=x, max_y=y)
    i = j = 0
    for line in lines:
        for val in list(line):
            map.add_tree(j, i, val)
            j = (j + 1) % x
        i += 1
    return map


def solve_pt1(lines: List[str]) -> int:
    map = parse(lines)
    return len(map.visible_trees)


def solve_pt2(lines: List[str]) -> int:
    map = parse(lines)
    max = 0
    for x in range(map.max_x + 1):
        for y in range(map.max_y + 1):
            if map.viewing_score(x, y) > max:
                max = map.viewing_score(x, y)
    return max
