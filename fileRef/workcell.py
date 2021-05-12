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
        world = Link(name="world")

        table = Box(
            name="table", material=white, width=1.0, depth=1.0, height=0.05, mass=1
        )

        return Model(
            name="test_robot",
            links=[
                world,
                table,
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
