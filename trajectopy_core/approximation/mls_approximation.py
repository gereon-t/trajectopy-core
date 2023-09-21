"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

import logging
from dataclasses import dataclass
from functools import lru_cache
from typing import FrozenSet, List, Tuple, Union

import numpy as np

from trajectopy_core.approximation.voxelizer import Voxelizer

# logger configuration
logger = logging.getLogger("root")


@dataclass
class Line3D:
    """A 3D line defined by a mean point and a direction vector.

    Attributes:
        mean (np.ndarray): The mean point of the line.
        direction (np.ndarray): The direction vector of the line.
    """

    # rest of the class implementation
    mean: np.ndarray
    direction: np.ndarray

    @classmethod
    def from_points(cls, points: np.ndarray) -> "Line3D":
        """Create a 3D line from a set of points.

        This method calculates the direction vector of the line
        from the eigenvector corresponding to the largest eigenvalue
        of the covariance matrix of the input points. The mean of the
        points is used as the mean point of the line.

        Args:
            cls (Line3D): The class object.
            points (np.ndarray): The input points.

        Returns:
            Line3D: A 3D line defined by a mean point and a direction vector.
        """
        cov_matrix = np.cov(points, rowvar=False)
        direction = np.linalg.eigh(cov_matrix)[1][:, -1]

        # mean of the points
        mean = np.mean(points, axis=0)
        return cls(mean=mean, direction=direction)

    def evaluate_at(self, location: np.ndarray) -> List[float]:
        """Evaluates the 3D line at a given location.

        This method calculates the projection of the input location
        onto the 3D line and returns the resulting point.

        Args:
            location (np.ndarray): The input location.

        Returns:
            list[float]: The resulting point on the 3D line.
        """
        tr = (
            (location[0] - self.mean[0]) * self.direction[0]
            + (location[1] - self.mean[1]) * self.direction[1]
            + (location[2] - self.mean[2]) * self.direction[2]
        ) * self.direction
        return [self.mean[0] + tr[0], self.mean[1] + tr[1], self.mean[2] + tr[2]]


def mls_iterative(
    xyz: np.ndarray, voxel_size: float = 0.05, k_nearest: int = 4, movement_threshold: float = 0.005
) -> np.ndarray:
    """Performs the mls approximation iteratively

    This method approximates the neighborhood of a point
    using a 3d line. Neighborhoods are defined using voxels.
    The mls approximation is repeatetly applied to the result
    from the previous iteration until the average point movement
    falls below a user defined threshold (movement_threshold).

    Args:
        xyz (np.ndarray): Input points that should be approximated
        voxel_size (float): length of one voxel side
        k_nearest (int): number of voxels that define a neighborhood
        movement_threshold (float, optional): Threshold that defines
                                              when to stop iterating.
                                              When the average point
                                              movement is below of the
                                              pointsDefaults to 0.005.

    Returns:
        np.ndarray: Approximated positions
    """
    cnt = 1
    avg_point_movement = np.Inf
    while avg_point_movement > movement_threshold:
        logger.info("Iteration %i ... ", cnt)
        xyz, avg_point_movement = mls_single(xyz=xyz, voxel_size=voxel_size, k_nearest=k_nearest)
        cnt += 1
        logger.info("... done! Average point movement: %.4f m", avg_point_movement)
        if cnt > 10:
            logger.warning("Maximum number of iterations reached!")
            break
    return xyz


def mls_single(xyz: np.ndarray, voxel_size: float, k_nearest: int) -> Tuple[np.ndarray, float]:
    """Performs the mls approximation iteratively

    This method approximates the neighborhood of a point
    using a 3d line. Neighborhoods are defined using voxels.

    Args:
        xyz (np.ndarray): Input points that should be approximated
        voxel_size (float): length of one voxel side
        k_nearest (int): number of voxels that define a neighborhood

    Returns:
        Tuple[np.ndarray, float]: Approximated positions, average point movement
    """
    voxelizer = Voxelizer(xyz, voxel_size=voxel_size)
    neighboring_voxels = voxelizer.k_nearest_query(xyz, k_nearest=k_nearest)
    mls_approx = np.zeros(xyz.shape, dtype=float)
    for i, voxel_set in enumerate(neighboring_voxels):
        line = cached_line_approximator(voxelizer=voxelizer, voxel_set=voxel_set)
        mls_approx[i, :] = line.evaluate_at(xyz[i, :]) if line is not None else xyz[i, :]

    avg_point_movement = np.mean(np.sqrt(np.sum(np.power(xyz - mls_approx, 2), axis=1)))
    return mls_approx, avg_point_movement


@lru_cache(maxsize=None)
def cached_line_approximator(voxelizer: Voxelizer, voxel_set: FrozenSet[str]) -> Union[Line3D, None]:
    """
    Approximates a 3D line from a set of points and returns it as a Line3D object.
    If the set contains only one point, returns None.

    Args:
        voxelizer (Voxelizer): A Voxelizer object used to extract points from the voxel set.
        voxel_set (frozenset[str]): A set of voxel indices.

    Returns:
        Union[Line3D, None]: A Line3D object representing the 3D line approximated from the points in the voxel set,
        or None if the set contains only one point.
    """
    points = voxelizer.points_from_voxel_set(voxel_set)
    return Line3D.from_points(points) if len(points) > 1 else None
