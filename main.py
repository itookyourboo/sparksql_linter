import sys

from inspector import Inspector
from linter import SqlLinter
from rules import L_RULES


def main():
    inspector: Inspector = Inspector()
    inspector.add_rules(L_RULES)

    sql: str = 'select digimon as "Digimon Name" from digimonn_mon_list'
    lint: SqlLinter = SqlLinter(sql, inspector)
    exit_code: int = lint()
    sys.exit(exit_code)


if __name__ == '__main__':
    main()
