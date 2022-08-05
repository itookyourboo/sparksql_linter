from typing import Optional

from lark import Lark


class GrammarLoader:
    """
    Класс-загрузчик SQL грамматики
    """
    def __init__(self, filename: str = 'sql.bnf'):
        """
        :param filename: Файл с грамматикой
        """
        self.filename: str = filename
        self._parser: Optional[Lark] = None

    def get_parser(self) -> Lark:
        """
        :return: парсер, объект типа Lark
        """
        if not self._parser:
            with open(self.filename) as sql_bnf_file:
                self._parser = Lark(sql_bnf_file.read())
        return self._parser
