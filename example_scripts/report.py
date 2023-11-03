import logging

from rich.logging import RichHandler

from trajectopy_core.alignment.actions import align_trajectories, apply_alignment
from trajectopy_core.alignment.settings import AlignmentSettings
from trajectopy_core.evaluation.comparison import compare_trajectories_absolute, compare_trajectories_relative
from trajectopy_core.evaluation.matching import match_trajectories
from trajectopy_core.evaluation.settings import MatchingMethod, MatchingSettings, RelativeComparisonSettings
from trajectopy_core.report import render_report, write_report
from trajectopy_core.trajectory import Trajectory

logging.basicConfig(
    format="%(message)s",
    level=logging.INFO,
    handlers=[RichHandler(omit_repeated_times=False, log_time_format="%Y-%m-%d %H:%M:%S")],
)


def main():
    # Import
    gt_traj = Trajectory.from_file("./example_data/KITTI_gt.traj")
    est_traj = Trajectory.from_file("./example_data/KITTI_ORB.traj")

    # Match (not necessary in this particular case, but for demonstration purposes)
    matching_settings = MatchingSettings(method=MatchingMethod.NEAREST_TEMPORAL)  # Default settings
    match_trajectories(traj_test=est_traj, traj_ref=gt_traj, settings=matching_settings)  # in-place by default

    # Align
    alignment_settings = AlignmentSettings()  # Default settings
    alignment = align_trajectories(
        traj_from=est_traj,
        traj_to=gt_traj,
        alignment_settings=alignment_settings,
        matching_settings=MatchingSettings(method=MatchingMethod.NEAREST_TEMPORAL),
    )
    est_traj_aligned = apply_alignment(trajectory=est_traj, alignment_result=alignment)

    # Compute ATE
    ate_result = compare_trajectories_absolute(traj_ref=gt_traj, traj_test=est_traj_aligned)

    # Compute RPE
    settings = RelativeComparisonSettings()  # Default settings
    rpe_result = compare_trajectories_relative(traj_ref=gt_traj, traj_test=est_traj, settings=settings)

    report = render_report(ate_result=ate_result, rpe_result=rpe_result, max_data_size=2000)
    write_report(output_file="./report.html", report_text=report)


if __name__ == "__main__":
    main()
