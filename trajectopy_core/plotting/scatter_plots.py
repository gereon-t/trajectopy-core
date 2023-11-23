"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot

from trajectopy_core.report.data import ReportData
from trajectopy_core.settings.report import ReportSettings


def setup_pos_axis_indices(report_settings: ReportSettings) -> tuple[list[str], list[int]]:
    pos_axis_labels = [
        f"{report_settings.pos_x_name} [{report_settings.pos_x_unit}]",
        f"{report_settings.pos_y_name} [{report_settings.pos_y_unit}]",
        f"{report_settings.pos_z_name} [{report_settings.pos_z_unit}]",
    ]
    axes = ["x", "y", "z"]
    axes_indices = [axes.index(ax_char) for ax_char in report_settings.scatter_axis_order]
    return pos_axis_labels, axes_indices


def scatter_plot(
    pos: np.ndarray, colors: np.ndarray, report_settings: ReportSettings, figure_title: str, colorbar_title: str
) -> str:
    cbar_min = min(colors)
    cbar_max = min(np.max(colors), cbar_min + np.std(colors) * report_settings.scatter_max_std)

    fig = go.Figure()
    plotting_dim = len(report_settings.scatter_axis_order)
    pos_axis_labels, axes_indices = setup_pos_axis_indices(report_settings)
    if plotting_dim == 2:
        fig.add_trace(
            go.Scatter(
                x=pos[:, axes_indices[0]],
                y=pos[:, axes_indices[1]],
                mode=report_settings.scatter_mode,
                marker=dict(
                    color=colors,
                    colorscale=report_settings.scatter_colorscale,
                    colorbar=dict(title=colorbar_title),
                    cmin=cbar_min,
                    cmax=cbar_max,
                    size=report_settings.scatter_marker_size,
                ),
            )
        )
    elif plotting_dim == 3:
        fig.add_trace(
            go.Scatter3d(
                x=pos[:, axes_indices[0]],
                y=pos[:, axes_indices[1]],
                z=pos[:, axes_indices[2]],
                mode=report_settings.scatter_mode,
                marker=dict(
                    color=colors,
                    colorscale=report_settings.scatter_colorscale,
                    colorbar=dict(title=colorbar_title),
                    cmin=cbar_min,
                    cmax=cbar_max,
                    size=report_settings.scatter_marker_size,
                ),
            )
        )
    else:
        raise ValueError(f"Invalid dimension {plotting_dim}.")

    fig.update_layout(
        xaxis=dict(title=pos_axis_labels[axes_indices[0]]),
        yaxis=dict(title=pos_axis_labels[axes_indices[1]]),
        title=figure_title,
    )

    if plotting_dim == 3:
        fig.update_layout(
            scene=dict(
                aspectmode="data",
                xaxis=dict(title=pos_axis_labels[axes_indices[0]]),
                yaxis=dict(title=pos_axis_labels[axes_indices[1]]),
                zaxis=dict(title=pos_axis_labels[axes_indices[2]]),
            ),
        )

    fig.update_yaxes(
        scaleanchor="x",
        scaleratio=1,
    )

    return plot(fig, output_type="div", config=report_settings.single_plot_export.to_config())


def render_pos_devs(report_data: ReportData) -> str:
    comb_pos_devs = report_data.comb_dev_pos

    return scatter_plot(
        pos=np.c_[report_data.pos_x, report_data.pos_y, report_data.pos_z],
        colors=comb_pos_devs,
        report_settings=report_data.settings,
        figure_title="Position Deviations",
        colorbar_title=f"[{report_data.ate_unit}]",
    )


def render_rot_devs(report_data: ReportData) -> str:
    comb_rot_devs = report_data.comb_dev_rot

    return scatter_plot(
        pos=np.c_[report_data.pos_x, report_data.pos_y, report_data.pos_z],
        colors=comb_rot_devs,
        report_settings=report_data.settings,
        figure_title="Rotation Deviations",
        colorbar_title=f"[{report_data.settings.rot_unit}]",
    )
