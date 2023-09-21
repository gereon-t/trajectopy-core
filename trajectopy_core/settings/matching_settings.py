"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any, Dict

from trajectopy_core.settings.core import Settings, field_extractor


class MatchingMethod(Enum):
    NEAREST_SPATIAL = auto()
    NEAREST_TEMPORAL = auto()
    INTERPOLATION = auto()
    UNKNOWN = auto()


@dataclass
class MatchingSettings(Settings):
    """Dataclass defining matching configuration"""

    method: MatchingMethod = MatchingMethod.INTERPOLATION
    max_time_diff: float = 0.01
    max_distance: float = 0.01

    def to_dict(self) -> Dict[str, Any]:
        return {
            "method": self.method.name,
            "max_time_diff": self.max_time_diff,
            "max_distance": self.max_distance,
        }

    @classmethod
    def from_config_dict(cls, config_dict: Dict):
        return matching_settings_from_dict(config_dict=config_dict)


def matching_method_from_string(string: str) -> MatchingMethod:
    if "nearest_spatial" in string.lower():
        return MatchingMethod.NEAREST_SPATIAL

    if "nearest_temporal" in string.lower():
        return MatchingMethod.NEAREST_TEMPORAL

    return MatchingMethod.INTERPOLATION if "interpolation" in string.lower() else MatchingMethod.UNKNOWN


def matching_settings_from_dict(config_dict: Dict):
    return field_extractor(
        config_class=MatchingSettings(),
        config_dict=config_dict,
        fill_missing_with={"default": 0.0},
        field_handler={"method": matching_method_from_string},
    )
