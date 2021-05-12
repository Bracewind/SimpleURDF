import math
from typing import List
from simpleurdf.urdf2model.metamodel import DynamicsModel, LimitModel, PackageUri, PrismaticJointTypeModel, XYZ
from simpleurdf.urdf2model.basemodel import (FixedJointType,
                                             PrismaticJointType,
                                             RevoluteJointType,
                                             Collision)
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
    def __init__(self):
        name_package = "urdf_tutorial"

        height_raised_bed = 0.15
        length_raised_bed = 3
        width_raised_bed = 1.5
        y_tracks_deviation = -0.19

        height_gantry = 0.6

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
                  visuals=[Visual(Mesh(PackageUri(name_package, "meshes/raised_bed.dae")))],
                  joints=[
                    Joint(
                      name="joint_raisedbed_tracks",
                      pose=Pose(rpy=[0, 0, math.pi / 2],
                                xyz=XYZ(width_raised_bed / 2, y_tracks_deviation,
                                        height_raised_bed)),
                      joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                      child=Link(
                        name="Tracks",
                        visuals=[Visual(Mesh(PackageUri(name_package, "meshes/tracks.dae")))],
                        joints=[
                          Joint(
                            name="joint_tracks_gantry",
                            pose=Pose(rpy=[0, 0, math.pi / 2],
                                      xyz=XYZ(-length_raised_bed / 2 - y_tracks_deviation,
                                              0,
                                              height_raised_bed)),
                            joint_type_characteristics=PrismaticJointType(translation_axis=XYZ(
                              1, 0, 0), ),
                            child=Link(
                              name="gantry",
                              visuals=[
                                Visual(geometry=Mesh(PackageUri(name_package, "meshes/gantry.dae")),
                                       pose=Pose(rpy=[0, 0, 0],
                                                 xyz=XYZ(width_raised_bed / 2, 0, height_gantry)))
                              ],
                              joints=[
                                Joint(
                                  name="joint_gantry_crossslide",
                                  joint_type_characteristics=PrismaticJointType(XYZ(1, 0, 0)),
                                  pose=Pose(
                                    rpy=[0, 0, 0],
                                    xyz=XYZ(0, 0, height_gantry),
                                  ),
                                  child=Link(
                                    name="cross_slide",
                                    visuals=[
                                      Visual(
                                        Mesh(PackageUri(name_package, "meshes/cross_slide.dae")))
                                    ],
                                    joints=[
                                      Joint(
                                        name="joint_crossslide_zaxis",
                                        joint_type_characteristics=PrismaticJointType(
                                          translation_axis=XYZ(0, 0, 1), ),
                                        child=Link(
                                          "z_axis",
                                          visuals=[
                                            Visual(
                                              Mesh(PackageUri(name_package, "meshes/z_axis.dae")))
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
              ),
            ],
          ),
        )
