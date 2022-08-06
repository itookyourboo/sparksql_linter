import sqlparse.sql
from sqlparse import sql

from rules.model import DataRule
from analysis.data_parser import filter_not_whitespace


class TableDoesNotExists(DataRule):
    category = 'D'
    num = 1
    text = 'Table does not exists'

    def __init__(self, tables=()):
        self.tables = tables
        self.context = ""

    def is_suitable(self, obj: sql.Statement | sql.Parenthesis) -> bool:
        tokens = filter_not_whitespace(obj.flatten())
        for i in range(len(tokens) - 1):
            token, next_token = tokens[i], tokens[i + 1]
            if token.value.upper() == "FROM" and next_token.value.isalnum() and \
                    not next_token.is_keyword:
                return True
        return False

    def is_correct(self, obj: sql.Statement | sql.Parenthesis) -> bool:
        tokens = filter_not_whitespace(obj.flatten())
        table_name = ""
        for i in range(len(tokens) - 1):
            token, next_token = tokens[i], tokens[i + 1]
            if token.value.upper() == "FROM" and next_token.value.isalnum() and \
                    not next_token.is_keyword:
                table_name = next_token.value
                for table in self.tables:
                    if table.name == table_name:
                        return True
        if table_name:
            self.context = table_name
        return False
