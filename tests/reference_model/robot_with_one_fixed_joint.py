from simpleurdf.urdf2model.metamodel import DynamicsModel
from simpleurdf.urdf2model.basemodel import FixedJointType, Joint
from simpleurdf.urdf2model import UrdfFactory
from simpleurdf.urdf2model import Model, Link


class RobotWithOneFixedJoint(UrdfFactory):
    def build_model(self) -> Model:
        return Model(
          name="test_robot",
          root_link=Link(
            name="link1",
            joints=[
              Joint(
                name="fixed_joint",
                joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                child=Link(name="link2"),
              )
            ],
          ),
        )
