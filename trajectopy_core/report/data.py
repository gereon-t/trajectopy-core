from typing import Optional

import numpy as np

from trajectopy_core.evaluation.ate_result import ATEResult
from trajectopy_core.evaluation.rpe_result import RPEResult
from trajectopy_core.util.datahandling import shrink_data


class ReportData:
    """
    Class to store all data needed to render the report.

    Args:
        ate_result: The ATE result to be rendered.
        rpe_result: The RPE result to be rendered.
        max_data_size: The maximum number of data points to be rendered.
        mm: Whether to render the ATE result in mm or m.
        max_std: The maximum standard deviation for colorbar limits

    Attributes:
        rpe_result: The RPE result to be rendered.
        ate_unit: The unit of the ATE result.
        max_std: The maximum standard deviation for colorbar limits
        has_ate_orientation: Whether the ATE result contains orientation data.
        has_rpe: Whether the RPE result is not None.
        x: The x positions of the trajectory.
        y: The y positions of the trajectory.
        tstamps: The timestamps of the trajectory.
        comb_pos_devs: The combined position deviations of the trajectory.
        along: The along track position deviations of the trajectory.
        cross_h: The horizontal cross track position deviations of the trajectory.
        cross_v: The vertical cross track position deviations of the trajectory.
        comb_rot_devs: The combined rotation deviations of the trajectory.
        roll: The roll rotation deviations of the trajectory.
        pitch: The pitch rotation deviations of the trajectory.
        yaw: The yaw rotation deviations of the trajectory.

    """

    def __init__(
        self,
        ate_result: ATEResult,
        rpe_result: Optional[RPEResult] = None,
        max_data_size: int = -1,
        mm: bool = False,
        max_std: float = 4.0,
    ) -> None:
        self.rpe_result = rpe_result
        self.ate_unit = "mm" if mm else "m"

        self.max_std = max_std
        self.has_ate_orientation = ate_result.has_orientation
        self.has_rpe = rpe_result is not None

        if mm:
            ate_result.abs_dev.pos_dev *= 1000.0
            ate_result.abs_dev.directed_pos_dev *= 1000.0

        self.x = shrink_data(ate_result.trajectory.pos.x, max_data_size)
        self.y = shrink_data(ate_result.trajectory.pos.y, max_data_size)

        self.function_of = shrink_data(ate_result.trajectory.function_of, max_data_size)
        self.function_of_unit = ate_result.trajectory.function_of_unit

        self.comb_pos_devs = shrink_data(ate_result.comb_pos_devs, max_data_size)
        self.along = shrink_data(ate_result.along, max_data_size)
        self.cross_h = shrink_data(ate_result.cross_h, max_data_size)
        self.cross_v = shrink_data(ate_result.cross_v, max_data_size)

        if not ate_result.has_orientation:
            return

        self.comb_rot_devs = np.rad2deg(shrink_data(ate_result.comb_rot_devs, max_data_size))
        self.roll = np.rad2deg(shrink_data(ate_result.roll, max_data_size))
        self.pitch = np.rad2deg(shrink_data(ate_result.pitch, max_data_size))
        self.yaw = np.rad2deg(shrink_data(ate_result.yaw, max_data_size))
