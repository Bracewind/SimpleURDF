from abc import ABC, abstractmethod
from enum import Enum
from simpleurdf.urdf_schema import name
from simpleUrdfModelExample.hopper import leg
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


class Mesh(IMesh):
    def __init__(self, uri, scale):
        super().__init__()
        self._uri = uri
        self._scale = scale

    @property
    def uri(self):
        return self._uri

    @property
    def scale(self):
        return self._scale


class IGeometryBox(ABC):
    @property
    @abstractmethod
    def size(self):
        pass


class GeometryBox(IGeometryBox):
    def __init__(self, size: List[float] = [1.0, 1.0, 1.0]):
        self._size = size

    @property
    def size(self):
        return self._size


class Capsule:
    def __init__(self, radius=0.5, length=1):
        self.radius = radius
        self.length = length


class Sphere:
    def __init__(self, radius=1):
        self.radius = radius


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


class GeometryCylinder(IGeometryCylinder):
    def __init__(self, radius: float = 1.0, length: float = 1.0):
        super().__init__()
        self._radius = radius
        self._length = length

    @property
    def radius(self) -> float:
        return self._radius

    @property
    def length(self) -> float:
        return self._length


class IInertial(ABC):
    def __init__(self) -> None:
        pass

    @property
    @abstractmethod
    def pose(self):
        pass

    @property
    @abstractmethod
    def mass(self):
        pass

    @property
    @abstractmethod
    def inertia(self):
        pass


class Inertial(IInertial):
    def __init__(self, pose, mass, inertia) -> None:
        self._pose = pose
        self._mass = mass
        self._inertia = inertia

    @property
    def pose(self):
        pass

    @property
    def mass(self):
        pass

    @property
    def inertia(self):
        pass


DEFAULT_INERTIAL = Inertial(Pose(), 1, [1, 0, 0, 1, 0, 1])

# endregion


# region Visual class

PARENT = "parent"
ROOT = "root"


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


class MaterialColor(IMaterial):
    def __init__(
        self,
        name,
        ambient=[0, 0, 0, 0],
        diffuse=[0, 0, 0, 0],
        specular=[0, 0, 0, 0],
        emissive=[0, 0, 0, 0],
    ):
        self._ambient = ambient
        self._diffuse = diffuse
        self._specular = specular
        self._emissive = emissive
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def ambient(self):
        return self._ambient

    @property
    def diffuse(self):
        return self._diffuse

    @property
    def specular(self):
        return self._specular

    @property
    def emissive(self):
        return self._emissive


white = MaterialColor(name="white", ambient=[0, 0, 0, 1])


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


class Visual(IVisual):
    def __init__(self, geometry, pose=Pose(), material=white, parent_frame=PARENT):
        self._pose = pose
        self._parent_frame = parent_frame
        self._material = material
        self._geometry = geometry

    @property
    def geometry(self):
        return self._geometry

    @property
    def pose(self):
        return self._pose

    @property
    def material(self):
        return self._material

    @property
    def parent_frame(self):
        return self._parent_frame


# endregion


class ICollision(ABC):
    def __init__(self) -> None:
        super().__init__()

    @property
    @abstractmethod
    def geometry(self):
        pass

    @property
    def pose(self):
        pass


LOWER_LIMIT = -math.inf
UPPER_LIMIT = math.inf

NO_EFFORT = -1
NO_VELOCITY_LIMIT = math.inf


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


class Limit(ILimit):
    def __init__(
        self,
        lower=LOWER_LIMIT,
        upper=UPPER_LIMIT,
        effort=NO_EFFORT,
        velocity=NO_VELOCITY_LIMIT,
    ):
        self._lower = lower
        self._upper = upper
        self._effort = effort
        self._velocity = velocity

    @property
    def lower(self):
        return self._lower

    @property
    def upper(self):
        return self._upper

    @property
    def effort(self):
        return self._effort

    @property
    def velocity(self):
        return self._velocity


class IAxis(ABC):
    @property
    @abstractmethod
    def xyz(self) -> List:
        pass

    @property
    @abstractmethod
    def limit(self) -> Limit:
        pass


class Axis(IAxis):
    def __init__(self, xyz=[], limit=Limit()):
        self._xyz = xyz
        self._limit = limit

    @property
    def xyz(self) -> List:
        return self._xyz

    @property
    def limit(self) -> Limit:
        return self._limit


class ILink(ABC):
    def __init__(self):
        self.URDF2type = MetamodelComponent(ILink)

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def visuals(self) -> List[IVisual]:
        pass

    @property
    @abstractmethod
    def inertial(self):
        pass


class Link(ILink):
    def __init__(
        self,
        name: str,
        pose: Pose = Pose(),
        visuals=[],
        inertial=DEFAULT_INERTIAL,
        parent_frame=PARENT,
    ):
        self._name = name
        self.pose = pose
        self._inertial = inertial
        self.visual = visuals
        self.URDF2type = LINK

    @property
    def name(self):
        return self._name

    @property
    def visuals(self):
        return self.visual

    @property
    def inertial(self):
        return self._inertial

    def __str__(self) -> str:
        return self._name


class Cylinder(ILink):
    def __init__(self, name, radius: float, length: float, mass=1, pose=Pose()):
        super().__init__()
        self._name = name
        self._radius = radius
        self._length = length
        self._mass = mass
        self._pose = pose

    @property
    def name(self):
        return self._name

    @property
    def visuals(self):
        return [Visual(GeometryCylinder(self._radius, self._length), self._pose)]

    @property
    def inertial(self):
        ixx = 1 / 12 * self._mass * (3 * self._radius ** 2 + self._length ** 2)
        iyy = ixx
        izz = 1 / 2 * self._mass * self._radius ** 2
        return Inertial(self._pose, self._mass, [ixx, 0.0, 0.0, iyy, 0.0, izz])


class Box(ILink):
    def __init__(
        self,
        name,
        width: float = 1.0,
        height: float = 1.0,
        depth: float = 1.0,
        mass=1,
        pose=Pose(),
    ):
        super().__init__()
        self._name = name
        self._size = [width, height, depth]
        self._mass = mass
        self._pose = pose

    @property
    def name(self):
        return self._name

    @property
    def visuals(self):
        return [Visual(GeometryBox(self._size), self._pose)]

    @property
    def inertial(self):
        width, height, depth = self._size
        ixx = 1 / 12 * self._mass * (height ** 2 + depth ** 2)
        iyy = 1 / 12 * self._mass * (width ** 2 + depth ** 2)
        izz = 1 / 12 * self._mass * (width ** 2 + height ** 2)
        return Inertial(self._pose, self._mass, [ixx, 0.0, 0.0, iyy, 0.0, izz])


class JointType(Enum):
    CONTINUOUS = 0
    FIXED = 1
    REVOLUTE = 2


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
    def parent(self) -> Link:
        pass

    @property
    @abstractmethod
    def child(self) -> Link:
        pass


class IFixedJoint(IJoint):
    def __init__(self) -> None:
        super().__init__()
        self.URDF2type = MetamodelComponent(IFixedJoint)


class IRevoluteJoint(IJoint):
    def __init__(self) -> None:
        super().__init__()
        self.URDF2type = MetamodelComponent(IRevoluteJoint)

    @property
    @abstractmethod
    def rotationAxis(self):
        pass


class Joint(IJoint):
    def __init__(
        self,
        name: str,
        parent,
        child,
        pose=Pose(),
        parent_frame=PARENT,
    ):
        self._name = name
        self._pose = pose
        self._parent = parent
        self._child = child

    @property
    def name(self) -> str:
        return self._name

    @property
    def pose(self):
        return self._pose

    @property
    def parent(self) -> Link:
        return self._parent

    @property
    def child(self) -> Link:
        return self._child


class FixedJoint(Joint, IFixedJoint):
    def __init__(
        self,
        name: str,
        parent,
        child,
        pose=Pose(),
        parent_frame=PARENT,
    ):
        super().__init__(name, parent, child, pose=pose, parent_frame=parent_frame)
        self.URDF2type = MetamodelComponent(IFixedJoint)


class RevoluteJoint(Joint, IRevoluteJoint):
    def __init__(
        self,
        name: str,
        parent,
        child,
        axis=Axis(),
        pose=Pose(),
        parent_frame=PARENT,
    ):
        super().__init__(
            name,
            parent,
            child,
            pose=pose,
            parent_frame=parent_frame,
        )

        self.URDF2type = MetamodelComponent(IRevoluteJoint)
        self._axis = axis

    @property
    def rotationAxis(self):
        return self._axis


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


class Model(IModel):
    def __init__(
        self,
        name: str,
        links: List[ILink] = [],
        joints: List[IJoint] = [],
        nestedModels: List[IModel] = [],
        pose=Pose(),
    ):
        self._name = name
        self._links = links
        self._joints = joints
        self._nestedModels = nestedModels
        self.pose = pose
        self.URDF2type = MODEL

    @property
    def name(self) -> str:
        return self._name

    @property
    def links(self) -> List[ILink]:
        return self._links

    @property
    def joints(self) -> List[IJoint]:
        return self._joints

    @property
    def nestedModels(self):
        return self._nestedModels

    def __str__(self) -> str:
        strRepr = self._name + "(\n"
        for link in self._links:
            strRepr += " " * 4 + link.__str__() + "\n"
        strRepr += ")"
        return strRepr


class World:
    def __init__(self, models):
        self.models = models
