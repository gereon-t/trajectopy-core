import logging

from matplotlib import pyplot as plt
from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table

from trajectopy_core.alignment.actions import align_trajectories, apply_alignment
from trajectopy_core.alignment.settings import AlignmentEstimationSettings, AlignmentSettings
from trajectopy_core.evaluation.comparison import compare_trajectories_absolute
from trajectopy_core.evaluation.matching import match_trajectories
from trajectopy_core.evaluation.settings import MatchingMethod, MatchingSettings
from trajectopy_core.plotting.deviation_plot import (
    plot_compact_hist,
    plot_combined_devs,
    plot_dof_dev,
    plot_raw_position_devs,
)
from trajectopy_core.trajectory import Trajectory

logging.basicConfig(
    format="%(message)s",
    level=logging.INFO,
    handlers=[RichHandler(omit_repeated_times=False, log_time_format="%Y-%m-%d %H:%M:%S")],
)


def dict_to_table(data: dict):
    """Converts a dictionary to a rich table."""
    table_data = Table(title="ATE Results")
    table_data.add_column("Property")
    table_data.add_column("Value")
    for key, value in data.items():
        table_data.add_row(key, str(value))
    return table_data


def main():
    console = Console()

    # Import
    gt_traj = Trajectory.from_file("./example_data/KITTI_gt.traj")
    est_traj = Trajectory.from_file("./example_data/KITTI_ORB.traj")

    # Match (not necessary in this particular case, but for demonstration purposes)
    matching_settings = MatchingSettings(method=MatchingMethod.NEAREST_TEMPORAL)  # Default settings
    match_trajectories(traj_test=est_traj, traj_ref=gt_traj, settings=matching_settings)  # in-place by default

    # Align
    alignment_settings = AlignmentSettings(
        estimation_of=AlignmentEstimationSettings.all(sensor_rotation=False)
    )  # Default settings
    alignment = align_trajectories(
        traj_from=est_traj,
        traj_to=gt_traj,
        alignment_settings=alignment_settings,
        matching_settings=MatchingSettings(method=MatchingMethod.NEAREST_TEMPORAL),
    )
    est_traj_aligned = apply_alignment(trajectory=est_traj, alignment_result=alignment, inplace=False)

    # Compute ATE
    ate_result = compare_trajectories_absolute(traj_ref=gt_traj, traj_test=est_traj_aligned)
    console.print(dict_to_table(ate_result.property_dict))

    # Plot
    plot_compact_hist(ate_result)
    plot_combined_devs(ate_result)
    plot_dof_dev(ate_result)
    plot_raw_position_devs(ate_result)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
