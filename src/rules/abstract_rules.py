import dataclasses
import abc


@dataclasses.dataclass
class Rule(abc.ABC):
    category: str
    num: int
    text: str

    @abc.abstractmethod
    def is_suitable(self, obj) -> bool:
        """Подходит ли по шаблону"""
        raise NotImplemented

    @abc.abstractmethod
    def is_correct(self, obj) -> bool:
        """Выполняется ли правило"""
        raise NotImplemented

    def __str__(self):
        return f"{self.category}{self.num}: {self.text}"


class TokenRule(Rule, abc.ABC):
    """Правило для одного токена"""
    pass


class QueryRule(Rule, abc.ABC):
    """Правило для одного запроса"""
    pass


class DataRule(Rule, abc.ABC):
    """Правило по использованию данных"""
    pass
