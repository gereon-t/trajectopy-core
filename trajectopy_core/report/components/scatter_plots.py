import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot

from trajectopy_core.report.data import ReportData


def render_pos_devs(report_data: ReportData) -> str:
    comb_pos_devs = report_data.comb_pos_devs

    cbar_min = min(comb_pos_devs)
    cbar_max = min(np.max(comb_pos_devs), cbar_min + np.std(comb_pos_devs) * report_data.max_std)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=report_data.x,
            y=report_data.y,
            mode="markers",
            marker=dict(
                color=comb_pos_devs,
                colorscale="RdYlBu_r",
                colorbar=dict(title=f"[{report_data.ate_unit}]"),
                cmin=cbar_min,
                cmax=cbar_max,
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


def render_rot_devs(report_data: ReportData) -> str:
    comb_rot_devs = report_data.comb_rot_devs

    cbar_min = min(comb_rot_devs)
    cbar_max = min(np.max(comb_rot_devs), cbar_min + np.std(comb_rot_devs) * report_data.max_std)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=report_data.x,
            y=report_data.y,
            mode="markers",
            marker=dict(
                color=comb_rot_devs,
                colorscale="RdYlBu_r",
                colorbar=dict(title="[°]"),
                cmin=cbar_min,
                cmax=cbar_max,
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
