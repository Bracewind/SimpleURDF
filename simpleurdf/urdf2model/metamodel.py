from abc import ABC, abstractmethod
from enum import Enum
from typing import List
import math

MODEL = "model"
LINK = "link"
JOINT = "joint"


class MetamodelComponent:
    def __init__(self, URDF2Type):
        self.URDF2type = URDF2Type

    @property
    def urdf2Type(self):
        return self.URDF2type.__name__


class Pose:
    def __init__(self, rpy=[0, 0, 0], xyz=[0, 0, 0]):
        if len(rpy) != 3 or len(xyz) != 3:
            raise Exception(f"Expected array of 3 values, got {rpy} and {xyz}")
        self.rpy = rpy
        self.xyz = xyz


# region Geometry and hardcoded ones
class GeometryType(Enum):
    MESH = "mesh"
    CYLINDER = "cylinder"


class IMesh(ABC):
    def __init__(self):
        self.URDF2type = MetamodelComponent(IMesh)

    @property
    @abstractmethod
    def uri(self):
        pass

    @property
    @abstractmethod
    def scale(self) -> List[float]:
        pass


class IGeometryBox(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.URDF2type = MetamodelComponent(IGeometryBox)

    @property
    @abstractmethod
    def size(self) -> List[float]:
        pass


class IGeometryCylinder(ABC):
    def __init__(self):
        self.URDF2type = MetamodelComponent(IGeometryCylinder)

    @property
    @abstractmethod
    def radius(self) -> float:
        pass

    @property
    @abstractmethod
    def length(self) -> float:
        pass


class IInertial(ABC):
    def __init__(self) -> None:
        pass

    @property
    @abstractmethod
    def pose(self) -> Pose:
        pass

    @property
    @abstractmethod
    def mass(self) -> float:
        pass

    @property
    @abstractmethod
    def inertia(self) -> List[float]:
        pass


# endregion


# region Visual class


class IMaterial(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @property
    @abstractmethod
    def ambient(self):
        pass

    @property
    @abstractmethod
    def diffuse(self):
        pass

    @property
    @abstractmethod
    def specular(self):
        pass

    @property
    @abstractmethod
    def emissive(self):
        pass


class IVisual(ABC):
    @property
    @abstractmethod
    def geometry(self):
        pass

    @property
    @abstractmethod
    def material(self) -> IMaterial:
        pass

    @property
    @abstractmethod
    def pose(self) -> Pose:
        pass

    @property
    @abstractmethod
    def parent_frame(self):
        pass


# endregion


class IDynamics(ABC):
    def __init__(self) -> None:
        super().__init__()

    @property
    @abstractmethod
    def damping(self):
        pass


class ICollision(ABC):
    def __init__(self) -> None:
        super().__init__()

    @property
    @abstractmethod
    def geometry(self):
        pass

    @property
    @abstractmethod
    def pose(self) -> Pose:
        pass


class ILimit(ABC):
    @property
    @abstractmethod
    def lower(self):
        pass

    @property
    @abstractmethod
    def upper(self):
        pass

    @property
    @abstractmethod
    def effort(self):
        pass

    @property
    @abstractmethod
    def velocity(self):
        pass


class ILink(ABC):
    def __init__(self):
        self.URDF2type = MetamodelComponent(ILink)

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def collision(self) -> ICollision:
        pass

    @property
    @abstractmethod
    def visuals(self) -> List[IVisual]:
        pass

    @property
    @abstractmethod
    def inertial(self) -> IInertial:
        pass


class JointType(Enum):
    CONTINUOUS = 0
    FIXED = 1
    REVOLUTE = 2


# region Joints


class IJointType(ABC):
    def __init__(self) -> None:
        super().__init__()

    @property
    @abstractmethod
    def dynamics(self) -> IDynamics:
        pass


class IJoint(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.URDF2type = MetamodelComponent(IJoint)

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def pose(self) -> Pose:
        pass

    @property
    @abstractmethod
    def parent(self) -> ILink:
        pass

    @property
    @abstractmethod
    def child(self) -> ILink:
        pass

    @property
    @abstractmethod
    def jointTypeCharacteristics(self) -> IJointType:
        pass


class IFixedJointType(IJointType):
    def __init__(self) -> None:
        super().__init__()
        self.URDF2type = MetamodelComponent(IFixedJointType)


class IPrismaticJointType(IJointType):
    def __init__(self) -> None:
        super().__init__()
        self.URDF2type = MetamodelComponent(IPrismaticJointType)

    @property
    @abstractmethod
    def translationAxis(self) -> List[float]:
        pass

    @property
    @abstractmethod
    def limit(self) -> ILimit:
        pass


class IContinuousJointType(IJointType):
    def __init__(self) -> None:
        super().__init__()
        self.URDF2type = MetamodelComponent(IContinuousJointType)

    @property
    @abstractmethod
    def rotationAxis(self) -> List[float]:
        pass


class IRevoluteJointType(IJointType):
    def __init__(self) -> None:
        super().__init__()
        self.URDF2type = MetamodelComponent(IRevoluteJointType)

    @property
    @abstractmethod
    def rotationAxis(self):
        pass

    @property
    @abstractmethod
    def limit(self) -> ILimit:
        pass


# endregion


class IModel(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def links(self) -> List[ILink]:
        pass

    @property
    @abstractmethod
    def joints(self) -> List[IJoint]:
        pass

    @property
    @abstractmethod
    def nestedModels(self) -> List:
        pass
