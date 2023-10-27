import plotly.graph_objects as go
from plotly.offline import plot

from trajectopy_core.report.data import ReportData


def render_pos_devs(report_data: ReportData) -> str:
    fig = go.Figure()

    fig.add_trace(go.Histogram(x=report_data.along, name="along", opacity=0.7))
    fig.add_trace(go.Histogram(x=report_data.cross_h, name="cross-h", opacity=0.7))
    fig.add_trace(go.Histogram(x=report_data.cross_v, name="cross-v", opacity=0.7))

    fig.update_layout(
        title="Position Deviations",
        xaxis=dict(title=f"Absolute Position Error [{report_data.ate_unit}]"),
        yaxis=dict(title="Count"),
        barmode="overlay",
        bargap=0.1,
    )

    return plot(fig, output_type="div")


def render_rot_devs(report_data: ReportData) -> str:
    fig = go.Figure()

    fig.add_trace(go.Histogram(x=report_data.roll, name="roll", opacity=0.7))
    fig.add_trace(go.Histogram(x=report_data.pitch, name="pitch", opacity=0.7))
    fig.add_trace(go.Histogram(x=report_data.yaw, name="yaw", opacity=0.7))

    fig.update_layout(
        title="Rotation Deviations",
        xaxis=dict(title="Absolute Rotation Error [°]"),
        yaxis=dict(title="Count"),
        barmode="overlay",
        bargap=0.1,
    )

    return plot(fig, output_type="div")
