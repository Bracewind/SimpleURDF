from abc import ABC, abstractmethod
import os
import math
import simpleurdf
from tests.reference_model.robot_with_one_fixed_joint import RobotWithOneFixedJoint

from lxml import etree
from lxml.objectify import ElementMaker

from simpleurdf.urdf2model import Mesh
from simpleurdf import UrdfParser

# import simpleurdf.urdfParser.urdf as urdf


e = ElementMaker()


def g():
    return None


f = e.link(g())


print(etree.tostring(f, pretty_print=True))

import subprocess

cmdlst = ["source", "/opt/ros/foxy/setup.bash"]
proc = subprocess.Popen(cmdlst, stdout=subprocess.PIPE)
stdout_value, stderr_value = proc.communicate()

cmdlst2 = ["ros2", "pkg", "lst"]
proc = subprocess.Popen(cmdlst, stdout=subprocess.PIPE)
stdout_value, stderr_value = proc.communicate()


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
