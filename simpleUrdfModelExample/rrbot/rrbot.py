from math import pi
from simpleurdf.urdf2model.metamodel import DynamicsModel, PackageUri, XYZ
from simpleurdf.urdf2model.basemodel import (
  Collision,
  ContinuousJointType,
  Dynamics,
  FixedJointType,
  GeometryBox,
  InertialBox,
  Mesh,
  Model,
)
from simpleurdf.urdf2model import Pose, Joint, MaterialColor, Visual

from simpleurdf.urdf2model import Link, Box


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

        super().__init__(
          name="rrbot",
          root_link=Link(
            name="world",
            joints=[
              Joint(
                name="fixed",
                joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                child=Box(
                  name="link1",
                  material=orange,
                  width=width,
                  depth=width,
                  height=height1,
                  mass=mass,
                  pose=Pose(xyz=[
                    0,
                    0,
                    height1 / 2,
                  ], ),
                  joints=[
                    Joint(
                      name="joint1",
                      pose=Pose(xyz=[0, width, height1 - axel_offset]),
                      joint_type_characteristics=ContinuousJointType(
                        XYZ(0, 1, 0),
                        joint_physic=Dynamics(0.7),
                      ),
                      child=Box(
                        name="link2",
                        material=black,
                        width=width,
                        depth=width,
                        height=height2,
                        mass=mass,
                        pose=Pose(xyz=[0, 0, height2 / 2 - axel_offset]),
                        joints=[
                          Joint(
                            name="joint2",
                            pose=Pose(xyz=[0, width, height2 - 2 * axel_offset]),
                            joint_type_characteristics=ContinuousJointType(
                              XYZ(0.0, 1.0, 0.0),
                              joint_physic=Dynamics(0.7),
                            ),
                            child=Box(
                              name="link3",
                              material=orange,
                              width=width,
                              depth=width,
                              height=height3,
                              mass=mass,
                              pose=Pose(xyz=[
                                0,
                                0,
                                height3 / 2 - axel_offset,
                              ], ),
                              joints=[
                                Joint(
                                  name="hokuyo_joint",
                                  joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                                  pose=Pose(xyz=[
                                    0.0,
                                    0.0,
                                    height3 - axel_offset / 2.0,
                                  ], ),
                                  child=Link(
                                    name="hokuyo_link",
                                    collision=Collision(GeometryBox(XYZ(
                                      0.1,
                                      0.1,
                                      0.1,
                                    ), ), ),
                                    visuals=[
                                      Visual(geometry=Mesh(uri=PackageUri(
                                        "rrbot_description",
                                        "meshes/hokuyo.dae",
                                      ), ), ),
                                    ],
                                    inertial=InertialBox(XYZ(0.1, 0.1, 0.1), mass=1e-5),
                                  ),
                                ),
                                Joint(
                                  name="camera_joint",
                                  joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                                  pose=Pose(xyz=[camera_link, 0, height3 - 2 * axel_offset]),
                                  child=Box(
                                    name="camera_link",
                                    material=red,
                                    width=camera_link,
                                    depth=camera_link,
                                    height=camera_link,
                                    mass=1e-5,
                                    joints=[
                                      Joint(
                                        name="camera_optical_joint",
                                        pose=Pose(rpy=[-pi / 2, 0, -pi / 2]),
                                        joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                                        child=Link("camera_link_optical"),
                                      ),
                                    ],
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        )
