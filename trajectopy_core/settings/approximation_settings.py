"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
from dataclasses import dataclass
from typing import Any, Dict

from trajectopy_core.settings.core import Settings
from trajectopy_core.util.definitions import RotApprox

ROT_APPROX = {
    "lap_interp": RotApprox.INTERP,
    "window": RotApprox.WINDOW,
    "cubic": RotApprox.CUBIC,
}


@dataclass
class ApproximationSettings(Settings):
    """Dataclass defining approximation configuration"""

    fe_int_size: float = 0.15
    fe_min_obs: int = 25
    rot_approx_technique: RotApprox = RotApprox.WINDOW
    rot_approx_win_size: float = 0.15

    @classmethod
    def from_config_dict(cls, config_dict: Dict):
        fe_int_size = float(config_dict.get("fe_int_size", 0.15))
        fe_min_obs = int(config_dict.get("fe_min_obs", 25))
        rot_approx_technique = ROT_APPROX.get(
            config_dict.get("rot_approx_technique", "").lower(),
            RotApprox.INTERP,
        )
        rot_approx_win_size = config_dict.get("rot_approx_win_size", 0.15)
        return cls(
            fe_int_size=fe_int_size,
            fe_min_obs=fe_min_obs,
            rot_approx_technique=rot_approx_technique,
            rot_approx_win_size=rot_approx_win_size,
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "fe_int_size": self.fe_int_size,
            "fe_min_obs": self.fe_min_obs,
            "rot_approx_technique": str(self.rot_approx_technique),
            "rot_approx_win_size": self.rot_approx_win_size,
        }
