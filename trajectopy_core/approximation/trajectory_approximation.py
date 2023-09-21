"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import copy
import logging
from typing import Union

import numpy as np
from pointset import PointSet

from trajectopy_core.approximation.cubic_approximation import CubicApproximation, piecewise_cubic
from trajectopy_core.approximation.rot_approximation import rot_average_slerp, rot_average_window
from trajectopy_core.settings.approximation_settings import ApproximationSettings
from trajectopy_core.trajectory import Sorting, Trajectory, TrajectoryProcessingState
from trajectopy_core.util.definitions import RotApprox
from trajectopy_core.util.rotationset import RotationSet

logger = logging.getLogger("root")


class TrajectoryApproximation(Trajectory):
    """Class representing an approximation"""

    def __init__(
        self,
        pos: PointSet,
        rot: Union[None, RotationSet] = None,
        tstamps: Union[np.ndarray, None] = None,
        name: str = "",
        sorting: Union[Sorting, None] = None,
        sort_index: Union[np.ndarray, None] = None,
        arc_lengths: Union[np.ndarray, None] = None,
        settings: Union[ApproximationSettings, None] = None,
        state: Union[TrajectoryProcessingState, None] = None,
    ) -> None:
        """Create new Approximation Trajectory

        During initialization, deep copies of the input
        trajectory field are made.

        Args:
            traj (Trajectory): Trajectory that should be approximated
            config (ApproximationConfig, optional): Contains approximation settings.
                                                    Defaults to ApproximationConfig().

        Raises:
            ValueError: _description_
        """
        super().__init__(
            pos=pos.copy(),
            rot=rot.copy() if rot is not None else None,
            tstamps=copy.deepcopy(tstamps) if tstamps is not None else None,
            name=copy.deepcopy(name),
            sorting=copy.deepcopy(sorting) if sorting is not None else None,
            sort_index=copy.deepcopy(sort_index) if sort_index is not None else None,
            arc_lengths=copy.deepcopy(arc_lengths) if arc_lengths is not None else None,
            state=copy.deepcopy(state) if state is not None else TrajectoryProcessingState(),
        )
        self._has_valid_sorting = sort_index is not None
        self.config = settings if settings is not None else ApproximationSettings()
        self.state_before_approximation = copy.deepcopy(state) if state is not None else TrajectoryProcessingState()
        self.approximation_epsg = self.pos.epsg
        self.state.approximated = True
        self.cubic_approximations: Union[None, list[CubicApproximation]] = None

        self._perform_approximation(self.config)

    def _perform_approximation(self, settings: ApproximationSettings):
        """Internal approximation method

        Approximates positions and orientations

        Args:
            settings (ApproximationSettings): Settings defining approximation
                                              techniques, window sizes, etc.

        """
        self.pos.xyz, self.cubic_approximations = piecewise_cubic(
            function_of=self.function_of,
            values=self.pos.xyz,
            int_size=settings.fe_int_size,
            min_obs=settings.fe_min_obs,
            return_approx_objects=True,
        )

        self._rotation_approximation(settings)

    def _rotation_approximation(self, settings: ApproximationSettings):
        """Internal approximation method

        Approximates orientations

        Args:
            settings (ApproximationSettings): Settings defining approximation
                                              techniques, window sizes, etc.

        Raises:
            ValueError: Raised when there is no valid sorting but lap interpolation
                        method is requested.
        """
        if self.rot is None:
            return

        if settings.rot_approx_technique == RotApprox.INTERP and self.state.sorting_known:
            self.set_sorting(Sorting.SPATIAL)
            quat_approx = rot_average_slerp(
                function_of=self.function_of,
                quat=self.rot.as_quat(),
                sort_switching_index=self.sort_switching_index,
            )

        elif settings.rot_approx_technique == RotApprox.WINDOW:
            quat_approx = rot_average_window(
                function_of=self.function_of,
                quat=self.rot.as_quat(),
                win_size=settings.rot_approx_win_size,
            )
        else:
            raise ValueError("Please provide a sorter object for 'INTERP' rotation approximation")

        self.rot = RotationSet.from_quat(quat_approx)
