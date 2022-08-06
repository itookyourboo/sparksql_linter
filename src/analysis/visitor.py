import typing as tp
import sqlparse
import sqlparse.sql as sql

from models.lint_message import LintMessage
from rules import token_rules
from rules import query_rules


def shift_position(position: tp.Tuple[int, int],
                   token: sql.Token) -> tp.Tuple[int, int]:
    row, col = position
    if isinstance(token, sql.Parenthesis):
        return row, col
    if token.ttype is sqlparse.tokens.Newline:
        row += 1
        col = 0
        return row, col
    col += len(token.value)
    return row, col


def visit_query(query: sql.Statement | sql.Parenthesis, position=(0, 0)) -> \
        tp.Tuple[tp.List[LintMessage], tp.Tuple[int]]:
    messages = []
    for query_rule in query_rules:
        if not query_rule.is_suitable(query):
            continue
        if not query_rule.is_correct(query):
            message = LintMessage(rule=query_rule, line=position[0],
                                  pos=position[1], context=query.value)
            messages.append(message)

    tokens: sql.TokenList = query.tokens
    for token in tokens:
        for token_rule in token_rules:
            if not token_rule.is_suitable(token):
                continue
            if not token_rule.is_correct(token):
                message = LintMessage(rule=token_rule,
                                      line=position[0], pos=position[1],
                                      context=token.value)
                messages.append(message)
        # print(token.__repr__())
        if isinstance(token, sqlparse.sql.Parenthesis):
            new_messages, position = visit_query(token, position=position)
            messages.extend(new_messages)
        position = shift_position(position, token)
    # print(messages)
    return messages, position
