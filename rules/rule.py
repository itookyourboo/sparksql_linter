from lark import Tree


class Rule:
    """
    Базовый класс для правила
    """
    name: str
    message: str
    trigger: str

    def handle_tree(self, tree: Tree) -> bool:
        """
        Валидирует элемент синтаксического дерева
        :param tree: валидируемый элемент
        :return: проходит ли валидацию
        """
        pass

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return f'{self.name}: {self.message}'
