"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

import logging
import os
from typing import List, Optional, Tuple

import jinja2
import numpy as np

from trajectopy_core.evaluation.ate_result import ATEResult
from trajectopy_core.evaluation.rpe_result import RPEResult
from trajectopy_core.plotting import bar_plots, histograms, line_plots, scatter_plots
from trajectopy_core.report.data import ReportData
from trajectopy_core.settings.report import ReportSettings
from trajectopy_core.report.utils import image_to_base64, number_to_string

base_path = os.path.join(os.path.dirname(__file__))

TEMPLATES_PATH = os.path.join(base_path)

logger = logging.getLogger("root")


def convert_images_to_base64() -> Tuple[str, str, str]:
    igg_path = os.path.join(os.path.join(base_path), "assets", "igg.png")
    uni_bonn_path = os.path.join(os.path.join(base_path), "assets", "uni_bonn.png")
    icon_path = os.path.join(os.path.join(base_path), "assets", "icon.png")

    igg_base64 = image_to_base64(igg_path)
    uni_bonn_base64 = image_to_base64(uni_bonn_path)
    icon_base64 = image_to_base64(icon_path)

    return igg_base64, uni_bonn_base64, icon_base64


def render_side_by_side_plots(report_data: ReportData) -> List[str]:
    side_by_side_plots = [scatter_plots.render_pos_devs(report_data)]

    if not report_data.has_ate_rot:
        return side_by_side_plots

    side_by_side_plots.append(scatter_plots.render_rot_devs(report_data))

    return side_by_side_plots


def render_one_line_plots(report_data: ReportData) -> List[str]:
    one_line_plots = []

    if report_data.has_rpe:
        one_line_plots.append(line_plots.render_rpe(report_data))

    one_line_plots.extend(
        (
            histograms.render_pos_devs(report_data),
            bar_plots.render_pos_bar_plot(report_data),
            line_plots.render_dev_edf(report_data),
            line_plots.render_dev_comb_plot(report_data),
            line_plots.render_dev_pos_plot(report_data),
        )
    )

    one_line_plots.append(line_plots.render_pos_plot(report_data))

    if not report_data.has_ate_rot:
        return one_line_plots

    one_line_plots.insert(2, histograms.render_rot_devs(report_data))
    one_line_plots.insert(4, bar_plots.render_rot_bar_plot(report_data))
    one_line_plots.insert(len(one_line_plots) - 1, line_plots.render_dev_rot_plot(report_data))
    one_line_plots.append(line_plots.render_rot_plot(report_data))

    return one_line_plots


def render_single_report(
    *,
    ate_result: ATEResult,
    rpe_result: Optional[RPEResult] = None,
    report_settings: ReportSettings = ReportSettings(),
) -> str:
    """
    Renders a html report string of a single trajectory comparison.

    Args:
        ate_result (ATEResult): The absolute trajectory error result
        rpe_result (Optional[RPEResult]): The relative pose error result
        max_std (float): The upper bound of scatter plot colorbars is set to max_std * std of the data
        report_settings (ReportSettings): The report settings

    Returns:
        str: The html report string

    """
    template = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_PATH)).get_template("template.html")
    igg, uni_bonn, icon = convert_images_to_base64()

    report_data = ReportData(ate_result=ate_result, rpe_result=rpe_result, settings=report_settings)

    side_by_side_plots = render_side_by_side_plots(report_data)
    one_line_plots = render_one_line_plots(report_data)

    if len(side_by_side_plots) == 1:
        one_line_plots = side_by_side_plots + one_line_plots
        side_by_side_plots = []

    context = {
        "title": ate_result.name,
        "ate_pos": number_to_string(ate_result.pos_ate),
        "ate_rot": number_to_string(np.rad2deg(ate_result.rot_ate)),
        "rpe_pos": number_to_string(rpe_result.pos_rpe) if rpe_result is not None else "-",
        "rpe_rot": number_to_string(np.rad2deg(rpe_result.rot_rpe)) if rpe_result is not None else "-",
        "rpe_pos_drift_unit": rpe_result.pos_drift_unit if rpe_result is not None else "-",
        "rpe_rot_drift_unit": rpe_result.rot_drift_unit if rpe_result is not None else "-",
        "ate_pos_unit": report_data.ate_unit,
        "rpe_available": rpe_result is not None,
        "side_by_side_plots": side_by_side_plots,
        "one_line_plots": one_line_plots,
        "icon": icon,
        "igg": igg,
        "uni_bonn": uni_bonn,
        "rot_unit": report_data.settings.rot_unit,
    }

    return template.render(context)