"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import numpy as np

from trajectopy_core.alignment.parameters import HelmertTransformation, Parameter
from trajectopy_core.util.definitions import Unit
from trajectopy_core.util.rotationset import RotationSet


def direct_helmert_transformation(
    xyz_from: np.ndarray, xyz_to: np.ndarray, weights: np.ndarray = np.zeros(0)
) -> HelmertTransformation:
    """
    Computes helmert transformation between two point sets

    Foerstner-Wrobel (2016) Photogrammetric Computer Vision pp. 406 - 411
    """
    if len(weights) == 0:
        weights = np.ones((len(xyz_from),))

    sum_of_weights = np.sum(weights)
    weighted_centroid_from = np.sum(xyz_from * weights[:, None], axis=0) / sum_of_weights

    weighted_centroid_to = np.sum(xyz_to * weights[:, None], axis=0) / sum_of_weights

    centered_from = xyz_from - weighted_centroid_from
    centered_to = xyz_to - weighted_centroid_to

    moment_matrix = weights * centered_from.T @ centered_to

    distances_from = np.linalg.norm(centered_from, axis=1)
    weighted_sum_of_squared_distances_from = (weights * distances_from) @ distances_from

    u, _, v = np.linalg.svd(moment_matrix, full_matrices=True)

    estimated_rotation = v.T @ u.T
    estimated_scale = (
        np.sum(weights[:, None] * centered_to @ estimated_rotation * centered_from)
        / weighted_sum_of_squared_distances_from
    )
    estimated_translation = weighted_centroid_to - estimated_scale * estimated_rotation @ weighted_centroid_from

    estimated_rotation_angles = RotationSet.from_matrix(estimated_rotation).as_euler(seq="xyz")
    return HelmertTransformation(
        trans_x=Parameter(value=estimated_translation[0], name="Translation x", unit=Unit.METER),
        trans_y=Parameter(value=estimated_translation[1], name="Translation y", unit=Unit.METER),
        trans_z=Parameter(value=estimated_translation[2], name="Translation z", unit=Unit.METER),
        rot_x=Parameter(value=estimated_rotation_angles[0], name="Rotation x", unit=Unit.RADIAN),
        rot_y=Parameter(value=estimated_rotation_angles[1], name="Rotation y", unit=Unit.RADIAN),
        rot_z=Parameter(value=estimated_rotation_angles[2], name="Rotation z", unit=Unit.RADIAN),
        scale=Parameter(value=estimated_scale, default=1.0, name="Scale", unit=Unit.SCALE),
    )
