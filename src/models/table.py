import dataclasses
import typing as tp

from models.datatypes import DataType, Int


@dataclasses.dataclass
class Column:
    name: str
    col_type: DataType
    primary: bool
    foreign: bool

    def __init__(self, name="", col_type=Int(), foreign=False, primary=False):
        self.name = name
        self.col_type = col_type
        self.foreign = foreign
        self.primary = primary


@dataclasses.dataclass
class Table:
    name: str
    columns: tp.List[Column]

    def __init__(self, name="", columns=None):
        self.name = name
        self.columns = [] if columns is None else columns
