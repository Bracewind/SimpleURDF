from urdf2 import World, Robot, Link

link1 = Link(name="link1")
link2 = Link(name="link2")


def model():
    return World(
        model=Robot(
            name="Robot1",
            links=[link1,
                   link2,
                   Link(name="link3"),
                   Link(name="link4")],
            joints=[]
        )
    )
