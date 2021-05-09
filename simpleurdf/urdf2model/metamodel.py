from abc import ABC
from enum import Enum
from typing import List, NamedTuple, Union
from dataclasses import dataclass

MODEL = "model"
LINK = "link"
JOINT = "joint"


class MetamodelComponent:
    def __init__(self, urdf2_type):
        self.urdf2type = urdf2_type

    @property
    def urdf2_type(self):
        return self.urdf2type.__name__


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


class XYZ(NamedTuple):
    x: float
    y: float
    z: float


class Inertia(NamedTuple):
    ixx: float
    ixy: float
    ixz: float
    iyy: float
    iyz: float
    izz: float


class Color(NamedTuple):
    red: float
    green: float
    blue: float
    alpha: float


@dataclass
class FullPathUri:
    path: str


@dataclass
class PackageUri:
    package: str
    path: str


class Geometry:
    pass


@dataclass
class MeshModel(Geometry):
    uri: Union[FullPathUri, PackageUri]
    scale: XYZ


@dataclass
class GeometryBoxModel(Geometry):
    size: XYZ


@dataclass
class GeometryCylinderModel(Geometry):
    radius: float
    length: float


@dataclass
class InertialModel:
    pose: Pose
    mass: float
    inertia: Inertia


# endregion

# region Visual class


@dataclass
class MaterialModel:
    name: str


@dataclass
class ClassicalMaterialModel(MaterialModel):
    ambient: Color
    diffuse: Color
    specular: Color
    emissive: Color


@dataclass
class VisualModel:
    geometry: Geometry
    material: MaterialModel
    pose: Pose


# endregion


@dataclass
class DynamicsModel:
    damping: float


@dataclass
class CollisionModel:
    geometry: Geometry
    pose: Pose


@dataclass
class LimitModel:
    lower: float
    upper: float
    effort: float
    velocity: float


@dataclass
class LinkModel:
    name: str
    collision: CollisionModel
    visuals: List[VisualModel]
    inertial: InertialModel
    pose: Pose

    def get_name(self):
        return self.name


# region Joints


@dataclass
class JointTypeModel(ABC):
    dynamics: DynamicsModel


@dataclass
class JointModel:
    name: str
    pose: Pose
    parent: LinkModel
    child: LinkModel
    joint_characteristics: JointTypeModel


@dataclass
class FixedJointTypeModel(JointTypeModel):
    pass


@dataclass
class PrismaticJointTypeModel(JointTypeModel):
    translation_axis: XYZ
    limit: LimitModel


@dataclass
class ContinuousJointTypeModel(JointTypeModel):
    rotation_axis: XYZ


@dataclass
class RevoluteJointTypeModel(JointTypeModel):
    rotation_axis: XYZ
    limit: LimitModel


# endregion


@dataclass
class ModelModel:
    name: str
    links: List[LinkModel]
    joints: List[JointModel]
    nested_models: List
