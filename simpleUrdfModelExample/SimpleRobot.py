from simpleurdf.urdf2model import World, Model, Link

link1 = Link(name="link1")
link2 = Link(name="link2")


class model:
    return World(
        models=Model(
            name="Robot1",
            links=[link1, link2, Link(name="link3"), Link(name="link4")],
            joints=[],
        )
    )
