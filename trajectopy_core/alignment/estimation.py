"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

import logging

from trajectopy_core.alignment.ghm.data import AlignmentData
from trajectopy_core.alignment.ghm.estimation import Alignment
from trajectopy_core.alignment.parameters import SensorRotationParameters
from trajectopy_core.alignment.result import AlignmentResult
from trajectopy_core.alignment.rotation_alignment import align_rotations
from trajectopy_core.settings.alignment import AlignmentSettings
from trajectopy_core.settings.matching import MatchingSettings
from trajectopy_core.trajectory import Trajectory

logger = logging.getLogger("root")


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
        alignment_settings (AlignmentSettings, optional): Settings for the alignment process. Defaults to AlignmentSettings().
        matching_settings (MatchingSettings, optional): Settings for the matching process. Defaults to MatchingSettings().

    Returns:
        AlignmentResult: Result of the alignment process
    """
    logger.info("Aligning trajectory positions ...")

    alignment_data = AlignmentData(
        traj_from=traj_from,
        traj_to=traj_to,
        alignment_settings=alignment_settings,
        matching_settings=matching_settings,
    )
    ghm_alignment = Alignment(alignment_data=alignment_data)
    estimated_parameters = ghm_alignment.estimate_parameters()

    if (
        alignment_data.traj_from.rot is not None
        and alignment_data.traj_to.rot is not None
        and alignment_settings.estimation_settings.sensor_rotation
    ):
        pre_aligned_trajectory = alignment_data.traj_from.apply_transformation(
            estimated_parameters.sim3_matrix, inplace=False
        )
        logger.info("Aligning rotations ...")
        sensor_rot_params = align_rotations(rot_from=pre_aligned_trajectory.rot, rot_to=alignment_data.traj_to.rot)
        print(sensor_rot_params)
    else:
        sensor_rot_params = SensorRotationParameters(enabled=False)

    return AlignmentResult(
        name=f"{alignment_data.traj_from.name} to {alignment_data.traj_to.name}",
        position_parameters=estimated_parameters,
        rotation_parameters=sensor_rot_params,
        estimation_of=ghm_alignment.settings.estimation_settings,
        converged=ghm_alignment.has_results,
    )
