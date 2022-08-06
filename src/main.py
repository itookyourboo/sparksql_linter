import sqlparse

from src.analysis.visitor import visit_query


def main(sql):
    messages, position = [], (1, 1)
    queries = sqlparse.parse(sql)
    for query in queries:
        new_messages, position = visit_query(query, position=position)
        messages.extend(new_messages)
    for message in messages:
        print(message)


if __name__ == '__main__':
    query = "select * from (select * from aboba); \n select * from aboba"
    main(query)
