"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from typing import Dict, List, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.axes import Axes
from matplotlib.collections import LineCollection, PolyCollection
from matplotlib.figure import Figure

import trajectopy_core.util.datahandling as datahandling
from trajectopy_core.evaluation.abs_traj_dev import AbsoluteTrajectoryDeviations, DeviationCollection
from trajectopy_core.evaluation.rel_traj_dev import RelativeTrajectoryDeviations
from trajectopy_core.plotting.heatmap import annotate_heatmap, heatmap
from trajectopy_core.plotting.util import norm_hist, scatter_plotter, stair_hist, vertical_subplots
from trajectopy_core.settings.plot_settings import PlotSettings
from trajectopy_core.trajectory import Sorting
from trajectopy_core.util.definitions import Unit

logger = logging.getLogger("root")

XLABEL_DICT = {Sorting.CHRONO: "time [s]", Sorting.SPATIAL: "trajectory length [m]"}
UNIT_DICT = {Sorting.CHRONO: "s", Sorting.SPATIAL: "m"}


def plot_combined_devs(devs: AbsoluteTrajectoryDeviations, plot_settings: PlotSettings = PlotSettings()) -> Figure:
    if devs.ate_result.rot_dev is None:
        comb_devs = [[devs.comb_pos_devs * plot_settings.unit_multiplier]]
        ylabels = [f"position deviations {plot_settings.unit_str}"]
    else:
        comb_devs = [
            [
                devs.comb_pos_devs * plot_settings.unit_multiplier,
                np.rad2deg(devs.comb_rot_devs),
            ]
        ]
        ylabels = [
            f"position deviations {plot_settings.unit_str}",
            "minimum rotation angle [°]",
        ]

    return vertical_subplots(
        x_list=[devs.trajectory.function_of] * len(comb_devs),
        y_list=comb_devs,
        xlabel=XLABEL_DICT[devs.trajectory.sorting],
        ylabels=ylabels,
        plot_settings=plot_settings,
    )


def plot_raw_rotation_devs(devs: AbsoluteTrajectoryDeviations, plot_settings: PlotSettings = PlotSettings()) -> Figure:
    rpy_dev = devs.rpy_dev
    vert_sp_data_rot = [
        [
            np.rad2deg(rpy_dev[:, 0]),
            np.rad2deg(rpy_dev[:, 1]),
            np.rad2deg(rpy_dev[:, 2]),
        ]
    ]
    ylabels = ["roll [°]", "pitch [°]", "yaw [°]"]

    return vertical_subplots(
        x_list=[devs.trajectory.function_of] * len(vert_sp_data_rot),
        y_list=vert_sp_data_rot,
        xlabel=XLABEL_DICT[devs.trajectory.sorting],
        ylabels=ylabels,
        plot_settings=plot_settings,
    )


def plot_raw_position_devs(devs: AbsoluteTrajectoryDeviations, plot_settings: PlotSettings = PlotSettings()) -> Figure:
    deviations_xa = (
        devs.ate_result.directed_pos_dev[:, 0] if plot_settings.show_directed_devs else devs.ate_result.pos_dev[:, 0]
    )
    deviations_yh = (
        devs.ate_result.directed_pos_dev[:, 1] if plot_settings.show_directed_devs else devs.ate_result.pos_dev[:, 1]
    )
    deviations_zv = (
        devs.ate_result.directed_pos_dev[:, 2] if plot_settings.show_directed_devs else devs.ate_result.pos_dev[:, 2]
    )

    if plot_settings.show_directed_devs:
        ylabels = [
            f"along {plot_settings.unit_str}",
            f"horiz. cross {plot_settings.unit_str}",
            f"vert. cross {plot_settings.unit_str}",
        ]
    else:
        ylabels = [
            f"x {plot_settings.unit_str}",
            f"y {plot_settings.unit_str}",
            f"z {plot_settings.unit_str}",
        ]

    vert_sp_data_pos = [
        [
            deviations_xa * plot_settings.unit_multiplier,
            deviations_yh * plot_settings.unit_multiplier,
            deviations_zv * plot_settings.unit_multiplier,
        ]
    ]

    return vertical_subplots(
        x_list=[devs.trajectory.function_of] * len(vert_sp_data_pos),
        y_list=vert_sp_data_pos,
        xlabel=XLABEL_DICT[devs.trajectory.sorting],
        ylabels=ylabels,
        plot_settings=plot_settings,
    )


def plot_dof_dev(*, devs: AbsoluteTrajectoryDeviations, plot_settings: PlotSettings = PlotSettings()) -> Figure:
    fig = plt.figure(figsize=(12, 4))

    plot_position_dof(devs, plot_settings)

    if devs.ate_result.rot_dev:
        plot_rot_dof(devs, plot_settings)

    return fig


def plot_position_dof(devs: AbsoluteTrajectoryDeviations, plot_settings: PlotSettings = PlotSettings()):
    deviations_xa = (
        devs.ate_result.directed_pos_dev[:, 0] if plot_settings.show_directed_devs else devs.ate_result.pos_dev[:, 0]
    )
    deviations_yh = (
        devs.ate_result.directed_pos_dev[:, 1] if plot_settings.show_directed_devs else devs.ate_result.pos_dev[:, 1]
    )
    deviations_zv = (
        devs.ate_result.directed_pos_dev[:, 2] if plot_settings.show_directed_devs else devs.ate_result.pos_dev[:, 2]
    )

    rows = 1 if devs.ate_result.rot_dev is None else 2
    xyz_dev = [devs.trajectory.pos.xyz]
    c_labels = [plot_settings.unit_str]

    plt.subplot(rows, 3, 1)
    scatter_plotter(
        xyz=xyz_dev,
        data=[deviations_xa * plot_settings.unit_multiplier],
        c_labels=c_labels,
        titles=["along-track" if plot_settings.show_directed_devs else "x"],
        figure=False,
        plot_settings=plot_settings,
    )

    plt.subplot(rows, 3, 2)
    scatter_plotter(
        xyz=xyz_dev,
        data=[deviations_yh * plot_settings.unit_multiplier],
        c_labels=c_labels,
        titles=["horizontal cross-track" if plot_settings.show_directed_devs else "y"],
        figure=False,
        plot_settings=plot_settings,
    )

    plt.subplot(rows, 3, 3)
    scatter_plotter(
        xyz=xyz_dev,
        data=[deviations_zv * plot_settings.unit_multiplier],
        c_labels=c_labels,
        titles=["vertical cross-track" if plot_settings.show_directed_devs else "z"],
        figure=False,
        plot_settings=plot_settings,
    )


def plot_rot_dof(devs: AbsoluteTrajectoryDeviations, plot_settings: PlotSettings = PlotSettings()) -> None:
    xyz_dev = [devs.trajectory.pos.xyz]
    rpy_dev = devs.rpy_dev
    plt.subplot(2, 3, 4)
    scatter_plotter(
        xyz=xyz_dev,
        data=[np.rad2deg(rpy_dev[:, 0])],
        c_labels=["[°]"],
        titles=["roll"],
        figure=False,
        plot_settings=plot_settings,
    )

    plt.subplot(2, 3, 5)
    scatter_plotter(
        xyz=xyz_dev,
        data=[np.rad2deg(rpy_dev[:, 1])],
        c_labels=["[°]"],
        titles=["pitch"],
        figure=False,
        plot_settings=plot_settings,
    )

    plt.subplot(2, 3, 6)
    scatter_plotter(
        xyz=xyz_dev,
        data=[np.rad2deg(rpy_dev[:, 2])],
        c_labels=["[°]"],
        titles=["yaw"],
        figure=False,
        plot_settings=plot_settings,
    )


def plot_compact_deviations(
    devs: AbsoluteTrajectoryDeviations, plot_settings: PlotSettings = PlotSettings()
) -> Union[Figure, None]:
    # positions
    dev_pos_list = [devs.trajectory.pos.xyz]
    comb_pos_rms = datahandling.moving_width(
        t=devs.trajectory.function_of,
        data=devs.comb_pos_devs,
        width=plot_settings.rms_window_width,
        function=datahandling.rms,
    )

    if devs.ate_result.rot_dev:
        comb_rot_rms = datahandling.moving_width(
            t=devs.trajectory.function_of,
            data=devs.comb_rot_devs,
            width=plot_settings.rms_window_width,
            function=datahandling.rms,
        )
        data_rms_plot = [
            comb_pos_rms * plot_settings.unit_multiplier,
            np.rad2deg(comb_rot_rms),
        ]
        titles_rms = [
            f"position rms ({plot_settings.rms_window_width:.2f} {UNIT_DICT[devs.trajectory.sorting]} window width)",
            f"rotation rms ({plot_settings.rms_window_width:.2f} {UNIT_DICT[devs.trajectory.sorting]} window width)",
        ]
        c_labels_dev = [plot_settings.unit_str, "[°]"]

    else:
        data_rms_plot = [comb_pos_rms * plot_settings.unit_multiplier]
        titles_rms = [
            f"position rms ({plot_settings.rms_window_width:.2f} {UNIT_DICT[devs.trajectory.sorting]} window width)"
        ]
        c_labels_dev = [plot_settings.unit_str]

    return scatter_plotter(
        xyz=dev_pos_list * len(data_rms_plot),
        data=data_rms_plot,
        c_labels=c_labels_dev,
        titles=titles_rms,
        plot_settings=plot_settings,
    )


def plot_compact_hist(devs: AbsoluteTrajectoryDeviations, plot_settings: PlotSettings = PlotSettings()) -> Figure:
    """
    Plot compact histograms of cross-track and rpy deviations
    """
    fig = plt.figure()
    pos_ax = plt.subplot(2, 1, 1)
    plot_position_hist(devs, plot_settings)
    pos_ax.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

    if devs.ate_result.rot_dev is not None:
        rot_ax = plt.subplot(2, 1, 2)
        plot_rotation_hist(devs, plot_settings)
        rot_ax.ticklabel_format(style="sci", axis="y", scilimits=(0, 0))

    return fig


def plot_rotation_hist(devs: AbsoluteTrajectoryDeviations, plot_settings: PlotSettings = PlotSettings()) -> None:
    roll = np.rad2deg(devs.rpy_dev[:, 0])
    pitch = np.rad2deg(devs.rpy_dev[:, 1])
    yaw = np.rad2deg(devs.rpy_dev[:, 2])

    plt.xlabel("[°]")
    plt.ylabel("counts")
    if plot_settings.hist_as_stairs:
        stair_hist(l=yaw)
        stair_hist(l=pitch)
        stair_hist(l=roll)
    else:
        norm_hist(l=yaw, alpha=0.6, norm=False)
        norm_hist(l=pitch, alpha=0.6, norm=False)
        norm_hist(l=roll, alpha=0.4, norm=False)
    plt.legend(["yaw", "pitch", "roll"])


def plot_position_hist(devs: AbsoluteTrajectoryDeviations, plot_settings: PlotSettings = PlotSettings()):
    deviations_xa = (
        devs.ate_result.directed_pos_dev[:, 0] if plot_settings.show_directed_devs else devs.ate_result.pos_dev[:, 0]
    )
    deviations_yh = (
        devs.ate_result.directed_pos_dev[:, 1] if plot_settings.show_directed_devs else devs.ate_result.pos_dev[:, 1]
    )
    deviations_zv = (
        devs.ate_result.directed_pos_dev[:, 2] if plot_settings.show_directed_devs else devs.ate_result.pos_dev[:, 2]
    )
    labels = ["vertical", "horizontal", "along"] if plot_settings.show_directed_devs else ["x", "y", "z"]

    plt.xlabel(plot_settings.unit_str)
    plt.ylabel("counts")
    if plot_settings.hist_as_stairs:
        stair_hist(l=deviations_zv, mm=plot_settings.unit_is_mm)
        stair_hist(l=deviations_yh, mm=plot_settings.unit_is_mm)
        stair_hist(l=deviations_xa, mm=plot_settings.unit_is_mm)
    else:
        norm_hist(l=deviations_zv, mm=plot_settings.unit_is_mm, norm=False)
        norm_hist(l=deviations_yh, mm=plot_settings.unit_is_mm, norm=False)
        norm_hist(l=deviations_xa, mm=plot_settings.unit_is_mm, norm=False)

    plt.legend(labels)


def plot_edf(
    deviation: Union[AbsoluteTrajectoryDeviations, List[AbsoluteTrajectoryDeviations]],
    plot_settings: PlotSettings = PlotSettings(),
) -> Figure:
    deviation_list = deviation if isinstance(deviation, list) else [deviation]

    fig = plt.figure()
    plot_position_edf(deviation_list, plot_settings)
    plot_rotation_edf(deviation_list)

    fig.legend([dev.name for dev in deviation_list], ncol=3, loc="upper center")
    return fig


def plot_position_edf(
    deviation_list: List[AbsoluteTrajectoryDeviations],
    plot_settings: PlotSettings = PlotSettings(),
) -> None:
    ax_pos = plt.subplot(2, 1, 1)
    ax_pos.set_xlabel(f"Deviation {plot_settings.unit_str}")
    ax_pos.set_ylabel("Cummulative Probability")

    for dev in deviation_list:
        sorted_comb_pos_dev = np.sort(dev.comb_pos_devs)
        pos_norm_cdf = np.arange(len(sorted_comb_pos_dev)) / float(len(sorted_comb_pos_dev))
        ax_pos.plot(sorted_comb_pos_dev * plot_settings.unit_multiplier, pos_norm_cdf)


def plot_rotation_edf(deviation_list: List[AbsoluteTrajectoryDeviations]) -> None:
    if all(dev.ate_result.rot_dev is None for dev in deviation_list):
        return

    ax_rot = plt.subplot(2, 1, 2)

    ax_rot.set_xlabel("Deviation [°]")
    ax_rot.set_ylabel("Cummulative Probability")

    for dev in deviation_list:
        if dev.ate_result.rot_dev is None:
            continue
        sorted_comb_rot_dev = np.sort(np.rad2deg(dev.comb_rot_devs))
        rot_norm_cdf = np.arange(len(sorted_comb_rot_dev)) / float(len(sorted_comb_rot_dev))
        ax_rot.plot(sorted_comb_rot_dev, rot_norm_cdf)


def plot_bars(
    deviation_list: List[AbsoluteTrajectoryDeviations],
    plot_settings: PlotSettings = PlotSettings(),
    mode: str = "positions",
) -> Figure:
    fig, ax = plt.subplots()
    bar_width = 0.9 / len(deviation_list)
    characteristics = ["Min", "Max", "Mean", "Median", "RMS", "STD"]
    unit = plot_settings.unit_str if mode == "positions" else "[°]"
    spacings = np.linspace(
        -bar_width * (len(deviation_list) - 1) / 2,
        bar_width * (len(deviation_list) - 1) / 2,
        len(deviation_list),
    )
    x_positions = np.arange(len(characteristics))
    for deviation, spacing in zip(deviation_list, spacings):
        if mode == "rotations" and deviation.ate_result.rot_dev is None:
            continue

        if mode == "positions":
            data = [
                deviation.min_pos * plot_settings.unit_multiplier,
                deviation.max_pos * plot_settings.unit_multiplier,
                deviation.mean_pos * plot_settings.unit_multiplier,
                deviation.median_pos * plot_settings.unit_multiplier,
                deviation.rms_pos * plot_settings.unit_multiplier,
                deviation.std_pos * plot_settings.unit_multiplier,
            ]
        elif mode == "rotations":
            data = [
                np.rad2deg(deviation.min_rot),
                np.rad2deg(deviation.max_rot),
                np.rad2deg(deviation.mean_rot),
                np.rad2deg(deviation.median_rot),
                np.rad2deg(deviation.rms_rot),
                np.rad2deg(deviation.std_rot),
            ]
        else:
            raise ValueError("Mode must be either 'positions' or 'rotations'")
        ax.bar(x_positions + spacing, data, width=bar_width, label=deviation.name)

    ax.set_xlabel("Characteristic")
    ax.set_ylabel(f"Value {unit}")
    ax.set_xticks(x_positions)
    ax.set_xticklabels(characteristics)
    ax.legend()

    return fig


def plot_rms_heatmap(
    deviation_collection: DeviationCollection,
    plot_settings: PlotSettings = PlotSettings(),
) -> Tuple[Figure, Union[Figure, None]]:
    pos_rms_fig = plot_position_rms_heatmap(deviation_collection, plot_settings)
    rpy_rms_fig = plot_rotation_rms_heatmap(deviation_collection)

    return pos_rms_fig, rpy_rms_fig


def plot_rotation_rms_heatmap(deviation_collection: DeviationCollection) -> Union[Figure, None]:
    if not deviation_collection.rpy_rms:
        return None

    rpy_rms_fig, ax = plt.subplots()
    ax.grid(False)
    im, _ = heatmap(
        np.rad2deg(np.array(deviation_collection.rpy_rms)),
        deviation_collection.names,
        ["roll rms", "pitch rms", "yaw rms"],
        ax=ax,
        cmap="YlOrRd",
        cbarlabel="RMS [°]",
        cbar_kw={"format": "%.2f"},
    )
    annotate_heatmap(im, valfmt="{x:.3f}")
    return rpy_rms_fig


def plot_position_rms_heatmap(
    deviation_collection: DeviationCollection,
    plot_settings: PlotSettings = PlotSettings(),
) -> Figure:
    pos_rms = (
        deviation_collection.directed_pos_rms if plot_settings.show_directed_devs else deviation_collection.pos_rms
    )

    pos_labels = ["along rms", "cross rms", "vertical rms"] if plot_settings.show_directed_devs else ["x", "y", "z"]
    pos_rms_fig, ax = plt.subplots()
    ax.grid(False)
    im, _ = heatmap(
        np.array(pos_rms) * plot_settings.unit_multiplier,
        deviation_collection.names,
        pos_labels,
        ax=ax,
        cmap="YlOrRd",
        cbarlabel=f"RMS {plot_settings.unit_str}",
        cbar_kw={"format": "%.2f"},
    )
    annotate_heatmap(im, valfmt="{x:.3f}")
    return pos_rms_fig


def plot_bias_heatmap(
    deviation_collection: DeviationCollection,
    plot_settings: PlotSettings = PlotSettings(),
) -> Tuple[Figure, Union[Figure, None]]:
    pos_bias_fig = plot_position_bias_heatmap(deviation_collection, plot_settings)

    rpy_bias_fig = plot_rotation_bias_heatmap(deviation_collection)

    return pos_bias_fig, rpy_bias_fig


def plot_rotation_bias_heatmap(deviation_collection: DeviationCollection) -> Union[Figure, None]:
    if not deviation_collection.rpy_bias:
        return None

    # roll pitch yaw bias
    rpy_bias_fig, ax = plt.subplots()
    ax.grid(False)
    im, _ = heatmap(
        np.rad2deg(np.array(deviation_collection.rpy_bias)),
        deviation_collection.names,
        ["bias roll", "bias pitch", "bias yaw"],
        ax=ax,
        cmap="bwr",
        cbarlabel="Bias [°]",
        norm=colors.CenteredNorm(),
        cbar_kw={"format": "%.2f"},
    )
    annotate_heatmap(im, valfmt="{x:.3f}", textcolors=("black", "black"))
    return rpy_bias_fig


def plot_position_bias_heatmap(
    deviation_collection: DeviationCollection,
    plot_settings: PlotSettings = PlotSettings(),
) -> Figure:
    pos_bias = (
        deviation_collection.directed_pos_bias if plot_settings.show_directed_devs else deviation_collection.pos_bias
    )

    pos_labels = ["along bias", "cross bias", "vertical bias"] if plot_settings.show_directed_devs else ["x", "y", "z"]
    pos_bias_fig, ax = plt.subplots()
    ax.grid(False)
    im, _ = heatmap(
        np.array(pos_bias) * plot_settings.unit_multiplier,
        deviation_collection.names,
        pos_labels,
        ax=ax,
        cmap="bwr",
        cbarlabel=f"Bias {plot_settings.unit_str}",
        norm=colors.CenteredNorm(),
        cbar_kw={"format": "%.2f"},
    )
    annotate_heatmap(im, valfmt="{x:.3f}", textcolors=("black", "black"))
    return pos_bias_fig


def derive_xlabel_from_sortings(sorting_list: List[Sorting]) -> str:
    if all(sorting == Sorting.SPATIAL for sorting in sorting_list):
        return XLABEL_DICT[Sorting.SPATIAL]

    if all(sorting == Sorting.CHRONO for sorting in sorting_list):
        return XLABEL_DICT[Sorting.CHRONO]

    logger.warning("Data is diffently sorted, weird things might happen.")
    return f"{XLABEL_DICT[Sorting.CHRONO]} / {XLABEL_DICT[Sorting.SPATIAL]}"


def plot_multiple_comb_deviations(
    deviation: Union[AbsoluteTrajectoryDeviations, List[AbsoluteTrajectoryDeviations]],
    plot_settings: PlotSettings = PlotSettings(),
) -> Figure:
    deviation_list = deviation if isinstance(deviation, list) else [deviation]
    x_label = derive_xlabel_from_sortings([dev.trajectory.sorting for dev in deviation_list])

    fig = plt.figure()
    ax_pos = plt.subplot(2, 1, 1)
    ax_pos.set_xlabel(x_label)
    ax_pos.set_ylabel(f"Deviation {plot_settings.unit_str}")

    if any(dev.ate_result.rot_dev for dev in deviation_list):
        ax_rot = plt.subplot(2, 1, 2)
        ax_rot.set_xlabel(x_label)
        ax_rot.set_ylabel("Deviation [°]")
    else:
        ax_rot = None

    min_x = np.inf
    max_x = -np.inf
    for dev in deviation_list:
        if len(dev.trajectory.function_of) == 0:
            logger.warning("Skipping %s as it has no data", dev.name)
            continue

        arc_length_sorting = np.argsort(dev.trajectory.function_of)
        function_of_sorted = dev.trajectory.function_of[arc_length_sorting]

        if (min_val := function_of_sorted[0]) < min_x:
            min_x = min_val

        if (max_val := function_of_sorted[-1]) > max_x:
            max_x = max_val

        ax_pos.plot(
            dev.trajectory.function_of[arc_length_sorting],
            dev.comb_pos_devs[arc_length_sorting] * plot_settings.unit_multiplier,
        )
        if ax_rot is not None:
            ax_rot.plot(
                dev.trajectory.function_of[arc_length_sorting],
                np.rad2deg(dev.comb_rot_devs[arc_length_sorting]),
            )

    ax_pos.set_xlim(min_x, max_x)
    ax_rot.set_xlim(min_x, max_x)

    fig.legend([dev.name for dev in deviation_list], ncol=3, loc="upper center")
    return fig


def plot_multiple_deviations(
    deviation_collection: DeviationCollection,
    plot_settings: PlotSettings = PlotSettings(),
) -> Tuple[Figure, Union[Figure, None]]:
    if plot_settings.show_directed_devs:
        pos_labels = [
            f"along {plot_settings.unit_str}",
            f"horiz. cross {plot_settings.unit_str}",
            f"vert. cross {plot_settings.unit_str}",
        ]
    else:
        pos_labels = [
            f"x {plot_settings.unit_str}",
            f"y {plot_settings.unit_str}",
            f"z {plot_settings.unit_str}",
        ]

    rpy_labels = ["roll [°]", "pitch [°]", "yaw [°]"]

    pos_dev = (
        deviation_collection.directed_pos_dev if plot_settings.show_directed_devs else deviation_collection.pos_dev
    )

    x_label = derive_xlabel_from_sortings(sorting_list=deviation_collection.sortings)

    xyz_dev_fig = _plot_components(
        x_list=deviation_collection.function_of,
        y_list=pos_dev,
        xlabel=x_label,
        ylabels=pos_labels,
        legend_list=deviation_collection.names,
        sharey=True,
        mm=plot_settings.unit_is_mm,
    )

    # rpy
    if deviation_collection.rpy_dev:
        rpy_dev_fig = _plot_components(
            x_list=deviation_collection.function_of,
            y_list=deviation_collection.rpy_dev,
            xlabel=x_label,
            ylabels=rpy_labels,
            legend_list=deviation_collection.names,
            sharey=True,
            deg=True,
        )
    else:
        rpy_dev_fig = None

    return xyz_dev_fig, rpy_dev_fig


def plot_rpe(devs: List[RelativeTrajectoryDeviations]) -> Tuple[Figure, Figure]:
    """Plots metric and time RPE for each Deviation given in devs

    Args:
        devs (list[RelativeTrajectoryDeviations]): list of RelativeTrajectoryDeviations

    Returns:
        Tuple[Figure, Figure]: metric and time RPE plots

    """
    if not isinstance(devs, list):
        devs = [devs]

    fig_metric, (fig_pos_metric, fig_rot_metric) = plt.subplots(2, 1)
    fig_time, (fig_pos_time, fig_rot_time) = plt.subplots(2, 1)

    fig_pos_metric.set_ylabel("Position RPE [%]")
    fig_pos_time.set_ylabel("Position RPE [m/s]")

    fig_rot_metric.set_ylabel("Rotation RPE [deg / 100m]")
    fig_rot_time.set_ylabel("Rotation RPE [deg/s]")

    fig_pos_metric.set_xlabel("pair distance [m]")
    fig_pos_time.set_xlabel("pair distance [s]")
    fig_rot_metric.set_xlabel("pair distance [m]")
    fig_rot_time.set_xlabel("pair distance [s]")

    figure_dict: Dict[str, Dict[Unit, Axes]] = {
        "pos": {Unit.METER: fig_pos_metric, Unit.SECOND: fig_pos_time},
        "rot": {Unit.METER: fig_rot_metric, Unit.SECOND: fig_rot_time},
    }

    _plot_rpe_pos(figure_dict["pos"], devs)
    _plot_rpe_rot(figure_dict["rot"], devs)

    _rpy_legend(figure_dict)

    ret_sum = 1 if any(dev.rpe_result.pair_distance_unit == Unit.METER for dev in devs) else 0
    if any(dev.rpe_result.pair_distance_unit == Unit.SECOND for dev in devs):
        ret_sum += 2

    plt.close({1: fig_time, 2: fig_metric}.get(ret_sum))

    return {
        0: (None, None),
        1: (fig_metric, None),
        2: (None, fig_time),
        3: (fig_metric, fig_time),
    }[ret_sum]


def _close_empty_figures(fig_metric: Figure, fig_time: Figure) -> None:
    if not fig_metric.axes:
        plt.close(fig_metric)
    if not fig_time.axes:
        plt.close(fig_time)


def _plot_rpe_pos(figure_dict: Dict[Unit, Axes], devs: List[RelativeTrajectoryDeviations]) -> None:
    for dev in devs:
        line_plot = figure_dict[dev.rpe_result.pair_distance_unit].plot(
            dev.mean_distances, dev.mean_pos_devs, label=dev.name
        )

        if len(devs) > len({dev.rpe_result.pair_distance_unit for dev in devs}):
            continue

        violin_plot = figure_dict[dev.rpe_result.pair_distance_unit].violinplot(
            [
                [val * dev.drift_factor for val in pos_list]
                for pos_list in list(dev.rpe_result.pos_dev.values())
                if pos_list
            ],
            positions=dev.mean_distances,
            showmeans=True,
            widths=max(0.5, dev.step / 4),
        )
        _set_violin_color(violin_plot, line_plot[0].get_color())


def _plot_rpe_rot(figure_dict: Dict[Unit, Axes], devs: List[RelativeTrajectoryDeviations]) -> None:
    plot_sum = 0
    for dev in devs:
        if not dev.has_rot_dev:
            continue

        plot_sum += 1
        line_plot = figure_dict[dev.rpe_result.pair_distance_unit].plot(
            dev.mean_distances, np.rad2deg(dev.mean_rot_devs), label=dev.name
        )

        if len(devs) > len({dev.rpe_result.pair_distance_unit for dev in devs}):
            continue

        violin_plot = figure_dict[dev.rpe_result.pair_distance_unit].violinplot(
            [
                list(np.rad2deg(rot_list) * dev.drift_factor)
                for rot_list in list(dev.rpe_result.rot_dev.values())
                if rot_list
            ],
            positions=dev.mean_distances,
            showmeans=True,
            widths=max(0.5, dev.step / 4),
        )
        _set_violin_color(violin_plot, line_plot[0].get_color())

    if plot_sum == 0:
        for ax in figure_dict.values():
            ax.axis(False)


def _set_violin_color(violin_dict: dict, color: str) -> None:
    for component in violin_dict.values():
        if isinstance(component, LineCollection):
            component.set_color(color)
            continue

        if not isinstance(component, list):
            continue

        for collection in component:
            if isinstance(collection, PolyCollection):
                collection.set_facecolor(color)
                collection.set_edgecolor(color)


def _rpy_legend(figure_dict: Dict[str, Dict[Unit, Axes]]):
    for d in figure_dict.values():
        for ax in d.values():
            if ax.lines:
                ax.legend()


def _plot_components(
    *,
    x_list: List[np.ndarray],
    y_list: List[np.ndarray],
    ylabels: list,
    legend_list: list,
    sharey: bool = False,
    mm: bool = False,
    deg: bool = False,
    xlabel: str = "trajectory length [m]",
) -> Figure:
    """
    Plots data for each lap for each component in x
    """
    fig, axes = plt.subplots(nrows=y_list[0].shape[1], ncols=1, sharex=True, sharey=sharey)
    for j, (ax, yl) in enumerate(zip(axes, ylabels)):
        if j == y_list[0].shape[1] - 1:
            ax.set_xlabel(xlabel)
        ax.set_ylabel(yl)

        x_max = 0
        for x_l, l_l in zip(y_list, x_list):
            idx = np.argsort(l_l)
            if mm:
                data = x_l[idx, j] * 1000
            elif deg:
                data = np.rad2deg(np.unwrap(x_l[idx, j]))
            else:
                data = x_l[idx, j]

            ax.plot(l_l[idx], data)
            if max(l_l[idx]) > x_max:
                x_max = max(l_l[idx])
        ax.set_xlim([0, x_max])

    fig.legend(legend_list, ncol=3, loc="upper center")
    fig.subplots_adjust(right=0.85)
    return fig
