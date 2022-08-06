import dataclasses
import typing as tp
from src.dataclasses.lint_message import LintMessage


@dataclasses.dataclass
class FileMetadata:
    """
    Класс данных .sql файла
    @:param name: имя файла
    @:param text: содержимое файла
    @:param errors: список ошибок, обнаруженных в файле
    """
    name: str
    text: str
    errors: tp.List[LintMessage]
