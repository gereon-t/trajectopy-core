from trajectopy_core.report.trajectory import render_trajectories
from trajectopy_core.report.utils import show_report
from trajectopy_core.settings.report import ReportSettings
from trajectopy_core.trajectory import Trajectory


def main():
    # Import
    gt_traj = Trajectory.from_file("./example_data/KITTI_gt.traj")
    est_traj = Trajectory.from_file("./example_data/KITTI_ORB.traj")

    report_settings = ReportSettings(scatter_axis_order="xy", ate_unit_is_mm=False)
    traj_report = render_trajectories(trajectories=[gt_traj, est_traj], report_settings=report_settings)
    show_report(traj_report, filepath="report.html")


if __name__ == "__main__":
    main()
