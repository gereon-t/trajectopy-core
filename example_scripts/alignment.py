from trajectopy_core.alignment.actions import align_trajectories
from trajectopy_core.report.alignment import render_heatmaps
from trajectopy_core.report.utils import show_report
from trajectopy_core.settings.processing import ProcessingSettings
from trajectopy_core.trajectory import Trajectory


def main():
    # Import
    gt_traj = Trajectory.from_file("./example_data/KITTI_gt.traj")
    est_traj = Trajectory.from_file("./example_data/KITTI_ORB.traj")

    # default settings
    settings = ProcessingSettings()

    alignment_result = align_trajectories(
        traj_from=est_traj,
        traj_to=gt_traj,
        alignment_settings=settings.alignment,
        matching_settings=settings.matching,
    )

    report = render_heatmaps(alignment_parameters=alignment_result.position_parameters, name=alignment_result.name)
    show_report(report_text=report, filepath="reports/report.html")


if __name__ == "__main__":
    main()
