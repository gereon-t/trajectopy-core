"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
from dataclasses import dataclass, field
from trajectopy_core.settings.base import Settings


@dataclass
class PNGExportSettings(Settings):
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
    png_export: PNGExportSettings = field(default_factory=PNGExportSettings)


if __name__ == "__main__":
    settings = ReportSettings()
    settings.to_file("report_settings.json")
    imported_settings = ReportSettings.from_file("report_settings.json")

    assert imported_settings == settings
    print(imported_settings)
