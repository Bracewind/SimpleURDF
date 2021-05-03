import math
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

base_link = Link(name="base_link")
body_link = Link(
    name="body_link",
    visuals=[
        Visual(
            geometry=Mesh(
                uri="package://urdf_tutorial/meshes/hopper_body.dae",
                scale=[0.001, 0.001, 0.001],
            )
        ),
    ],
)
arrow = Link(
    name="arrow",
    visuals=[
        Visual(
            geometry=GeometryCylinder(length=0.2, radius=0.01),
            material=red,
            pose=Pose(xyz=[0.1, 0.0, 0.0], rpy=[0.0, math.pi / 2, 0]),
        )
    ],
)

imu = Link(name="imu")

laser = Link(name="laser")

pose_right_rear = Pose(xyz=[-0.115, -0.063, 0.0])
right_rear = Leg(
    sideName="right",
    positionName="rear",
    angle=-math.pi / 2,
    axis=1.0,
)
pose_right_middle = Pose(xyz=[0.0, 0.103, 0.0])
right_middle = Leg(
    sideName="right",
    positionName="middle",
    angle=-math.pi / 2,
    axis=1.0,
)
pose_right_front = Pose(xyz=[0.115, -0.063, 0.0])
right_front = Leg(
    sideName="right",
    positionName="front",
    angle=-math.pi / 2,
    axis=1.0,
)
pose_left_rear = Pose(xyz=[-0.115, 0.063, 0.0])
left_rear = Leg(
    sideName="left",
    positionName="rear",
    angle=math.pi / 2,
    axis=-1.0,
)
pose_left_middle = Pose(xyz=[0.0, 0.103, 0.0])
left_middle = Leg(sideName="left", positionName="middle", angle=math.pi / 2, axis=-1.0)
pose_left_front = Pose(xyz=[0.115, 0.063, 0.0])
left_front = Leg(
    sideName="left",
    positionName="front",
    angle=math.pi / 2,
    axis=-1.0,
)


def model():
    return Model(
        name="Hopper",
        links=[base_link, body_link, arrow, laser, imu],
        nestedModels=[
            right_rear,
            right_middle,
            right_front,
            left_rear,
            left_middle,
            left_front,
        ],
        joints=[
            Joint(
                name="base_joint",
                parent=base_link,
                child=body_link,
                jointTypeCharacteristics=FixedJointType(),
            ),
            Joint(
                name="arrow_joint",
                parent=base_link,
                child=arrow,
                jointTypeCharacteristics=FixedJointType(),
            ),
            Joint(
                name="body_laser_joint",
                parent=body_link,
                child=laser,
                pose=Pose(xyz=[0.035, 0, 0.112], rpy=[0, 0, math.pi]),
                jointTypeCharacteristics=FixedJointType(),
            ),
            Joint(
                name="body_imu_joint",
                parent=body_link,
                child=imu,
                pose=Pose(xyz=[0.025, 0, 0], rpy=[math.pi, 0, math.pi]),
                jointTypeCharacteristics=FixedJointType(),
            ),
            Joint(
                name="right_rear_leg_base_joint",
                parent=body_link,
                child=right_rear.getBaseLink(),
                pose=pose_right_rear,
                jointTypeCharacteristics=FixedJointType(),
            ),
            Joint(
                name="right_middle_leg_base_joint",
                parent=body_link,
                child=right_middle.getBaseLink(),
                pose=pose_right_middle,
                jointTypeCharacteristics=FixedJointType(),
            ),
            Joint(
                name="right_front_leg_base_joint",
                parent=body_link,
                child=right_front.getBaseLink(),
                pose=pose_right_front,
                jointTypeCharacteristics=FixedJointType(),
            ),
            Joint(
                name="left_rear_leg_base_joint",
                parent=body_link,
                child=left_rear.getBaseLink(),
                pose=pose_left_rear,
                jointTypeCharacteristics=FixedJointType(),
            ),
            Joint(
                name="left_middle_leg_base_joint",
                parent=body_link,
                child=left_middle.getBaseLink(),
                pose=pose_left_middle,
                jointTypeCharacteristics=FixedJointType(),
            ),
            Joint(
                name="left_front_leg_base_joint",
                parent=body_link,
                child=left_front.getBaseLink(),
                pose=pose_left_front,
                jointTypeCharacteristics=FixedJointType(),
            ),
        ],
    )
