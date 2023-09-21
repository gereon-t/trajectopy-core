"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import numpy as np

from trajectopy_core.alignment.parameters import Parameter, SensorRotationParameters
from trajectopy_core.util.definitions import Unit
from trajectopy_core.util.rotationset import RotationSet


def align_rotations(rot_from: RotationSet, rot_to: RotationSet) -> SensorRotationParameters:
    """Aligns the rotations of two trajectories"""

    if rot_to is None or rot_from is None:
        return RotationSet.from_quat(np.array([0, 0, 0, 1]))

    rot_difference = (rot_to - rot_from).mean()
    rpy_diff = rot_difference.as_euler(seq="xyz")
    return SensorRotationParameters(
        sensor_rot_x=Parameter(name="Rotation x", value=rpy_diff[0], enabled=True, unit=Unit.RADIAN),
        sensor_rot_y=Parameter(name="Rotation y", value=rpy_diff[1], enabled=True, unit=Unit.RADIAN),
        sensor_rot_z=Parameter(name="Rotation z", value=rpy_diff[2], enabled=True, unit=Unit.RADIAN),
    )
