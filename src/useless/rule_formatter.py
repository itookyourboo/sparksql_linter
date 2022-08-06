from src.useless.rule import Rule


class RuleFormatter:
    def format(self, rule: Rule):
        if rule.raised_by:
            return f'{rule.name}:{rule.message} ({rule.raised_by})'
        return f'{rule.name}:{rule.message}'
