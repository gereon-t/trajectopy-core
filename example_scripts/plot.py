from matplotlib import pyplot as plt
from trajectopy_core.plotting.trajectory_plot import plot_trajectories
from trajectopy_core.trajectory import Trajectory


def main():
    # Import
    gt_traj = Trajectory.from_file("./example_data/KITTI_gt.traj")
    est_traj = Trajectory.from_file("./example_data/KITTI_ORB.traj")

    # Plot
    plot_trajectories([gt_traj, est_traj], dim=2)
    plt.show()


if __name__ == "__main__":
    main()
