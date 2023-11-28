"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from dataclasses import dataclass
from typing import List, Tuple, Union

import numpy as np

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


def lengths_from_xyz(xyz: np.ndarray) -> np.ndarray:
    """
    Computes the cumulative distance along a path defined by a sequence of
    3D points.

    Args:
        xyz (np.ndarray): An array of shape (n, 3) containing the x, y, and z
            coordinates of the path.

    Returns:
        np.ndarray: An array of shape (n,) containing the cumulative distance
            along the path.
    """
    if not isinstance(xyz, np.ndarray):
        logger.error("Invalid data type %s", type(xyz))
        return np.array([])

    xyz_1 = xyz[0:-1, :]
    xyz_2 = xyz[1:, :]

    diff = xyz_2 - xyz_1

    dists = np.linalg.norm(diff, axis=1)
    return np.r_[0, np.cumsum(dists)]


def gradient_3d(xyz: np.ndarray, tstamps: np.ndarray) -> np.ndarray:
    """
    Computes the gradient of a 3D trajectory.

    Args:
        xyz (np.ndarray): Positions of the trajectory [nx3].
        tstamps (np.ndarray): Timestamps of the trajectory [nx1].

    Returns:
        np.ndarray: Gradient of the trajectory [nx3].
    """
    # gradient (use target positions for this as they are probably more precise)
    diff = xyz[1:, :] - xyz[0:-1, :]
    t_diff = tstamps[1:] - tstamps[:-1]

    # no gradient for last position
    return np.r_[diff / t_diff[:, None], np.zeros((1, 3))]


def common_time_span(tstamps1: np.ndarray, tstamps2: np.ndarray) -> Union[Tuple[float, float], None]:
    """
    Computes the common time span between two arrays of timestamps.

    Args:
        tstamps1 (np.ndarray): First array of timestamps.
        tstamps2 (np.ndarray): Second array of timestamps.

    Returns:
        Union[Tuple[float, float], None]: A tuple containing the start and end times of the common time span,
        or None if there is no overlap between the two arrays.
    """
    tstamps1 = np.sort(tstamps1)
    tstamps2 = np.sort(tstamps2)

    overlap = (
        tstamps1[0] <= tstamps2[0] <= tstamps1[-1]
        or tstamps1[0] <= tstamps2[-1] <= tstamps1[-1]
        or tstamps2[0] <= tstamps1[0] <= tstamps2[-1]
        or tstamps2[0] <= tstamps1[-1] <= tstamps2[-1]
    )
    if not overlap:
        return None

    # get limits (largest common time span)
    t_start = max(tstamps1[0], tstamps2[0])
    t_end = min(tstamps1[-1], tstamps2[-1])

    return (t_start, t_end)
