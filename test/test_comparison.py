import unittest
from test.testdata import generated_trajectory
from test.util import random_number

import numpy as np
from trajectopy_core.alignment.actions import apply_alignment

from trajectopy_core.alignment.parameters import AlignmentParameters, Parameter
from trajectopy_core.alignment.result import AlignmentResult
from trajectopy_core.evaluation.ate_result import ATEResult
from trajectopy_core.evaluation.comparison import compare_trajectories_absolute, compare_trajectories_relative
from trajectopy_core.matching import match_trajectories
from trajectopy_core.evaluation.rpe_result import RPEResult
from trajectopy_core.settings.matching import MatchingMethod, MatchingSettings
from trajectopy_core.settings.comparison import RelativeComparisonSettings
from trajectopy_core.trajectory import Trajectory
from trajectopy_core.utils.definitions import Unit


def compare_trajectories_abs(traj_ref: Trajectory, traj_test: Trajectory) -> ATEResult:
    matching_settings = MatchingSettings(method=MatchingMethod.NEAREST_TEMPORAL)

    traj_test, traj_ref = match_trajectories(traj_test=traj_test, traj_ref=traj_ref, settings=matching_settings)

    if len(traj_ref) != len(traj_test):
        raise ValueError("Something went wrong during matching.")

    return compare_trajectories_absolute(traj_test=traj_test, traj_ref=traj_ref)


def compare_trajectories_rel(
    traj_ref: Trajectory, traj_test: Trajectory, settings: RelativeComparisonSettings
) -> RPEResult:
    matching_settings = MatchingSettings(method=MatchingMethod.NEAREST_TEMPORAL)

    traj_test, traj_ref = match_trajectories(traj_test=traj_test, traj_ref=traj_ref, settings=matching_settings)

    if len(traj_ref) != len(traj_test):
        raise ValueError("Something went wrong during matching.")

    return compare_trajectories_relative(traj_test=traj_test, traj_ref=traj_ref, settings=settings)


class TestComparison(unittest.TestCase):
    def test_body_frame_deviations(self) -> None:
        trajectory = generated_trajectory.copy()

        parameters = AlignmentParameters(
            lever_x=Parameter(value=random_number(min=-1, max=1), unit=Unit.METER),
            lever_y=Parameter(value=random_number(min=-1, max=1), unit=Unit.METER),
            lever_z=Parameter(value=random_number(min=-1, max=1), unit=Unit.METER),
        )
        transformed = apply_alignment(
            trajectory=generated_trajectory,
            alignment_result=AlignmentResult(position_parameters=parameters),
            inplace=False,
        )

        deviations = compare_trajectories_abs(traj_ref=trajectory, traj_test=transformed)

        np.testing.assert_almost_equal(deviations.bias_along, parameters.lever_x.value)
        np.testing.assert_almost_equal(deviations.bias_cross_h, parameters.lever_y.value)
        np.testing.assert_almost_equal(deviations.bias_cross_v, parameters.lever_z.value)

    def test_xyz_deviations(self) -> None:
        trajectory = generated_trajectory.copy()

        parameters = AlignmentParameters(
            sim_trans_x=Parameter(value=random_number(min=-1, max=1), unit=Unit.METER),
            sim_trans_y=Parameter(value=random_number(min=-1, max=1), unit=Unit.METER),
            sim_trans_z=Parameter(value=random_number(min=-1, max=1), unit=Unit.METER),
        )
        transformed = apply_alignment(
            trajectory=generated_trajectory,
            alignment_result=AlignmentResult(position_parameters=parameters),
            inplace=False,
        )

        deviations = compare_trajectories_abs(traj_ref=trajectory, traj_test=transformed)

        np.testing.assert_almost_equal(-deviations.bias_x, parameters.sim_trans_x.value)
        np.testing.assert_almost_equal(-deviations.bias_y, parameters.sim_trans_y.value)
        np.testing.assert_almost_equal(-deviations.bias_z, parameters.sim_trans_z.value)
