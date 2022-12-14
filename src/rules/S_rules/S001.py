from sqlparse import sql

from rules.model import TokenRule, Correction


class KeyWordIsUpperCase(TokenRule):
    category = "S"
    num = 1
    text = "Keyword should be uppercase"

    def is_suitable(self, obj: sql.Token) -> bool:
        if not obj.is_keyword:
            return False
        return True

    def is_correct(self, obj: sql.Token) -> Correction:
        name: str = obj.value
        correct: str = name.upper()
        if name.isupper():
            return True, None
        return False, (name, correct)
