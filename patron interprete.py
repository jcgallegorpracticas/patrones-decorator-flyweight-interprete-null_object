"""
Define a represention for a grammar of the given language along with an
interpreter that uses the representation to interpret sentences in the
language.
"""

import abc


class AbstractExpression(metaclass=abc.ABCMeta):
    """
    Declare an abstract Interpret operation that is common to all nodes
    in the abstract syntax tree.
    """

    @abc.abstractmethod
    def interpret(self):
        pass


class NonterminalExpression(AbstractExpression):
    """
    Implement an Interpret operation for nonterminal symbols in the grammar.
    """

    def __init__(self, expression):
        self._expression = expression

    def interpret(self):
        return self._expression.interpret() + int("1",2)


class TerminalExpression(AbstractExpression):
    """
    Implement an Interpret operation associated with terminal symbols in
    the grammar.
    """

    def interpret(self):
        return int("101",2)


def main():
    abstract_syntax_tree = NonterminalExpression(TerminalExpression())
    print(abstract_syntax_tree.interpret())


if __name__ == "__main__":
    main()
