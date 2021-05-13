from typing import List
from simpleurdf.utils.python_extension.deepcopy_attribute import init_with_deepcopy


class hello:
    @init_with_deepcopy
    def __init__(  #pylint: disable=dangerous-default-value
      self,
      name: str,
      b_long: List = [0, 0],
    ) -> None:
        self.name = name
        self.b_long = b_long


class Hola:
    @init_with_deepcopy
    def __init__(self, h: hello) -> None:
        self.hello = h


a1 = hello("a1")
a1.b_long.append(3)
a2 = hello("a2")


def test_replace_default():
    a_e = hello("a3", [1, 0])
    assert a_e.b_long == [1, 0]
