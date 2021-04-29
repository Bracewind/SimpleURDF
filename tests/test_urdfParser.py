import os

from simpleurdf.urdf2Metamodel import Model, Joint, Link
from simpleurdf import UrdfParser

from simpleUrdfModelExample.hopper.hopper import model


def test_ok():
    value = 2
    assert value == 2, "Found errors"


def test_robot_with_name_only():
    broker = UrdfParser()

    robot_with_name_only = Model(name="hello")
    robot_urdf = broker.createURDFString(robot_with_name_only)
    resultExpected = b'<robot name="hello"/>\n'
    assert (
        robot_urdf == resultExpected
    ), f"robot name test not passed, found {robot_urdf}, should be {resultExpected}"

    robot_with_name_only2 = Model(name="test_robot")
    robot_urdf2 = broker.createURDFString(robot_with_name_only2)
    resultExpected2 = b'<robot name="test_robot"/>\n'
    assert (
        robot_urdf2 == resultExpected2
    ), f"robot name test not passed, found {robot_urdf2}, should be {resultExpected2}"


def test_robot_with_only_link():
    broker = UrdfParser()

    robot_one_link = Model(name="one_link", links=[Link(name="link1")])
    robot_urdf = broker.createURDFString(robot_one_link)
    resultExpected = b'<robot name="one_link">\n  <link name="link1"/>\n</robot>\n'
    assert (
        robot_urdf == resultExpected
    ), f"robot name test not passed, found {robot_urdf}, should be {resultExpected}"

    robot_multiple_links = Model(
        name="multiple_links", links=[Link(name="link1"), Link(name="link2")]
    )
    robot_urdf = broker.createURDFString(robot_multiple_links)
    print(robot_urdf)
    resultExpected = b'<robot name="multiple_links">\n  <link name="link1"/>\n  <link name="link2"/>\n</robot>\n'
    assert (
        robot_urdf == resultExpected
    ), f"robot name test not passed, found {robot_urdf}, should be {resultExpected}"


def test_real_file():
    broker = UrdfParser()
    model2 = model()
    robot_urdf = broker.createURDFString(model2)
    print(robot_urdf)


def test_create_file():
    broker = UrdfParser()
    model2 = model()
    path = os.getcwd()
    pathToFile = os.path.join(path, "tests/model_generated/hexapod_gene.urdf")
    broker.createURDFFile(model2, pathToFile)
