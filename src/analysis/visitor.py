import typing as tp
import sqlparse
import sqlparse.sql as sql

from models.lint_message import LintMessage
from rules import token_rules
from rules import query_rules
from rules import data_rules
from analysis.data_parser import is_ddl, parse_table
from models.table import Table


def shift_position(position: tp.Tuple[int, int],
                   token: sql.Token) -> tp.Tuple[int, int]:
    row, col = position
    if isinstance(token, (sql.Parenthesis, sql.IdentifierList)):
        return row, col
    if token.ttype is sqlparse.tokens.Newline:
        # print(row, col)
        row += 1
        col = 1
        return row, col
    col += len(token.value)
    return row, col


def visit_query(query: sql.Statement | sql.Parenthesis, position=(1, 1),
                source="inline", tables=()) -> \
        tp.Tuple[tp.List[LintMessage], tp.Tuple[int], tp.List[Table]]:
    messages = []
    if is_ddl(query):
        table = parse_table(query)
        tables.append(table)
    # обработка правил запросов
    for query_rule in query_rules:
        if not query_rule.is_suitable(query):
            continue
        is_correct, correction = query_rule.is_correct(query)
        if not is_correct:
            message = LintMessage(rule=query_rule, line=position[0],
                                  pos=position[1], context=query.value,
                                  file=source, resolve=correction)
            messages.append(message)

    # обработка правил данных
    for data_rule in data_rules:
        data_rule = data_rule.__class__(tables)
        if not data_rule.is_suitable(query):
            continue
        if not data_rule.is_correct(query):
            message = LintMessage(rule=data_rule, line=position[0],
                                  pos=position[1], context=data_rule.context,
                                  file=source, resolve=("Create table", data_rule.context))
            messages.append(message)

    # обработка правил токенов
    tokens: sql.TokenList = query.tokens
    for token in tokens:
        for token_rule in token_rules:
            if not token_rule.is_suitable(token):
                continue
            is_correct, correction = token_rule.is_correct(token)
            if not is_correct:
                message = LintMessage(rule=token_rule, line=position[0],
                                      pos=position[1], context=token.value,
                                      file=source, resolve=correction)
                messages.append(message)
        # print(token.__repr__())
        if isinstance(token, (sqlparse.sql.Parenthesis, sqlparse.sql.IdentifierList)):
            new_messages, position, new_tables \
                = visit_query(token, position=position, source=source, tables=tables)
            messages.extend(new_messages)
            tables.extend(new_tables)
        position = shift_position(position, token)
    # print(messages)
    return messages, position, tables
