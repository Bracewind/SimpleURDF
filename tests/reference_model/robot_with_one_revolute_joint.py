import math
from simpleurdf.urdf2model.basemodel import (Joint, Limit, RevoluteJointType, XYZ)
from simpleurdf.urdf2model import UrdfFactory
from simpleurdf.urdf2model import Model, Link


class RobotWithOneRevoluteJoint(UrdfFactory):
    def build_model(self) -> Model:
        return Model(
          name="test_robot",
          root_link=Link(
            name="link1",
            joints=[
              Joint(
                name="fixed_joint",
                joint_type_characteristics=RevoluteJointType(
                  rotation_axis=XYZ(0, 1, 0),
                  limit=Limit(
                    lower=-math.pi,
                    upper=math.pi,
                    effort=1000.0,
                    velocity=1,
                  ),
                ),
                child=Link(name="link2"),
              )
            ],
          ),
        )
