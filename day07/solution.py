# AOC 2022 Day 5
import attrs
from pathlib import Path
from typing import List, Union


@attrs.define
class File:
    name: str
    size: int

    def __repr__(self) -> str:
        return f'File(name="{self.name}", size={self.size})'


class Directory:
    def __init__(self, name: str = None) -> None:
        if name is None:
            name = "/"
        self.name = name
        self.__children = dict()
        if name == "/":
            self.__parent = self

    def __len__(self) -> int:
        return len(self.__children)

    # recurse into directories to get sizes
    @property
    def size(self) -> int:
        size = 0
        for child in self.children.values():
            if isinstance(child, Directory):
                size += child.size
            else:
                size += child.size
        return size

    def add_child(self, child) -> None:
        if isinstance(child, Directory):
            child.__parent == self
        self.__children[child.name] = child

    @property
    def has_dirs(self):
        return len(self.directories) > 0

    @property
    def parent(self):
        return self.__parent

    @property
    def directories(self):
        return [c for _, c in self.__children.items() if isinstance(c, Directory)]

    @property
    def files(self) -> List[File]:
        return [c for _, c in self.__children.items() if isinstance(c, File)]

    @property
    def children(self) -> dict:
        return self.__children

    def get_child(self, name: str):
        return self.children[name]

    def add_child(self, child) -> None:
        if isinstance(child, Directory):
            child.__parent = self
        self.__children[child.name] = child

    def __repr__(self) -> str:
        return f'Directory(name="{self.name}", size={self.size})'


class FileSystem:  # this is a tree
    def __init__(self) -> None:
        self.root_directory = Directory()
        self.directories = []  # type: List[Directory]
        self.working_directory = self.root_directory  # type: Directory

    def cd(self, name: str) -> None:
        if name == "..":
            self.working_directory = self.working_directory.parent
        elif name == "/":
            while self.working_directory != self.root_directory:
                self.cd(name="..")
        else:  # traverse into the directory by name
            # if child exists
            if name in self.working_directory.children:
                self.working_directory = self.working_directory.children[name]
            else:
                self.working_directory.add_child(Directory(name=name))

    def ls(self):
        return self.working_directory.children


def get_nested_dir_list(d: Directory, arr: list = None) -> List[Directory]:
    if not isinstance(arr, list):
        arr = []

    if d.has_dirs:
        for c in d.directories:
            arr += get_nested_dir_list(c)
    arr.append(d)
    return arr


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


def parse(lines: List[str]) -> FileSystem:
    fs = FileSystem()

    for line in lines:
        parts = line.split(" ")
        if parts[0] == "$":
            cmd = parts[1]
            if cmd == "cd":
                fs.cd(parts[2])
        elif parts[0] == "dir":
            fs.working_directory.add_child(Directory(name=parts[1]))
        else:
            # this is a file
            fs.working_directory.add_child(File(name=parts[1], size=int(parts[0])))
    return fs


def solve_pt1(lines: List[str]) -> int:
    """Find all the direcories with a total size of 100000 or less
    What is the sum of their total sizes?
    """
    SIZE_CHECK = 100000
    fs = parse(lines)
    small_dirs = [
        d for d in get_nested_dir_list(fs.root_directory) if d.size <= SIZE_CHECK
    ]
    return sum([d.size for d in small_dirs])


TOTAL_DISK_SIZE = 70000000
UNUSED_NEED = 30000000


def solve_pt2(lines: List[str]) -> int:
    fs = parse(lines)
    all_dirs = get_nested_dir_list(fs.root_directory)
    disk_left = TOTAL_DISK_SIZE - fs.root_directory.size
    target_delete = UNUSED_NEED - disk_left
    big_enough = [d for d in all_dirs if d.size >= target_delete]
    return min([d.size for d in big_enough])
    
