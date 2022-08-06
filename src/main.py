import sys
from runner import run
from pathlib import Path

if __name__ == '__main__':
    if len(sys.argv) <= 1:
        # print('No files to lint')
        sys.exit(0)

    files = sys.argv[1:]
    exit_code: int = 0
    for filename in files:
        path = Path(filename)
        to_run = [path] if path.is_file() else path.glob('**/*')
        for p in to_run:
            print(p.name)
            sql = p.read_text()
            exit_code |= run(sql)

    sys.exit(exit_code)
