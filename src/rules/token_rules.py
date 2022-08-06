import sqlparse.sql as sql
import typing as tp

from src.rules.abstract_rules import TokenRule


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
