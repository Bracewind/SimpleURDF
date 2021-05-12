import math
from simpleurdf.urdf2model.metamodel import DynamicsModel, PackageUri, XYZ
from simpleurdf.urdf2model.basemodel import FixedJointType
from simpleurdf.urdf2model import (
  MaterialColor,
  Link,
  Mesh,
  GeometryCylinder,
  Visual,
  Model,
  Joint,
  Pose,
)

from .leg import Leg

white = MaterialColor(name="white", ambient=[1, 1, 1, 1])
red = MaterialColor(name="red", ambient=[1, 0, 0, 1])

height_body_link = 110.0
depth_body_link = 290.0
width_body_link = 70.0


class Hopper(Model):
    def __init__(self):

        super().__init__(
          name="Hopper",
          root_link=Link(
            name="base_link",
            joints=[
              Joint(
                name="arrow_joint",
                joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                child=Link(
                  name="arrow",
                  visuals=[
                    Visual(
                      geometry=GeometryCylinder(length=0.2, radius=0.01),
                      material=red,
                      pose=Pose(xyz=[0.1, 0.0, 0.0], rpy=[0.0, math.pi / 2, 0]),
                    ),
                  ],
                ),
              ),
              Joint(
                name="base_joint",
                joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                child=Link(
                  name="body_link",
                  visuals=[
                    Visual(geometry=Mesh(
                      uri=PackageUri("urdf_tutorial", "meshes/hopper_body.dae"),
                      scale=XYZ(0.001, 0.001, 0.001),
                    ), ),
                  ],
                  joints=[
                    Joint(
                      name="body_laser_joint",
                      pose=Pose(xyz=[0.035, 0, 0.112], rpy=[0, 0, math.pi]),
                      joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                      child=Link(name="laser"),
                    ),
                    Joint(
                      name="body_imu_joint",
                      pose=Pose(xyz=[0.025, 0, 0], rpy=[math.pi, 0, math.pi]),
                      joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                      child=Link(name="imu"),
                    ),
                    Joint(
                      name="right_rear_leg_base_joint",
                      pose=Pose(xyz=[-0.115, -0.063, 0.0]),
                      joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                      child=(
                        Leg(
                          sideName="right",
                          positionName="rear",
                          angle=-math.pi / 2,
                          axis=1.0,
                        ),
                        0,
                      ),
                    ),
                    Joint(
                      name="right_middle_leg_base_joint",
                      pose=Pose(xyz=[0.0, 0.103, 0.0]),
                      joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                      child=(
                        Leg(
                          sideName="right",
                          positionName="middle",
                          angle=-math.pi / 2,
                          axis=1.0,
                        ),
                        0,
                      ),
                    ),
                    Joint(
                      name="right_front_leg_base_joint",
                      pose=Pose(xyz=[0.115, -0.063, 0.0]),
                      joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                      child=(
                        Leg(
                          sideName="right",
                          positionName="front",
                          angle=-math.pi / 2,
                          axis=1.0,
                        ),
                        0,
                      ),
                    ),
                    Joint(
                      name="left_rear_leg_base_joint",
                      pose=Pose(xyz=[-0.115, 0.063, 0.0]),
                      joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                      child=(
                        Leg(
                          sideName="left",
                          positionName="rear",
                          angle=math.pi / 2,
                          axis=-1.0,
                        ),
                        0,
                      ),
                    ),
                    Joint(
                      name="left_middle_leg_base_joint",
                      pose=Pose(xyz=[0.0, 0.103, 0.0]),
                      joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                      child=(
                        Leg(
                          sideName="left",
                          positionName="middle",
                          angle=math.pi / 2,
                          axis=-1.0,
                        ),
                        0,
                      ),
                    ),
                    Joint(
                      name="left_front_leg_base_joint",
                      pose=Pose(xyz=[0.115, 0.063, 0.0]),
                      joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                      child=(
                        Leg(
                          sideName="left",
                          positionName="front",
                          angle=math.pi / 2,
                          axis=-1.0,
                        ),
                        0,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        )
