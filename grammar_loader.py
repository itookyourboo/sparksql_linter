from lark import Lark


def _get_grammar() -> str:
    with open('sql.ebnf') as sql_bnf_file:
        return sql_bnf_file.read()


__parser = None


def get_parser() -> Lark:
    global __parser
    if not __parser:
        grammar: str = _get_grammar()
        __parser: Lark = Lark(grammar)
    return __parser
