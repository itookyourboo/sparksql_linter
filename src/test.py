import pathlib
from runner import run


def f_test_all():
    files = [
        "sql/test.sql",
        # "sql/test_create.sql",
        # "sql/wrong_syntax.sql"
    ]
    for file in files:
        # print(file)
        line = pathlib.Path(file).read_text()
        run(line, source=file)


if __name__ == '__main__':
    f_test_all()
