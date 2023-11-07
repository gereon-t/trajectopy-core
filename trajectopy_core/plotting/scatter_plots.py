import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot

from trajectopy_core.report.data import ReportData


def render_pos_devs(report_data: ReportData) -> str:
    comb_pos_devs = report_data.comb_dev_pos

    cbar_min = min(comb_pos_devs)
    cbar_max = min(np.max(comb_pos_devs), cbar_min + np.std(comb_pos_devs) * report_data.settings.scatter_max_std)

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=report_data.pos_x,
            y=report_data.pos_y,
            mode=report_data.settings.scatter_mode,
            marker=dict(
                color=comb_pos_devs,
                colorscale=report_data.settings.scatter_colorscale,
                colorbar=dict(title=f"[{report_data.ate_unit}]"),
                cmin=cbar_min,
                cmax=cbar_max,
            ),
        )
    )

    fig.update_layout(
        xaxis=dict(title=f"{report_data.settings.pos_x_name} [{report_data.settings.pos_x_unit}]"),
        yaxis=dict(title=f"{report_data.settings.pos_y_name} [{report_data.settings.pos_y_unit}]"),
        title="Position Deviations",
    )
    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )

    return plot(fig, output_type="div", config=report_data.settings.single_plot_export.to_config())


def render_rot_devs(report_data: ReportData) -> str:
    comb_rot_devs = report_data.comb_dev_rot

    cbar_min = min(comb_rot_devs)
    cbar_max = min(np.max(comb_rot_devs), cbar_min + np.std(comb_rot_devs) * report_data.settings.scatter_max_std)

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=report_data.pos_x,
            y=report_data.pos_y,
            mode=report_data.settings.scatter_mode,
            marker=dict(
                color=comb_rot_devs,
                colorscale=report_data.settings.scatter_colorscale,
                colorbar=dict(title=f"[{report_data.settings.rot_unit}]"),
                cmin=cbar_min,
                cmax=cbar_max,
            ),
        )
    )

    fig.update_layout(
        xaxis=dict(title=f"{report_data.settings.pos_x_name} [{report_data.settings.pos_x_unit}]"),
        yaxis=dict(title=f"{report_data.settings.pos_y_name} [{report_data.settings.pos_y_unit}]"),
        title="Rotation Deviations",
    )
    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )

    return plot(fig, output_type="div", config=report_data.settings.single_plot_export.to_config())
