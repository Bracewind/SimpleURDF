from abc import ABC, abstractmethod

from simpleurdf.urdf2model import IModel


class SimpleUrdf(ABC):
    """interface used to load, traverse, and create URDF files"""

    @abstractmethod
    def loadURDFFile(self, file) -> IModel:
        """This method is used to create a robot using the python class from an urdf file"""
        pass

    @abstractmethod
    def createURDFString(self, robot: IModel) -> str:
        """create a string containing the urdf model of the robot in xml format"""
        pass

    @abstractmethod
    def createURDFFile(self, robot: IModel, pathToFile: str):
        """create a file at the given ABSOLUTE path containing the urdf model of the robot in xml format"""
        pass
