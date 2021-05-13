from simpleurdf.urdf2model.metamodel import DynamicsModel
from simpleurdf.urdf2model import (
  Box,
  Cylinder,
  FixedJointType,
  Joint,
  MaterialColor,
)
from simpleurdf.urdf2model import UrdfFactory
from simpleurdf.urdf2model import Model


class RobotWithGeometryForm(UrdfFactory):
    def build_model(self) -> Model:
        return Model(
          name="test_robot",
          root_link=Box(
            name="base_link",
            material=MaterialColor(name="red", ambient=[1, 0, 0]),
            width=3,
            depth=2,
            height=2,
            mass=10,
            joints=[
              Joint(
                name="fixed_joint",
                joint_type_characteristics=FixedJointType(dynamics=DynamicsModel(1)),
                child=Cylinder(
                  name="link2",
                  radius=0.5,
                  length=5,
                  mass=10,
                ),
              )
            ],
          ),
        )
