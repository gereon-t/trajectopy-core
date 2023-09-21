"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
from dataclasses import dataclass

from trajectopy_core.settings.core import Settings


@dataclass
class SortingSettings(Settings):
    """This class stores all sorting settings"""

    discard_missing: bool = True
    voxel_size: float = 0.05
    movement_threshold: float = 0.005
    k_nearest: int = 4

    @classmethod
    def from_config_dict(cls, config_dict: dict):
        voxel_size = float(config_dict.get("voxel_size", 0.05))
        movement_threshold = float(config_dict.get("movement_threshold", 0.005))
        discard_missing = config_dict.get("discard_missing", True)
        k_nearest = int(config_dict.get("k_nearest", 4))
        return cls(
            discard_missing=discard_missing,
            voxel_size=voxel_size,
            k_nearest=k_nearest,
            movement_threshold=movement_threshold,
        )
