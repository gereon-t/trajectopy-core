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
from trajectopy_core.plotting import multi_line_plots, bar_plots
from trajectopy_core.report.data import ReportData
from trajectopy_core.settings.report import ReportSettings
from trajectopy_core.report.utils import TEMPLATES_PATH, convert_images_to_base64


logger = logging.getLogger("root")


def render_one_line_plots(report_data: List[ReportData]) -> List[str]:
    return [
        multi_line_plots.render_dev_comb_plot(report_data),
        multi_line_plots.render_rpe(report_data),
        bar_plots.render_pos_bar_plot(report_data),
        multi_line_plots.render_dev_pos_plot(report_data),
        multi_line_plots.render_dev_rot_plot(report_data),
        multi_line_plots.render_dev_edf(report_data),
    ]


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

    rpy_available = any(rpe_results) if rpe_results is not None else False
    report_data = [
        ReportData(ate_result=ate_result, rpe_result=rpe_result, settings=report_settings)
        for ate_result, rpe_result in zip(ate_results, rpe_results)
    ]

    one_line_plots = render_one_line_plots(report_data)

    context = {
        "title": "Trajectory Comparison",
        "rpe_available": rpy_available,
        "one_line_plots": one_line_plots,
        "icon": icon,
        "igg": igg,
        "uni_bonn": uni_bonn,
    }

    return template.render(context)
