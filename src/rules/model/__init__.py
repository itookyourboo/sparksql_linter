import abc
from typing import Optional

from sqlparse import sql


Correction = tuple[bool, Optional[tuple[str, str]]]


class Rule(abc.ABC):
    category: str = ''
    num: int = -1
    text: str = ''

    @abc.abstractmethod
    def is_suitable(self, obj: sql.Statement | sql.Parenthesis) -> bool:
        """Подходит ли по шаблону"""
        raise NotImplemented

    @abc.abstractmethod
    def is_correct(self, obj: sql.Statement | sql.Parenthesis) -> Correction:
        """Выполняется ли правило"""
        raise NotImplemented

    def __str__(self):
        return f"{self.category}{self.num}: {self.text}"


token_rules = []


class TokenRule(Rule, abc.ABC):
    """Правило для одного токена"""
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        token_rules.append(cls())

    @abc.abstractmethod
    def is_suitable(self, obj: sql.Token) -> bool:
        """Подходит ли по шаблону"""
        raise NotImplemented

    @abc.abstractmethod
    def is_correct(self, obj: sql.Token) -> bool:
        """Выполняется ли правило"""
        raise NotImplemented


query_rules = []


class QueryRule(Rule, abc.ABC):
    """Правило для одного запроса"""
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        query_rules.append(cls())


data_rules = []


class DataRule(Rule, abc.ABC):
    """Правило по использованию данных"""
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        data_rules.append(cls())
