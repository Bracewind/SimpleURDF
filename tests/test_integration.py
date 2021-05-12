import pytest
import os

from .reference_model.robot_with_link_only import RobotWithLinkOnly
from simpleurdf import ModelIntegration


def test_ok2():
    print("hello")


def test_folder_created():
    robot = RobotWithLinkOnly().build_model()

    integration = ModelIntegration(robot)
    current_path = os.getcwd()
    path_to_ref_model_from_module = os.path.join(current_path, "tests", "package_generation")

    #integration.create_ros2_pkg(path_to_ref_model_from_module)
