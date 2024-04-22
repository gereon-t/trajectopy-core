from trajectopy_core.evaluation import ate, rpe
from trajectopy_core.report.multi import render_multi_report
from trajectopy_core.report.utils import show_report
from trajectopy_core.settings.processing import ProcessingSettings
from trajectopy_core.trajectory import Trajectory


def main():
    # Import
    gt_traj = Trajectory.from_file("./example_data/KITTI_gt.traj")
    est_traj_1 = Trajectory.from_file("./example_data/KITTI_ORB.traj")
    est_traj_2 = Trajectory.from_file("./example_data/KITTI_SPTAM.traj")

    # default settings
    settings = ProcessingSettings()

    ate_result_1 = ate(trajectory_gt=gt_traj, trajectory_est=est_traj_1, settings=settings)
    rpe_result_1 = rpe(trajectory_gt=gt_traj, trajectory_est=est_traj_1, settings=settings)

    ate_result_2 = ate(trajectory_gt=gt_traj, trajectory_est=est_traj_2, settings=settings)
    rpe_result_2 = rpe(trajectory_gt=gt_traj, trajectory_est=est_traj_2, settings=settings)

    multi_report = render_multi_report(
        ate_results=[ate_result_1, ate_result_2], rpe_results=[rpe_result_1, rpe_result_2]
    )

    show_report(report_text=multi_report, filepath="reports/report.html")


if __name__ == "__main__":
    main()
