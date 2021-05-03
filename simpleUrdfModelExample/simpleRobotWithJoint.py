from simpleurdf.urdf2model.basemodel import ContinuousJointType
from simpleurdf.urdf2model import World, Model, Link

link1 = Link(name="link1")
link2 = Link(name="link2")
link3 = Link(name="link3")

World(
    models=Model(
        name="testMultipleJoint",
        links=[link1, link2, link3, Link(name="link4")],
        joints=[
            Joint(
                name="joint1",
                jointType=ContinuousJointType(),
                parent=link1,
                child=link2,
            ),
            Joint(
                name="joint2",
                jointType=JointType.JOINT_CONTINUOUS,
                parent=link2,
                child=link3,
            ),
        ],
    )
)
