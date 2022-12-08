# AOC 2022 Day 5
import attrs
from pathlib import Path
from typing import List, Union


def read_input(filepath: str) -> List[str]:
    """Read input file and return a list of something"""
    filepath = Path(filepath)  # type: Path
    if not filepath.exists:
        raise ValueError(
            f"The path {filepath.expanduser().absolute()} could not be found"
        )
    with open(filepath) as f:
        lines = f.readlines()
    return [_l for _l in lines if _l]


@attrs.define
class File:
    name: str
    size: int
       
    
    
class Directory:
    def __init__(self, name: str = None) -> None:
        if name is None:
            name = "/"
        self.__parent = None  # type: Directory
        self.__children = dict()
        if name == "/":
            self.__parent = self
    
    # recurse into directories to get sizes
    @property
    def size(self) -> int:
        size = 0
        for child in self.children.values():
            if isinstance(child, Directory):
                size +=  sum([c.size for c in self.__children])
            else:
                size += child.size
        return size
    
    def add_child(self, child) -> None:
        if isinstance(child, Directory):
            child.__parent == self
        self.__children[child.name] = child
        
    @property
    def parent(self):
        return self.__parent
    
    @property
    def directories(self):
        return self.__directories
    
    @property
    def files(self) -> List[File]:
        return self.__files
    
    @property
    def children(self) -> dict:
        return self.__children
    
    def get_child(self, name: str):
        return self.children[name]
    
    def add_child(self, child) -> None:
        if isinstance(child, Directory):
            child.__parent = self
        self.children[child.name] = child
        
            
class FileSystem:  # this is a tree
    def __init__(self) -> None:
        self.root_directory = Directory(name="/")
        self.directories = []  # type: List[Directory]
        self.working_directory = self.root_directory  # type: Directory
        
    def __cd(self, name: str) -> None:
        if name == "..":
            return self.working_directory.parent
        elif name == "/":
            while self.working_directory != self.root_directory:
                self.__cd(name="..")
        else:  # traverse into the directory by name
            self.working_directory = self.working_directory.children[name]
            
    def __ls(self):
        return self.working_directory.children
            
    
def solve(lines: List[str]) -> int:
    """Represent each directory as a dictionary of either File or Directory

    Args:
        lines (List[str]): _description_

    Returns:
        int: _description_
    """
    pass
