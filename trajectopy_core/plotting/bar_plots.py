"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""

from typing import List
import pandas as pd
import plotly.express as px
from plotly.offline import plot
from trajectopy_core.report.data import ReportData


def to_metrics_df(report_data: List[ReportData]) -> pd.DataFrame:
    metrics = {}

    def add_to_dict(field_name: str, content: list):
        current_content = metrics.get(field_name) or []
        current_content.extend(content)
        metrics[field_name] = current_content

    for data in report_data:
        add_to_dict("Trajectory", [data.short_name] * 6)
        add_to_dict("Metric", ["ATE", "ATE Min", "ATE Max", "ATE Median", "ATE RMS", "ATE Std"])
        add_to_dict(
            "Value",
            [
                data.ate_result.pos_ate,
                data.ate_result.pos_dev_min,
                data.ate_result.pos_dev_max,
                data.ate_result.pos_dev_median,
                data.ate_result.pos_dev_rms,
                data.ate_result.pos_std,
            ],
        )

    return pd.DataFrame(metrics)


def render_pos_bar_plot(report_data: List[ReportData]) -> None:
    metrics_df = to_metrics_df(report_data)

    fig = px.bar(metrics_df, barmode="group", x="Metric", y="Value", color="Trajectory")

    fig.update_yaxes(title_text=f"Value [{report_data[0].ate_unit}]")
    return plot(fig, output_type="div", config=report_data[0].settings.single_plot_export.to_config())
