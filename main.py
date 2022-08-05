import argparse
import sys
import typing as tp


def main(*files: str):
    for file in files:
        with open(file, "r", encoding="utf-8") as infile:
            lint = lambda text: []  # TODO: Функция синтаксического анализа,
            # принимает текст файла, возвращает замечания и ошибки
            marks = lint(infile.read())
            for mark in marks:
                print(mark)


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    if len(sys.argv) > 1:
        main(*sys.argv[1:])
    else:
        main("test.sql")
