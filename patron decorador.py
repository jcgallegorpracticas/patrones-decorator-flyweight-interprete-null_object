"""
Attach additional responsibilities to an object dynamically. Decorators
provide a flexible alternative to subclassing for extending
functionality.
"""

import abc
import math


class Component(metaclass=abc.ABCMeta):
    """
    Define the interface for objects that can have responsibilities
    added to them dynamically.
    """

    @abc.abstractmethod
    def operation(self):
        pass


class Decorator(Component, metaclass=abc.ABCMeta):
    """
    Maintain a reference to a Component object and define an interface
    that conforms to Component's interface.
    """

    def __init__(self, component):
        self._component = component

    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteDecoratorA(Decorator):
    """
    Add responsibilities to the component.
    """

    def operation(self):
        lado1, lado2 = self._component.operation()
        perimetro = 2*lado1 + 2*lado2
        print("operacion añadida A: perimetro: " + str(perimetro))
        return lado1, lado2


class ConcreteDecoratorB(Decorator):
    """
    Add responsibilities to the component.
    """

    def operation(self):
        lado1, lado2=self._component.operation()
        diagonal = math.sqrt(lado1*lado1 + lado2*lado2)
        print("operacion añadida B: diagonal: " + str(diagonal))
        return lado1, lado2


class ConcreteComponent(Component):
    """
    Define an object to which additional responsibilities can be
    attached.
    """
    def operation(self):
        lado1 = int(input())
        lado2 = int(input())
        area = lado1 * lado2
        print("operacion basica: area: " + str(area))
        return lado1, lado2


def main():
    concrete_component = ConcreteComponent()
    concrete_decorator_a = ConcreteDecoratorA(concrete_component)
    concrete_decorator_b = ConcreteDecoratorB(concrete_decorator_a)
    concrete_decorator_b.operation()


if __name__ == "__main__":
    main()
