from abc import ABC, abstractmethod
import os
import math

from lxml import etree
from lxml.objectify import ElementMaker

from simpleurdf.urdf2Metamodel import Mesh

# import simpleurdf.urdfParser.urdf as urdf


e = ElementMaker()
print(etree.tostring(e.a({"name": "ert"}, *[]), pretty_print=True))


class ILink(ABC):
    @property
    @abstractmethod
    def test(self):
        pass


class ILinkSpecial(ILink):
    @property
    @abstractmethod
    def test2(self):
        pass


testset = frozenset([4, 8, 5, 9])
print(testset)
for elem in testset:
    print(elem)
print(ILinkSpecial.__base__.__dict__)

path = os.getcwd()
print(math.inf + 2)

a = 3
print("hello" if a == 3 else "ok")

test = [1, 2, 3]
a, b, c = test
print(a)

print(Mesh.__dict__)
# with open(os.path.join(path, "model_test/test.xml"), "r") as f:
#    urdfFile = urdf.CreateFromDocument(f.read())
