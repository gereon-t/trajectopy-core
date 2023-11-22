import logging

from trajectopy_core.pipelines import ate, rpe
from trajectopy_core.report.single import render_single_report
from trajectopy_core.report.utils import show_report, write_report
from trajectopy_core.settings.processing import ProcessingSettings
from trajectopy_core.trajectory import Trajectory

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)


def main():
    # Import
    gt_traj = Trajectory.from_file("./example_data/KITTI_gt.traj")
    est_traj = Trajectory.from_file("./example_data/KITTI_ORB.traj")

    # default settings
    settings = ProcessingSettings()

    ate_result = ate(trajectory_gt=gt_traj, trajectory_est=est_traj, settings=settings)
    rpe_result = rpe(trajectory_gt=gt_traj, trajectory_est=est_traj, settings=settings)

    report = render_single_report(ate_result=ate_result, rpe_result=rpe_result)
    # write_report(output_file="report.html", report_text=report)
    show_report(report_text=report)


if __name__ == "__main__":
    main()
