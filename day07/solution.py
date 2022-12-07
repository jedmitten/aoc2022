# AOC 2022 Day 5
import attrs
from pathlib import Path
from typing import List


def read_input(filepath: str) -> List[str]:
    """Read input file and return a list of something"""
    filepath = Path(filepath)  # type: Path
    if not filepath.exists:
        raise ValueError(
            f"The path {filepath.expanduser().absolute()} could not be found"
        )
    with open(filepath) as f:
        lines = f.readlines()
    return [_l for _l in lines]


@attrs.define
class File:
    name: str
    size: int
    
    
@attrs.define
class Directory:
    files: List[File]
    children: None  # type: List[Directory]
    parent: None  # type: Dict[str, Directory]
    
    # recurse into directories to get sizes
    def size(self) -> int:
        if self.children:
            return sum([d.size for d in self.children])
        return sum([s.size for s in self.files])
    
    
@attrs.define
class FileSystem:
    directories: List[Directory]
    working_directory: Directory
    root_directory: Directory
        
    def cd(self, path: str) -> None:
        if path == "..":
            self.working_directory = self.working_directory.parent
        elif path == "/":
            while self.working_directory != self.root_directory:
                self.cd(path="..")
        else:  # traverse into the directory by name
            self.working_directory = self.working_directory.children[path]
                        
    
