from lark import Visitor, Tree
from rules import Rule


class Inspector(Visitor):
    """
    Класс, делающий обход по синтаксическому дереву
    """
    def __init__(self):
        self.results: list[Rule] = list()
        self.rules: dict[str, list[Rule]] = {}

    def _call_userfunc(self, tree: Tree):
        """
        Переопределяет _call_userfunc класса Visitor.
        Вызывает валидацию правил, подписавшихся на данный элемент.
        :param tree: текущий элемент обхода дерева
        """
        trigger: str = tree.data
        for rule in self.rules.get(trigger, []):
            rule.handle_tree(tree) or self.results.append(rule)

    def add_rule(self, rule: Rule):
        """
        Добавляет правило в словарь {trigger: rule}
        """
        self.rules.setdefault(rule.trigger, []).append(rule)

    def add_rules(self, rules: list[Rule]):
        """
        Добавляет список правил в словарь {trigger: rule}
        """
        for rule in rules:
            self.add_rule(rule)
