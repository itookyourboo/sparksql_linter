from lark import Lark, Tree

from grammar_loader import GrammarLoader
from inspector import Inspector


class SqlLinter:
    def __init__(self, sql: str, inspector: Inspector, grammar_loader: GrammarLoader = GrammarLoader()):
        """
        :param sql: код SQL запроса
        :param inspector: объект типа Inspector
        :param grammar_loader: загрузчик грамматики
        """
        self.sql: str = sql
        self.inspector: Inspector = inspector
        self.parser: Lark = grammar_loader.get_parser()

    def print_results(self) -> int:
        """
        Печатает результаты линтинга
        :return: код возврата. 0, если ошибок нет, иначе 1.
        """
        if not self.inspector.results:
            return 0
        for rule in self.inspector.results:
            print(rule)
        return 1

    def __call__(self) -> int:
        """
        Запускает обход инспектора по синтаксическому дереву.
        Печатает результаты, вызывая print_results.
        :return: код возврата
        """
        tree: Tree = self.parser.parse(self.sql)
        self.inspector.visit(tree)
        return self.print_results()
