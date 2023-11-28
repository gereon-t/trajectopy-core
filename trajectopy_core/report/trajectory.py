"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

import logging
import os
from typing import List

import jinja2

from trajectopy_core.plotting import multi_line_plots, scatter_plots
from trajectopy_core.report.utils import convert_images_to_base64
from trajectopy_core.settings.report import ReportSettings
from trajectopy_core.trajectory import Trajectory

base_path = os.path.join(os.path.dirname(__file__))

TEMPLATES_PATH = os.path.join(base_path)

logger = logging.getLogger("root")


def render_one_line_plots(
    trajectories: list[Trajectory], report_settings: ReportSettings = ReportSettings()
) -> List[str]:
    one_line_plots = [scatter_plots.render_trajectories(trajectories, report_settings)]
    one_line_plots.append(multi_line_plots.render_pos_plot(trajectories, report_settings))

    rot_trajectories = [traj for traj in trajectories if traj.has_orientation]

    if rot_trajectories:
        one_line_plots.append(multi_line_plots.render_rot_plot(rot_trajectories, report_settings))

    return one_line_plots


def render_trajectories(*, trajectories: list[Trajectory], report_settings: ReportSettings = ReportSettings()) -> str:
    """
    Render trajectories as scatter plot.

    Args:
        trajectories: List of trajectories to render.
        report_settings: Report settings.

    Returns:
        HTML string of the rendered report including the trajectory plots.
    """

    template = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATES_PATH)).get_template("generic.html")
    igg, uni_bonn, icon = convert_images_to_base64()

    one_line_plots = render_one_line_plots(trajectories, report_settings)

    context = {
        "one_line_plots": one_line_plots,
        "icon": icon,
        "igg": igg,
        "uni_bonn": uni_bonn,
        "report_width": report_settings.report_width,
    }

    return template.render(context)
