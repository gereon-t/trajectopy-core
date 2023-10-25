import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
from plotly.subplots import make_subplots

from trajectopy_core.evaluation.ate_result import ATEResult
from trajectopy_core.evaluation.rpe_result import RPEResult


def render_pos_time_plot(ate_result: ATEResult, ate_pos_unit: str) -> str:
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
    fig.add_trace(
        go.Scatter(x=ate_result.trajectory.tstamps, y=ate_result.along, mode="lines+markers", name="along"),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=ate_result.trajectory.tstamps, y=ate_result.cross_h, mode="lines+markers", name="cross-h"),
        row=2,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=ate_result.trajectory.tstamps, y=ate_result.cross_v, mode="lines+markers", name="cross-v"),
        row=3,
        col=1,
    )

    fig.update_layout(
        title="Position Deviations per Direction",
    )

    fig.update_xaxes(title_text="Time [s]", row=3, col=1)
    fig.update_yaxes(title_text=f"[{ate_pos_unit}]", row=1, col=1)
    fig.update_yaxes(title_text=f"[{ate_pos_unit}]", row=2, col=1)
    fig.update_yaxes(title_text=f"[{ate_pos_unit}]", row=3, col=1)

    return plot(fig, output_type="div")


def render_rot_time_plot(ate_result: ATEResult) -> str:
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True)

    fig.add_trace(
        go.Scatter(x=ate_result.trajectory.tstamps, y=np.rad2deg(ate_result.roll), mode="lines+markers", name="roll"),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=ate_result.trajectory.tstamps, y=np.rad2deg(ate_result.pitch), mode="lines+markers", name="pitch"
        ),
        row=2,
        col=1,
    )
    fig.add_trace(
        go.Scatter(x=ate_result.trajectory.tstamps, y=np.rad2deg(ate_result.yaw), mode="lines+markers", name="yaw"),
        row=3,
        col=1,
    )

    fig.update_layout(
        title="Rotation Deviations per Axis",
    )
    fig.update_xaxes(title_text="Time [s]", row=3, col=1)
    fig.update_yaxes(title_text="[°]", row=1, col=1)
    fig.update_yaxes(title_text="[°]", row=2, col=1)
    fig.update_yaxes(title_text="[°]", row=3, col=1)

    return plot(fig, output_type="div")


def render_sum_line_plot(ate_result: ATEResult, ate_pos_unit: str) -> str:
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True)

    fig.add_trace(
        go.Scatter(
            x=ate_result.trajectory.tstamps,
            y=ate_result.comb_pos_devs,
            mode="lines+markers",
            name="position",
        ),
        row=1,
        col=1,
    )
    fig.add_trace(
        go.Scatter(
            x=ate_result.trajectory.tstamps,
            y=np.rad2deg(ate_result.comb_rot_devs),
            mode="lines+markers",
            name="rotation",
        ),
        row=2,
        col=1,
    )

    fig.update_layout(
        title="Trajectory Deviations",
    )

    fig.update_xaxes(title_text="Time [s]", row=2, col=1)
    fig.update_yaxes(title_text=f"[{ate_pos_unit}]", row=1, col=1)
    fig.update_yaxes(title_text="[°]", row=2, col=1)

    return plot(fig, output_type="div")


def render_rpe(rpe_result: RPEResult) -> str:
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

    fig.update_layout(title="Relative Pose Error")
    fig.update_yaxes(title_text=f"[{rpe_result.pos_drift_unit}]", row=1, col=1)
    fig.update_yaxes(title_text=f"[{rpe_result.rot_drift_unit}]", row=2, col=1)
    fig.update_xaxes(title_text=f"Pose Distance [{rpe_result.pose_distance_unit}]", row=2, col=1)

    return plot(fig, output_type="div")
