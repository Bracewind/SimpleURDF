from simpleurdf.urdf2model import UrdfFactory
from simpleurdf.urdf2model import Model, Link


class RobotWithLinkOnly(UrdfFactory):
    def buildModel(self):
        return Model(
            name="test_robot",
            links=[
                Link(name="link1"),
                Link(name="link2"),
                Link(name="link3"),
                Link(name="link4"),
            ],
        )
