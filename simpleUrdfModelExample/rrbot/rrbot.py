from math import pi
from simpleurdf.urdf2model.basemodel import (
    ContinuousJointType,
    Dynamics,
    FixedJointType,
    Mesh,
    Model,
)
from simpleurdf.urdf2model import Pose, Joint, MaterialColor, Visual

from simpleurdf.urdf2model import Link, Box, IModel


class RRbot(Model):
    def __init__(self):
        # materials
        orange = MaterialColor("orange")
        black = MaterialColor("black")
        red = MaterialColor("red")

        mass = 1

        # Square dimensions (width x width) of beams
        width = 0.1

        height1 = 2.0  # Link1
        height2 = 1.0  # Link2
        height3 = 1.0  # Link3
        camera_link = 0.05  # Size of square 'camera' box
        axel_offset = 0.05  # Space btw top of beam and the each joint

        world = Link(name="world")
        link1 = Box(
            name="link1",
            material=orange,
            width=width,
            depth=width,
            height=height1,
            mass=mass,
            pose=Pose(xyz=[0, 0, height1 / 2]),
        )
        link2 = Box(
            name="link2",
            material=black,
            width=width,
            depth=width,
            height=height2,
            mass=mass,
            pose=Pose(xyz=[0, 0, height2 / 2 - axel_offset]),
        )
        link3 = Box(
            name="link3",
            material=orange,
            width=width,
            depth=width,
            height=height3,
            mass=mass,
            pose=Pose(xyz=[0, 0, height3 / 2 - axel_offset]),
        )

        # link not used in model
        ref_box_for_hokuyo = Box(
            name="void_link", material=red, width=0.1, depth=0.1, height=0.1, mass=1e-5
        )
        hokuyo_link = Link(
            name="hokuyo_link",
            collision=ref_box_for_hokuyo.collision,
            visuals=[
                Visual(geometry=Mesh("package://rrbot_description/meshes/hokuyo.dae"))
            ],
            inertial=ref_box_for_hokuyo.inertial,
        )

        camera_link = Box(
            name="camera_link",
            material=red,
            width=camera_link,
            depth=camera_link,
            height=camera_link,
            mass=1e-5,
        )
        camera_link_optical = Link("camera_link_optical")

        super().__init__(
            name="rrbot",
            links=[
                world,
                link1,
                link2,
                link3,
                hokuyo_link,
                camera_link,
                camera_link_optical,
            ],
            joints=[
                Joint(
                    name="fixed",
                    parent=world,
                    child=link1,
                    jointTypeCharacteristics=FixedJointType(),
                ),
                Joint(
                    name="joint1",
                    parent=link1,
                    child=link2,
                    pose=Pose(xyz=[0, width, height1 - axel_offset]),
                    jointTypeCharacteristics=ContinuousJointType(
                        [0, 1, 0], jointPhysic=Dynamics(0.7)
                    ),
                ),
                Joint(
                    name="joint2",
                    parent=link2,
                    child=link3,
                    pose=Pose(xyz=[0, width, height2 - 2 * axel_offset]),
                    jointTypeCharacteristics=ContinuousJointType(
                        [0.0, 1.0, 0.0], jointPhysic=Dynamics(0.7)
                    ),
                ),
                Joint(
                    name="hokuyo_joint",
                    parent=link3,
                    child=hokuyo_link,
                    jointTypeCharacteristics=FixedJointType(),
                    pose=Pose(xyz=[0.0, 0.0, height3 - axel_offset / 2.0]),
                ),
                Joint(
                    name="camera_joint",
                    parent=link3,
                    child=camera_link,
                    jointTypeCharacteristics=FixedJointType(),
                    pose=Pose(xyz=[camera_link, 0.0, height3 - 2 * axel_offset]),
                ),
                Joint(
                    name="camera_optical_joint",
                    parent=camera_link,
                    child=camera_link_optical,
                    pose=Pose(rpy=[-pi / 2, 0, -pi / 2]),
                    jointTypeCharacteristics=FixedJointType(),
                ),
            ],
        )
