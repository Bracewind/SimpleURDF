from simpleurdf.urdf2model import metamodel
from simpleurdf.urdf2model.basemodel import IInertial, Inertial
from simpleurdf.urdf2model.metamodel import ICollision, IGeometryBox
from lxml.builder import ElementMaker
from lxml.etree import ElementTree

import functools

from typing import List, Optional

from simpleurdf.urdf2model import (
    Pose,
    IModel,
    ILink,
    IVisual,
    IMesh,
    IGeometryCylinder,
    IMaterial,
    IJoint,
    IFixedJointType,
    ILimit,
    IRevoluteJointType,
)


def _createNothingIfNullDecorator(method):
    @functools.wraps(method)
    def createNothingIfNull(self, fstArg):
        if fstArg is None:
            return None
        else:
            return method(self, fstArg)

    return createNothingIfNull


class Urdf2ToUrdf:
    URDF_JOINT_MAPPING = {
        IFixedJointType.__name__: "fixed",
        IRevoluteJointType.__name__: "revolute",
    }

    def __init__(self):
        self.E = ElementMaker()
        self.ROBOT = self.E.robot
        self.LINK = self.E.link
        self.VISUAL = self.E.visual
        self.COLLISION = self.E.collision
        self.INERTIAL = self.E.inertial
        self.INERTIA = self.E.inertia
        self.MASS = self.E.mass
        self.GEOMETRY = self.E.geometry
        self.MESH = self.E.mesh
        self.BOX = self.E.box
        self.CYLINDER = self.E.cylinder
        self.POSE = self.E.origin
        self.AXIS = self.E.axis
        self.LIMIT = self.E.limit
        self.MATERIAL = self.E.material
        self.JOINT = self.E.joint
        self.JOINT_PARENT = self.E.parent
        self.JOINT_CHILD = self.E.child

    def _removeNoneValue(self, l):
        return [elem for elem in l if elem is not None]

    def createPose(self, pose: Pose):
        x_position, y_position, z_position = pose.xyz
        r, p, y = pose.rpy
        return self.POSE(
            {"rpy": f"{r} {p} {y}", "xyz": f"{x_position} {y_position} {z_position}"}
        )

    def createRobot(self, robot: IModel) -> ElementTree:
        allLinks = []
        allJoints = []
        for model in robot.nestedModels:
            allLinks += model.links
            allJoints += model.joints
        allLinks += robot.links
        allJoints += robot.joints

        linksUrdf = []
        for link in allLinks:
            linksUrdf.append(self.createLink(link))
        jointsUrdf = []
        for joint in allJoints:
            jointsUrdf.append(self.createJoint(joint))
        finalURDF = self._removeNoneValue(
            [{"name": robot.name}] + linksUrdf + jointsUrdf
        )
        return self.ROBOT(*finalURDF)

    def createLink(self, link: ILink) -> ElementTree:
        val = self.createCollision(link.collision)
        return self.LINK(
            *self._removeNoneValue(
                [
                    {"name": link.name},
                    self.createCollision(link.collision),
                    *self.createVisual(link.visuals),
                    self.createInertial(link.inertial),
                ]
            )
        )

    @_createNothingIfNullDecorator
    def createCollision(self, collision: Optional[ICollision]):
        return self.COLLISION(
            self.createPose(collision.pose),
            self.createGeometry(collision.geometry),
        )

    def createVisual(self, visuals: List[IVisual]):
        urdfVisuals = []
        for visual in visuals:
            urdfVisuals.append(
                self.VISUAL(
                    self.createPose(visual.pose),
                    self.createGeometry(visual.geometry),
                    self.createMaterial(visual.material),
                )
            )
        return urdfVisuals

    def createGeometry(self, shape):
        possibleGeometries = {
            IMesh.__name__: self.createMesh,
            IGeometryBox.__name__: self.createBox,
            IGeometryCylinder.__name__: self.createCylinder,
        }
        return self.GEOMETRY(possibleGeometries[shape.URDF2type.urdf2Type](shape))

    def createMesh(self, shape: IMesh):
        x_scale, y_scale, z_scale = shape.scale
        return self.MESH(
            {"filename": shape.uri, "scale": f"{x_scale} {y_scale} {z_scale}"}
        )

    def createBox(self, shape: IGeometryBox):
        width, depth, length = shape.size
        return self.BOX({"size": f"{width:.2f} {depth:.2f} {length:.2f}"})

    def createCylinder(self, shape: IGeometryCylinder):
        return self.CYLINDER({"radius": str(shape.radius), "length": str(shape.length)})

    def createMaterial(self, material: IMaterial):
        return self.MATERIAL({"name": material.name})

    @_createNothingIfNullDecorator
    def createInertial(self, inertial: IInertial):
        ixx, ixy, ixz, iyy, iyz, izz = inertial.inertia
        return self.INERTIAL(
            self.createPose(inertial.pose),
            self.MASS({"value": str(inertial.mass)}),
            self.INERTIA(
                {
                    "ixx": str(ixx),
                    "ixy": str(ixy),
                    "ixz": str(ixz),
                    "iyy": str(iyy),
                    "iyz": str(iyz),
                    "izz": str(izz),
                }
            ),
        )

    def createJoint(self, joint) -> ElementTree:

        # Used to add to the xml axis and limit if it makes sense for the joint
        switcher = {
            IFixedJointType.__name__: lambda: [],
            IRevoluteJointType.__name__: lambda: [
                self.createAxis(joint.jointTypeCharacteristics.rotationAxis),
                self.createLimit(joint.jointTypeCharacteristics.limit),
            ],
        }

        return self.JOINT(
            {
                "name": joint.name,
                "type": Urdf2ToUrdf.URDF_JOINT_MAPPING[
                    joint.jointTypeCharacteristics.URDF2type.urdf2Type
                ],
            },
            *switcher[joint.jointTypeCharacteristics.URDF2type.urdf2Type](),
            self.createPose(joint.pose),
            self.JOINT_PARENT({"link": joint.parent.name}),
            self.JOINT_CHILD({"link": joint.child.name}),
        )

    def createAxis(self, axis: List[float]):
        x, y, z = axis
        return self.AXIS({"xyz": f"{x:.5f} {y:.5f} {z:.5f}"})

    def createLimit(self, limit: ILimit):
        return self.LIMIT(
            {
                "lower": f"{limit.lower:.5f}",
                "upper": f"{limit.upper:.5f}",
                "effort": f"{limit.effort:.5f}",
                "velocity": f"{limit.velocity:.5f}",
            }
        )
