"""
Use sharing to support large numbers of fine-grained objects
efficiently.
"""

import abc


class FlyweightFactory:
    """
    Create and manage flyweight objects.
    Ensure that flyweights are shared properly. When a client requests a
    flyweight, the FlyweightFactory object supplies an existing instance
    or creates one, if none exists.
    """

    def __init__(self):
        self._flyweights = {}

    def get_flyweight(self, key):
        try:
            flyweight = self._flyweights[key]
        except KeyError:
            flyweight = ConcreteFlyweight()
            self._flyweights[key] = flyweight
        return flyweight


class Flyweight(metaclass=abc.ABCMeta):
    """
    Declare an interface through which flyweights can receive and act on
    extrinsic state.
    """

    def __init__(self):
        self.intrinsic_state = None

    @abc.abstractmethod
    def operation(self, extrinsic_state):
        pass


class ConcreteFlyweight(Flyweight):
    """
    Implement the Flyweight interface and add storage for intrinsic
    state, if any. A ConcreteFlyweight object must be sharable. Any
    state it stores must be intrinsic; that is, it must be independent
    of the ConcreteFlyweight object's context.
    """

    def operation(self, extrinsic_state):
        self.intrinsic_state = extrinsic_state


def main():
    flyweight_factory = FlyweightFactory()
    concrete_flyweight = flyweight_factory.get_flyweight(1)
    concrete_flyweight.operation("ocupado")
    concrete_flyweight = flyweight_factory.get_flyweight(2)
    concrete_flyweight.operation("ocupado")
    i = 1
    while flyweight_factory.get_flyweight(i).intrinsic_state != None:
      print("posicion "+str(i)+" esta ocupada")
      i+=1
    print("libre desde la posicion "+str(i))


if __name__ == "__main__":
    main()
