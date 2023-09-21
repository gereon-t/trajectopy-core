"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
from dataclasses import dataclass, field
from typing import Any, Dict

from trajectopy_core.evaluation.comparison import RelativeComparisonSettings
from trajectopy_core.settings.alignment_settings import AlignmentSettings
from trajectopy_core.settings.approximation_settings import ApproximationSettings
from trajectopy_core.settings.core import Settings, yaml2dict
from trajectopy_core.settings.matching_settings import MatchingSettings
from trajectopy_core.settings.sorting_settings import SortingSettings


@dataclass
class ProcessingSettings(Settings):
    """This class stores all processing settings

    It can be initialized by either providing separate
    configurationsets for

    - sorting
    - approximation
    - alignment

    or by using the 'from_file' method together with a yaml configuration file
    """

    sorting: SortingSettings = field(default_factory=SortingSettings)
    approximation: ApproximationSettings = field(default_factory=ApproximationSettings)
    alignment: AlignmentSettings = field(default_factory=AlignmentSettings)
    rel_comparison: RelativeComparisonSettings = field(default_factory=RelativeComparisonSettings)
    matching: MatchingSettings = field(default_factory=MatchingSettings)

    def __str__(self) -> str:
        return str(self.sorting) + str(self.approximation) + str(self.alignment)

    @classmethod
    def from_file(cls, file: str):
        return ProcessingSettings.from_config_dict(config_dict=yaml2dict(file))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "sorting": self.sorting.to_dict(),
            "approximation": self.approximation.to_dict(),
            "alignment": self.alignment.to_dict(),
            "rel_comparison": self.rel_comparison.to_dict(),
            "matching": self.matching.to_dict(),
        }

    @classmethod
    def from_config_dict(cls, config_dict: Dict):
        sorting_settings = SortingSettings.from_config_dict(config_dict.get("sorting", {}))
        approximation_settings = ApproximationSettings.from_config_dict(config_dict.get("approximation", {}))
        alignment_settings = AlignmentSettings.from_config_dict(config_dict.get("alignment", {}))
        rel_comparison_settings = RelativeComparisonSettings.from_config_dict(config_dict.get("rel_comparison", {}))
        matching_settings = MatchingSettings.from_config_dict(config_dict.get("matching", {}))

        return cls(
            approximation=approximation_settings,
            sorting=sorting_settings,
            alignment=alignment_settings,
            rel_comparison=rel_comparison_settings,
            matching=matching_settings,
        )
