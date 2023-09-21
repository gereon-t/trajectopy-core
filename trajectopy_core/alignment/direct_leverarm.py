"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from typing import Tuple, Union

import numpy as np
from scipy.sparse import spdiags

from trajectopy_core.alignment.parameters import Leverarm, Parameter
from trajectopy_core.approximation.util import least_squares
from trajectopy_core.util.definitions import Unit

# logger configuration
logger = logging.getLogger("root")


def direct_leverarm(
    *,
    xyz_to: np.ndarray,
    xyz_from: np.ndarray,
    rpy_body: np.ndarray,
    weights: Union[np.ndarray, None] = None,
    speed: Union[np.ndarray, None] = None,
) -> Tuple[Leverarm, Parameter, np.ndarray]:
    """Leverarm (+time) estimation

    Estimates the leverarm and the time offset
    between two trajectories using a gauß-markov model.

    The observations are the difference between the target
    and the source positions.
    The parameters are:
        - time (if gradients / speeds are provided)
        - leverarm (dx, dy, dz)

    Args:
        xyz_to (np.ndarray): Source positions
        xyz_from (np.ndarray): target positions
        rpy_body (np.ndarray): platform orientations
        weights (np.ndarray, optional): observation weights.
                                        Defaults to None.
        speed (np.ndarray, optional): speed of the platform.
                                         Defaults to None.

    Returns:
        Tuple[np.ndarray, np.ndarray]: Tuple containing the estimated
                                       parameters and the residuals of
                                       the adjustment.
    """

    if not len(xyz_to) == len(xyz_from) == len(rpy_body):
        raise ValueError("estimate_leverarm: All arrays must have equal dimensions!")

    if weights is None:
        weights = np.ones(xyz_to.size)
        logger.debug("Using default uniform weighting")
    else:
        logger.debug("Using custom weighting")

    # x_1 - x_2 = (cos(b) * cos(g) * d_x + (sin(a) * sin(b) * cos(g) - cos(a) * sin(g)) * d_y + (cos(a) * sin(b) * cos(g) + sin(a) * sin(g)) * d_z)
    # y_1 - y_2 = (cos(b) * sin(g) * d_x + (sin(a) * sin(b) * sin(g) + cos(a) * cos(g)) * d_y + (cos(a) * sin(b) * sin(g) - sin(a) * cos(g)) * d_z)
    # z_2 - z_2 = (-sin(b) * d_x + sin(a) * cos(b) * d_y + cos(a) * cos(b) * d_z)

    # or

    # x_1 - x_2 = v_x * d_t + (cos(b) * cos(g) * d_x + (sin(a) * sin(b) * cos(g) - cos(a) * sin(g)) * d_y + (cos(a) * sin(b) * cos(g) + sin(a) * sin(g)) * d_z)
    # y_1 - y_2 = v_y * d_t + (cos(b) * sin(g) * d_x + (sin(a) * sin(b) * sin(g) + cos(a) * cos(g)) * d_y + (cos(a) * sin(b) * sin(g) - sin(a) * cos(g)) * d_z)
    # z_2 - z_2 = v_z * d_t + (-sin(b) * d_x + sin(a) * cos(b) * d_y + cos(a) * cos(b) * d_z)
    a_design = design_matrix(rpy_body, speed=speed)

    observations = np.r_[
        xyz_to[:, 0] - xyz_from[:, 0],
        xyz_to[:, 1] - xyz_from[:, 1],
        xyz_to[:, 2] - xyz_from[:, 2],
    ]
    sigma_ll = spdiags(weights, 0, len(weights), len(weights))

    est_params, _, residuals = least_squares(a_design, observations, sigma_ll=sigma_ll)

    if speed is not None:
        time_shift = est_params[0]
        idx_offset = 1
    else:
        time_shift = 0
        idx_offset = 0

    return (
        Leverarm(
            x=Parameter(value=est_params[idx_offset], name="Leverarm x", unit=Unit.METER),
            y=Parameter(value=est_params[idx_offset + 1], name="Leverarm y", unit=Unit.METER),
            z=Parameter(value=est_params[idx_offset + 2], name="Leverarm z", unit=Unit.METER),
        ),
        Parameter(value=time_shift, name="Time shift", unit=Unit.SECOND),
        residuals,
    )


def design_matrix(rpy: np.ndarray, speed: Union[np.ndarray, None] = None) -> np.ndarray:
    """Builds design matrix for leverarm (+ time) estimation

    Contains the derivation of the observation equations with respect
    to the parameters

    Args:
        rpy (np.ndarray): platform orientations
        speed (np.ndarray, optional): Gradients / speeds at the
                                         positions. Defaults to None.
                                         If no gradients are provided
                                         the adjustment will fall back
                                         to a leverarm only estimation.

    Returns:
        np.ndarray: design matrix
    """
    a = rpy[:, 0]
    b = rpy[:, 1]
    g = rpy[:, 2]

    # design matrix
    a_design_x = np.c_[
        np.cos(b) * np.cos(g),
        -np.cos(a) * np.sin(g) + np.sin(a) * np.sin(b) * np.cos(g),
        np.sin(a) * np.sin(g) + np.cos(a) * np.sin(b) * np.cos(g),
    ]

    a_design_y = np.c_[
        np.cos(b) * np.sin(g),
        np.sin(a) * np.sin(b) * np.sin(g) + np.cos(a) * np.cos(g),
        -np.sin(a) * np.cos(g) + np.cos(a) * np.sin(b) * np.sin(g),
    ]

    a_design_z = np.c_[-np.sin(b), np.sin(a) * np.cos(b), np.cos(a) * np.cos(b)]

    if speed is not None:
        return np.c_[
            speed.T.reshape(
                speed.size,
            ),
            np.r_[a_design_x, a_design_y, a_design_z],
        ]
    else:
        return np.r_[a_design_x, a_design_y, a_design_z]
