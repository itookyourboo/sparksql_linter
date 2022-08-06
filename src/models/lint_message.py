import dataclasses
from rules.model import Rule


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

    def __str__(self):
        return (
            f'{self.file}\n{self.line}:{self.pos:<4}| {self.rule.category}'
            f'{self.rule.num:03}: {self.rule.text} [{self.context.strip()}]'
        )
