import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot

from trajectopy_core.evaluation.ate_result import ATEResult


def render_pos_devs(ate_result: ATEResult, ate_pos_unit: str, max_std: float = 3.0) -> str:
    comb_pos_devs = ate_result.comb_pos_devs
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=ate_result.trajectory.pos.x,
            y=ate_result.trajectory.pos.y,
            mode="lines+markers",
            marker=dict(
                color=comb_pos_devs,  # Color based on comb_pos_error
                colorscale="RdYlBu_r",  # You can choose a different color scale
                colorbar=dict(title=f"[{ate_pos_unit}]"),
                cmin=min(comb_pos_devs),
                cmax=min(np.max(comb_pos_devs), np.std(comb_pos_devs) * max_std),
            ),
        )
    )

    fig.update_layout(
        xaxis=dict(title="x [m]"),
        yaxis=dict(title="y [m]"),
        title="Position Deviations",
    )
    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )

    return plot(fig, output_type="div")


def render_rot_devs(ate_result: ATEResult, max_std: float = 3.0) -> str:
    comb_rot_devs = np.rad2deg(ate_result.comb_rot_devs)
    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=ate_result.trajectory.pos.x,
            y=ate_result.trajectory.pos.y,
            mode="lines+markers",
            marker=dict(
                color=comb_rot_devs,  # Color based on comb_pos_error
                colorscale="RdYlBu_r",  # You can choose a different color scale
                colorbar=dict(title="[°]"),
                cmin=min(comb_rot_devs),
                cmax=min(np.max(comb_rot_devs), np.std(comb_rot_devs) * max_std),
            ),
        )
    )

    fig.update_layout(
        xaxis=dict(title="x [m]"),
        yaxis=dict(title="y [m]"),
        title="Rotation Deviations",
    )
    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )

    return plot(fig, output_type="div")
