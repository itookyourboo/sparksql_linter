import sqlparse.sql as sql
import typing as tp

from src.rules.abstract_rules import QueryRule


class FromAfterSelect(QueryRule):

    def is_suitable(self, obj) -> bool:
        pass

    def is_correct(self, obj) -> bool:
        pass


def get_query_rules():
    yield from [
        FromAfterSelect()
    ]
