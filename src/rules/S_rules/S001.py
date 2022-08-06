from sqlparse import sql

from rules.model import TokenRule


class KeyWordIsUpperCase(TokenRule):
    category = "S"
    num = 1
    text = "Keyword should be uppercase"

    def __init__(self):
        # TODO: исправить костыль
        pass

    def is_suitable(self, obj: sql.Token) -> bool:
        if not obj.is_keyword:
            return False
        return True

    def is_correct(self, obj: sql.Token) -> bool:
        return obj.value.isupper()
