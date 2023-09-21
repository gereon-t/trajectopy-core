"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

import logging
import multiprocessing
from itertools import repeat
from typing import List, Tuple

import numpy as np
from scipy.spatial.transform import Rotation, Slerp

from trajectopy_core.util.datahandling import rndodd
from trajectopy_core.util.rotationset import RotationSet
from trajectopy_core.util.spatialsorter import detect_laps_by_length

# logger configuration
logger = logging.getLogger("root")


def rot_average_slerp(
    function_of: np.ndarray,
    quat: np.ndarray,
    sort_switching_index: np.ndarray,
) -> np.ndarray:
    """Rotation averaging using multiple laps

    This function will detect multiple laps of a repeated
    closed-loop trajectory and will average the rotations
    of those laps to a mean rotation. For this, the rotations
    of individual laps are first interpolated onto common
    arc lengths using spherical linear interpolation (SLERP).
    Then, the rotations of the laps are averaged for each arc length
    using the chordal L2 mean.

    Args:
        function_of (np.ndarray): Sorted arc lengths describing the
                                  "location" of the given rotations
                                  in trajectory length (meters).
        quat (np.ndarray): Sorted quaternions at those arc lengths
        sort_switching_index (np.ndarray): Index that reverts the sorted input
                                           data back to chronological order.

    Returns:
        np.ndarray: Averaged quaternions for each arc length
    """
    logger.info("Using lap interpolation technique for rotation averaging.")
    function_of_unsorted = function_of[sort_switching_index]

    quat_us = quat[sort_switching_index, :]

    idx = detect_laps_by_length(function_of_unsorted)
    num_laps = max(len(idx) - 2, 1)
    lap_slerp: list[Tuple[Slerp, float, float]] = []
    for i in range(num_laps):
        if i == num_laps - 1:
            t_i = function_of_unsorted[idx[i] :]
            quat_i = quat_us[idx[i] :, :]
        else:
            t_i = function_of_unsorted[idx[i] : idx[i + 1]]
            quat_i = quat_us[idx[i] : idx[i + 1], :]

        t_idx = np.argsort(t_i)
        t_i_sorted = t_i[t_idx]
        quat_i_sorted = quat_i[t_idx]

        t_i_u, idx_u = np.unique(t_i_sorted, return_index=True)
        quat_i_u = quat_i_sorted[idx_u]

        quat_set = Rotation(quat=quat_i_u)
        slerp = Slerp(t_i_u, quat_set)
        lap_slerp.append((slerp, t_i_u[0], t_i_u[-1]))

    # parallel computation of mean
    with multiprocessing.Pool(4) as pool:
        output = pool.starmap(
            _average_rot,
            zip(function_of, repeat(lap_slerp)),
        )

    rot_approx = np.array(output)

    # nan indices (there was no data)
    nan_indices = np.argwhere(np.isnan(rot_approx[:, 0]))[:, 0]
    rot_approx[nan_indices, :] = quat[nan_indices, :]

    return rot_approx


def rot_average_window(function_of: np.ndarray, quat: np.ndarray, win_size: float = 0.15) -> np.ndarray:
    """
    Function that averages rotations for a given
    window size using quaternion averaging.

    For each rotation, all rotations within a window centered
    at the current rotation are averaged for the compuation of
    the mean rotation. For this, the chordal L2 mean is used.

    The average rotation for the first and last rotations are
    computed using smaller window sizes (minimum half of the window size)

    Args:
        function_of (np.ndarray): The time / arc lengths describing the
                                  "location" of the given rotations either
                                  in time or in trajectory length.
        quat (np.ndarray): _description_
        win_size (float, optional): Window size used for rotation averaging
                                    in meters. Defaults to 0.15.

    Returns:
        np.ndarray: Averaged quaternions.
    """
    logger.info("Using window technique for rotation averaging.")

    # define window
    steps = rndodd(len(function_of) / len(np.unique(np.round(function_of / (win_size)))))
    ext = int(np.floor(steps / 2))

    if ext == 0:
        logger.warning(
            "Window size for rotation approximation is set too small. There are no rotations to approximate within the windows."
        )
        return quat

    quat_mean = np.zeros((len(function_of), 4))
    num_rotations = len(quat)
    for i in range(num_rotations):
        window_start_index = max(0, i - ext)
        window_end_index = min(num_rotations - 1, i + ext)
        quat_i = quat[window_start_index:window_end_index, :]
        # compute mean
        quat_mean[i, :] = RotationSet.from_quat(quat_i).mean().as_quat()
    return quat_mean


def _average_rot(x: float, lap_slerp: List[Tuple[Slerp, float, float]]) -> np.ndarray:
    """
    Function that interpolates multiple laps of orientation data
    stored in 'lap_slerp' onto the trajectory length provided by 'x'
    """

    if rots := [l[0](x).as_quat() for l in lap_slerp if l[1] <= x <= l[2]]:
        return RotationSet.from_quat(np.array(rots)).mean().as_quat()

    return np.array([np.NaN, np.NaN, np.NaN, np.NaN])
