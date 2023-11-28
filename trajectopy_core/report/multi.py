"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

import logging
from typing import List, Optional

import jinja2

from trajectopy_core.evaluation.ate_result import ATEResult
from trajectopy_core.evaluation.rpe_result import RPEResult
from trajectopy_core.plotting import bar_plots, multi_line_plots
from trajectopy_core.report.data import ReportData, ReportDataCollection
from trajectopy_core.report.utils import TEMPLATES_PATH, convert_images_to_base64
from trajectopy_core.settings.report import ReportSettings

logger = logging.getLogger("root")


def render_one_line_plots(report_data_collection: ReportDataCollection) -> List[str]:
    one_line_plots = [
        multi_line_plots.render_dev_comb_plot(report_data_collection),
        bar_plots.render_multi_pos_bar_plot(report_data_collection),
        multi_line_plots.render_dev_pos_plot(report_data_collection),
        multi_line_plots.render_dev_edf(report_data_collection),
    ]

    if report_data_collection.has_ate_rot:
        one_line_plots.insert(2, bar_plots.render_multi_rot_bar_plot(report_data_collection))
        multi_line_plots.render_dev_rot_plot(report_data_collection)

    if report_data_collection.has_rpe:
        one_line_plots.insert(1, multi_line_plots.render_rpe(report_data_collection))

    return one_line_plots


def render_multi_report(
    *,
    ate_results: List[ATEResult],
    rpe_results: Optional[List[RPEResult]] = None,
    report_settings: ReportSettings = ReportSettings(),
) -> str:
    """
    Renders a html report string of multiple trajectory comparisons

    Args:
        ate_results (list[ATEResult]): A list of absolute trajectory error results
        rpe_results (Optional[list[RPEResult]]): A list of relative pose error results
        report_settings (ReportSettings): The report settings

    Returns:
        str: The html report string

    """
    template = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_PATH)).get_template("multi_template.html")
    igg, uni_bonn, icon = convert_images_to_base64()

    rpe_available = any(rpe_results) if rpe_results is not None else False

    if not rpe_available:
        rpe_results = [None] * len(ate_results)

    report_data_collection = ReportDataCollection(
        [
            ReportData(ate_result=ate_result, rpe_result=rpe_result, settings=report_settings)
            for ate_result, rpe_result in zip(ate_results, rpe_results)
        ]
    )

    one_line_plots = render_one_line_plots(report_data_collection)

    context = {
        "title": "Trajectory Comparison",
        "rpe_available": rpe_available,
        "one_line_plots": one_line_plots,
        "icon": icon,
        "igg": igg,
        "uni_bonn": uni_bonn,
    }

    return template.render(context)
