from simpleurdf.urdf2model import UrdfFactory
from simpleurdf.urdf2model import Model


class RobotWithNameOnly(UrdfFactory):
    def buildModel(self):
        return Model(name="hello")
