"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

from dataclasses import dataclass, field
from functools import cached_property
from typing import List, Optional

import numpy as np

from trajectopy_core.evaluation.ate_result import ATEResult
from trajectopy_core.evaluation.rpe_result import RPEResult
from trajectopy_core.settings.report import ReportSettings


@dataclass
class ReportData:
    """
    Class to store all data needed to render the report.

    Args:
        ate_result: The ATE result to be rendered.
        rpe_result: The RPE result to be rendered.
        settings: The report settings.

    """

    ate_result: ATEResult
    rpe_result: Optional[RPEResult] = None
    settings: ReportSettings = field(default_factory=ReportSettings)

    def __post_init__(self) -> None:
        if self.settings.ate_unit_is_mm:
            self.ate_result.abs_dev.pos_dev *= 1000.0
            self.ate_result.abs_dev.directed_pos_dev *= 1000.0

    @property
    def short_name(self) -> str:
        return self.ate_result.name.split("vs")[0]

    @property
    def ate_unit(self) -> str:
        return "mm" if self.settings.ate_unit_is_mm else "m"

    @property
    def has_ate_rot(self) -> bool:
        return self.ate_result.has_orientation

    @property
    def has_rpe(self) -> bool:
        return self.rpe_result is not None

    @property
    def function_of_label(self) -> str:
        return self.ate_result.trajectory.function_of_label

    @cached_property
    def pos_x(self) -> np.ndarray:
        return self.ate_result.trajectory.pos.x

    @cached_property
    def pos_y(self) -> np.ndarray:
        return self.ate_result.trajectory.pos.y

    @cached_property
    def pos_z(self) -> np.ndarray:
        return self.ate_result.trajectory.pos.z

    @cached_property
    def function_of(self) -> np.ndarray:
        return self.ate_result.trajectory.function_of

    @cached_property
    def comb_dev_pos(self) -> np.ndarray:
        return self.ate_result.pos_dev_comb

    @cached_property
    def pos_dev_x(self) -> np.ndarray:
        return self.ate_result.pos_dev_along if self.settings.directed_ate else self.ate_result.abs_dev.pos_dev[:, 0]

    @cached_property
    def pos_dev_y(self) -> np.ndarray:
        return self.ate_result.pos_dev_cross_h if self.settings.directed_ate else self.ate_result.abs_dev.pos_dev[:, 1]

    @cached_property
    def pos_dev_z(self) -> np.ndarray:
        return self.ate_result.pos_dev_cross_v if self.settings.directed_ate else self.ate_result.abs_dev.pos_dev[:, 2]

    @property
    def pos_dev_x_name(self) -> str:
        return "along" if self.settings.directed_ate else "x"

    @property
    def pos_dev_y_name(self) -> str:
        return "cross-h" if self.settings.directed_ate else "y"

    @property
    def pos_dev_z_name(self) -> str:
        return "cross-v" if self.settings.directed_ate else "z"

    @cached_property
    def roll(self) -> np.ndarray:
        if not self.ate_result.has_orientation:
            raise ValueError("ATE result has no orientation.")

        return np.rad2deg(self.ate_result.trajectory.rpy[:, 0])

    @cached_property
    def pitch(self) -> np.ndarray:
        if not self.ate_result.has_orientation:
            raise ValueError("ATE result has no orientation.")

        return np.rad2deg(self.ate_result.trajectory.rpy[:, 1])

    @cached_property
    def yaw(self) -> np.ndarray:
        if not self.ate_result.has_orientation:
            raise ValueError("ATE result has no orientation.")

        return np.rad2deg(self.ate_result.trajectory.rpy[:, 2])

    @cached_property
    def comb_dev_rot(self) -> np.ndarray:
        if not self.ate_result.has_orientation:
            raise ValueError("ATE result has no orientation.")

        return np.rad2deg(self.ate_result.rot_dev_comb)

    @cached_property
    def rot_dev_x(self) -> np.ndarray:
        if not self.ate_result.has_orientation:
            raise ValueError("ATE result has no orientation.")

        return np.rad2deg(self.ate_result.rot_dev_x)

    @cached_property
    def rot_dev_y(self) -> np.ndarray:
        if not self.ate_result.has_orientation:
            raise ValueError("ATE result has no orientation.")

        return np.rad2deg(self.ate_result.rot_dev_y)

    @cached_property
    def rot_dev_z(self) -> np.ndarray:
        if not self.ate_result.has_orientation:
            raise ValueError("ATE result has no orientation.")

        return np.rad2deg(self.ate_result.rot_dev_z)


@dataclass
class ReportDataCollection:
    """
    Class to store multiple ReportData objects in a list
    """

    items: List[ReportData]

    @property
    def has_ate_rot(self) -> bool:
        return any(item.has_ate_rot for item in self.items)

    @property
    def has_rpe(self) -> bool:
        return any(item.has_rpe for item in self.items)

    @property
    def has_rpe_rot(self) -> bool:
        if not self.has_rpe:
            return False

        rpe_results = [item.rpe_result for item in self.items]
        return any(result.has_rot_dev for result in rpe_results)

    def get_ate_results(self, rot_required: bool = False) -> list[ATEResult]:
        return [item.ate_result for item in self.items if not rot_required or item.has_ate_rot]

    def get_rpe_results(self, rot_required: bool = False) -> list[RPEResult]:
        return [item.rpe_result for item in self.items if not rot_required or item.rpe_result.has_rot_dev]
