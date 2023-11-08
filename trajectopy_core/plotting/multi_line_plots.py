"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

from typing import Tuple
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
from plotly.subplots import make_subplots

from trajectopy_core.report.data import ReportDataCollection


def setup_edf_axis(report_data_collection: ReportDataCollection) -> Tuple[go.Figure, dict]:
    report_data_item = report_data_collection.items[0]
    if report_data_collection.has_ate_rot:
        fig = make_subplots(rows=2, cols=1)
        height = report_data_item.settings.two_subplots_height
        config = report_data_item.settings.two_subplots_export.to_config()

        fig.update_xaxes(title_text=f"[{report_data_item.settings.rot_unit}]", row=2, col=1)
        fig.update_yaxes(title_text="CDF", row=2, col=1)
    else:
        fig = make_subplots(rows=1, cols=1)
        height = report_data_item.settings.single_plot_height
        config = report_data_item.settings.single_plot_export.to_config()

    fig.update_layout(title="Cummulative Probability", height=height)
    fig.update_xaxes(title_text=f"[{report_data_item.ate_unit}]", row=1, col=1)
    fig.update_yaxes(title_text="CDF", row=1, col=1)

    return fig, config


def render_dev_edf(report_data_collection: ReportDataCollection) -> str:
    fig, config = setup_edf_axis(report_data_collection)

    for data in report_data_collection.items:
        sorted_comb_pos_dev = np.sort(data.comb_dev_pos)
        pos_norm_cdf = np.arange(len(sorted_comb_pos_dev)) / float(len(sorted_comb_pos_dev))
        fig.add_trace(
            go.Scatter(
                x=sorted_comb_pos_dev,
                y=pos_norm_cdf,
                mode=data.settings.plot_mode,
                name=f"{data.short_name} Pos.",
            ),
            row=1,
            col=1,
        )

        if data.has_ate_rot:
            sorted_comb_rot_dev = np.sort(data.comb_dev_rot)
            rot_norm_cdf = np.arange(len(sorted_comb_rot_dev)) / float(len(sorted_comb_rot_dev))
            fig.add_trace(
                go.Scatter(
                    x=sorted_comb_rot_dev,
                    y=rot_norm_cdf,
                    mode=data.settings.plot_mode,
                    name=f"{data.short_name} Rot.",
                ),
                row=2,
                col=1,
            )
    return plot(fig, output_type="div", config=config)


def setup_dev_comb_axis(report_data_collection: ReportDataCollection) -> Tuple[go.Figure, dict]:
    report_data_item = report_data_collection.items[0]
    if report_data_collection.has_ate_rot:
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
        fig.update_xaxes(title_text=report_data_item.function_of_label, row=2, col=1)
        fig.update_yaxes(title_text=f"[{report_data_item.settings.rot_unit}]", row=2, col=1)

        config = report_data_item.settings.two_subplots_export.to_config()
        height = report_data_item.settings.two_subplots_height
    else:
        fig = make_subplots(rows=1, cols=1)
        fig.update_xaxes(title_text=report_data_item.function_of_label, row=1, col=1)

        config = report_data_item.settings.single_plot_export.to_config()
        height = report_data_item.settings.single_plot_height

    fig.update_layout(title="Trajectory Deviations", height=height)
    fig.update_yaxes(title_text=f"[{report_data_item.ate_unit}]", row=1, col=1)

    return fig, config


def render_dev_comb_plot(report_data_collection: ReportDataCollection) -> str:
    fig, config = setup_dev_comb_axis(report_data_collection)

    for data in report_data_collection.items:
        fig.add_trace(
            go.Scatter(
                x=data.function_of,
                y=data.comb_dev_pos,
                mode=data.settings.plot_mode,
                name=f"{data.short_name} Pos.",
            ),
            row=1,
            col=1,
        )

        if data.has_ate_rot:
            fig.add_trace(
                go.Scatter(
                    x=data.function_of,
                    y=data.comb_dev_rot,
                    mode=data.settings.plot_mode,
                    name=f"{data.short_name} Rot.",
                ),
                row=2,
                col=1,
            )
            fig.update_yaxes(title_text=f"[{data.settings.rot_unit}]", row=2, col=1)

    return plot(fig, output_type="div", config=config)


def setup_dev_pos_axis(report_data_collection: ReportDataCollection) -> go.Figure:
    report_data = report_data_collection.items[0]
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True)
    fig.update_layout(title="Position Deviations per Direction", height=report_data.settings.three_subplots_height)

    fig.update_xaxes(title_text=report_data.function_of_label, row=3, col=1)
    fig.update_yaxes(title_text=f"[{report_data.ate_unit}]", row=1, col=1)
    fig.update_yaxes(title_text=f"[{report_data.ate_unit}]", row=2, col=1)
    fig.update_yaxes(title_text=f"[{report_data.ate_unit}]", row=3, col=1)

    return fig


def render_dev_pos_plot(report_data_collection: ReportDataCollection) -> str:
    fig = setup_dev_pos_axis(report_data_collection)

    for data in report_data_collection.items:
        fig.add_trace(
            go.Scatter(
                x=data.function_of,
                y=data.pos_dev_x,
                mode=data.settings.plot_mode,
                name=f"{data.short_name} {data.pos_dev_x_name}",
            ),
            row=1,
            col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=data.function_of,
                y=data.pos_dev_y,
                mode=data.settings.plot_mode,
                name=f"{data.short_name} {data.pos_dev_y_name}",
            ),
            row=2,
            col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=data.function_of,
                y=data.pos_dev_z,
                mode=data.settings.plot_mode,
                name=f"{data.short_name} {data.pos_dev_z_name}",
            ),
            row=3,
            col=1,
        )

    return plot(
        fig, output_type="div", config=report_data_collection.items[0].settings.three_subplots_export.to_config()
    )


def setup_dev_rot_axis(report_data_collection: ReportDataCollection) -> go.Figure:
    report_data_item = report_data_collection.items[0]
    fig = make_subplots(rows=3, cols=1, shared_xaxes=True)

    fig.update_layout(title="Rotation Deviations per Axis", height=report_data_item.settings.three_subplots_height)
    fig.update_xaxes(title_text=report_data_item.function_of_label, row=3, col=1)
    fig.update_yaxes(title_text=f"[{report_data_item.settings.rot_unit}]", row=1, col=1)
    fig.update_yaxes(title_text=f"[{report_data_item.settings.rot_unit}]", row=2, col=1)
    fig.update_yaxes(title_text=f"[{report_data_item.settings.rot_unit}]", row=3, col=1)

    return fig


def render_dev_rot_plot(report_data_collection: ReportDataCollection) -> str:
    fig = setup_dev_rot_axis(report_data_collection)

    for data in report_data_collection.items:
        if not data.has_ate_rot:
            continue

        fig.add_trace(
            go.Scatter(
                x=data.function_of,
                y=data.rot_dev_x,
                mode=data.settings.plot_mode,
                name=f"{data.short_name} {data.settings.rot_x_name}",
            ),
            row=1,
            col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=data.function_of,
                y=data.rot_dev_y,
                mode=data.settings.plot_mode,
                name=f"{data.short_name} {data.settings.rot_y_name}",
            ),
            row=2,
            col=1,
        )
        fig.add_trace(
            go.Scatter(
                x=data.function_of,
                y=data.rot_dev_z,
                mode=data.settings.plot_mode,
                name=f"{data.short_name} {data.settings.rot_z_name}",
            ),
            row=3,
            col=1,
        )

    return plot(
        fig, output_type="div", config=report_data_collection.items[0].settings.three_subplots_export.to_config()
    )


def setup_rpe_axis(report_data_collection: ReportDataCollection) -> Tuple[go.Figure, dict]:
    report_data_item = report_data_collection.items[0]
    if report_data_collection.has_rpe_rot:
        rpe_rot_item = report_data_collection.get_rpe_results(rot_required=True)[0]
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True)
        height = report_data_item.settings.two_subplots_height
        config = report_data_item.settings.two_subplots_export.to_config()
        fig.update_xaxes(title_text=f"Pose Distance [{rpe_rot_item.pair_distance_unit}]", row=2, col=1)
        fig.update_yaxes(title_text=f"[{rpe_rot_item.rot_drift_unit}]", row=2, col=1)

    else:
        fig = make_subplots(rows=1, cols=1, shared_xaxes=True)
        height = report_data_item.settings.single_plot_height
        config = report_data_item.settings.single_plot_export.to_config()
        fig.update_xaxes(title_text=f"Pose Distance [{report_data_item.rpe_result.pair_distance_unit}]", row=1, col=1)

    fig.update_layout(title="Relative Pose Error", height=height)
    fig.update_yaxes(title_text=f"[{report_data_item.rpe_result.pos_drift_unit}]", row=1, col=1)

    return fig, config


def render_rpe(report_data_collection: ReportDataCollection) -> str:
    fig, config = setup_rpe_axis(report_data_collection)

    for data in report_data_collection.items:
        rpe_result = data.rpe_result

        fig.add_trace(
            go.Scatter(
                x=rpe_result.mean_pair_distances,
                y=rpe_result.pos_dev_mean,
                mode=data.settings.plot_mode,
                name=f"{data.short_name} Pos.",
                error_y=dict(
                    type="data",
                    array=rpe_result.pos_std,
                    visible=True,
                ),
            ),
            row=1,
            col=1,
        )

        if rpe_result.has_rot_dev:
            fig.add_trace(
                go.Scatter(
                    x=rpe_result.mean_pair_distances,
                    y=np.rad2deg(rpe_result.rot_dev_mean),
                    mode=data.settings.plot_mode,
                    name=f"{data.short_name} Rot.",
                    error_y=dict(
                        type="data",
                        array=np.rad2deg(rpe_result.rot_std),
                        visible=True,
                    ),
                ),
                row=2,
                col=1,
            )

    return plot(fig, output_type="div", config=config)
