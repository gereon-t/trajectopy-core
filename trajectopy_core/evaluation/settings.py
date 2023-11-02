"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Dict

from yaml_dataclass import Settings, dataclass

from trajectopy_core.utils.definitions import Unit


class ComparisonMethod(Enum):
    ABSOLUTE = auto()
    RELATIVE = auto()
    UNKNOWN = auto()

    @classmethod
    def from_string(cls, string: str):
        return comparison_method_from_string(string)


def comparison_method_from_string(string: str) -> ComparisonMethod:
    if "absolute" in string.lower():
        return ComparisonMethod.ABSOLUTE

    return ComparisonMethod.RELATIVE if "relative" in string.lower() else ComparisonMethod.UNKNOWN


@dataclass
class RelativeComparisonSettings(Settings):
    """
    A class representing the settings for relative trajectory comparison.

    Attributes:
        relative_pair_min_distance (float): The minimum distance between two poses in a relative pair.
        relative_pair_max_distance (float): The maximum distance between two poses in a relative pair.
        relative_pair_distance_step (float): The step size for the distance between two poses in a relative pair.
        relative_pair_distance_unit (Unit): The unit of measurement for the distance between two poses in a relative pair.
        use_all_pose_pairs (bool): Whether to use all possible pose pairs for relative comparison.
    """

    pair_min_distance: float = 100.0
    pair_max_distance: float = 800.0
    pair_distance_step: float = 100.0
    pair_distance_unit: Unit = Unit.METER
    use_all_pose_pairs: bool = True

    def to_dict(self) -> Dict[str, Any]:
        return {
            "pair_min_distance": self.pair_min_distance,
            "pair_max_distance": self.pair_max_distance,
            "pair_distance_step": self.pair_distance_step,
            "pair_distance_unit": self.pair_distance_unit.name,
            "use_all_pose_pairs": self.use_all_pose_pairs,
        }


class MatchingMethod(Enum):
    NEAREST_SPATIAL = auto()
    NEAREST_TEMPORAL = auto()
    INTERPOLATION = auto()
    NEAREST_SPATIAL_INTERPOLATED = auto()
    UNKNOWN = auto()


@dataclass
class MatchingSettings(Settings):
    """Dataclass defining matching configuration"""

    method: MatchingMethod = MatchingMethod.INTERPOLATION
    max_time_diff: float = 0.01
    max_distance: float = 0.00
    k_nearest: int = 10
