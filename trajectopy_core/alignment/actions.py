"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from typing import Tuple

import numpy as np

from trajectopy_core.alignment.ghm.data import AlignmentData
from trajectopy_core.alignment.ghm.estimation import Alignment
from trajectopy_core.alignment.ghm.functional_model.equations import leverarm_time_component
from trajectopy_core.alignment.parameters import AlignmentParameters, SensorRotationParameters
from trajectopy_core.alignment.result import AlignmentResult
from trajectopy_core.alignment.rotation_alignment import align_rotations
from trajectopy_core.rotationset import RotationSet
from trajectopy_core.settings.alignment import AlignmentSettings, AlignmentStochastics
from trajectopy_core.settings.matching import MatchingSettings
from trajectopy_core.trajectory import Trajectory

logger = logging.getLogger("root")


def apply_alignment(
    *, trajectory: Trajectory, alignment_result: AlignmentResult, inplace: bool = True
) -> "Trajectory":
    """Transforms trajectory using alignment parameters.

    After computing the alignment parameters needed to align
    two trajectories, they can be applied to arbitrary trajectories.

    Args:
        alignment_result (AlignmentResult)
        inplace (bool, optional): Perform in-place. Defaults to True.

    Returns:
        Trajectory: Aligned trajectory
    """
    trajectory = trajectory if inplace else trajectory.copy()

    # leverarm and time
    (
        euler_x,
        euler_y,
        euler_z,
        lever_x,
        lever_y,
        lever_z,
    ) = _prepare_alignment_application(trajectory, alignment_result.position_parameters)

    speed_3d = trajectory.speed_3d
    speed_x, speed_y, speed_z = speed_3d[:, 0], speed_3d[:, 1], speed_3d[:, 2]

    trafo_x, trafo_y, trafo_z = leverarm_time_component(
        euler_x=euler_x,
        euler_y=euler_y,
        euler_z=euler_z,
        lever_x=lever_x,
        lever_y=lever_y,
        lever_z=lever_z,
        time_shift=alignment_result.position_parameters.time_shift.value,
        speed_x=speed_x,
        speed_y=speed_y,
        speed_z=speed_z,
    )
    trajectory.pos.xyz += np.c_[trafo_x, trafo_y, trafo_z]

    # similiarity transformation
    trajectory.apply_transformation(alignment_result.position_parameters.sim3_matrix)

    logger.info("Applied alignment parameters to positions.")

    # sensor orientation
    if trajectory.rot is not None:
        trajectory.rot = alignment_result.rotation_parameters.rotation_set * trajectory.rot
        logger.info("Applied alignment parameters to orientations.")

    return trajectory


def _prepare_alignment_application(
    trajectory: Trajectory, alignment_parameters: AlignmentParameters
) -> Tuple[float, ...]:
    if trajectory.rot is not None:
        rpy = trajectory.rot.as_euler("xyz", degrees=False)
        euler_x, euler_y, euler_z = rpy[:, 0], rpy[:, 1], rpy[:, 2]
        lever_x, lever_y, lever_z = (
            alignment_parameters.lever_x.value,
            alignment_parameters.lever_y.value,
            alignment_parameters.lever_z.value,
        )
    else:
        logger.error("Trajectory has no orientations. Cannot apply leverarm.")
        euler_x, euler_y, euler_z = 0, 0, 0
        lever_x, lever_y, lever_z = 0, 0, 0

    return euler_x, euler_y, euler_z, lever_x, lever_y, lever_z


def adopt_first_pose(*, traj_from: Trajectory, traj_to: Trajectory) -> Trajectory:
    """Transform trajectory so that the first pose is identical in both

    Args:
        traj_from (Trajectory): Trajectory to be transformed
        traj_to (Trajectory): Target Trajectory

    Returns:
        Trajectory: Transformed trajectory
    """
    adopt_first_position(traj_from=traj_from, traj_to=traj_to)
    adopt_first_orientation(traj_from=traj_from, traj_to=traj_to)
    traj_from.state.aligned = True
    return traj_from


def adopt_first_position(*, traj_from: Trajectory, traj_to: Trajectory) -> Trajectory:
    """Transform trajectory so that the first position is identical in both

    Args:
        traj_from (Trajectory): Trajectory to be transformed
        traj_to (Trajectory): Target Trajectory

    Returns:
        Trajectory: Transformed trajectory
    """
    position_difference = traj_to.pos.xyz[0, :] - traj_from.pos.xyz[0, :]
    traj_from.pos.xyz += position_difference
    return traj_from


def adopt_first_orientation(*, traj_from: Trajectory, traj_to: Trajectory) -> Trajectory:
    """Transform trajectory so that the first orientation is identical in both

    Args:
        traj_from (Trajectory): Trajectory to be transformed
        traj_to (Trajectory): Target Trajectory

    Returns:
        Trajectory: Transformed trajectory
    """
    if traj_from.rot is not None and traj_to.rot is not None:
        rpy_from = traj_from.rot.as_euler(seq="xyz")
        rotation_difference = traj_to.rot.as_euler(seq="xyz")[0, :] - rpy_from[0, :]

        traj_from.rot = RotationSet.from_euler(seq="xyz", angles=rpy_from + rotation_difference)

    return traj_from


def align_trajectories(
    *,
    traj_from: Trajectory,
    traj_to: Trajectory,
    alignment_settings: AlignmentSettings = AlignmentSettings(),
    matching_settings: MatchingSettings = MatchingSettings(),
) -> AlignmentResult:
    """Aligns two trajectories

    Performs a
    - Helmert
    - Leverarm
    - Time shift

    estimation depending on the configuration.
    After this, the estimated parameters are applied
    to the 'traj_from' trajectory.

    Args:
        traj_from (Trajectory)
        traj_to (Trajectory)
        alignment_config (AlignmentConfig): Configuration holding all
                                            relevant settings for aligning
                                            the trajectories.

    Returns:
        Tuple[Trajectory, Trajectory]: Aligned trajectories
    """
    # one of the trajectories is in an unknown datum
    if (
        None in [traj_to.pos.local_transformer, traj_to.pos.local_transformer]
        and not alignment_settings.estimation_of.helmert_enabled
    ):
        print(
            "\n ____________________________________________________\n"
            "| --------------------- WARNING --------------------- |\n"
            f"| {'One of the trajectories is in an unknown datum.':<51} |\n"
            f"| {'However, according to the configuration, no Helmert':<51} |\n"
            f"| {'transformation should be performed.':<51} |\n"
            f"| {'Consider performing a Helmert transformation.':<51} |\n"
            "|_____________________________________________________|\n"
        )
    logger.info("Aligning trajectory positions ...")

    alignment_data = AlignmentData(
        traj_from=traj_from,
        traj_to=traj_to,
        alignment_settings=alignment_settings,
        matching_settings=matching_settings,
    )

    if (
        alignment_settings.stochastics.variance_component_estimation
        and len(alignment_data) > alignment_settings.stochastics.variance_component_estimation_subset_size
    ):
        _set_group_variances(alignment_data)

    estimation_settings_changed = True
    while estimation_settings_changed:
        ghm_alignment = Alignment(alignment_data=alignment_data)
        estimated_parameters = ghm_alignment.estimate()

        if alignment_settings.estimation_of.auto_update:
            estimation_settings = ghm_alignment.updated_estimation_settings
        else:
            estimation_settings = None

        if estimation_settings is not None:
            estimation_settings_changed = True
            alignment_data.alignment_settings.estimation_of = estimation_settings
        else:
            estimation_settings_changed = False

    if (
        alignment_data.traj_from.rot is not None
        and alignment_data.traj_to.rot is not None
        and alignment_settings.estimation_of.sensor_rotation
    ):
        alignment_data.traj_from.apply_transformation(estimated_parameters.sim3_matrix)
        logger.info("Aligning rotations ...")
        sensor_rot_params = align_rotations(rot_from=alignment_data.traj_from.rot, rot_to=alignment_data.traj_to.rot)
        print(sensor_rot_params)
    else:
        sensor_rot_params = SensorRotationParameters(enabled=False)

    return AlignmentResult(
        name=f"{alignment_data.traj_from.name} to {alignment_data.traj_to.name}",
        position_parameters=estimated_parameters,
        rotation_parameters=sensor_rot_params,
        estimation_of=ghm_alignment.settings.estimation_of,
        converged=ghm_alignment.has_results,
    )


def _set_group_variances(alignment_data: AlignmentData) -> None:
    alignment_data_subset = alignment_data.get_variance_estimation_subset(
        alignment_data.alignment_settings.stochastics.variance_component_estimation_subset_size
    )
    ghm_subset_alignment = Alignment(alignment_data=alignment_data_subset)
    ghm_subset_alignment.estimate()

    group_std_dict = alignment_data.alignment_settings.stochastics.to_dict()
    group_std_dict |= {f"std_{key.lower()}": value for key, value in ghm_subset_alignment.data.group_stds.items()}
    group_std_dict |= {
        "error_probability": alignment_data.alignment_settings.stochastics.error_probability,
        "variance_component_estimation": False,
        "variance_component_estimation_subset_size": 200,
    }
    alignment_data.alignment_settings.stochastics = AlignmentStochastics.from_dict(group_std_dict)
    alignment_data.var_vector = alignment_data.build_var_vector()
