"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from typing import Tuple

import numpy as np
from scipy.sparse import spdiags

from trajectopy_core.alignment.parameters import Parameter
from trajectopy_core.approximation.util import least_squares
from trajectopy_core.util.definitions import Unit

# logger configuration
logger = logging.getLogger("root")


def direct_timeshift(
    *,
    xyz_to: np.ndarray,
    xyz_from: np.ndarray,
    speed: np.ndarray,
    weights: np.ndarray = np.zeros(0),
) -> Tuple[Parameter, np.ndarray]:
    """Time shift estimation

    Estimates the time offset between two trajectories using a gauß-markov model.

    The observations are the difference between the target
    and the source positions.
    The parameters are:
        - time

    Args:
        xyz_to (np.ndarray): Source positions
        xyz_from (np.ndarray): target positions
        speed (np.ndarray): speed of the platform.
        weights (np.ndarray, optional): observation weights.
                                        Defaults to None.


    Returns:
        Tuple[np.ndarray, np.ndarray]: Tuple containing the estimated
                                       parameters and the residuals of
                                       the adjustment.
    """

    if len(xyz_to) != len(xyz_from):
        raise ValueError("estimate_leverarm: All arrays must have equal dimensions!")

    if weights is None:
        weights = np.ones(xyz_to.size)
        logger.debug("Using default uniform weighting")
    else:
        logger.debug("Using custom weighting")

    a_design = speed.T.reshape(speed.size, 1)

    observations = np.r_[
        xyz_to[:, 0] - xyz_from[:, 0],
        xyz_to[:, 1] - xyz_from[:, 1],
        xyz_to[:, 2] - xyz_from[:, 2],
    ]
    sigma_ll = spdiags(weights, 0, len(weights), len(weights))

    est_params, _, residuals = least_squares(a_design, observations, sigma_ll=sigma_ll)

    return (
        Parameter(value=est_params[0], name="Time shift", unit=Unit.SECOND),
        residuals,
    )
