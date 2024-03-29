"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from typing import Dict, Union

import numpy as np
from numpy import matlib
from scipy.sparse import csc_matrix, spdiags
from scipy.sparse.linalg import spsolve
from scipy.stats.distributions import chi2

from trajectopy_core.alignment.direct.helmert_transformation import direct_helmert_transformation
from trajectopy_core.alignment.direct.leverarm import direct_leverarm
from trajectopy_core.alignment.direct.timeshift import direct_timeshift
from trajectopy_core.alignment.ghm.data import AlignmentData
from trajectopy_core.alignment.ghm.functional_model.interface import FunctionalRelationship
from trajectopy_core.alignment.parameters import AlignmentParameters, HelmertTransformation, Leverarm, Parameter
from trajectopy_core.alignment.utils import dict2table
from trajectopy_core.definitions import Unit
from trajectopy_core.settings.alignment import AlignmentEstimationSettings, AlignmentSettings

logger = logging.getLogger("root")


class Alignment:
    """Class representing the alignment of two trajectories

    This class will align two trajectories using a combination
    of a 3d Helmert-transformation, a leverarm estimation and a
    time-shift estimation.

    It can fully align two trajectories their separation can be
    described by:
    - a translational shift
    - a rotation of the positions
    - a rotation of the orientations (rotation of the n-frame)
    - a scale factor
    - a time shift
    - a leverarm (e.g. mounted at different locations on the platform)
    """

    def __init__(self, alignment_data: AlignmentData) -> None:
        """Constructor

        This method prepares the data and performs an trajectory alignment

        Args:
            alignment_data (AlignmentData): Stores all data required for the alignment
            mode (AlignmentMode, optional): Indicates the desired mode, i.e. whether a
                                            - helmert transformation
                                            - scale estimation
                                            - leverarm estimation
                                            - time shift estimation
                                            should be performed
            error_probability (float, optional): Used for the stochastic global test.
                                                 Defaults to 0.05.
        """
        self.funcrel = FunctionalRelationship()
        self.data = alignment_data

        self._est_params = self.init_parameters()
        self._reestimation_required = True
        self._has_results = False
        self._converged = False
        self._group_redundancies = {}

        logger.info("Initialized Alignment!")
        logger.info(self)

    def __str__(self) -> str:
        return settings_str(self)

    @property
    def settings(self) -> AlignmentSettings:
        return self.data.alignment_settings

    def update_estimation_settings(self) -> Union[AlignmentEstimationSettings, None]:
        """Checks if enabled parameters are actually needed and returns the updated settings"""

        def default_check(parameter: Parameter) -> bool:
            return abs(parameter.value) <= 3 * np.sqrt(parameter.variance)

        def scale_check(parameter: Parameter) -> bool:
            return abs(parameter.value - 1) <= 3 * np.sqrt(parameter.variance)

        if not self.has_results:
            logger.warning("No results available. Returning None.")
            return None

        logger.info("Checking if enabled parameters are needed...")

        check_mapping = {Unit.SCALE: scale_check}

        settings_changed = False
        for parameter in self.est_params:
            if not parameter.enabled:
                continue

            if check_mapping.get(parameter.unit, default_check)(parameter):
                logger.info("Parameter %s is enabled but not needed. Disabling.", parameter.name)
                parameter.enabled = False
                settings_changed = True

        if not settings_changed:
            logger.info("No settings changed.")
            return None

        return self.est_params.to_estimation_settings()

    def estimate(self) -> AlignmentParameters:
        """Handles the estimation of the parameters

        Calls either robust reweighting or variance
        estimation methods.
        """
        logger.info("Performing alignment...")
        if self.settings.estimation_of.all_lq_disabled:
            logger.warning("Nothing to estimate since all parameters are disabled")
            return AlignmentParameters()

        max_recomputations = 10
        cnt = 0
        while self._reestimation_required:
            if cnt > max_recomputations:
                logger.warning("Maximum number of recomputations reached. Aborting.")
                break

            self._reestimation_required = False
            self._estimate_parameters()

            if self.data.alignment_settings.stochastics.variance_component_estimation:
                self.variance_component_estimation()

            # after adjusting the group variances, the parameters need to be re-estimated before performing the global test
            # we only want to change one thing at a time
            if self._reestimation_required:
                self._estimate_parameters()

            self.variance_estimation()

            cnt += 1

        if not self._converged:
            logger.info("Adjustment did not converge. Returning initial parameters.")
            return self.init_parameters()

        self._has_results = True
        print_summary(self)

        return self._est_params

    @property
    def has_results(self) -> bool:
        return self._has_results

    @property
    def est_params(self) -> AlignmentParameters:
        return self._est_params

    @property
    def group_redundancies(self) -> Dict[str, bool]:
        return self._group_redundancies

    @property
    def num_of_equations(self) -> int:
        return self.data.number_of_epochs * 3

    @property
    def redundancy(self) -> int:
        return self.num_of_equations - self._est_params.num_enabled

    def init_parameters(self) -> AlignmentParameters:
        """This method computes initial parameters
        for the iterative adjustment

        For this, the helmert transformation and
        the leverarm estimation are done separatetly
        using methods that do not require inital
        parameters.

        Returns:
            AlignmentParameters: Hold the estimates parameters.
                                 14 = 7 (helmert+scale) 3 (leverarm) 1 (time) 3 (orientation)
        """
        if self.settings.estimation_of.helmert_enabled:
            helmert_init = direct_helmert_transformation(xyz_from=self.data.xyz_from, xyz_to=self.data.xyz_to)
            xyz_init = helmert_init.apply_to(self.data.xyz_from)
        else:
            helmert_init = HelmertTransformation()
            xyz_init = self.data.xyz_from

        logger.debug("Initial Helmert: %s \n", str(helmert_init))

        if self.settings.estimation_of.time_shift_enabled and not self.settings.estimation_of.leverarm_enabled:
            time_shift_init, _ = direct_timeshift(xyz_from=xyz_init, xyz_to=self.data.xyz_to, speed=self.data.speed)
        else:
            time_shift_init = Parameter(value=0.0, name="Time shift", unit=Unit.SECOND)

        logger.debug("Initial time shift: %.3f", time_shift_init.value)

        if self.settings.estimation_of.leverarm_enabled:
            leverarm_init, time_shift_init, _ = direct_leverarm(
                speed=self.data.speed if self.settings.estimation_of.time_shift_enabled else None,
                xyz_from=xyz_init,
                xyz_to=self.data.xyz_to,
                rpy_body=self.data.rpy_from,
            )
        else:
            leverarm_init = Leverarm()

        logger.debug("Initial leverarm: %s \n", str(leverarm_init))

        alignparams = AlignmentParameters(
            sim_trans_x=helmert_init.trans_x,
            sim_trans_y=helmert_init.trans_y,
            sim_trans_z=helmert_init.trans_z,
            sim_rot_x=helmert_init.rot_x,
            sim_rot_y=helmert_init.rot_y,
            sim_rot_z=helmert_init.rot_z,
            sim_scale=helmert_init.scale,
            time_shift=time_shift_init,
            lever_x=leverarm_init.x,
            lever_y=leverarm_init.y,
            lever_z=leverarm_init.z,
        )

        alignparams.apply_settings(self.settings.estimation_of)
        logger.debug("Applied settings: %s \n", str(self.settings.estimation_of))
        return alignparams

    @property
    def variance_factor(self) -> float:
        return (
            self.data.res_vector.T @ spsolve(csc_matrix(self.data.sigma_ll), self.data.res_vector)
        ) / self.redundancy

    @property
    def _condition_xyz_to(self) -> list:
        """
        Helper function returning the constant xyz_to component of
        the condition matrix
        """
        return [
            np.c_[
                -np.ones((self.data.number_of_epochs, 1)),
                np.zeros((self.data.number_of_epochs, 1)),
                np.zeros((self.data.number_of_epochs, 1)),
            ],
            np.c_[
                np.zeros((self.data.number_of_epochs, 1)),
                -np.ones((self.data.number_of_epochs, 1)),
                np.zeros((self.data.number_of_epochs, 1)),
            ],
            np.c_[
                np.zeros((self.data.number_of_epochs, 1)),
                np.zeros((self.data.number_of_epochs, 1)),
                -np.ones((self.data.number_of_epochs, 1)),
            ],
        ]

    def variance_component_estimation(self) -> Dict[str, bool]:
        """Performs an estimation of the variances for different observation groups

        The observations groups are:
            - x and y components of xyz_from
            - z component of xyz_from
            - x and y components of xyz_to
            - z component of xyz_to
            - roll / pitch components of rpy_body
            - yaw component of rpy_body
            - speed (at target positions)

        """
        group_global_tests: Dict[str, bool] = {}
        group_variance_factors = []

        for group_key in self.data.variance_groups:
            group_variances = np.c_[self.data.get_var_group(key=group_key)]
            group_residuals = np.c_[self.data.get_res_group(key=group_key)]

            group_redundancy = self.group_redundancies[group_key]
            group_variance_factor = (
                np.sum(group_residuals * np.reciprocal(group_variances) * group_residuals) / group_redundancy
            )

            if np.allclose(group_variance_factor, 0):
                logger.warning("Variance factor is 0 for group %s. Skipping.", group_key)
                continue

            group_global_test = self._global_test(
                variance_factor=group_variance_factor, redundancy=group_redundancy, description=group_key
            )

            # global test for group
            self.data.set_var_group(values=group_variances * group_variance_factor, key=group_key)
            logger.info("Adjusted variance for group %s by factor %.3f", group_key, group_variance_factor)

            group_global_tests[group_key] = group_global_test
            group_variance_factors.append(group_variance_factor)

        if any((abs(factor - 1)) > 0.1 for factor in group_variance_factors):
            logger.info("Group variance components are different from 1, re-estimation required.")
            self._reestimation_required = True
        else:
            logger.info("Finished with variance component estimation. Re-estimation not required.")

        logging.info(dict2table(group_global_tests, title="Group Stochastic Test Results"))
        return group_global_tests

    def variance_estimation(self) -> None:
        """
        Tests the consistency of the functional and stochastic model and
        adjusts the variance vector if necessary.
        """
        self._global_test(variance_factor=self.variance_factor, redundancy=self.redundancy)

        logger.info("Adjusting variance vector by factor %.3f", self.variance_factor)

        if np.allclose(self.variance_factor, 0):
            logger.warning("Variance factor is 0. Aborting.")
            return

        if abs(self.variance_factor - 1) > 0.1:
            logger.info("Variance component is different from 1, re-estimation required.")
            self._reestimation_required = True
        else:
            logger.info("Finished with variance estimation. Re-estimation not required.")

        self.data._var_vector *= self.variance_factor

    def _global_test(self, variance_factor: float, redundancy: int, description: str = "global") -> bool:
        tau = variance_factor * redundancy
        quantile = chi2.ppf(1 - self.settings.stochastics.error_probability, redundancy)

        logger.info(
            "Stochastic test passed (%s): %s, quantile: %.3f, test value: %.3f, variance factor: %.3f",
            description,
            str(tau <= quantile),
            quantile,
            tau,
            variance_factor,
        )
        return tau <= quantile

    def _estimate_parameters(self) -> None:
        """Helmert-Leverarm-Time Transformation using the Gauß-Helmert-Model

        The observation-equations are sorted in the following way:
        [X, Y, Z, X, Y, Z, ..., X, Y, Z]
        """
        # obs = [x_from, y_from, z_from, x_to, y_to, z_to, roll_body, pitch_body, yaw_body]

        # preparation for iterative adjustment
        delta_params = np.ones((len(self._est_params),)) * np.Inf
        self.data.res_vector = np.zeros_like(self.data.obs_vector)

        contradiction_w = self._auto_functional_relationship()

        it_counter = 0
        max_iterations = 10
        self._converged = True
        while any(abs(value) > threshold for value, threshold in zip(delta_params, self.data.thresholds)):
            if it_counter > max_iterations:
                logger.error(
                    "Adjustment did not converge after %i iterations. Maximum parameter update: %.3e",
                    it_counter,
                    np.max(np.abs(delta_params)),
                )
                self._converged = False
                break

            a_design = self.auto_design_matrix()

            # filter design matrix
            a_design = a_design[:, self.settings.estimation_of.lq_parameter_filter]
            b_cond = self._condition_matrix()

            bbt = b_cond @ self.data.sigma_ll @ b_cond.T

            # solve normal equations
            delta_params = self._compute_parameter_deltas(contradiction_w, a_design, bbt)
            correlates_k = -spsolve(bbt, a_design @ delta_params + contradiction_w)
            self.data.res_vector = self.data.sigma_ll @ b_cond.T @ correlates_k

            # update
            self._est_params.values_enabled += delta_params
            contradiction_w = self._auto_functional_relationship() - b_cond @ self.data.res_vector.ravel()
            it_counter += 1

        if self._converged:
            logger.info("Adjustment did converge after %i iterations", it_counter)

        self._compute_parameter_variances(a_design, bbt)

        if self.data.alignment_settings.stochastics.variance_component_estimation:
            self._compute_group_redundancies(a_design, b_cond, bbt)

    def _compute_group_redundancies(self, a_design: csc_matrix, b_cond: csc_matrix, bbt: csc_matrix) -> None:
        q_22 = -self.est_params.get_covariance_matrix()
        q_12 = -spsolve(bbt, a_design @ q_22)
        q_21 = q_12.T if q_12.ndim == 2 else q_12[None, :]
        q_11 = spsolve(
            bbt, spdiags(np.ones(a_design.shape[0]), 0, a_design.shape[0], a_design.shape[0]) - a_design @ q_21
        )
        red_components = (
            self.data.sigma_ll @ b_cond.T @ q_11 @ b_cond @ self.data.sigma_ll
        ).diagonal() * np.reciprocal(self.data.var_vector)

        group_redundancies = {
            "XY_FROM": (
                sum(red_components[0 :: self.data.num_obs_per_epoch])
                + sum(red_components[1 :: self.data.num_obs_per_epoch])
            ),
            "Z_FROM": sum(red_components[2 :: self.data.num_obs_per_epoch]),
            "XY_TO": (
                sum(red_components[3 :: self.data.num_obs_per_epoch])
                + sum(red_components[4 :: self.data.num_obs_per_epoch])
            ),
            "Z_TO": sum(red_components[5 :: self.data.num_obs_per_epoch]),
            "ROLL_PITCH": (
                sum(red_components[6 :: self.data.num_obs_per_epoch])
                + sum(red_components[7 :: self.data.num_obs_per_epoch])
            ),
            "YAW": sum(red_components[8 :: self.data.num_obs_per_epoch]),
            "SPEED": (
                sum(red_components[9 :: self.data.num_obs_per_epoch])
                + sum(red_components[10 :: self.data.num_obs_per_epoch])
                + sum(red_components[11 :: self.data.num_obs_per_epoch])
            ),
        }

        self._group_redundancies = group_redundancies

    def _compute_parameter_variances(self, a_design: csc_matrix, bbt: csc_matrix) -> None:
        sigma_xx_inv: csc_matrix = a_design.T @ spsolve(bbt, a_design)
        if sigma_xx_inv.size == 1:
            self._est_params.set_covariance_matrix(np.reciprocal(sigma_xx_inv[:, None]))
        else:
            self._est_params.set_covariance_matrix(np.linalg.pinv(sigma_xx_inv.toarray()))

    def _compute_parameter_deltas(
        self, contradiction_w: np.ndarray, a_design: csc_matrix, bbt: csc_matrix
    ) -> np.ndarray:
        if a_design.shape[1] == 1:
            return -(a_design.T @ spsolve(bbt, contradiction_w)) / (a_design.T @ spsolve(bbt, a_design))

        # quasi vermittelnd
        # spsolve(-a_design.T @ spsolve(bbt, -a_design), -a_design.T @ spsolve(bbt, contradiction_w))
        return -spsolve(
            a_design.T @ spsolve(bbt, a_design),
            a_design.T @ spsolve(bbt, contradiction_w),
        )

    def auto_design_matrix(self) -> csc_matrix:
        a_design = np.zeros((self.data.number_of_epochs * 3, 11))
        a_design[0::3, :] = self._auto_design_x()
        a_design[1::3, :] = self._auto_design_y()
        a_design[2::3, :] = self._auto_design_z()
        return csc_matrix(a_design)

    def _auto_design_z(self) -> np.ndarray:
        return np.c_[
            np.zeros((self.data.number_of_epochs, 1)),
            np.zeros((self.data.number_of_epochs, 1)),
            self.funcrel.eval(
                func=self.funcrel.dz_dsim_trans_z,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dz_dsim_rot_x,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dz_dsim_rot_y,
                parameters=self.est_params,
                observations=self.data,
            ),
            np.zeros((self.data.number_of_epochs, 1)),
            self.funcrel.eval(
                func=self.funcrel.dz_dsim_scale,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dz_dtime_shift,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dz_dlever_x,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dz_dlever_y,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dz_dlever_z,
                parameters=self.est_params,
                observations=self.data,
            ),
        ]

    def _auto_design_y(self) -> np.ndarray:
        return np.c_[
            np.zeros((self.data.number_of_epochs, 1)),
            self.funcrel.eval(
                func=self.funcrel.dy_dsim_trans_y,
                parameters=self.est_params,
                observations=self.data,
            ),
            np.zeros((self.data.number_of_epochs, 1)),
            self.funcrel.eval(
                func=self.funcrel.dy_dsim_rot_x,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dy_dsim_rot_y,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dy_dsim_rot_z,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dy_dsim_scale,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dy_dtime_shift,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dy_dlever_x,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dy_dlever_y,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dy_dlever_z,
                parameters=self.est_params,
                observations=self.data,
            ),
        ]

    def _auto_design_x(self) -> np.ndarray:
        return np.c_[
            self.funcrel.eval(
                func=self.funcrel.dx_dsim_trans_x,
                parameters=self.est_params,
                observations=self.data,
            ),
            np.zeros((self.data.number_of_epochs, 1)),
            np.zeros((self.data.number_of_epochs, 1)),
            self.funcrel.eval(
                func=self.funcrel.dx_dsim_rot_x,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dx_dsim_rot_y,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dx_dsim_rot_z,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dx_dsim_scale,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dx_dtime_shift,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dx_dlever_x,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dx_dlever_y,
                parameters=self.est_params,
                observations=self.data,
            ),
            self.funcrel.eval(
                func=self.funcrel.dx_dlever_z,
                parameters=self.est_params,
                observations=self.data,
            ),
        ]

    def _auto_functional_relationship(self) -> np.ndarray:
        # accounting for the time shift not by using the velocity model but by shifting the time stamps and re-interpolating
        func_xyz = np.zeros((self.data.number_of_epochs * 3,))
        func_xyz[::3] = self.funcrel.eval(func=self.funcrel.x, parameters=self.est_params, observations=self.data)
        func_xyz[1::3] = self.funcrel.eval(func=self.funcrel.y, parameters=self.est_params, observations=self.data)
        func_xyz[2::3] = self.funcrel.eval(func=self.funcrel.z, parameters=self.est_params, observations=self.data)
        return func_xyz

    def _condition_matrix(self) -> csc_matrix:
        """Computes the condition-matrix for the Gauß-Helmert-Model

        The matrix contains the derivatives of the
        observation equations with respect to the observations.

        Depending on whether the lever arm is to be estimated,
        additional columns are added to the condition matrix
        corresponding to the derivation of the functional
        relationship with respect to the platform orientations.

        Its dimensions are:
            [#Obs.-Equations x #Observations]

            #Obs.-Equations: 3 * #Points

        This matrix is sparse.

        Args:
            parameters (AlignmentParameters): (current) estimated parameters

        Returns:
            csc_matrix: sparse condition matrix
        """
        cond_xyz = self._get_condition_stack()

        # row indices
        # [0,0,0,0,0,0; 1,1,1,1,1,1; 2,2,2,2,2,2; 3,3,3,3,3,3; ...]
        row_idx = np.repeat(np.arange(0, self.num_of_equations, 1), self.data.num_obs_per_epoch)

        # column indices [0,1,2,3,4,5; 6,7,8,9,10,11; 12,13,14,15,16,17; ...]
        col_idx_matrix = (
            matlib.repmat(
                np.arange(0, self.data.num_obs_per_epoch),
                self.num_of_equations,
                1,
            )
            + np.repeat(
                np.arange(
                    0,
                    self.data.number_of_epochs * self.data.num_obs_per_epoch,
                    self.data.num_obs_per_epoch,
                ),
                3,
            )[:, None]
        )
        col_idx = np.reshape(col_idx_matrix, (col_idx_matrix.size,))

        return csc_matrix((np.reshape(cond_xyz, (cond_xyz.size,)), (row_idx, col_idx)))

    def _get_condition_stack(self) -> np.ndarray:
        """Helper function to get the non-zero data of the condition matrix

        Depending on which parameters are estimated, this function returns
        different data.

        Args:
            parameters (AlignmentParameters): (current) estimated parameters

        Returns:
            np.ndarray: condition matrix data
        """
        xyz_from_component = self._auto_condition_xyz_from()

        rpy_body_component = self._auto_condition_rpy_body() if self.settings.estimation_of.leverarm_enabled else None

        speed_to_component = (
            self._auto_condition_speed_to() if self.settings.estimation_of.time_shift_enabled else None
        )

        if (
            self.settings.estimation_of.leverarm_enabled
            and not self.settings.estimation_of.time_shift_enabled
            and rpy_body_component is not None
        ):
            return np.column_stack(
                [
                    np.c_[
                        xyz_from_component[i],
                        self._condition_xyz_to[i],
                        rpy_body_component[i],
                    ]
                    for i in range(3)
                ]
            )

        if (
            self.settings.estimation_of.time_shift_enabled
            and not self.settings.estimation_of.leverarm_enabled
            and speed_to_component is not None
        ):
            return np.column_stack(
                [
                    np.c_[
                        xyz_from_component[i],
                        self._condition_xyz_to[i],
                        speed_to_component[i],
                    ]
                    for i in range(3)
                ]
            )

        if (
            self.settings.estimation_of.leverarm_enabled
            and self.settings.estimation_of.time_shift_enabled
            and rpy_body_component is not None
            and speed_to_component is not None
        ):
            return np.column_stack(
                [
                    np.c_[
                        xyz_from_component[i],
                        self._condition_xyz_to[i],
                        rpy_body_component[i],
                        speed_to_component[i],
                    ]
                    for i in range(3)
                ]
            )

        return np.column_stack(
            [
                np.c_[
                    xyz_from_component[i],
                    self._condition_xyz_to[i],
                ]
                for i in range(3)
            ]
        )

    def _auto_condition_rpy_body(self) -> list:
        return [
            np.c_[
                self.funcrel.eval(
                    func=self.funcrel.dx_deuler_x,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dx_deuler_y,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dx_deuler_z,
                    parameters=self.est_params,
                    observations=self.data,
                ),
            ],
            np.c_[
                self.funcrel.eval(
                    func=self.funcrel.dy_deuler_x,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dy_deuler_y,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dy_deuler_z,
                    parameters=self.est_params,
                    observations=self.data,
                ),
            ],
            np.c_[
                self.funcrel.eval(
                    func=self.funcrel.dz_deuler_x,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dz_deuler_y,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dz_deuler_z,
                    parameters=self.est_params,
                    observations=self.data,
                ),
            ],
        ]

    def _auto_condition_xyz_from(self) -> list:
        return [
            np.c_[
                self.funcrel.eval(
                    func=self.funcrel.dx_dx_from,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dx_dy_from,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dx_dz_from,
                    parameters=self.est_params,
                    observations=self.data,
                ),
            ],
            np.c_[
                self.funcrel.eval(
                    func=self.funcrel.dy_dx_from,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dy_dy_from,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dy_dz_from,
                    parameters=self.est_params,
                    observations=self.data,
                ),
            ],
            np.c_[
                self.funcrel.eval(
                    func=self.funcrel.dz_dx_from,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dz_dy_from,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dz_dz_from,
                    parameters=self.est_params,
                    observations=self.data,
                ),
            ],
        ]

    def _auto_condition_speed_to(self) -> list:
        return [
            np.c_[
                self.funcrel.eval(
                    func=self.funcrel.dx_dspeed_x,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dx_dspeed_y,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dx_dspeed_z,
                    parameters=self.est_params,
                    observations=self.data,
                ),
            ],
            np.c_[
                self.funcrel.eval(
                    func=self.funcrel.dy_dspeed_x,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dy_dspeed_y,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dy_dspeed_z,
                    parameters=self.est_params,
                    observations=self.data,
                ),
            ],
            np.c_[
                self.funcrel.eval(
                    func=self.funcrel.dz_dspeed_x,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dz_dspeed_y,
                    parameters=self.est_params,
                    observations=self.data,
                ),
                self.funcrel.eval(
                    func=self.funcrel.dz_dspeed_z,
                    parameters=self.est_params,
                    observations=self.data,
                ),
            ],
        ]


def print_summary(alignment: Alignment) -> None:
    logger.info(dict2table(alignment.data.group_stds, title="Group Standard Deviations"))
    logger.info(alignment.est_params)


def settings_str(alignment: Alignment) -> str:
    return (
        f"\n _____________________________________________________________________\n"
        f"| ---------------------------- Alignment ---------------------------- |\n"
        f"| Estimation of:           {alignment.settings.estimation_of.short_mode_str:<42} |\n"
        f"| Error probability [%]:   {alignment.settings.stochastics.error_probability*100:<42} |\n"
        f"|_____________________________________________________________________|\n"
    )
