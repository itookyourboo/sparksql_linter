# sparksql_linter

Статический анализатор SparkSQL с возможностью добавления пользовательских правил.

## Запуск

Для запуска склонируйте репозиторий
```shell
git clone https://github.com/itookyourboo/sparksql_linter.git
cd sparksql_linter
```

Внимание! Требуется Python 3.10.

Установите необходимые зависимости:
```shell
pip install -r requirements.txt
```

Далее запустите утилиту командой:
```shell
python ./src/main.py [file1[, file2, [file3]]]
```
Где `sql files` - набор файлов для синтаксического анализа.

Например:
```shell
python ./src/main.py sql_folder/ test_file.sql
```