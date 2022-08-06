import abc
import dataclasses
from pprint import pprint
import typing as tp
import sqlparse.sql as sql
import sqlparse


@dataclasses.dataclass
class Rule(abc.ABC):
    category: str
    num: int
    text: str

    @abc.abstractmethod
    def is_suitable(self, obj) -> bool:
        """Подходит ли по шаблону"""
        raise NotImplemented

    @abc.abstractmethod
    def is_correct(self, obj) -> bool:
        """Выполняется ли правило"""
        raise NotImplemented

    def __str__(self):
        return f"{self.category}{self.num}: {self.text}"


class TokenRule(Rule, abc.ABC):
    """Правило для одного токена"""
    pass


class QueryRule(Rule, abc.ABC):
    """Правило для одного запроса"""
    pass


class DataRule(Rule, abc.ABC):
    """Правило по использованию данных"""
    pass


class KeyWordIsUpperCase(TokenRule):
    def __init__(self):
        self.category = "S"
        self.num = 1
        self.text = "Keyword should be uppercase"

    def is_suitable(self, obj: sql.Token) -> bool:
        if not obj.is_keyword:
            return False
        return True

    def is_correct(self, obj: sql.Token) -> bool:
        return obj.value.isupper()


def get_token_rules() -> tp.Iterator[TokenRule]:
    yield from [
        KeyWordIsUpperCase()
    ]


@dataclasses.dataclass
class LintMessage:
    rule: Rule
    line: int
    pos: int
    context: str

    def __str__(self):
        return f"line: {self.line}, col: {self.pos} - {self.rule} ({self.context})"


def shift_position(position: tp.Tuple[int, int],
                   token: sql.Token) -> tp.Tuple[int, int]:
    row, col = position
    if isinstance(token, sql.Parenthesis):
        return row, col
    if token == sqlparse.tokens.Newline:
        row += 1
        col = 0
        return row, col
    col += len(token.value)
    return row, col


def visit_query(query: sql.Statement | sql.Parenthesis, position=(0, 0)) -> \
tp.Tuple[tp.List[LintMessage], tp.Tuple[int]]:
    messages = []
    tokens = query.tokens
    for token in tokens:
        for token_rule in get_token_rules():
            if not token_rule.is_suitable(token):
                continue
            if not token_rule.is_correct(token):
                message = LintMessage(rule=token_rule,
                                      line=position[0], pos=position[1],
                                      context=token.value)
                messages.append(message)
        # print(token.__repr__())
        if isinstance(token, sqlparse.sql.Parenthesis):
            new_messages, position = visit_query(token)
            messages.extend(new_messages)
        position = shift_position(position, token)
    return messages, position


def main(sql):
    messages, position = [], (0, 0)
    queries = sqlparse.parse(sql)
    for query in queries:
        messages, position = visit_query(query)
    for message in messages:
        print(message)

    # pprint(queries)
    # pprint(sqlparse.parse(sql)[0].tokens)


if __name__ == '__main__':
    query = "select * from (select * from aboba); select * from aboba"
    main(query)
