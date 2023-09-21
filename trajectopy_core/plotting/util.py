"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from typing import Union

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colorbar import Colorbar

import trajectopy_core.util.datahandling as datahandling
from trajectopy_core.settings.plot_settings import PlotSettings

# logger configuration
logger = logging.getLogger("root")


def vertical_subplots(
    *,
    x_list: list,
    y_list: list,
    xlabel: str,
    ylabels: list,
    sharex: bool = True,
    sharey: bool = False,
    plot_settings: PlotSettings = PlotSettings(),
):
    """
    Creates a vertical array of subplots containing data provided in vals
    """
    fig, axes = plt.subplots(
        nrows=len(y_list[0]),
        ncols=1,
        sharex=sharex,
        sharey=sharey,
    )

    if len(y_list[0]) == 1:
        axes = [axes]

    smoothing_enabled = plot_settings.smoothing_window_size not in {0.0, -1.0}
    legend_list = [
        i
        for i in [
            "raw deviations" if smoothing_enabled else "",
            f"smoothed (avg. window-size of {plot_settings.smoothing_window_size:.1f} {'m' if '[m]' in xlabel else 's'})"
            if smoothing_enabled
            else "deviations",
            "mean" if plot_settings.show_mean_line else "",
        ]
        if i
    ]
    for i, (ax, yl) in enumerate(zip(axes, ylabels)):
        x_min, x_max = np.Inf, -np.Inf
        for x_j, yvals in zip(x_list, y_list):
            raw_sorting = np.argsort(x_j)

            if smoothing_enabled:
                win_size = int(
                    datahandling.rndodd(len(x_j) / len(np.unique(np.round(x_j / plot_settings.smoothing_window_size))))
                )

                x_j_smoothed, yvals_smoothed = datahandling.round_to_precision(
                    function_of=x_j[raw_sorting], data=yvals[i][raw_sorting], resolution=1e-4, filter_size=win_size
                )
                ax.plot(
                    x_j[raw_sorting],
                    yvals[i][raw_sorting],
                    ".",
                    color=[0.6, 0.6, 0.6],
                    alpha=0.5,
                )
            else:
                x_j_smoothed, yvals_smoothed = (x_j[raw_sorting], yvals[i][raw_sorting])

            ax.plot(
                x_j_smoothed,
                yvals_smoothed,
                alpha=0.9,
            )

            if plot_settings.show_mean_line:
                ax.plot(
                    [np.min(x_j), np.max(x_j)],
                    [np.mean(yvals[i])] * 2,
                    "r",
                )

            if min(x_j) < x_min:
                x_min = min(x_j)

            if max(x_j) > x_max:
                x_max = max(x_j)

        ax.set_xlim([x_min, x_max])
        ax.set_ylabel(yl)

        if i == len(axes) - 1:
            ax.set_xlabel(xlabel)

    if plot_settings.show_mean_line or smoothing_enabled:
        fig.legend(
            legend_list,
            ncol=3,
            loc="upper center",
        )
    fig.tight_layout()
    return fig


def scatter_plotter(
    *,
    xyz: list,
    data: list,
    titles: list,
    c_labels: list,
    nrows: int = 0,
    ncols: int = 0,
    separate: bool = False,
    xlabels: Union[list, None] = None,
    ylabels: Union[list, None] = None,
    figure: bool = True,
    plot_settings: PlotSettings = PlotSettings(),
):
    """
    Scatter plotter function that plots 2d data with data mapped onto it using
    colors
    """
    if xlabels is None:
        xlabels = ["[m]"] * len(data)

    if ylabels is None:
        ylabels = ["[m]"] * len(data)

    if len(data) != len(xyz) and len(xyz) == 1:
        xyz *= len(data)

    if nrows == 0:
        nrows = len(data)

    if ncols == 0:
        ncols = 1

    if plot_settings.scatter_rotate:
        xyz = [datahandling.rotate_to_main_axis(x_i - np.mean(x_i, axis=0)) + np.mean(x_i, axis=0) for x_i in xyz]

    fig = plt.figure(figsize=(7.2, 4.45)) if not separate and figure else None

    for i, (xyz_i, d, t, cl, xl_i, yl_i) in enumerate(zip(xyz, data, titles, c_labels, xlabels, ylabels)):
        if not separate and figure:
            plt.subplot(nrows, ncols, i + 1)
        elif figure:
            plt.figure(figsize=(7.2, 4.45))
        grid = datahandling.togrid(xyz=xyz_i, data=d, grid_mp=plot_settings.grid_mp)

        _colored_scatter_plot(
            xyz=grid.scaled_grid_cells[:, 0:2],
            c_list=grid.scaled_grid_cells[:, 2].tolist(),
            c_label=cl,
            title=t,
            plot_settings=plot_settings,
        )

        if xlabels:
            plt.xlabel(xl_i)
        if ylabels:
            plt.ylabel(yl_i)

    return fig


def norm_hist(*, l, mm: bool = False, alpha: float = 0.5, norm: bool = True) -> None:
    """
    Plots a histogram
    """
    hist, bin_edges = np.histogram(l, bins="auto")
    if norm:
        hist = hist / len(l)
    if mm:
        bin_edges *= 1000
    plt.bar(bin_edges[:-1], hist, width=np.diff(bin_edges), align="edge", alpha=alpha)
    return max(hist)


def stair_hist(*, l, mm: bool = False, linewidth: float = 1.5) -> None:
    """
    Plots a stair histogram
    """
    hist, bin_edges = np.histogram(l, bins="auto")
    n_hist = hist / len(l)
    if mm:
        bin_edges *= 1000
    plt.stairs(hist, bin_edges, linewidth=linewidth)
    return max(n_hist)


def _colored_scatter_plot(
    *, xyz: np.ndarray, c_list: list, c_label: str, title: str, plot_settings: PlotSettings = PlotSettings()
) -> None:
    """
    Plots 2d positions with colorcode
    """
    plt.axis("equal")
    plt.title(title)

    plt.xlabel("x [m]")
    plt.xlabel("y [m]")

    c_list, lower_bound, upper_bound, c_bar_ticks, c_bar_ticklabels = _setup_cbar_params(c_list, plot_settings)

    sc = plt.scatter(
        xyz[:, 0],
        xyz[:, 1],
        c=c_list,
        cmap="RdYlBu_r",
        vmax=upper_bound,
        vmin=lower_bound,
    )

    cbar: Colorbar = plt.colorbar(sc, format="%.2f")
    cbar.set_label(c_label)
    cbar.set_ticks(c_bar_ticks)
    cbar.set_ticklabels(c_bar_ticklabels)

    if plot_settings.scatter_no_axis:
        plt.axis("off")


def _setup_cbar_params(c_list, plot_settings: PlotSettings):
    """Configures the colorbar ticks and labels for the scatter plot"""
    if plot_settings.scatter_sigma_factor == 0:
        lower_bound = np.min(c_list)
        upper_bound = np.max(c_list)
        geq_leq_dict = {0: "", plot_settings.c_bar_step_divisor: ""}
    else:
        lower_bound = np.max([np.min(c_list), np.mean(c_list) - plot_settings.scatter_sigma_factor * np.std(c_list)])
        upper_bound = np.min([np.max(c_list), np.mean(c_list) + plot_settings.scatter_sigma_factor * np.std(c_list)])
        geq_leq_dict = {0: "$\leq$", plot_settings.c_bar_step_divisor: "$\geq$"}

    c_bar_range = np.abs(upper_bound - lower_bound)

    c_bar_ticks_and_labels = {
        lower_bound
        + i
        / plot_settings.c_bar_step_divisor
        * c_bar_range: f"{geq_leq_dict.get(i, '')}{lower_bound + i/plot_settings.c_bar_step_divisor * c_bar_range:.2f}"
        for i in range(plot_settings.c_bar_step_divisor + 1)
    }

    c_list = np.clip(c_list, lower_bound, upper_bound)

    if lower_bound < 0 and upper_bound > 0 and plot_settings.always_show_zero:
        c_bar_ticks_and_labels = {
            key: value
            for key, value in c_bar_ticks_and_labels.items()
            if abs(key) > 0.5 / plot_settings.c_bar_step_divisor * c_bar_range
        }
        c_bar_ticks_and_labels[0] = "0"

    c_bar_ticks = list(c_bar_ticks_and_labels.keys())
    c_bar_ticklabels = list(c_bar_ticks_and_labels.values())
    return c_list, lower_bound, upper_bound, c_bar_ticks, c_bar_ticklabels
