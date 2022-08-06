import dataclasses
from src.rules.abstract_rules import Rule

@dataclasses.dataclass
class LintMessage:
    rule_num: str
    message: str


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
        return f"line: {self.line}, col: {self.pos} - {self.rule} ({self.context})"
