"""
Trajectopy - Trajectory Evaluation in Python

High-level API for trajectory evaluation in Python.

Gereon Tombrink, 2023
mail@gtombrink.de
"""


from trajectopy_core.alignment import align_trajectories, apply_alignment
from trajectopy_core.evaluation.ate_result import ATEResult
from trajectopy_core.evaluation.comparison import compare_trajectories_absolute, compare_trajectories_relative
from trajectopy_core.evaluation.rpe_result import RPEResult
from trajectopy_core.matching import match_trajectories
from trajectopy_core.settings.processing import ProcessingSettings
from trajectopy_core.trajectory import Trajectory


def ate(
    trajectory_gt: Trajectory, trajectory_est: Trajectory, settings: ProcessingSettings = ProcessingSettings()
) -> ATEResult:
    """
    Computes the absolute trajectory error (ATE) between two trajectories.

    Args:
        trajectory_gt (Trajectory): Ground truth trajectory.
        trajectory_est (Trajectory): Estimated trajectory.
        settings (ProcessingSettings, optional): Processing settings.

    Returns:
        ATEResult: Result of the ATE computation.

    """
    match_trajectories(traj_test=trajectory_est, traj_ref=trajectory_gt, settings=settings.matching)
    alignment = align_trajectories(
        traj_from=trajectory_est,
        traj_to=trajectory_gt,
        alignment_settings=settings.alignment,
        matching_settings=settings.matching,
    )
    trajectory_est_aligned = apply_alignment(trajectory=trajectory_est, alignment_result=alignment, inplace=False)
    return compare_trajectories_absolute(traj_ref=trajectory_gt, traj_test=trajectory_est_aligned)


def rpe(
    trajectory_gt: Trajectory, trajectory_est: Trajectory, settings: ProcessingSettings = ProcessingSettings()
) -> RPEResult:
    match_trajectories(traj_test=trajectory_est, traj_ref=trajectory_gt, settings=settings.matching)
    return compare_trajectories_relative(
        traj_ref=trajectory_gt, traj_test=trajectory_est, settings=settings.relative_comparison
    )