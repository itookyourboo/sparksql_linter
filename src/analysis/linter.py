from pprint import pprint

from lark import Lark, Tree

from src.grammar.grammar_loader import GrammarLoader
from src.analysis.inspector import Inspector
from src.rules import RuleFormatter


class SqlLinter:
    def __init__(self, sql: str, inspector: Inspector, grammar_loader: GrammarLoader = GrammarLoader(),
                 rule_formatter: RuleFormatter = RuleFormatter()):
        """
        :param sql: код SQL запроса
        :param inspector: объект типа Inspector
        :param grammar_loader: загрузчик грамматики
        """
        self.sql: str = sql
        self.inspector: Inspector = inspector
        self.parser: Lark = grammar_loader.get_parser()
        self.rule_formatter: RuleFormatter = rule_formatter

    def print_results(self) -> int:
        """
        Печатает результаты линтинга
        :return: код возврата. 0, если ошибок нет, иначе 1.
        """
        if not self.inspector.results:
            return 0
        for rule in self.inspector.results:
            print(self.rule_formatter.format(rule))
        return 1

    def __call__(self) -> int:
        """
        Запускает обход инспектора по синтаксическому дереву.
        Печатает результаты, вызывая print_results.
        :return: код возврата
        """
        tree: Tree = self.parser.parse(self.sql)
        print(tree.pretty())
        self.inspector.visit(tree)
        return self.print_results()
