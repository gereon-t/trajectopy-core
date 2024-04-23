from trajectopy_core.evaluation.metrics import ate, rpe
from trajectopy_core.report.single import render_single_report
from trajectopy_core.report.utils import show_report
from trajectopy_core.settings.processing import ProcessingSettings
from trajectopy_core.settings.report import ReportSettings
from trajectopy_core.trajectory import Trajectory


def main():
    # Import
    gt_traj = Trajectory.from_file("./example_data/KITTI_gt.traj")
    est_traj = Trajectory.from_file("./example_data/KITTI_ORB.traj")

    # default settings
    settings = ProcessingSettings()

    ate_result = ate(trajectory_gt=gt_traj, trajectory_est=est_traj, settings=settings)
    rpe_result = rpe(trajectory_gt=gt_traj, trajectory_est=est_traj, settings=settings)

    report_settings = ReportSettings(ate_unit_is_mm=False, scatter_marker_size=8)
    report = render_single_report(ate_result=ate_result, rpe_result=rpe_result, report_settings=report_settings)
    show_report(report_text=report, filepath="reports/report.html")


if __name__ == "__main__":
    main()
