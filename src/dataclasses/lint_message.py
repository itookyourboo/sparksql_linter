import dataclasses


@dataclasses.dataclass
class LintMessage:
    """
    Сообщение линтера
    @:param rule_num: номер правила
    @:param message: текст сообщения
    """
    rule_num: str
    message: str
