from typing import List

import pytest

from simpleurdf.utils.python_extension.deepcopy_attribute import init_with_deepcopy


class hello:
    @init_with_deepcopy
    def __init__(self, name: str, b: List = [0, 0]) -> None:
        self.name = name
        self.b = b


class Hola:
    @init_with_deepcopy
    def __init__(self, h: hello) -> None:
        self.hello = h


a1 = hello("a1")
a1.b.append(3)
a2 = hello("a2")


def test_replace_default():
    a3 = hello("a3", [1, 0])
    assert a3.b == [1, 0]