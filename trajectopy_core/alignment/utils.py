"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from typing import Tuple

import numpy as np
from scipy.linalg import solve
from scipy.sparse import identity

# logger configuration
logger = logging.getLogger("root")


def least_squares(
    design_matrix: np.ndarray,
    observations: np.ndarray,
    sigma_ll: np.ndarray = np.array([]),
) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Solves a least squares problem with a dense matrix A and a dense vector l.

    Parameters:
    design_matrix (np.ndarray): A numpy array of shape (m, n) representing the design matrix.
    observations (np.ndarray): A numpy array of shape (m,) containing the observations.
    sigma_ll (np.ndarray): A numpy array of shape (m, m) containing the weights of the observations (default is an identity matrix).

    Returns:
    Tuple[np.ndarray, np.ndarray, np.ndarray]: A tuple containing the solution vector x_s, the approximated observations l_s, and the residuals v.
    """
    observations = observations.reshape(
        len(observations),
    )
    if sigma_ll.shape[0] == 0:
        sigma_ll = identity(len(observations))
    # solve normal equations
    x_s = solve(
        design_matrix.T @ sigma_ll @ design_matrix,
        design_matrix.T @ sigma_ll @ observations,
    )

    # approximated observations
    l_s = design_matrix @ x_s

    # residuals
    v = l_s - observations

    return x_s, l_s, v
