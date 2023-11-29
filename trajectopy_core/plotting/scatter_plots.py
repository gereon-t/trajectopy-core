"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot

from trajectopy_core.plotting.utils import get_axis_label
from trajectopy_core.report.data import ReportData
from trajectopy_core.settings.report import ReportSettings
from trajectopy_core.trajectory import Trajectory


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
    pos: np.ndarray,
    report_settings: ReportSettings,
    figure_title: str,
    colorbar_title: str,
    colors: np.ndarray | None = None,
) -> str:
    marker_dict = get_marker_dict(report_settings, colorbar_title, colors)
    pos_axis_labels, axes_indices = setup_pos_axis_indices(report_settings)

    fig = go.Figure()

    plotting_dim = len(report_settings.scatter_axis_order)
    if plotting_dim == 2:
        fig.add_trace(
            go.Scattergl(
                x=pos[:, axes_indices[0]],
                y=pos[:, axes_indices[1]],
                mode=report_settings.scatter_mode,
                marker=marker_dict,
            )
        )
    elif plotting_dim == 3:
        fig.add_trace(
            go.Scatter3d(
                x=pos[:, axes_indices[0]],
                y=pos[:, axes_indices[1]],
                z=pos[:, axes_indices[2]],
                mode=report_settings.scatter_mode,
                marker=marker_dict,
            )
        )
    else:
        raise ValueError(f"Invalid dimension {plotting_dim}.")

    fig.update_layout(
        xaxis=dict(title=pos_axis_labels[axes_indices[0]]),
        yaxis=dict(title=pos_axis_labels[axes_indices[1]]),
        title=figure_title,
        legend=dict(font={"family": "Courier New, monospace", "size": 12, "color": "black"}),
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


def get_marker_dict(
    report_settings: ReportSettings, colorbar_title: str = "", colors: np.ndarray | None = None
) -> dict:
    if colors is None:
        return dict(size=report_settings.scatter_marker_size)
    cbar_min = min(colors)
    cbar_max = min(np.max(colors), cbar_min + np.std(colors) * report_settings.scatter_max_std)
    return dict(
        color=colors,
        colorscale=report_settings.scatter_colorscale,
        colorbar=dict(title=colorbar_title),
        cmin=cbar_min,
        cmax=cbar_max,
        size=report_settings.scatter_marker_size,
    )


def render_pos_devs(report_data: ReportData) -> str:
    comb_pos_devs = report_data.comb_dev_pos

    return scatter_plot(
        pos=np.c_[report_data.pos_x, report_data.pos_y, report_data.pos_z],
        colors=comb_pos_devs,
        report_settings=report_data.settings,
        figure_title="Position Deviations",
        colorbar_title=f"[{report_data.ate_unit}]",
    )


def render_pos_x_devs(report_data: ReportData) -> str:
    return scatter_plot(
        pos=np.c_[report_data.pos_x, report_data.pos_y, report_data.pos_z],
        colors=report_data.pos_dev_x,
        report_settings=report_data.settings,
        figure_title=f"{report_data.settings.pos_x_name} Deviations",
        colorbar_title=f"{report_data.settings.pos_x_name} [{report_data.settings.pos_x_unit}]",
    )


def render_pos_y_devs(report_data: ReportData) -> str:
    return scatter_plot(
        pos=np.c_[report_data.pos_x, report_data.pos_y, report_data.pos_z],
        colors=report_data.pos_dev_y,
        report_settings=report_data.settings,
        figure_title=f"{report_data.settings.pos_y_name} Deviations",
        colorbar_title=f"{report_data.settings.pos_y_name} [{report_data.settings.pos_y_unit}]",
    )


def render_pos_z_devs(report_data: ReportData) -> str:
    return scatter_plot(
        pos=np.c_[report_data.pos_x, report_data.pos_y, report_data.pos_z],
        colors=report_data.pos_dev_z,
        report_settings=report_data.settings,
        figure_title=f"{report_data.settings.pos_z_name} Deviations",
        colorbar_title=f"{report_data.settings.pos_z_name} [{report_data.settings.pos_z_unit}]",
    )


def render_rot_x_devs(report_data: ReportData) -> str:
    return scatter_plot(
        pos=np.c_[report_data.pos_x, report_data.pos_y, report_data.pos_z],
        colors=report_data.rot_dev_x,
        report_settings=report_data.settings,
        figure_title=f"{report_data.settings.rot_x_name} Deviations",
        colorbar_title=f"{report_data.settings.rot_x_name} [{report_data.settings.rot_unit}]",
    )


def render_rot_y_devs(report_data: ReportData) -> str:
    return scatter_plot(
        pos=np.c_[report_data.pos_x, report_data.pos_y, report_data.pos_z],
        colors=report_data.rot_dev_y,
        report_settings=report_data.settings,
        figure_title=f"{report_data.settings.rot_y_name} Deviations",
        colorbar_title=f"{report_data.settings.rot_y_name} [{report_data.settings.rot_unit}]",
    )


def render_rot_z_devs(report_data: ReportData) -> str:
    return scatter_plot(
        pos=np.c_[report_data.pos_x, report_data.pos_y, report_data.pos_z],
        colors=report_data.rot_dev_z,
        report_settings=report_data.settings,
        figure_title=f"{report_data.settings.rot_z_name} Deviations",
        colorbar_title=f"{report_data.settings.rot_z_name} [{report_data.settings.rot_unit}]",
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


def render_trajectories(trajectories: list[Trajectory], report_settings: ReportSettings) -> str:
    x_label, y_label, z_label = get_axis_label(trajectories=trajectories)
    pos_axis_labels = [x_label, y_label, z_label]

    marker_dict = get_marker_dict(report_settings)
    _, axes_indices = setup_pos_axis_indices(report_settings)

    fig = go.Figure()

    plotting_dim = len(report_settings.scatter_axis_order)

    for trajectory in trajectories:
        pos = trajectory.pos.xyz
        if plotting_dim == 2:
            fig.add_trace(
                go.Scattergl(
                    x=pos[:, axes_indices[0]],
                    y=pos[:, axes_indices[1]],
                    mode=report_settings.scatter_mode,
                    marker=marker_dict,
                    name=trajectory.name,
                )
            )
        elif plotting_dim == 3:
            fig.add_trace(
                go.Scatter3d(
                    x=pos[:, axes_indices[0]],
                    y=pos[:, axes_indices[1]],
                    z=pos[:, axes_indices[2]],
                    mode=report_settings.scatter_mode,
                    marker=marker_dict,
                    name=trajectory.name,
                )
            )
        else:
            raise ValueError(f"Invalid dimension {plotting_dim}.")

    fig.update_layout(
        xaxis=dict(title=pos_axis_labels[axes_indices[0]]),
        yaxis=dict(title=pos_axis_labels[axes_indices[1]]),
        title="Trajectory Plot",
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
