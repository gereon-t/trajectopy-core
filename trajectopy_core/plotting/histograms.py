import plotly.graph_objects as go
from plotly.offline import plot

from trajectopy_core.report.data import ReportData


def render_pos_devs(report_data: ReportData) -> str:
    fig = go.Figure()

    fig.add_trace(
        go.Histogram(
            x=report_data.pos_dev_x, name=report_data.pos_dev_x_name, opacity=report_data.settings.histogram_opacity
        )
    )
    fig.add_trace(
        go.Histogram(
            x=report_data.pos_dev_y, name=report_data.pos_dev_y_name, opacity=report_data.settings.histogram_opacity
        )
    )
    fig.add_trace(
        go.Histogram(
            x=report_data.pos_dev_z, name=report_data.pos_dev_z_name, opacity=report_data.settings.histogram_opacity
        )
    )

    fig.update_layout(
        title="Position Deviations",
        xaxis=dict(title=f"Absolute Position Error [{report_data.ate_unit}]"),
        yaxis=dict(title="Count"),
        barmode="overlay",
        bargap=0.1,
    )
    return plot(fig, output_type="div", config=report_data.settings.png_export.to_config())


def render_rot_devs(report_data: ReportData) -> str:
    fig = go.Figure()

    fig.add_trace(go.Histogram(x=report_data.rot_dev_x, name="roll", opacity=report_data.settings.histogram_opacity))
    fig.add_trace(go.Histogram(x=report_data.rot_dev_y, name="pitch", opacity=report_data.settings.histogram_opacity))
    fig.add_trace(go.Histogram(x=report_data.rot_dev_z, name="yaw", opacity=report_data.settings.histogram_opacity))

    fig.update_layout(
        title="Rotation Deviations",
        xaxis=dict(title="Absolute Rotation Error [deg]"),
        yaxis=dict(title="Count"),
        barmode="overlay",
        bargap=0.1,
    )

    return plot(fig, output_type="div", config=report_data.settings.png_export.to_config())
