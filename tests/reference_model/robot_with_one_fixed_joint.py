from simpleurdf.urdf2model.basemodel import FixedJointType, Joint
from simpleurdf.urdf2model import UrdfFactory
from simpleurdf.urdf2model import Model, Link


class RobotWithOneFixedJoint(UrdfFactory):
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
                    jointTypeCharacteristics=FixedJointType(),
                )
            ],
        )
