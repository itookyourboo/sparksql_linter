import dataclasses
import typing as tp
from src.dataclasses.lint_message import LintMessage


@dataclasses.dataclass
class FileMetadata:
    name: str
    text: str
    errors: tp.List[LintMessage]
