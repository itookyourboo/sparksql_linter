import sys
from src import main
from src.dataclasses.file_metadata import FileMetadata
from main import lint_files

def read_files(*files: str):
    metadata_list = []
    for file in files:
        with open(file, "r", encoding="utf-8") as infile:
            file_metadata = FileMetadata(name=file, text=infile.read(), errors=[])
            metadata_list.append(file_metadata)
    return metadata_list


def handle_files(*files: str):
    lint_files(read_files(*files))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        args = sys.argv[1:]
    else:
        args = ["sql/test.sql"]
    handle_files(*args)

