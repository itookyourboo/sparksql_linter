import dataclasses
from rules.model import Rule


@dataclasses.dataclass
class LintMessage:
    """
    Сообщение линтера
    @:param rule: правило
    @:param message: текст сообщения
    @:param line:
    @:param pos:
    @:param context:

    """
    rule: Rule
    line: int
    pos: int
    context: str

    def __str__(self):
        return (
            f'{self.line}:{self.pos:<4}| {self.rule.category}{self.rule.num:03}: {self.rule.text} '
            f'[{self.context.strip()}]'
        )
