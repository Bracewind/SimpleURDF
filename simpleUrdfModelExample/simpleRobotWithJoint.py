from simpleurdf.urdf2Metamodel import World, Robot, Link, Joint
from simpleurdf import JointType

link1 = Link(name="link1")
link2 = Link(name="link2")
link3 = Link(name="link3")

World(
    model=Robot(
        links=[link1, link2, link3, Link(name="link4")],
        joints=[
            Joint(
                name="joint1",
                jointType=JointType.JOINT_CONTINUOUS,
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
