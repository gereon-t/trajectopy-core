"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging

from trajectopy_core.alignment.data import AlignmentData
from trajectopy_core.alignment.ghm_estimation import Alignment
from trajectopy_core.alignment.parameters import SensorRotationParameters
from trajectopy_core.alignment.result import AlignmentResult
from trajectopy_core.alignment.rotation_alignment import align_rotations
from trajectopy_core.settings.alignment_settings import AlignmentSettings
from trajectopy_core.settings.matching_settings import MatchingSettings
from trajectopy_core.trajectory import Trajectory
from trajectopy_core.util.rotationset import RotationSet

logger = logging.getLogger("root")


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
    alignment_settings: AlignmentSettings,
    matching_settings: MatchingSettings,
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
        and not alignment_settings.estimation_of.helmert
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
    ghm_alignment = Alignment(alignment_data=alignment_data)
    estimated_parameters = ghm_alignment.estimate()

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
    )
