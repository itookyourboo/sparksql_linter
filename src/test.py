import pathlib
from src.main import main


def f_test_all():
    files = [
        "sql/test.sql",
        "sql/test_create.sql",
        "sql/wrong_syntax.sql"
    ]
    for file in files:
        line = pathlib.Path(file).read_text()
        print(file)
        main(line)


if __name__ == '__main__':
    f_test_all()