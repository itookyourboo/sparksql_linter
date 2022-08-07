import dataclasses
from rules.model import Rule
from termcolor import colored


@dataclasses.dataclass
class LintMessage:
    """
    Сообщение линтера
    @:param rule: правило
    @:param message: текст сообщения
    @:param line: линия в файле
    @:param pos: столбец в файле
    @:param context: слово или запрос вызвавшее сообщение
    @:param file: файл-источник
    """
    rule: Rule
    line: int
    pos: int
    context: str
    file: str
    resolve: tuple[str, str]

    def __str__(self):
        file_info = f'{self.file}:{self.line}:{self.pos}'
        base_str = f'{file_info:<25}| {self.rule.category}{self.rule.num:03}: ' \
                   f'{self.rule.text} [{colored(self.context.strip(), "blue")}]'
        if self.resolve:
            x_from, x_to = self.resolve
            hint: str = f'Hint: {x_from} --> {x_to}'
            return (
                f'{base_str}\n'
                f'{colored(hint, "yellow")}'
            )
        return base_str
