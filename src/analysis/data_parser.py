import sqlparse.sql as sql
import typing as tp
import sqlparse.tokens
from models.datatypes import *
from models.table import Table, Column, DataType


def filter_not_whitespace(tokens: tp.List[sql.Token]):
    return list(filter(lambda token: not token.is_whitespace, tokens))


def is_ddl(query: sql.Statement):
    tokens: tp.List = filter_not_whitespace(query.tokens)
    if tokens[0].ttype == sqlparse.tokens.DDL:
        return True
    return False


def parse_table(query: sql.Statement):
    tokens: tp.List[sql.Token] = filter_not_whitespace(query.tokens)
    table = Table(name=tokens[2].value)
    column = Column(name="")
    for token in tokens:
        if isinstance(token, sqlparse.sql.Parenthesis):
            col_tokens = filter_not_whitespace(token.flatten())
            for col_token in col_tokens:
                if col_token.value.upper() == "VARCHAR":
                        column.col_type = Varchar
                elif col_token.value.upper() == "PRIMARY":
                    column.primary = True
                    column.foreign = False
                elif col_token.value.upper() == "INTEGER":
                    column.col_type = Int
                elif col_token.value.upper() == "DATE":
                    column.col_type = Date
                elif col_token.ttype == sqlparse.tokens.Name:
                    if column.name == "":
                        column.name = col_token.value
                    else:
                        table.columns.append(column)
                        column = Column(name=col_token.value)
    if column.name != "":
        table.columns.append(column)
    return table
