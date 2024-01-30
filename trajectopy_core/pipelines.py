"""
Trajectopy - Trajectory Evaluation in Python

High-level API for trajectory evaluation in Python.

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from typing import List, Tuple, Union

import numpy as np
from pointset import PointSet

from trajectopy_core.alignment import align_trajectories, apply_alignment
from trajectopy_core.alignment.result import AlignmentResult
from trajectopy_core.approximation.cubic_approximation import piecewise_cubic
from trajectopy_core.approximation.rot_approximation import rot_average_window
from trajectopy_core.evaluation.ate_result import ATEResult
from trajectopy_core.evaluation.comparison import compare_trajectories_absolute, compare_trajectories_relative
from trajectopy_core.evaluation.rpe_result import RPEResult
from trajectopy_core.matching import match_trajectories
from trajectopy_core.rotationset import RotationSet
from trajectopy_core.settings.approximation import ApproximationSettings
from trajectopy_core.settings.processing import ProcessingSettings
from trajectopy_core.settings.sorting import SortingSettings
from trajectopy_core.spatialsorter import Sorting, sort_mls
from trajectopy_core.trajectory import Trajectory

logger = logging.getLogger("root")


def ate(
    trajectory_gt: Trajectory,
    trajectory_est: Trajectory,
    settings: ProcessingSettings = ProcessingSettings(),
    return_alignment: bool = False,
) -> Union[ATEResult, Tuple[ATEResult, AlignmentResult]]:
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
    return (
        (
            compare_trajectories_absolute(traj_ref=trajectory_gt, traj_test=trajectory_est_aligned),
            alignment,
        )
        if return_alignment
        else compare_trajectories_absolute(traj_ref=trajectory_gt, traj_test=trajectory_est_aligned)
    )


def rpe(
    trajectory_gt: Trajectory, trajectory_est: Trajectory, settings: ProcessingSettings = ProcessingSettings()
) -> RPEResult:
    match_trajectories(traj_test=trajectory_est, traj_ref=trajectory_gt, settings=settings.matching)
    return compare_trajectories_relative(
        traj_ref=trajectory_gt, traj_test=trajectory_est, settings=settings.relative_comparison
    )


def sort_spatially(
    trajectory: Trajectory, sorting_settings: SortingSettings = SortingSettings(), inplace: bool = True
) -> Trajectory:
    """
    Sorts the trajectory spatially.

    Args:
        trajectory (Trajectory): Trajectory to sort.
        sorting_settings (SortingSettings): Sorting settings.
        inplace (bool, optional): Whether to sort the trajectory in-place. Defaults to True.

    Returns:
        Trajectory: Sorted trajectory.

    """
    sort_idx, arc_lengths = sort_mls(xyz_unsorted=trajectory.pos.xyz, settings=sorting_settings)
    arg_sort_sort_idx = np.argsort(sort_idx)
    trajectory = trajectory.apply_index(sorted(sort_idx), inplace=inplace)
    trajectory.arc_lengths = arc_lengths[arg_sort_sort_idx]
    trajectory.sorting = Sorting.ARC_LENGTH
    return trajectory


def approximate(
    trajectory: Trajectory,
    approximation_settings: ApproximationSettings = ApproximationSettings(),
    inplace: bool = True,
) -> Trajectory:
    """
    Approximates the trajectory using piecewise cubic polynomial.

    Args:
        trajectory (Trajectory): Trajectory to approximate.
        approximation_settings (ApproximationSettings): Approximation settings.

    Returns:
        Trajectory: Approximated trajectory.

    """
    xyz_approx = piecewise_cubic(
        function_of=trajectory.function_of,
        values=trajectory.xyz,
        int_size=approximation_settings.fe_int_size,
        min_obs=approximation_settings.fe_min_obs,
    )

    traj_approx = trajectory if inplace else trajectory.copy()
    traj_approx.pos.xyz = xyz_approx[trajectory.sort_switching_index, :]

    if not traj_approx.has_orientation:
        return traj_approx

    quat_approx = rot_average_window(
        function_of=trajectory.function_of,
        quat=trajectory.quat,
        win_size=approximation_settings.rot_approx_win_size,
    )
    traj_approx.rot = RotationSet.from_quat(quat_approx[trajectory.sort_switching_index, :])

    return traj_approx


def merge(trajectories: List[Trajectory]) -> Trajectory:
    """
    Merges a list of trajectories into one trajectory.

    This function ignores EPSG codes and merges the
    trajectories based on their timestamps.

    Args:
        list[Trajectory]: List of trajectories to merge.

    Returns:
        Trajectory: Merged trajectory.

    """
    epsg_set = {t.pos.epsg for t in trajectories}

    if len(epsg_set) > 1:
        logger.warning(
            "Merging trajectories with different EPSG codes. "
            "This may lead to unexpected results. "
            "Consider reprojecting the trajectories to the same EPSG code."
        )

    epsg = epsg_set.pop()

    merged_xyz = np.concatenate([t.pos.xyz for t in trajectories], axis=0)
    merged_quat = np.concatenate(
        [t.rot.as_quat() if t.has_orientation else RotationSet.identity(len(t)).as_quat() for t in trajectories],
        axis=0,
    )
    has_rot = [t.has_orientation for t in trajectories]
    merged_timestamps = np.concatenate([t.tstamps for t in trajectories], axis=0)

    merged = Trajectory(
        name="Merged",
        tstamps=merged_timestamps,
        pos=PointSet(xyz=merged_xyz, epsg=epsg),
        rot=RotationSet.from_quat(merged_quat) if any(has_rot) else None,
    )

    merged.apply_index(np.argsort(merged.tstamps), inplace=True)
    return merged
