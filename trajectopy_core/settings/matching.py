"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any

from trajectopy_core.settings.base import Settings


class MatchingMethod(Enum):
    NEAREST_SPATIAL = auto()
    NEAREST_TEMPORAL = auto()
    INTERPOLATION = auto()
    NEAREST_SPATIAL_INTERPOLATED = auto()
    UNKNOWN = auto()


@dataclass
class MatchingSettings(Settings):
    method: MatchingMethod = MatchingMethod.INTERPOLATION
    max_time_diff: float = 0.01
    max_distance: float = 0.00
    k_nearest: int = 10

    @staticmethod
    def encoder(name: str, value: Any) -> Any:
        if name == "method":
            return value.value
        return value

    @staticmethod
    def decoder(name: str, value: Any) -> Any:
        if name == "method":
            return MatchingMethod(value)
        return value


if __name__ == "__main__":
    settings = MatchingSettings()
    settings.to_file("matching_settings.json")
    imported_settings = MatchingSettings.from_file("matching_settings.json")

    assert imported_settings == settings
    print(imported_settings)
