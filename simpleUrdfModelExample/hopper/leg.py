import math
from simpleurdf.urdf2model.metamodel import DynamicsModel, PackageUri, XYZ
from simpleurdf.urdf2model.basemodel import FixedJointType, RevoluteJointType
from simpleurdf.urdf2model import (
  Joint,
  Link,
  Mesh,
  Model,
  Pose,
  Visual,
  Limit,
)

coxa_length = 0.044
femur_length = 0.07
tibia_length = 0.128


class Leg(Model):
    def __init__(self, sideName: str, positionName: str, angle, axis: float):
        self._name = f"{sideName}_{positionName}"

        super().__init__(
          self._name,
          root_link=Link(
            name=f"{sideName}_{positionName}_leg_base",
            joints=[
              Joint(
                name=f"{sideName}_{positionName}_coxa_joint",
                pose=Pose(rpy=[0.0, 0.0, angle]),
                joint_type_characteristics=RevoluteJointType(
                  rotation_axis=XYZ(0.0, 0.0, 1.0),
                  limit=Limit(lower=-math.pi, upper=math.pi, effort=1000.0, velocity=1),
                ),
                child=Link(
                  name=f"{sideName}_{positionName}_coxa",
                  visuals=[
                    Visual(geometry=Mesh(
                      uri=PackageUri("urdf_tutorial", "meshes/hopper_leg_coxa.dae"),
                      scale=XYZ(0.001, 0.001, 0.001),
                    ), ),
                  ],
                  joints=[
                    Joint(
                      name=f"{sideName}_{positionName}_femur_joint",
                      pose=Pose(
                        xyz=[coxa_length, 0.0, 0.0],
                        rpy=[-math.pi / 2, math.pi / 2, 0.0],
                      ),
                      joint_type_characteristics=RevoluteJointType(
                        rotation_axis=XYZ(0.0, 0.0, -axis),
                        limit=Limit(
                          lower=-math.pi,
                          upper=math.pi,
                          effort=1000.0,
                          velocity=1,
                        ),
                      ),
                      child=Link(
                        name=f"{sideName}_{positionName}_femur",
                        visuals=[
                          Visual(geometry=Mesh(
                            uri=PackageUri("urdf_tutorial", "meshes/hopper_leg_femur.dae"),
                            scale=XYZ(0.001, 0.001, 0.001),
                          ), ),
                        ],
                        joints=[
                          Joint(
                            name=f"{sideName}_{positionName}_tibia_joint",
                            pose=Pose(
                              xyz=[0.0, -femur_length, 0.0],
                              rpy=[math.pi, 0.0, 0.0],
                            ),
                            joint_type_characteristics=RevoluteJointType(
                              rotation_axis=XYZ(0.0, 0.0, axis),
                              limit=Limit(
                                lower=-math.pi,
                                upper=math.pi,
                                effort=1000.0,
                                velocity=1,
                              ),
                            ),
                            child=Link(
                              name=f"{sideName}_{positionName}_tibia",
                              visuals=[
                                Visual(geometry=Mesh(
                                  uri=PackageUri("urdf_tutorial", "meshes/hopper_leg_tibia.dae"),
                                  scale=XYZ(0.001, 0.001, 0.001),
                                ), ),
                              ],
                              joints=[
                                Joint(
                                  name=f"{sideName}_{positionName}_tibia_button",
                                  pose=Pose(xyz=[tibia_length, 0.0, 0.0]),
                                  joint_type_characteristics=FixedJointType(DynamicsModel(1)),
                                  child=Link(name=f"{sideName}_{positionName}_button"),
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
