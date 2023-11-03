import unittest

from trajectopy_core.alignment.actions import align_trajectories, apply_alignment
from trajectopy_core.alignment.settings import AlignmentSettings
from trajectopy_core.evaluation.comparison import compare_trajectories_absolute, compare_trajectories_relative
from trajectopy_core.evaluation.matching import match_trajectories
from trajectopy_core.evaluation.settings import MatchingMethod, MatchingSettings, RelativeComparisonSettings
from trajectopy_core.trajectory import Trajectory


class TestPipeline(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()

        self.gt = Trajectory.from_file("example_data/KITTI_gt.traj")
        self.est = Trajectory.from_file("example_data/KITTI_ORB.traj")

    def test_ate(self) -> None:
        matching_settings = MatchingSettings(method=MatchingMethod.NEAREST_TEMPORAL)
        match_trajectories(traj_test=self.est, traj_ref=self.gt, settings=matching_settings)

        # Align
        alignment_settings = AlignmentSettings()
        alignment = align_trajectories(
            traj_from=self.est,
            traj_to=self.gt,
            alignment_settings=alignment_settings,
            matching_settings=MatchingSettings(method=MatchingMethod.NEAREST_TEMPORAL),
        )
        est_traj_aligned = apply_alignment(trajectory=self.est, alignment_result=alignment)

        # Compute ATE
        compare_trajectories_absolute(traj_ref=self.gt, traj_test=est_traj_aligned)

    def test_rpe(self) -> None:
        # Match (not necessary in this particular case, but for demonstration purposes)
        matching_settings = MatchingSettings(method=MatchingMethod.NEAREST_TEMPORAL)  # Default settings
        match_trajectories(traj_test=self.est, traj_ref=self.gt, settings=matching_settings)  # in-place by default

        # Compute RPE
        settings = RelativeComparisonSettings()  # Default settings
        compare_trajectories_relative(traj_ref=self.gt, traj_test=self.est, settings=settings)
