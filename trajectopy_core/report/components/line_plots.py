import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
from plotly.subplots import make_subplots

from trajectopy_core.report.data import ReportData


def render_pos_time_plot(report_data: ReportData) -> str:
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
    fig.add_trace(
        go.Scatter(x=report_data.function_of, y=report_data.along, mode="lines+markers", name="along"),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=report_data.function_of, y=report_data.cross_h, mode="lines+markers", name="cross-h"),
        row=2,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=report_data.function_of, y=report_data.cross_v, mode="lines+markers", name="cross-v"),
        row=3,
        col=1,
    )

    fig.update_layout(
        title="Position Deviations per Direction",
        height=750,
    )

    fig.update_xaxes(title_text=report_data.function_of_unit, row=3, col=1)
    fig.update_yaxes(title_text=f"[{report_data.ate_unit}]", row=1, col=1)
    fig.update_yaxes(title_text=f"[{report_data.ate_unit}]", row=2, col=1)
    fig.update_yaxes(title_text=f"[{report_data.ate_unit}]", row=3, col=1)

    return plot(fig, output_type="div")


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

    fig.update_layout(
        title="Rotation Deviations per Axis",
        height=750,
    )
    fig.update_xaxes(title_text=report_data.function_of_unit, row=3, col=1)
    fig.update_yaxes(title_text="[°]", row=1, col=1)
    fig.update_yaxes(title_text="[°]", row=2, col=1)
    fig.update_yaxes(title_text="[°]", row=3, col=1)

    return plot(fig, output_type="div")


def render_sum_line_plot(report_data: ReportData) -> str:
    if report_data.has_ate_orientation:
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
    else:
        fig = make_subplots(rows=1, cols=1)

    fig.add_trace(
        go.Scatter(
            x=report_data.function_of,
            y=report_data.comb_pos_devs,
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
                y=report_data.comb_rot_devs,
                mode="lines+markers",
                name="rotation",
            ),
            row=2,
            col=1,
        )
        fig.update_yaxes(title_text="[°]", row=2, col=1)

    fig.update_layout(
        title="Trajectory Deviations",
        height=540 if report_data.has_ate_orientation else 400,
    )

    fig.update_xaxes(title_text=report_data.function_of_unit, row=2 if report_data.has_ate_orientation else 1, col=1)
    fig.update_yaxes(title_text=f"[{report_data.ate_unit}]", row=1, col=1)

    return plot(fig, output_type="div")


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

    return plot(fig, output_type="div")
