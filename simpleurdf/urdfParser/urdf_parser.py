# from .URDFRepresentation import URDFRepresentation
# from .UrdfToUrdf2 import UrdfToUrdf2

from lxml import etree

from simpleurdf.urdf2model import Model

from .urdf2_to_urdf import Urdf2ToUrdf

#import simpleurdf.urdfParser.urdf as urdf


class UrdfParser:
    """class used to load, traverse, and create URDF files"""
    def createURDFString(self, robot: Model) -> str:
        model = robot.build()
        treeRobot = Urdf2ToUrdf().create_robot(model)
        return etree.tostring(treeRobot, pretty_print=True, encoding=str)
        # world = urdfSerializer.createWorld(world)
        # etree.indent(world)
        # etree.ElementTree(world).write(open(pathToFile, "wb"))

    def createURDFFile(self, robot: Model, pathToFile: str):
        urdfRobot = self.createURDFString(robot)
        with open(pathToFile, "w") as file:
            file.write(urdfRobot)
