import sys
import typing as tp

from inspector import Inspector
from linter import SqlLinter
from rules import L_RULES


def main(*files: str):
    inspector: Inspector = Inspector()
    inspector.add_rules(L_RULES)

    sql: str = 'select digimon as "Digimon Name" from dIgimonn_mon_list'
    lint: SqlLinter = SqlLinter(sql, inspector)
    exit_code: int = lint()
    sys.exit(exit_code)
    for file in files:
        with open(file, "r", encoding="utf-8") as infile:
            lint = lambda text: []  # TODO: Функция синтаксического анализа,
            # принимает текст файла, возвращает замечания и ошибки
            marks = lint(infile.read())
            for mark in marks:
                print(mark)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    if len(sys.argv) > 1:
        main(*sys.argv[1:])
    else:
        main("test.sql")
