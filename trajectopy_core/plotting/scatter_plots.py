"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot

from trajectopy_core.report.data import ReportData


def render_pos_devs(report_data: ReportData) -> str:
    comb_pos_devs = report_data.comb_dev_pos

    cbar_min = min(comb_pos_devs)
    cbar_max = min(np.max(comb_pos_devs), cbar_min + np.std(comb_pos_devs) * report_data.settings.scatter_max_std)

    fig = go.Figure()
    plotting_dim = len(report_data.settings.scatter_axis_order)
    pos_axes, pos_axis_labels, axes_indices = setup_pos_axis_indices(report_data)
    if plotting_dim == 2:
        fig.add_trace(
            go.Scatter(
                x=pos_axes[axes_indices[0]],
                y=pos_axes[axes_indices[1]],
                mode=report_data.settings.scatter_mode,
                marker=dict(
                    color=comb_pos_devs,
                    colorscale=report_data.settings.scatter_colorscale,
                    colorbar=dict(title=f"[{report_data.ate_unit}]"),
                    cmin=cbar_min,
                    cmax=cbar_max,
                    size=report_data.settings.scatter_marker_size,
                ),
            )
        )
    elif plotting_dim == 3:
        fig.add_trace(
            go.Scatter3d(
                x=pos_axes[axes_indices[0]],
                y=pos_axes[axes_indices[1]],
                z=pos_axes[axes_indices[2]],
                mode=report_data.settings.scatter_mode,
                marker=dict(
                    color=comb_pos_devs,
                    colorscale=report_data.settings.scatter_colorscale,
                    colorbar=dict(title=f"[{report_data.ate_unit}]"),
                    cmin=cbar_min,
                    cmax=cbar_max,
                    size=report_data.settings.scatter_marker_size,
                ),
            )
        )
    else:
        raise ValueError(f"Invalid dimension {plotting_dim}.")

    fig.update_layout(
        xaxis=dict(title=pos_axis_labels[axes_indices[0]]),
        yaxis=dict(title=pos_axis_labels[axes_indices[1]]),
        title="Position Deviations",
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

    return plot(fig, output_type="div", config=report_data.settings.single_plot_export.to_config())


def setup_pos_axis_indices(report_data: ReportData) -> tuple[list[np.ndarray], list[str], list[int]]:
    pos_axes = [report_data.pos_x, report_data.pos_y, report_data.pos_z]
    pos_axis_labels = [
        f"{report_data.settings.pos_x_name} [{report_data.settings.pos_x_unit}]",
        f"{report_data.settings.pos_y_name} [{report_data.settings.pos_y_unit}]",
        f"{report_data.settings.pos_z_name} [{report_data.settings.pos_z_unit}]",
    ]
    axes = ["x", "y", "z"]
    axes_indices = [axes.index(ax_char) for ax_char in report_data.settings.scatter_axis_order]
    return pos_axes, pos_axis_labels, axes_indices


def render_rot_devs(report_data: ReportData) -> str:
    comb_rot_devs = report_data.comb_dev_rot

    cbar_min = min(comb_rot_devs)
    cbar_max = min(np.max(comb_rot_devs), cbar_min + np.std(comb_rot_devs) * report_data.settings.scatter_max_std)

    fig = go.Figure()
    plotting_dim = len(report_data.settings.scatter_axis_order)
    pos_axes, pos_axis_labels, axes_indices = setup_pos_axis_indices(report_data)
    if plotting_dim == 2:
        fig.add_trace(
            go.Scatter(
                x=pos_axes[axes_indices[0]],
                y=pos_axes[axes_indices[1]],
                mode=report_data.settings.scatter_mode,
                marker=dict(
                    color=comb_rot_devs,
                    colorscale=report_data.settings.scatter_colorscale,
                    colorbar=dict(title=f"[{report_data.settings.rot_unit}]"),
                    cmin=cbar_min,
                    cmax=cbar_max,
                    size=report_data.settings.scatter_marker_size,
                ),
            )
        )
    elif plotting_dim == 3:
        fig.add_trace(
            go.Scatter3d(
                x=pos_axes[axes_indices[0]],
                y=pos_axes[axes_indices[1]],
                z=pos_axes[axes_indices[2]],
                mode=report_data.settings.scatter_mode,
                marker=dict(
                    color=comb_rot_devs,
                    colorscale=report_data.settings.scatter_colorscale,
                    colorbar=dict(title=f"[{report_data.settings.rot_unit}]"),
                    cmin=cbar_min,
                    cmax=cbar_max,
                    size=report_data.settings.scatter_marker_size,
                ),
            )
        )
    else:
        raise ValueError(f"Invalid dimension {plotting_dim}.")

    fig.update_layout(
        xaxis=dict(title=pos_axis_labels[axes_indices[0]]),
        yaxis=dict(title=pos_axis_labels[axes_indices[1]]),
        title="Rotation Deviations",
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

    return plot(fig, output_type="div", config=report_data.settings.single_plot_export.to_config())
