import sqlparse
from analysis.visitor import visit_query


def run(sql, source="inline") -> bool:
    """
    Запускает линтер и возвращает код выхода
    :param sql: SQL-код в текстовом представлении
    :param source: название файла (или inline)
    :return: 0, если сообщений нет, иначе 1
    """
    messages, position = [], (1, 1)
    queries = sqlparse.parse(sql)
    for query in queries:
        new_messages, position = visit_query(query, position=position,
                                             source=source)
        messages.extend(new_messages)
    for message in messages:
        print(message)

    return bool(messages)


if __name__ == '__main__':
    raw = "select * from (select * from aboba); select * from aboba"
    run(raw)
