import math
from typing import List
from simpleurdf.urdf2model.metamodel import DynamicsModel, LimitModel, PackageUri, PrismaticJointTypeModel, XYZ
from simpleurdf.urdf2model.basemodel import FixedJointType, PrismaticJointType, RevoluteJointType
from simpleurdf.urdf2model import (
  Joint,
  Link,
  Mesh,
  Model,
  Pose,
  Visual,
  Limit,
)


class Farmbot(Model):
    def __init__(self, name: str, root_link: Link, linksInterface: List[Link], pose):
        super().__init__(
          name="Farmbot",
          root_link=Link(
            name="base_link",
            joints=[
              Joint(
                name="base_joint",
                joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                child=Link(
                  name="raised_bed",
                  joints=[
                    Joint(
                      name="joint_raisedbed_tracks",
                      joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                      child=Link(
                        name="Tracks",
                        joints=[
                          Joint(
                            name="joint_tracks_gantry",
                            joint_type_characteristics=PrismaticJointType(translation_axis=XYZ(
                              1, 0, 0), ),
                            child=Link(
                              name="gantry",
                              joints=[
                                Joint(
                                  name="joint_gantry_crossslide",
                                  joint_type_characteristics=PrismaticJointType(XYZ(0, 1, 0)),
                                  child=Link(
                                    name="cross_slide",
                                    joints=[
                                      Joint(
                                        name="joint_crossslide_zaxis",
                                        joint_type_characteristics=PrismaticJointType(
                                          translation_axis=XYZ(0, 0, 1), ),
                                        child=Link("z_axis"),
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
