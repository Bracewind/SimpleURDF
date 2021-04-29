from simpleurdf.urdf2Metamodel.metamodel import (
    IAxis,
    IFixedJoint,
    ILimit,
    IRevoluteJoint,
)
from lxml.builder import ElementMaker
from lxml.etree import ElementTree

from typing import List

from simpleurdf.urdf2Metamodel import (
    IModel,
    ILink,
    IVisual,
    IMesh,
    IGeometryCylinder,
    IMaterial,
    IJoint,
    Pose,
    Joint,
    Link,
    World,
)


class Urdf2ToUrdf:
    URDF_JOINT_MAPPING = {
        IFixedJoint.__name__: "fixed",
        IRevoluteJoint.__name__: "revolute",
    }

    def __init__(self):
        self.E = ElementMaker()
        self.ROBOT = self.E.robot
        self.LINK = self.E.link
        self.VISUAL = self.E.visual
        self.GEOMETRY = self.E.geometry
        self.MESH = self.E.mesh
        self.CYLINDER = self.E.cylinder
        self.POSE = self.E.origin
        self.AXIS = self.E.axis
        self.LIMIT = self.E.limit
        self.MATERIAL = self.E.material
        self.JOINT = self.E.joint
        self.JOINT_PARENT = self.E.parent
        self.JOINT_CHILD = self.E.child

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
        finalURDF = [{"name": robot.name}] + linksUrdf + jointsUrdf
        return self.ROBOT(*finalURDF)

    def createLink(self, link: ILink) -> ElementTree:
        return self.LINK({"name": link.name}, *self.createVisual(link.visuals))

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
            IGeometryCylinder.__name__: self.createCylinder,
        }
        return self.GEOMETRY(possibleGeometries[shape.URDF2type.urdf2Type](shape))

    def createMesh(self, shape: IMesh):
        x_scale, y_scale, z_scale = shape.scale
        return self.MESH(
            {"filename": shape.uri, "scale": f"{x_scale} {y_scale} {z_scale}"}
        )

    def createCylinder(self, shape: IGeometryCylinder):
        return self.CYLINDER({"length": str(shape.length), "radius": str(shape.radius)})

    def createMaterial(self, material: IMaterial):
        return self.MATERIAL({"name": material.name})

    def createJoint(self, joint) -> ElementTree:

        # Used to add to the xml axis and limit if it makes sense for the joint
        switcher = {
            IFixedJoint.__name__: lambda: [],
            IRevoluteJoint.__name__: lambda: [
                self.createAxis(joint.rotationAxis),
                self.createLimit(joint.rotationAxis.limit),
            ],
        }

        return self.JOINT(
            {
                "name": joint.name,
                "type": Urdf2ToUrdf.URDF_JOINT_MAPPING[joint.URDF2type.urdf2Type],
            },
            *switcher[joint.URDF2type.urdf2Type](),
            self.createPose(joint.pose),
            self.JOINT_PARENT({"link": joint.parent.name}),
            self.JOINT_CHILD({"link": joint.child.name}),
        )

    def createAxis(self, axis: IAxis):
        x, y, z = axis.xyz
        return self.AXIS({"xyz": f"{x} {y} {z}"})

    def createLimit(self, limit: ILimit):
        return self.LIMIT(
            {
                "lower": f"{limit.lower:.3f}",
                "upper": f"{limit.upper:.3f}",
                "effort": f"{limit.effort:.3f}",
                "velocity": f"{limit.velocity:.3f}",
            }
        )
