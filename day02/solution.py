# AOC 2022 Day 2
from typing import List, Tuple
from pathlib import Path

ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
LOSE = 0
DRAW = 3

THEY_PLAY = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

I_PLAY = {
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}


def read_input(filepath: str) -> List[Tuple[str, str]]:
    """Read input file and return a list of something"""
    filepath = Path(filepath)  # type: Path
    if filepath.exists:
        raise ValueError(f"The path {filepath.expanduser} could not be found")
    with open(filepath) as f:
        lines = f.readlines()
    return lines


def score(they_play: int, i_play: int) -> int:
    """Return an int for win/lose/draw as defined. Return based on play1.
    i.e., if play1 wins, this will be WIN
    """
    if i_play == ROCK:
        if they_play == ROCK:
            score =  DRAW
        elif they_play == PAPER:
            score =  LOSE
        elif they_play == SCISSORS:
            score =  WIN
    elif i_play == PAPER:
        if they_play == ROCK:
            score =  WIN
        elif they_play == PAPER:
            score =  DRAW
        elif they_play == SCISSORS:
            score =  LOSE
    elif i_play == SCISSORS:
        if they_play == ROCK:
            score =  LOSE
        elif they_play == PAPER:
            score =  WIN
        elif they_play == SCISSORS:
            score =  DRAW
    return score + i_play
        

def parse(lines: List[str]) -> Tuple[str, str]:
    """Parse input lines"""
    for line in lines:
        they_play, i_play = line.strip().split(" ")
        yield THEY_PLAY[they_play], I_PLAY[i_play]
        
        
def solve(lines: List[str]) -> int:
    """Read input, parse, calculate score"""
    plays = list(parse(lines))
    total_score = 0
    for play1, play2 in plays:
        total_score += score(they_play=play1, i_play=play2)
    return total_score
    