import os
from typing import Optional

import jinja2

from trajectopy_core.evaluation.ate_result import ATEResult
from trajectopy_core.evaluation.rpe_result import RPEResult
from trajectopy_core.pdf_report.components import histograms, line_plots, scatter_plots
from trajectopy_core.pdf_report.util import number_to_string
from trajectopy_core.util.path import TEMPLATES_PATH, resource_path

STYLE = os.path.relpath(resource_path("trajectopy_core/pdf_report/assets/style.css"))
UNI_BONN = os.path.relpath(resource_path("trajectopy_core/pdf_report/assets/uni-bonn.png"))
IGG = os.path.relpath(resource_path("trajectopy_core/pdf_report/assets/igg.png"))
ICON = os.path.relpath(resource_path("trajectopy_core/pdf_report/assets/icon.png"))


def write_report(
    output_file: str,
    ate_result: ATEResult,
    rpe_result: Optional[RPEResult] = None,
    max_std: float = 3.0,
    mm: bool = False,
):
    template = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_PATH)).get_template("report.html")

    if mm:
        ate_result.abs_dev.pos_dev /= 1000.0
        ate_pos_unit = "mm"
    else:
        ate_pos_unit = "m"

    pos_histogram_plot = histograms.render_pos_devs(ate_result)
    rot_histogram_plot = histograms.render_rot_devs(ate_result)

    sum_line_plot = line_plots.render_sum_line_plot(ate_result)

    pos_line_plot = line_plots.render_pos_time_plot(ate_result)
    rot_line_plot = line_plots.render_rot_time_plot(ate_result)

    pos_scatter_plot = scatter_plots.render_pos_devs(ate_result, max_std=max_std)
    rot_scatter_plot = scatter_plots.render_rot_devs(ate_result, max_std=max_std)

    if rpe_result is not None:
        rpe_plot = line_plots.render_rpe(rpe_result)
    else:
        rpe_plot = None

    context = {
        "title": ate_result.name,
        "ate_pos": number_to_string(ate_result.ate_pos),
        "ate_rot": number_to_string(ate_result.ate_rot),
        "rpe_pos": number_to_string(rpe_result.rpe_pos) if rpe_result is not None else "-",
        "rpe_rot": number_to_string(rpe_result.rpe_rot) if rpe_result is not None else "-",
        "rpe_pos_drift_unit": rpe_result.pos_drift_unit if rpe_result is not None else "-",
        "rpe_rot_drift_unit": rpe_result.rot_drift_unit if rpe_result is not None else "-",
        "ate_pos_unit": ate_pos_unit,
        "pos_histogram_plot": pos_histogram_plot,
        "rot_histogram_plot": rot_histogram_plot,
        "sum_line_plot": sum_line_plot,
        "pos_line_plot": pos_line_plot,
        "rot_line_plot": rot_line_plot,
        "pos_scatter_plot": pos_scatter_plot,
        "rot_scatter_plot": rot_scatter_plot,
        "rpe_plot": rpe_plot,
        "style_file": STYLE,
        "uni_bonn_file": UNI_BONN,
        "igg_file": IGG,
        "icon_file": ICON,
    }

    report_text = template.render(context)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report_text)
