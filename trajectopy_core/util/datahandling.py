"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from dataclasses import dataclass
from typing import Any, Callable, Dict, Tuple, Union

import numpy as np
import pandas as pd

from trajectopy_core.approximation.util import skew_symmetric_matrix

# logger configuration
logger = logging.getLogger("root")


@dataclass
class Grid:
    """
    A class representing a 2D grid of values, with methods for accessing and manipulating the grid.

    Attributes:
        full_grid (np.ndarray): The full 2D grid of values.
        x_bin_locations (list[int]): The x-coordinates of the grid cells.
        y_bin_locations (list[int]): The y-coordinates of the grid cells.
        pixel_size (float): The size of each pixel in the grid.

    Methods:
        values() -> np.ndarray:
            Returns the values of the grid cells.
        populated_grid_cells() -> np.ndarray:
            Returns the x and y coordinates and values of the populated grid cells.
        scaled_grid_cells() -> np.ndarray:
            Returns the x and y coordinates and values of the populated grid cells, scaled by the pixel size.
    """

    full_grid: np.ndarray
    x_bin_locations: np.ndarray
    y_bin_locations: np.ndarray
    pixel_size: float

    @property
    def values(self) -> np.ndarray:
        return self.full_grid[self.x_bin_locations, self.y_bin_locations]

    @property
    def populated_grid_cells(self) -> np.ndarray:
        return np.c_[self.x_bin_locations, self.y_bin_locations, self.values]

    @property
    def scaled_grid_cells(self) -> np.ndarray:
        return np.c_[
            self.x_bin_locations * self.pixel_size,
            self.y_bin_locations * self.pixel_size,
            self.values,
        ]


def rms(x: Union[np.ndarray, float]) -> float:
    """
    Calculates the root mean square of an array.

    Args:
        x (np.ndarray): The input array.

    Returns:
        float: The root mean square of the input array.
    """
    return np.sqrt(np.mean(np.square(x)))


def merge_dicts(dicts: Tuple[Dict[str, str], ...]):
    """
    Merges multiple dictionaries into a single dictionary, where each key in the merged dictionary
    corresponds to a list of values from each input dictionary.

    Args:
        dicts (Tuple[dict]): A tuple of dictionaries to be merged.

    Returns:
        dict: A dictionary containing the merged key-value pairs.
    """
    merged_dict: Dict[Any, Any] = {}
    for i, d in enumerate(dicts):
        for k, v in d.items():
            if k not in merged_dict:
                merged_dict[k] = ["-"] * len(dicts)
            merged_dict[k][i] = v
    return merged_dict


def get_rot_matrix(nframe: str) -> np.ndarray:
    """Returns rotation matrix to transform rotations to ENU

    Args:
        nframe (str): String defining the current nframe definition.
                      e.g. "ned". This string must contain "e", "n",
                      and either "d" OR "u"

    Returns:
        np.ndarray: Rotation Matrix
    """
    nframe = nframe.lower()

    if "e" not in nframe or "n" not in nframe or "u" not in nframe and "d" not in nframe:
        raise ValueError("Invalid input: The input string must contain at least 'e', 'n', and either 'u' or 'd'")

    sign_flipped = "d" in nframe
    nframe = nframe.replace("d", "u")
    rot_matrix = np.zeros((3, 3))

    for i, char in enumerate(nframe):
        index = "enu".find(char)
        value = -1 if char == "u" and sign_flipped else 1
        rot_matrix[i, index] = value

    return rot_matrix


def moving(*, x: np.ndarray, win_size: int, function: Callable[[np.ndarray], float]) -> np.ndarray:
    """
    Computes values with a given window size and function.
    For example, if function=np.std this method computes the moving
    standard deviation.

    Args:
        x (np.ndarray): The input array.
        win_size (int): The size of the window.
        function (Callable[[np.ndarray], float]): The function to apply to the window.

    Returns:
        np.ndarray: An array containing the computed values.
    """
    if not callable(function):
        raise TypeError("'function' must be Callable[[np.ndarray], float]")

    if win_size in {1, 0, -1}:
        return x

    ext = int(win_size // 2)

    # extend array
    x_ext = np.pad(x, pad_width=(ext, ext + 1), mode="wrap")

    # moving
    mov = [function(x_ext[i - ext : i + ext + 1]) for i in range(ext, len(x_ext) - ext - 1)]

    return np.array(mov)


def moving_width(
    *,
    t: np.ndarray,
    data: np.ndarray,
    width: float,
    function: Callable[[np.ndarray], float],
) -> np.ndarray:
    """
    Computes values with a given width and function.
    For example, if function=np.std this method computes the moving
    standard deviation.

    Args:
        t (np.ndarray): The time array.
        data (np.ndarray): The input array.
        width (float): The width of the window.
        function (Callable[[np.ndarray], float]): The function to apply to the window.

    Returns:
        np.ndarray: An array containing the computed values.
    """
    if width in {0.0, -1.0}:
        return data

    win_size_n = rndodd(len(data) / len(np.unique(np.round(t / width))))
    return np.array(moving(x=data, win_size=win_size_n, function=function))


def round_to_precision(
    function_of: np.ndarray, data: np.ndarray, resolution: float, filter_size: int = 100
) -> Tuple[np.ndarray, np.ndarray]:
    """Reduces the amount of deviations using smoothing and rounding

    It will first smooth the data using a convolution with a filter
    of size filter_size. Then, the data is rounded to the specified
    resolution and duplicate values that can result from this operation
    are deleted.

    Args:
        function_of (np.ndarray): nxm array that contains for example
                                  time stamps, arc lengths or positions
                                  corresponding to the data.
        data (np.ndarray): nx1 array that contains the data that should
                           be smoothed.
        precision (float): Desired resolution
        filter_size (int): Window / filter size for smoothing

    Returns:
        downsampled function_of and data
    """
    data_smoothed = np.convolve(data, [1 / filter_size] * filter_size, "same")
    data_rounded = np.round(data_smoothed / resolution) * resolution
    _, indices = np.unique(np.c_[function_of, data_rounded], return_index=True, axis=0)
    indices_sorted = np.sort(indices)

    function_of_unique = function_of[indices_sorted, :] if function_of.ndim > 1 else function_of[indices_sorted]
    data_unique = data_smoothed[indices_sorted]

    return function_of_unique, data_unique


def rndodd(s: float) -> int:
    """
    Rounds a float to the nearest odd integer.

    Args:
        s (float): The float to round.

    Returns:
        int: The rounded odd integer.
    """
    idx = s % 2 < 1
    s = np.floor(s)

    if idx:
        s += 1
    return int(s)


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


def nearest_point(*, p: np.ndarray, line_pts: list) -> Tuple[np.ndarray, float]:
    """
    Finds the nearest point on a 3D line to a given point.

    Args:
        p (np.ndarray): The point to find the nearest point to.
        line_pts (list): A list of two points that define the 3D line.

    Returns:
        np.ndarray: The nearest point on the 3D line to the given point.
    """
    a = line_pts[0]
    b = line_pts[1]

    # direction vector
    r_v = b - a

    r_v_norm = np.linalg.norm(r_v)

    # if both points are identical
    if r_v_norm == 0:
        p_nearest = a
        t = 0
    else:
        r_v = r_v / r_v_norm
        t = (p - a) @ r_v

        # nearest point on the 3d line
        p_nearest = a + t * r_v
    return p_nearest, t


def remove_nan_vals(a: np.ndarray) -> np.ndarray:
    """
    Removes NaN values from a numpy array.

    Args:
        a (np.ndarray): The numpy array to remove NaN values from.

    Returns:
        np.ndarray: The numpy array with NaN values removed.
    """
    if isinstance(a, np.ndarray):
        return a[~np.isnan(a)]
    logger.error("Invalid input type %s", type(a))
    return np.array([])


def rotate_to_main_axis(xyz: np.ndarray) -> np.ndarray:
    """
    Rotates a point cloud to align with its main axis.

    Args:
        xyz (np.ndarray): An array of shape (n, 3) containing the x, y, and z
            coordinates of the point cloud.

    Returns:
        np.ndarray: An array of shape (n, 3) containing the rotated point cloud.
    """
    angle = line_angle(main_axis(xyz))
    rot_m = rot_z(angle, dim=xyz.shape[1])
    xyz_rot = rot_m @ xyz.T
    return xyz_rot.T


def main_axis(xyz: np.ndarray) -> np.ndarray:
    """
    Computes the main axis of a point cloud.

    Args:
        xyz (np.ndarray): An array of shape (n, 3) containing the x, y, and z
            coordinates of the point cloud.

    Returns:
        np.ndarray: An array of shape (3,) containing the direction cosines of
            the main axis.
    """
    N = np.cov(xyz.T)
    return np.linalg.eigh(N)[1][:, -1]


def line_angle(line: np.ndarray) -> float:
    """
    Calculates the angle between a 2D line and the x-axis.

    Args:
        line (np.ndarray): A 2D line represented as a numpy array of shape (2,).

    Returns:
        float: The angle between the line and the x-axis in radians.
    """
    return np.pi / 2 + np.arctan2(line[0], line[1])


def rot_from_vec(vec_a: np.ndarray, vec_b: np.ndarray) -> np.ndarray:
    """
    Computes the rotation matrix that rotates vector a to vector b.

    Args:
        vec_a (np.ndarray): The vector to rotate.
        vec_b (np.ndarray): The target vector.

    Returns:
        np.ndarray: The rotation matrix that rotates vector a to vector b.
    """
    vec_a /= np.linalg.norm(vec_a)
    vec_b /= np.linalg.norm(vec_b)

    cross_ab = np.cross(vec_a, vec_b)
    dot_ab = np.dot(vec_a, vec_b)

    skew_cab = skew_symmetric_matrix(cross_ab)

    return np.eye(len(vec_a)) + skew_cab + skew_cab**2 * 1 / (1 + dot_ab)


def cart2pol(x, y):
    """
    Converts Cartesian coordinates to polar coordinates.

    Args:
        x (float): The x-coordinate.
        y (float): The y-coordinate.

    Returns:
        np.ndarray: An array of shape (1, 2) containing the polar coordinates
            (rho and phi) of the input Cartesian coordinates.
    """
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return np.c_[rho, phi]


def pol2cart(rho, phi):
    """
    Converts polar coordinates to Cartesian coordinates.

    Args:
        rho (float): The radial distance from the origin to the point.
        phi (float): The angle between the x-axis and the line connecting the
            origin to the point, in radians.

    Returns:
        np.ndarray: An array of shape (1, 2) containing the Cartesian
            coordinates (x and y) of the input polar coordinates.
    """
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return np.c_[x, y]


def get_tau(ts_pos: np.ndarray, ts_target: np.ndarray) -> float:
    """
    Calculates the angle between a position and a target point.

    Args:
        ts_pos (np.array): A numpy array of shape (2,) representing the position.
        ts_target (np.array): A numpy array of shape (2,) representing the target point.

    Returns:
        float: The angle between the position and the target point in radians.
    """
    return np.pi / 2 + np.arctan2(ts_pos[1] - ts_target[1], ts_pos[0] - ts_target[0])


def rot_z(gamma: float, dim: int = 3) -> np.ndarray:
    """
    Computes the rotation matrix around the z-axis.

    Args:
        gamma (float): The rotation angle in radians.
        dim (int, optional): The dimension of the rotation matrix. Defaults to 3.

    Returns:
        np.ndarray: The rotation matrix around the z-axis.
    """
    if dim == 2:
        return np.array(
            [
                [np.cos(gamma), -np.sin(gamma)],
                [np.sin(gamma), np.cos(gamma)],
            ]
        )
    if dim == 3:
        return np.array(
            [
                [np.cos(gamma), -np.sin(gamma), 0],
                [np.sin(gamma), np.cos(gamma), 0],
                [0, 0, 1],
            ]
        )

    raise ValueError("rot_z: Unknown dimension!")


def filter_from_limits(tstamps: np.ndarray, gap_limits: np.ndarray) -> np.ndarray:
    """
    Creates a boolean filter which filters tstamps
    according to limits defined in gap_limits

    Args:
        tstamps (np.ndarray): Timestamps that should be filtered
        gap_limits (np.ndarray): [nx2] array containing the time
                                 limits of n gaps

    Returns:
        np.ndarray: Boolean filter which filter tstamps so that
                    all gaps are removed.
    """
    gap_start_indices = np.searchsorted(tstamps, gap_limits[:, 0])
    gap_end_indices = np.searchsorted(tstamps, gap_limits[:, 1])

    filt = np.full(tstamps.shape, True)

    for g_start, g_end in zip(gap_start_indices, gap_end_indices):
        filt[g_start:g_end] = False

    return filt


def detect_time_gaps(*, tstamps: np.ndarray, max_gap_size: float) -> np.ndarray:
    """
    Function that detect gaps within a timespan

    As soon as two timestamps have a difference
    greater than 'max_gap_size' they are considered
    as start and end points of a time gap.
    This methods returns those timestamps as a
    [nx2] array.

    Args:
        tstamps (np.ndarray): Timestamps in which gaps
                              should be detected
        max_gap_size (float): Maximum tolerated gap size
                              in seconds.

    Returns:
        np.ndarray: [nx2] array containing time limits
                    of all detected gaps
    """
    tstamps_idx = np.argsort(tstamps)
    tstamps = tstamps[tstamps_idx]

    # peaks in t vec indicate gaps
    gaps = np.where(np.abs(np.diff(tstamps)) >= max_gap_size)[0]
    # this should always work since len(gaps) is always smaller than len(tstamps)
    return np.c_[tstamps[gaps], tstamps[gaps + 1]]


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


def togrid(xyz: np.ndarray, data: np.ndarray, grid_mp: float = 1.0) -> Grid:
    """Discretizes data into a grid of size grid_mp

    Args:
        xyz (np.ndarray): Positions of data values [nx2] / [nx3]
        data (np.ndarray): data values [nx1]
        grid_mp (float, optional): Number of grid bins in megapixels.
                                 Defaults to 1.0.

    Returns:
        np.ndarray: grid with averaged values
    """
    dx = max(1, max(xyz[:, 0]) - min(xyz[:, 0]))
    dy = max(1, max(xyz[:, 1]) - min(xyz[:, 1]))
    ratio = dy / dx

    px = int(np.sqrt(grid_mp * 1e6 / ratio))
    py = int(ratio * px)
    pixel_size = np.mean([dx / px, dy / py])

    grid_x = np.linspace(min(xyz[:, 0]), max(xyz[:, 0]), px)
    grid_y = np.linspace(min(xyz[:, 1]), max(xyz[:, 1]), py)

    x_bin_ids = np.searchsorted(grid_x, xyz[:, 0])
    y_bin_ids = np.searchsorted(grid_y, xyz[:, 1])

    grid_df = pd.DataFrame(np.c_[x_bin_ids, y_bin_ids, data])
    grid_df_mean = grid_df.groupby([0, 1], sort=False).mean().reset_index()

    x_bin_locations = grid_df_mean.iloc[:, 0].to_numpy(dtype=int)
    y_bin_locations = grid_df_mean.iloc[:, 1].to_numpy(dtype=int)
    grid_values = grid_df_mean.iloc[:, 2].to_numpy(dtype=float)

    full_grid = np.zeros((px, py))
    full_grid[x_bin_locations, y_bin_locations] = grid_values

    return Grid(
        full_grid=full_grid,
        x_bin_locations=x_bin_locations,
        y_bin_locations=y_bin_locations,
        pixel_size=float(pixel_size),
    )
