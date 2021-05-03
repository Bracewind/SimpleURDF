import sys
from typing import Union

# from .URDFRepresentation import URDFRepresentation
# from .UrdfToUrdf2 import UrdfToUrdf2
from .urdf2_to_urdf import Urdf2ToUrdf

from simpleurdf.urdf2model import Model, World

from lxml import etree, objectify
import simpleurdf.urdfParser.urdf as urdf


class UrdfParser:
    """class used to load, traverse, and create URDF files"""

    def loadURDFFile(self, file):
        """with open(sys.path[0] + "/../xsdFile/urdf_modified.xsd", "r") as f:
        schema = etree.XMLSchema(file=f)
        parser = objectify.makeparser(schema=schema)
        urdfFile = objectify.parse(file, parser).getroot()
        urdf2Builder = UrdfToUrdf2()
        return urdf2Builder.createRobot(urdfFile)"""
        with open(file, "r") as f:
            urdfFile = urdf.CreateFromDocument(f.read())
            a = 4

    def createURDFString(self, robot) -> str:
        treeRobot = Urdf2ToUrdf().createRobot(robot)
        return etree.tostring(treeRobot, pretty_print=True, encoding=str)
        # world = urdfSerializer.createWorld(world)
        # etree.indent(world)
        # etree.ElementTree(world).write(open(pathToFile, "wb"))

    def createURDFFile(self, robot, pathToFile):
        urdfRobot = self.createURDFString(robot)
        a = type(urdfRobot)
        with open(pathToFile, "w") as file:
            file.write(urdfRobot)
