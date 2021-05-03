from simpleurdf.urdf2model.basemodel import (
    Box,
    Cylinder,
    FixedJointType,
    GeometryBox,
    Joint,
    Limit,
    MaterialColor,
    RevoluteJointType,
)
from simpleurdf.urdf2model import UrdfFactory
from simpleurdf.urdf2model import Model, Link

import math


class RobotWithGeometryForm(UrdfFactory):
    def buildModel(self):
        link1 = Box(
            name="link1",
            material=MaterialColor(name="red", ambient=[1, 0, 0]),
            width=3,
            depth=2,
            height=2,
            mass=10,
        )
        link2 = Cylinder(name="link2", radius=0.5, length=5, mass=10)
        return Model(
            name="test_robot",
            links=[
                link1,
                link2,
            ],
            joints=[
                Joint(
                    name="fixed_joint",
                    parent=link1,
                    child=link2,
                    jointTypeCharacteristics=FixedJointType(),
                )
            ],
        )
