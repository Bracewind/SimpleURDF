#pylint: disable=too-few-public-methods

from abc import ABC
from typing import List, NamedTuple, Union, Optional, Dict
from dataclasses import dataclass

MODEL = "model"
LINK = "link"
JOINT = "joint"


class PoseModel:
    def __init__(self, rpy, xyz):
        if len(rpy) != 3 or len(xyz) != 3:
            raise Exception(f"Expected array of 3 values, got {rpy} and {xyz}")
        self.rpy = rpy
        self.xyz = xyz


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
    radius: float = 1.0
    length: float = 1.0


GeometryTypes = [MeshModel, GeometryBoxModel, GeometryCylinderModel]


@dataclass
class InertialModel:
    pose: PoseModel
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
    pose: PoseModel


# endregion

# region Collision class


@dataclass
class DynamicsModel:
    damping: float


@dataclass
class CollisionModel:
    geometry: Geometry
    pose: PoseModel


#endregion


@dataclass
class LinkModel:
    name: str
    collision: Optional[CollisionModel]
    visuals: List[VisualModel]
    inertial: Optional[InertialModel]
    pose: PoseModel

    def get_name(self):
        return self.name


# region Joints


@dataclass
class LimitModel:
    lower: float
    upper: float
    effort: float
    velocity: float


@dataclass
class JointTypeModel(ABC):
    dynamics: DynamicsModel


@dataclass
class JointModel:
    name: str
    pose: PoseModel
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


JointTypeModelAvailable = [
  FixedJointTypeModel.__name__,
  PrismaticJointTypeModel.__name__,
  ContinuousJointTypeModel.__name__,
  RevoluteJointTypeModel.__name__
]
# endregion


@dataclass
class ModelModel:
    name: str
    links: List[LinkModel]
    joints: List[JointModel]
    nested_models: List
    saved_states: Dict[str, List]
