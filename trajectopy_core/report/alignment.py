"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

import logging
from typing import List

import jinja2
import numpy as np
import pandas as pd

from trajectopy_core.alignment.parameters import AlignmentParameters
from trajectopy_core.alignment.result import AlignmentResult
from trajectopy_core.plotting import heatmaps, tables
from trajectopy_core.report.utils import TEMPLATES_PATH, convert_images_to_base64
from trajectopy_core.settings.report import ReportSettings

logger = logging.getLogger("root")


def build_correlation_dataframe(estimated_parameters: AlignmentParameters, enabled_only: bool = True) -> pd.DataFrame:
    covariance_matrix = estimated_parameters.get_covariance_matrix(enabled_only=enabled_only)
    std_devs = np.sqrt(np.diag(covariance_matrix))
    correlation_matrix = covariance_matrix / np.outer(std_devs, std_devs)
    np.fill_diagonal(correlation_matrix, np.nan)
    labels = estimated_parameters.params_labels(enabled_only=enabled_only, lower_case=True)
    return pd.DataFrame(
        correlation_matrix,
        index=labels,
        columns=labels,
    )


def render_one_line_plots(
    alignment_result: AlignmentResult, report_settings: ReportSettings = ReportSettings()
) -> List[str]:
    dataframe = build_correlation_dataframe(alignment_result.position_parameters, enabled_only=True)

    one_line_plots = [tables.render_alignment_table(alignment_result.position_parameters, report_settings)]
    one_line_plots.append(heatmaps.render_heatmap(dataframe, report_settings))

    return one_line_plots


def render_heatmaps(*, alignment_result: AlignmentResult, report_settings: ReportSettings = ReportSettings()) -> str:
    """
    Render trajectory alignment heatmaps.

    Heatmaps are covariance matrix and correlation matrix.

    Args:
        alignment_result: The alignment result to render.
        report_settings: Report settings.

    Returns:
        HTML string of the rendered report including the heatmap plots.
    """

    template = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_PATH)).get_template("generic.html")
    igg, uni_bonn, icon = convert_images_to_base64()

    one_line_plots = render_one_line_plots(alignment_result, report_settings)

    context = {
        "title": alignment_result.name,
        "one_line_plots": one_line_plots,
        "icon": icon,
        "igg": igg,
        "uni_bonn": uni_bonn,
        "report_width": report_settings.report_width,
    }

    return template.render(context)
