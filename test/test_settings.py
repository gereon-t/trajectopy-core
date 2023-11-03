import unittest
from pathlib import Path

from yaml_dataclass import Settings

from trajectopy_core.alignment.settings import (
    AlignmentEstimationSettings,
    AlignmentPreprocessing,
    AlignmentSettings,
    AlignmentStochastics,
)
from trajectopy_core.evaluation.settings import MatchingSettings, RelativeComparisonSettings
from trajectopy_core.plotting.settings import PlotSettings


class TestSettings(unittest.TestCase):
    _file = 0

    def setUp(self) -> None:
        super().setUp()
        Path("./test/tmp").mkdir(parents=True, exist_ok=True)

    def settings_io_test(self, Settings: Settings) -> None:
        filename = f"./test/tmp/settings{TestSettings._file}.yaml"
        created_settings = Settings()
        created_settings.to_yaml(filename)
        imported_settings = Settings.from_yaml(filename)
        self.assertTrue(imported_settings == created_settings)
        TestSettings._file += 1

    def test_alignment_settings(self) -> None:
        self.settings_io_test(AlignmentSettings)

    def test_alignment_preprocessing_settings(self) -> None:
        self.settings_io_test(AlignmentPreprocessing)

    def test_rel_comparison_settings(self) -> None:
        self.settings_io_test(RelativeComparisonSettings)

    def test_alignment_estimation_settings(self) -> None:
        self.settings_io_test(AlignmentEstimationSettings)

    def test_alignment_stochastics_settings(self) -> None:
        self.settings_io_test(AlignmentStochastics)

    def test_matching_settings(self) -> None:
        self.settings_io_test(MatchingSettings)

    def test_plot_settings(self) -> None:
        self.settings_io_test(PlotSettings)
