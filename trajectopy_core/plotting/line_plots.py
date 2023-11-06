import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
from plotly.subplots import make_subplots

from trajectopy_core.report.data import ReportData


def render_dev_edf(report_data: ReportData) -> str:
    if report_data.has_ate_orientation:
        fig = make_subplots(rows=2, cols=1)
    else:
        fig = make_subplots(rows=1, cols=1)

    sorted_comb_pos_dev = np.sort(report_data.comb_dev_pos)
    pos_norm_cdf = np.arange(len(sorted_comb_pos_dev)) / float(len(sorted_comb_pos_dev))
    fig.add_trace(go.Scatter(x=sorted_comb_pos_dev, y=pos_norm_cdf, mode="lines", name="position"), row=1, col=1)

    if report_data.has_ate_orientation:
        sorted_comb_rot_dev = np.sort(report_data.comb_dev_rot)
        rot_norm_cdf = np.arange(len(sorted_comb_rot_dev)) / float(len(sorted_comb_rot_dev))
        fig.add_trace(go.Scatter(x=sorted_comb_rot_dev, y=rot_norm_cdf, mode="lines", name="rotation"), row=2, col=1)
        fig.update_xaxes(title_text="[deg]", row=2, col=1)
        fig.update_yaxes(title_text="CDF", row=2, col=1)

    fig.update_layout(title="Cummulative Probability", height=540 if report_data.has_ate_orientation else 400)
    fig.update_xaxes(title_text=f"[{report_data.ate_unit}]", row=1, col=1)
    fig.update_yaxes(title_text="CDF", row=1, col=1)

    return plot(fig, output_type="div", config=report_data.settings.png_export.to_config())


def render_pos_time_plot(report_data: ReportData) -> str:
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
    fig.add_trace(
        go.Scatter(x=report_data.function_of, y=report_data.pos_x, mode="lines+markers", name="x"),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=report_data.function_of, y=report_data.pos_y, mode="lines+markers", name="y"),
        row=2,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=report_data.function_of, y=report_data.pos_z, mode="lines+markers", name="z"),
        row=3,
        col=1,
    )

    fig.update_layout(title="Position Components", height=750)

    fig.update_xaxes(title_text=report_data.function_of_label, row=3, col=1)
    fig.update_yaxes(title_text="[m]", row=1, col=1)
    fig.update_yaxes(title_text="[m]", row=2, col=1)
    fig.update_yaxes(title_text="[m]", row=3, col=1)

    return plot(fig, output_type="div", config=report_data.settings.png_export.to_config())


def render_rot_time_plot(report_data: ReportData) -> str:
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
    fig.add_trace(
        go.Scatter(x=report_data.function_of, y=report_data.roll, mode="lines+markers", name="roll"),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=report_data.function_of, y=report_data.pitch, mode="lines+markers", name="pitch"),
        row=2,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=report_data.function_of, y=report_data.yaw, mode="lines+markers", name="yaw"),
        row=3,
        col=1,
    )

    fig.update_layout(title="Rotation Components", height=750)

    fig.update_xaxes(title_text=report_data.function_of_label, row=3, col=1)
    fig.update_yaxes(title_text="[deg]", row=1, col=1)
    fig.update_yaxes(title_text="[deg]", row=2, col=1)
    fig.update_yaxes(title_text="[deg]", row=3, col=1)

    return plot(fig, output_type="div", config=report_data.settings.png_export.to_config())


def render_dev_pos_time_plot(report_data: ReportData) -> str:
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
    fig.add_trace(
        go.Scatter(
            x=report_data.function_of, y=report_data.pos_dev_x, mode="lines+markers", name=report_data.pos_dev_x_name
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=report_data.function_of, y=report_data.pos_dev_y, mode="lines+markers", name=report_data.pos_dev_y_name
        ),
        row=2,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=report_data.function_of, y=report_data.pos_dev_z, mode="lines+markers", name=report_data.pos_dev_z_name
        ),
        row=3,
        col=1,
    )

    fig.update_layout(title="Position Deviations per Direction", height=750)

    fig.update_xaxes(title_text=report_data.function_of_label, row=3, col=1)
    fig.update_yaxes(title_text=f"[{report_data.ate_unit}]", row=1, col=1)
    fig.update_yaxes(title_text=f"[{report_data.ate_unit}]", row=2, col=1)
    fig.update_yaxes(title_text=f"[{report_data.ate_unit}]", row=3, col=1)

    return plot(fig, output_type="div", config=report_data.settings.png_export.to_config())


def render_dev_rot_time_plot(report_data: ReportData) -> str:
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True)

    fig.add_trace(
        go.Scatter(x=report_data.function_of, y=report_data.rot_dev_x, mode="lines+markers", name="roll"),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=report_data.function_of, y=report_data.rot_dev_y, mode="lines+markers", name="pitch"),
        row=2,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=report_data.function_of, y=report_data.rot_dev_z, mode="lines+markers", name="yaw"),
        row=3,
        col=1,
    )

    fig.update_layout(title="Rotation Deviations per Axis", height=750)
    fig.update_xaxes(title_text=report_data.function_of_label, row=3, col=1)
    fig.update_yaxes(title_text="[deg]", row=1, col=1)
    fig.update_yaxes(title_text="[deg]", row=2, col=1)
    fig.update_yaxes(title_text="[deg]", row=3, col=1)

    return plot(fig, output_type="div", config=report_data.settings.png_export.to_config())


def render_dev_sum_line_plot(report_data: ReportData) -> str:
    if report_data.has_ate_orientation:
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
    else:
        fig = make_subplots(rows=1, cols=1)

    fig.add_trace(
        go.Scatter(
            x=report_data.function_of,
            y=report_data.comb_dev_pos,
            mode="lines+markers",
            name="position",
        ),
        row=1,
        col=1,
    )

    if report_data.has_ate_orientation:
        fig.add_trace(
            go.Scatter(
                x=report_data.function_of,
                y=report_data.comb_dev_rot,
                mode="lines+markers",
                name="rotation",
            ),
            row=2,
            col=1,
        )
        fig.update_yaxes(title_text="[deg]", row=2, col=1)

    fig.update_layout(title="Trajectory Deviations", height=540 if report_data.has_ate_orientation else 400)

    fig.update_xaxes(title_text=report_data.function_of_label, row=2 if report_data.has_ate_orientation else 1, col=1)
    fig.update_yaxes(title_text=f"[{report_data.ate_unit}]", row=1, col=1)

    return plot(fig, output_type="div", config=report_data.settings.png_export.to_config())


def render_rpe(report_data: ReportData) -> str:
    rpe_result = report_data.rpe_result
    if rpe_result is None:
        return ""

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
    fig.add_trace(
        go.Scatter(
            x=rpe_result.mean_distances,
            y=rpe_result.mean_pos_devs,
            mode="lines+markers",
            name="position",
            error_y=dict(
                type="data",
                array=rpe_result.pos_stds,
                visible=True,
            ),
        ),
        row=1,
        col=1,
    )

    if rpe_result.has_rot_dev:
        fig.add_trace(
            go.Scatter(
                x=rpe_result.mean_distances,
                y=np.rad2deg(rpe_result.mean_rot_devs),
                mode="lines+markers",
                name="rotation",
                error_y=dict(
                    type="data",
                    array=np.rad2deg(rpe_result.rot_stds),
                    visible=True,
                ),
            ),
            row=2,
            col=1,
        )
        fig.update_yaxes(title_text=f"[{rpe_result.rot_drift_unit}]", row=2, col=1)

    fig.update_layout(title="Relative Pose Error", height=540 if rpe_result.has_rot_dev else 400)
    fig.update_yaxes(title_text=f"[{rpe_result.pos_drift_unit}]", row=1, col=1)
    fig.update_xaxes(
        title_text=f"Pose Distance [{rpe_result.pose_distance_unit}]", row=2 if rpe_result.has_rot_dev else 1, col=1
    )

    return plot(fig, output_type="div", config=report_data.settings.png_export.to_config())
