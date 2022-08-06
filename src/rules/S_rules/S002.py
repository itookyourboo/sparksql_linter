from inflection import underscore
from sqlparse import sql
from sqlparse.sql import Identifier

from rules.model import TokenRule, Correction


class KeyWordIsUpperCase(TokenRule):
    category = "S"
    num = 2
    text = "Identifier should be in snake case"

    def is_suitable(self, obj: sql.Token) -> bool:
        return isinstance(obj, Identifier)

    def is_correct(self, obj: sql.Token) -> Correction:
        name: str = obj.value
        correct: str = underscore(name)
        if name == correct:
            return True, None
        return False, (name, correct)
