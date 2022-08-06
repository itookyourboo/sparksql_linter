import sys
import typing as tp

from src.dataclasses.file_metadata import FileMetadata
from src.analysis.inspector import Inspector
from src.analysis.linter import SqlLinter
from src.rules import L_RULES


def get_inspector():
    inspector: Inspector = Inspector()
    inspector.add_rules(L_RULES)
    return inspector


def lint_files(files: tp.List[FileMetadata]):
    inspector: Inspector = get_inspector()
    for file in files:
        lint_text(file.text, filename=file.name, inspector=inspector)


def lint_text(text: str, filename="inline", inspector=None):
    if inspector is None:
        inspector: Inspector = get_inspector()

    lint: SqlLinter = SqlLinter(text, inspector)
    exit_code: int = lint()
    if exit_code != 0:
        sys.exit(exit_code)


if __name__ == '__main__':
    lint_text('select digimon as "Digimon Name" from dIgimonn_mon_list')
