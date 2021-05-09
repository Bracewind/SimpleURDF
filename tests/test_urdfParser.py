import os
from simpleUrdfModelExample.hopper.hopper import Hopper
from simpleurdf.urdf2model.metamodel import ModelModel
from tests.reference_model.robot_with_geometry_form import RobotWithGeometryForm
from tests.reference_model.robot_with_one_fixed_joint import RobotWithOneFixedJoint
from tests.reference_model.robot_with_link_only import RobotWithLinkOnly
from tests.reference_model.robot_with_one_revolute_joint import (
  RobotWithOneRevoluteJoint, )
from tests.reference_model.robot_with_geometry_form import RobotWithGeometryForm
from tests.reference_model.model_in_model import ModelInModel
import pytest

#from simpleUrdfModelExample import RRbot

from simpleurdf.urdf2model import Model, Joint, Link
from simpleurdf import UrdfParser

from simpleUrdfModelExample import RRbot

from lxml import etree

from simpleurdf.urdfParser import urdf

#from simpleUrdfModelExample.hopper.hopper import model


def test_ok():
    value = 2
    assert value == 2, "Found errors"


@pytest.mark.parametrize(
  "robot_in_python, filename_containing_urdf_model",
  [
    (RobotWithLinkOnly().build_model(), "robot_with_link_only.urdf"),
    (RobotWithOneFixedJoint().build_model(), "robot_with_one_fixed_joint.urdf"),
    (
      RobotWithOneRevoluteJoint().build_model(),
      "robot_with_one_revolute_joint.urdf",
    ),
    (RobotWithGeometryForm().build_model(), "robot_with_geometry_form.urdf"),
    (RRbot(), "rrbot.urdf"),
    (ModelInModel().build_model(), "model_in_model.urdf"),
    (Hopper(), "hopper.urdf"),
  ],
)
def test_with_ref_file(robot_in_python: Model, filename_containing_urdf_model):
    """robot_in_python contains the robot representation in python,
    filename_containing_urdf_model is the file containing the representation of the robot in urdf"""

    parser = UrdfParser()
    urdfRepr = parser.createURDFString(robot_in_python)

    current_path = os.getcwd()
    path_to_ref_model_from_module = os.path.join(current_path, "tests", "reference_model")

    complete_path = os.path.join(path_to_ref_model_from_module, filename_containing_urdf_model)
    with open(complete_path, "r") as f:
        urdf_robot_repr = etree.parse(f)
        urdf_robot_linted = etree.tostring(urdf_robot_repr, pretty_print=True, encoding=str)
        assert urdf_robot_linted == urdfRepr


@pytest.mark.parametrize(
  "model, filename_for_model",
  [
    (RobotWithLinkOnly().build_model(), "robot_with_link_only.urdf"),
    (RobotWithOneFixedJoint().build_model(), "robot_with_one_fixed_joint.urdf"),
    (
      RobotWithOneRevoluteJoint().build_model(),
      "robot_with_one_revolute_joint.urdf",
    ),
    (RobotWithGeometryForm().build_model(), "robot_with_geometry_form.urdf"),
    (RRbot(), "rrbot.urdf"),
    (ModelInModel().build_model(), "model_in_model.urdf"),
    (Hopper(), "hopper.urdf"),
  ],
)
def test_create_file(model, filename_for_model):
    broker = UrdfParser()
    path = os.getcwd()
    pathToFile = os.path.join(path, "tests", "model_generated", filename_for_model)
    broker.createURDFFile(model, pathToFile)
