"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import csv
from typing import Any, Callable, Dict, List

import numpy as np
import pandas as pd

from trajectopy_core.evaluation.results import RPEResult
from trajectopy_core.io.trajectory_io import read_data
from trajectopy_core.util.definitions import Unit


class RelativeTrajectoryDeviations:
    """
    This class represents a set of relative trajectory deviations

    Relative trajectory deviations describe relative pose deviations between
    two trajectories. The deviations are calculated by comparing pairs of
    positions and orientations in the test and reference trajectory.
    """

    def __init__(
        self,
        rpe_result: RPEResult,
        name: str,
    ) -> None:
        self.name = name
        self.rpe_result = rpe_result

    def __eq__(self, other) -> bool:
        for self_value, other_value in zip(self.property_dict.values(), other.property_dict.values()):
            assert self_value == other_value

        return True

    def __len__(self) -> int:
        return self.rpe_result.num_pairs

    @property
    def has_rot_dev(self) -> bool:
        return any(self.rpe_result.rot_dev.values())

    @property
    def step(self) -> float:
        return np.mean(np.diff(self.mean_distances)) if len(self.mean_distances) > 1 else 0.0

    @property
    def pose_distance_unit(self) -> str:
        return "m" if self.rpe_result.pair_distance_unit == Unit.METER else "s"

    @property
    def pos_drift_unit(self) -> str:
        return "%" if self.rpe_result.pair_distance_unit == Unit.METER else "m/s"

    @property
    def rot_drift_unit(self) -> str:
        return "deg/100m" if self.rpe_result.pair_distance_unit == Unit.METER else "deg/s"

    @property
    def drift_factor(self) -> float:
        return 100.0 if self.rpe_result.pair_distance_unit == Unit.METER else 1.0

    def compute_metric(self, key: str, func: Callable[[Any], float], factor: float = 1.0) -> List[float]:
        return [float(func(values) * factor) for values in self.rpe_result.__dict__[key].values() if values]

    @property
    def num_pairs(self) -> List[int]:
        return [len(values) for values in self.rpe_result.pair_distance.values() if values]

    @property
    def mean_distances(self) -> List[float]:
        return self.compute_metric(key="pair_distance", func=np.mean)

    @property
    def mean_pos_devs(self) -> List[float]:
        return self.compute_metric(key="pos_dev", func=np.mean, factor=self.drift_factor)

    @property
    def min_pos_devs(self) -> List[float]:
        return self.compute_metric(key="pos_dev", func=np.min, factor=self.drift_factor)

    @property
    def max_pos_devs(self) -> List[float]:
        return self.compute_metric(key="pos_dev", func=np.max, factor=self.drift_factor)

    @property
    def median_pos_devs(self) -> List[float]:
        return self.compute_metric(key="pos_dev", func=np.median, factor=self.drift_factor)

    @property
    def mean_rot_devs(self) -> List[float]:
        if not self.has_rot_dev:
            return []

        return self.compute_metric(key="rot_dev", func=np.mean, factor=self.drift_factor)

    @property
    def min_rot_devs(self) -> List[float]:
        if not self.has_rot_dev:
            return []

        return self.compute_metric(key="rot_dev", func=np.min, factor=self.drift_factor)

    @property
    def max_rot_devs(self) -> List[float]:
        if not self.has_rot_dev:
            return []

        return self.compute_metric(key="rot_dev", func=np.max, factor=self.drift_factor)

    @property
    def median_rot_devs(self) -> List[float]:
        if not self.has_rot_dev:
            return []

        return self.compute_metric(key="rot_dev", func=np.median, factor=self.drift_factor)

    def get_all(self, key: str) -> List[float]:
        ret_list: List[float] = []
        model_dict = self.rpe_result.__dict__

        if key not in model_dict:
            return ret_list

        for value in model_dict[key].values():
            ret_list.extend(value)

        return ret_list

    @property
    def all_distances(self) -> List[float]:
        return self.get_all(key="pair_distance")

    @property
    def all_pos_devs(self) -> List[float]:
        return self.get_all(key="pos_dev")

    @property
    def all_rot_devs(self) -> List[float]:
        return self.get_all(key="rot_dev")

    @property
    def dynamic_pos_dict(self) -> Dict[str, str]:
        return {
            f"Average position drift at {dist:.3f} (avg) {self.pose_distance_unit}": f"{dev:.3f} {self.pos_drift_unit}"
            for dist, dev in zip(self.mean_distances, self.mean_pos_devs)
        }

    @property
    def dynamic_rot_dict(self) -> Dict[str, str]:
        if not self.has_rot_dev:
            return {}

        return {
            f"Average rotation drift at {dist:.3f} (avg) {self.pose_distance_unit}": f"{np.rad2deg(dev):.3f} {self.rot_drift_unit}"
            for dist, dev in zip(self.mean_distances, self.mean_rot_devs)
        }

    @property
    def property_dict(self) -> Dict[str, str]:
        """
        Returns a dictionary containing the properties of the deviation set
        relevant for time based comparisons. This is the case when pose-pairs
        are defined by a time difference.
        """
        basic_dict = {
            "Name": self.name,
            "Type": self.__class__.__name__,
            "Number of pose pairs": str(len(self)),
        }
        dynamic_pos_dict = self.dynamic_pos_dict
        static_pos_dict = {
            "Maximum Position Drift": f"{np.max(self.max_pos_devs):.3f} {self.pos_drift_unit}",
            "Minimum Position Drift": f"{np.min(self.min_pos_devs):.3f} {self.pos_drift_unit}",
            "Average Position Drift": f"{np.mean(self.mean_pos_devs):.3f} {self.pos_drift_unit}",
            "Median Position Drift": f"{np.median(self.median_pos_devs):.3f} {self.pos_drift_unit}",
        }

        pos_dict = basic_dict.copy()
        pos_dict.update(dynamic_pos_dict)
        pos_dict.update(static_pos_dict)

        if not self.has_rot_dev:
            return pos_dict

        dynamic_rot_dict = self.dynamic_rot_dict
        static_rot_dict = {
            "Maximum Rotation Drift": f"{np.rad2deg(np.max(self.max_rot_devs)):.3f} {self.rot_drift_unit}",
            "Minimum Rotation Drift": f"{np.rad2deg(np.min(self.min_rot_devs)):.3f} {self.rot_drift_unit}",
            "Average Rotation Drift": f"{np.rad2deg(np.mean(self.mean_rot_devs)):.3f} {self.rot_drift_unit}",
            "Median Rotation Drift": f"{np.rad2deg(np.median(self.median_rot_devs)):.3f} {self.rot_drift_unit}",
        }
        pos_dict.update(dynamic_rot_dict)
        pos_dict.update(static_rot_dict)
        return pos_dict

    def to_dataframe(self) -> pd.DataFrame:
        if self.has_rot_dev:
            return pd.DataFrame(
                np.c_[self.all_distances, self.all_pos_devs, self.all_rot_devs],
                columns=["pair_distance", "pos_dev", "rot_dev"],
            )
        else:
            return pd.DataFrame(
                np.c_[self.all_distances, self.all_pos_devs],
                columns=["pair_distance", "pos_dev"],
            )

    def to_file(self, filename: str) -> None:
        with open(filename, "a", encoding="utf-8", newline="") as file:
            file.write(f"#relative_dist_unit {self.rpe_result.pair_distance_unit.name}\n")

            writer = csv.writer(file)
            file.write("#num_pairs ")
            writer.writerow(self.num_pairs)
        self.to_dataframe().to_csv(filename, header=False, index=False, mode="a", float_format="%.12f")

    @classmethod
    def from_file(cls, filename: str):
        """Reads a set of relative trajectory deviations from a file."""
        header_data, deviation_data = read_data(filename=filename)

        pos_dev: Dict[float, List[float]] = {}
        rot_dev: Dict[float, List[float]] = {}
        pair_distance: Dict[float, List[float]] = {}

        last_index = 0
        for index in header_data.num_pairs:
            dev_block = deviation_data[last_index : last_index + index, :]
            mean_dist = np.mean(dev_block[:, 0])

            pair_distance[mean_dist] = list(dev_block[:, 0])
            pos_dev[mean_dist] = list(dev_block[:, 1])
            rot_dev[mean_dist] = list(dev_block[:, 2]) if dev_block.shape[1] > 2 else []

            last_index += index

        rpe_result = RPEResult(
            pair_distance=pair_distance,
            pos_dev=pos_dev,
            rot_dev=rot_dev,
            pair_distance_unit=header_data.relative_dist_unit,
        )

        return cls(rpe_result=rpe_result, name=header_data.name)
