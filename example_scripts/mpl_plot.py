import matplotlib.pyplot as plt

from trajectopy_core.alignment.estimation import estimate_alignment
from trajectopy_core.evaluation.metrics import ate, rpe
from trajectopy_core.plotting.mpl.alignment_plot import plot_correlation_heatmap, plot_covariance_heatmap
from trajectopy_core.plotting.mpl.deviation_plot import (
    plot_bars,
    plot_compact_hist,
    plot_deviations,
    plot_edf,
    plot_rpe,
    scatter_deviations,
)
from trajectopy_core.plotting.mpl.trajectory_plot import plot_trajectories
from trajectopy_core.trajectory import Trajectory


def main():
    gt = Trajectory.from_file("./example_data/KITTI_gt.traj")
    orb = Trajectory.from_file("./example_data/KITTI_ORB.traj")
    sptam = Trajectory.from_file("./example_data/KITTI_SPTAM.traj")
    plot_trajectories([gt, orb])

    alignment = estimate_alignment(gt, orb)
    ate_result_orb = ate(gt, orb)
    ate_result_sptam = ate(gt, sptam)
    rpe_result = rpe(gt, orb)

    # All available plotting functions
    plot_covariance_heatmap(alignment.position_parameters)
    plot_correlation_heatmap(alignment.position_parameters)

    plot_compact_hist(ate_result_orb)
    plot_deviations([ate_result_orb, ate_result_sptam])
    plot_bars([ate_result_orb, ate_result_sptam], mode="positions")
    plot_bars([ate_result_orb, ate_result_sptam], mode="rotations")

    plot_edf(ate_result_orb)

    scatter_deviations(ate_result_orb)

    plot_rpe(rpe_result)

    plt.show()


if __name__ == "__main__":
    main()
