"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
from dataclasses import dataclass, field
from trajectopy_core.settings.base import Settings


@dataclass
class ExportSettings(Settings):
    format: str = "png"  # one of png, svg, jpeg, webp
    height: int = 500
    width: int = 800
    scale: int = 6

    def to_config(self) -> dict:
        return {
            "toImageButtonOptions": {
                "format": self.format,
                "height": self.height,
                "width": self.width,
                "scale": self.scale,
            }
        }


@dataclass
class ReportSettings(Settings):
    downsample_size: int = 2000
    scatter_max_std: float = 4.0
    ate_unit_is_mm: bool = False
    directed_ate: bool = True

    histogram_opacity: float = 0.7
    histogram_bargap: float = 0.1
    histogram_barmode: str = "overlay"
    histogram_yaxis_title: str = "Count"

    plot_mode: str = "lines+markers"

    scatter_mode: str = "markers"
    scatter_colorscale: str = "RdYlBu_r"

    pos_x_name: str = "x"
    pos_y_name: str = "y"
    pos_z_name: str = "z"
    pos_x_unit: str = "m"
    pos_y_unit: str = "m"
    pos_z_unit: str = "m"

    rot_x_name: str = "roll"
    rot_y_name: str = "pitch"
    rot_z_name: str = "yaw"
    rot_unit: str = "°"

    single_plot_export: ExportSettings = field(default_factory=lambda: ExportSettings(width=800, height=450))
    two_subplots_export: ExportSettings = field(default_factory=lambda: ExportSettings(width=800, height=540))
    three_subplots_export: ExportSettings = field(default_factory=lambda: ExportSettings(width=800, height=750))

    single_plot_height: int = 450
    two_subplots_height: int = 540
    three_subplots_height: int = 750


if __name__ == "__main__":
    settings = ReportSettings()
    settings.to_file("report_settings.json")
    imported_settings = ReportSettings.from_file("report_settings.json")

    assert imported_settings == settings
    print(imported_settings)
