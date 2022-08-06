import sqlparse.sql as sql
import typing as tp

from sqlparse.tokens import DML, Wildcard, Keyword

from src.rules.abstract_rules import QueryRule


class FromAfterSelect(QueryRule):

    def __init__(self):
        self.category = "E"
        self.num = 1
        self.text = "FROM follows immediately after SELECT"
        self.__idx = -1

    def is_suitable(self, obj: sql.Statement | sql.Parenthesis) -> bool:
        tokens: sql.TokenList = obj.tokens
        for idx, item in enumerate(tokens):
            if item.ttype is DML and item.value.upper() == 'SELECT':
                self.__idx = idx
                return True
        return False

    def is_correct(self, obj: sql.Statement | sql.Parenthesis) -> bool:
        tokens: list[sql.Token] = obj.tokens
        has_field: bool = False
        for i in range(self.__idx + 1, len(tokens)):
            if tokens[i].ttype is Wildcard or type(tokens[i]) == sql.Identifier:
                has_field = True
            if tokens[i].ttype is Keyword and tokens[i].value.upper() == 'FROM':
                return has_field
        return True


def get_query_rules():
    yield from [
        FromAfterSelect()
    ]