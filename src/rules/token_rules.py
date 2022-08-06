import sqlparse.sql as sql
import typing as tp

from src.rules.abstract_rules import TokenRule


class KeyWordIsUpperCase(TokenRule):
    category = "S"
    num = 1
    text = "Keyword should be uppercase"

    def __init__(self):
        self.category = self.__class__.category
        self.text = self.__class__.text
        self.num = self.__class__.num

    def is_suitable(self, obj: sql.Token) -> bool:
        if not obj.is_keyword:
            return False
        return True

    def is_correct(self, obj: sql.Token) -> bool:
        return obj.value.isupper()


class CamelCaseIdentifier(TokenRule):
    category = "S"
    num = 2
    text = "Identifier shouldn't be CamelCase, use snake_case instead"

    def is_suitable(self, obj: sql.Identifier) -> bool:
        # token.
        pass

    def is_correct(self, obj) -> bool:
        pass


def get_token_rules() -> tp.Iterator[TokenRule]:
    yield from [
        KeyWordIsUpperCase()
    ]
