from abc import abstractmethod
import math
from typing import List, Optional

from .metamodel import (
    IContinuousJointType,
    MetamodelComponent,
    IMesh,
    IGeometryBox,
    Pose,
    IFixedJointType,
    IRevoluteJointType,
    IJoint,
    IJointType,
    IInertial,
    ILink,
    IMaterial,
    IVisual,
    IGeometryCylinder,
    ILimit,
    IModel,
    IDynamics,
    ICollision,
)

PARENT = "parent"
ROOT = "root"

LOWER_LIMIT = -math.inf
UPPER_LIMIT = math.inf

NO_EFFORT = -1
NO_VELOCITY_LIMIT = math.inf


class Mesh(IMesh):
    def __init__(self, uri, scale: List[float] = [1.0, 1.0, 1.0]):
        super().__init__()
        self._uri = uri
        self._scale = scale

    @property
    def uri(self):
        return self._uri

    @property
    def scale(self):
        return self._scale


class GeometryBox(IGeometryBox):
    def __init__(self, size: List[float] = [1.0, 1.0, 1.0]):
        super().__init__()
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


class Inertial(IInertial):
    def __init__(self, pose: Pose, mass: float, inertia: List[float]) -> None:
        self._pose = pose
        self._mass = mass
        self._inertia = inertia

    @property
    def pose(self) -> Pose:
        return self._pose

    @property
    def mass(self) -> float:
        return self._mass

    @property
    def inertia(self) -> List[float]:
        return self._inertia


DEFAULT_INERTIAL = Inertial(Pose(), 1, [1, 0, 0, 1, 0, 1])


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


class Collision(ICollision):
    def __init__(self, geometry, pose=Pose()) -> None:
        super().__init__()
        self._geometry = geometry
        self._pose = pose

    @property
    def geometry(self):
        return self._geometry

    @property
    def pose(self):
        return self._pose


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


class Dynamics(IDynamics):
    def __init__(self, damping=0.0) -> None:
        super().__init__()
        self._damping = damping

    @property
    def damping(self):
        return super().damping


# region link


class Link(ILink):
    def __init__(
        self,
        name: str,
        visuals: List[Visual] = [],
        collision=None,
        inertial=None,
        pose: Pose = Pose(),
        parent_frame=PARENT,
    ):
        self._name = name
        self.pose = pose
        self._inertial = inertial
        self._visuals = visuals
        self._collision = collision

    @property
    def name(self) -> str:
        return self._name

    @property
    def visuals(self) -> List[Visual]:
        return self._visuals

    @property
    def inertial(self) -> Optional[Inertial]:
        return self._inertial

    @property
    def collision(self) -> Optional[ICollision]:
        return self._collision

    def __str__(self) -> str:
        return self._name


class Cylinder(ILink):
    def __init__(
        self,
        name,
        radius: float,
        length: float,
        mass: float = 1,
        pose=Pose(),
        collision_pose=Pose(),
    ):
        super().__init__()
        self._name = name
        self._radius = float(radius)
        self._length = float(length)
        self._mass = float(mass)
        self._pose = pose

        geometryCylinder = GeometryCylinder(self._radius, self._length)

        if pose != Pose():
            if collision_pose != Pose():
                self._collision = Collision(geometryCylinder, collision_pose)
            else:
                self._collision = Collision(geometryCylinder, pose)

        self._visuals = [Visual(geometryCylinder, self._pose)]

        ixx = 1 / 12 * self._mass * (3 * self._radius ** 2 + self._length ** 2)
        iyy = ixx
        izz = 1 / 2 * self._mass * self._radius ** 2
        self._inertial = Inertial(
            self._pose, self._mass, [ixx, 0.0, 0.0, iyy, 0.0, izz]
        )

    @property
    def name(self):
        return self._name

    @property
    def visuals(self):
        return self._visuals

    @property
    def inertial(self):
        return self._inertial

    @property
    def collision(self) -> ICollision:
        return self._collision


class Box(ILink):
    def __init__(
        self,
        name,
        material,
        width: float = 1.0,
        depth: float = 1.0,
        height: float = 1.0,
        mass: float = 1.0,
        pose=Pose(),
        collision_pose=Pose(),
    ):
        super().__init__()
        self._name = name
        self._size = [float(width), float(height), float(depth)]
        self._mass = float(mass)
        self._pose = pose

        # if pose was set
        if pose != Pose():
            # if collection_pose was set
            if collision_pose != Pose():
                self._collision = Collision(GeometryBox(self._size), collision_pose)
            # if not set, put pose of visual
            else:
                self._collision = Collision(GeometryBox(self._size), pose)

        # create visuals
        self._visuals = [Visual(GeometryBox(self._size), self._pose)]

        # create inertials
        width, height, depth = self._size
        ixx = 1 / 12 * self._mass * (height ** 2 + depth ** 2)
        iyy = 1 / 12 * self._mass * (width ** 2 + depth ** 2)
        izz = 1 / 12 * self._mass * (width ** 2 + height ** 2)
        self._inertial = Inertial(
            self._pose, self._mass, [ixx, 0.0, 0.0, iyy, 0.0, izz]
        )

    @property
    def name(self):
        return self._name

    @property
    def collision(self) -> ICollision:
        return self._collision

    @property
    def visuals(self):
        return self._visuals

    @property
    def inertial(self):
        return self._inertial


# endregion

# region joints


class FixedJointType(IFixedJointType):
    def __init__(self) -> None:
        super().__init__()

    @property
    def dynamics(self):
        return None


class ContinuousJointType(IContinuousJointType):
    def __init__(self, rotationAxis: List[float], jointPhysic=Dynamics()):
        super().__init__()
        self._jointPhysic = jointPhysic
        self._rotationAxis = rotationAxis

    @property
    def dynamics(self):
        return self._jointPhysic

    @property
    def rotationAxis(self) -> List[float]:
        return self._rotationAxis


class RevoluteJointType(IRevoluteJointType):
    def __init__(self, rotationAxis, limit, jointPhysic=Dynamics()):
        super().__init__()
        self._jointPhysic = jointPhysic
        self._rotationAxis = rotationAxis
        self._limit = limit

    @property
    def dynamics(self):
        return self._jointPhysic

    @property
    def rotationAxis(self) -> List[float]:
        return self._rotationAxis

    @property
    def limit(self) -> ILimit:
        return self._limit


class Joint(IJoint):
    def __init__(
        self,
        name: str,
        parent,
        child,
        jointTypeCharacteristics: IJointType,
        pose=Pose(),
        parent_frame=PARENT,
    ):
        self._name = name
        self._pose = pose
        self._parent = parent
        self._child = child
        self._jointTypeCharacteristics = jointTypeCharacteristics

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

    @property
    def jointTypeCharacteristics(self) -> IJointType:
        return self._jointTypeCharacteristics


# endregion


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
        self.URDF2type = MetamodelComponent(IModel)

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
    def nestedModels(self) -> List[IModel]:
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
