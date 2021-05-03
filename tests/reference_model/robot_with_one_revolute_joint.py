from simpleurdf.urdf2model.basemodel import (
    FixedJointType,
    Joint,
    Limit,
    RevoluteJointType,
)
from simpleurdf.urdf2model import UrdfFactory
from simpleurdf.urdf2model import Model, Link

import math


class RobotWithOneRevoluteJoint(UrdfFactory):
    def buildModel(self):
        link1 = Link(name="link1")
        link2 = Link(name="link2")
        return Model(
            name="test_robot",
            links=[
                link1,
                Link(name="link2"),
                Link(name="link3"),
                Link(name="link4"),
            ],
            joints=[
                Joint(
                    name="fixed_joint",
                    parent=link1,
                    child=link2,
                    jointTypeCharacteristics=RevoluteJointType(
                        rotationAxis=[0, 1, 0],
                        limit=Limit(
                            lower=-math.pi, upper=math.pi, effort=1000.0, velocity=1
                        ),
                    ),
                )
            ],
        )
