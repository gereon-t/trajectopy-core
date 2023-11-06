"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from dataclasses import dataclass

from yaml_dataclass import Settings, dataclass

logger = logging.getLogger("root")


@dataclass
class PlotSettings(Settings):
    """Dataclass defining plot configuration"""

    window_title: str = "Trajectopy"
    rms_window_width: float = 1.0
    grid_mp: float = 4.0
    always_show_zero: bool = True
    c_bar_step_divisor: int = 4
    scatter_no_axis: bool = True
    scatter_sigma_factor: float = 3.0
    scatter_rotate: bool = False
    unit_is_mm: bool = False
    hist_as_stairs: bool = False
    smoothing_window_size: float = 1.0
    show_mean_line: bool = True
    heatmap_spacing: float = 1.0
    show_directed_devs: bool = True

    @property
    def unit_multiplier(self) -> float:
        return 1000 if self.unit_is_mm else 1

    @property
    def unit_str(self) -> str:
        return "[mm]" if self.unit_is_mm else "[m]"

    def reset(self):
        self.__init__()
