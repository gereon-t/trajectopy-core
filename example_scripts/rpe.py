import logging

from matplotlib import pyplot as plt
from rich.console import Console
from rich.logging import RichHandler
from rich.table import Table

from trajectopy_core.evaluation.comparison import compare_trajectories_relative
from trajectopy_core.evaluation.matching import match_trajectories
from trajectopy_core.evaluation.settings import MatchingMethod, MatchingSettings, RelativeComparisonSettings
from trajectopy_core.plotting.deviation_plot import plot_rpe
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

    # Compute RPE
    settings = RelativeComparisonSettings()  # Default settings
    rpe_result = compare_trajectories_relative(traj_ref=gt_traj, traj_test=est_traj, settings=settings)
    console.print(dict_to_table(rpe_result.property_dict))

    # Plot
    plot_rpe(rpe_result)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
