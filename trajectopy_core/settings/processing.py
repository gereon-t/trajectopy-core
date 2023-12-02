"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

from dataclasses import dataclass, field

from trajectopy_core.settings.alignment import AlignmentSettings
from trajectopy_core.settings.approximation import ApproximationSettings
from trajectopy_core.settings.base import Settings
from trajectopy_core.settings.comparison import RelativeComparisonSettings
from trajectopy_core.settings.matching import MatchingSettings
from trajectopy_core.settings.sorting import SortingSettings


@dataclass
class ProcessingSettings(Settings):
    """Settings for processing the trajectory."""

    alignment: AlignmentSettings = field(default_factory=AlignmentSettings)
    matching: MatchingSettings = field(default_factory=MatchingSettings)
    relative_comparison: RelativeComparisonSettings = field(default_factory=RelativeComparisonSettings)
    approximation: ApproximationSettings = field(default_factory=ApproximationSettings)
    sorting: SortingSettings = field(default_factory=SortingSettings)


if __name__ == "__main__":
    settings = ProcessingSettings()
    settings.to_file("processing_settings.json")
    imported_settings = ProcessingSettings.from_file("processing_settings.json")

    assert imported_settings == settings
    print(imported_settings)
