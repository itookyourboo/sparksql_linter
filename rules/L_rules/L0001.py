from lark import Tree
from rules.rule import Rule


class TableNameShouldBeInSnakeCase(Rule):
    name: str = 'L0001'
    message: str = 'Table name should be in snake_case.'
    trigger: str = 'table'

    def handle_tree(self, tree: Tree) -> bool:
        table_name: str = tree.children[0].children[0].value
        self.raised_by = table_name
        return table_name.islower()
