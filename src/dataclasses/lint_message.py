import dataclasses


@dataclasses.dataclass
class LintMessage:
    number: int
    message: str
