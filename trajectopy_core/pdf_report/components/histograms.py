import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot

from trajectopy_core.evaluation.ate_result import ATEResult


def render_pos_devs(ate_result: ATEResult) -> str:
    fig = go.Figure()

    fig.add_trace(go.Histogram(x=ate_result.along, name="along", opacity=0.7))
    fig.add_trace(go.Histogram(x=ate_result.cross_h, name="cross-h", opacity=0.7))
    fig.add_trace(go.Histogram(x=ate_result.cross_v, name="cross-v", opacity=0.7))

    fig.update_layout(
        title="Position Deviations",
        xaxis=dict(title="Absolute Position Error [m]"),
        yaxis=dict(title="Count"),
        barmode="overlay",
        bargap=0.1,
    )

    return plot(fig, output_type="div")


def render_rot_devs(ate_result: ATEResult) -> str:
    fig = go.Figure()

    fig.add_trace(go.Histogram(x=np.rad2deg(ate_result.roll), name="roll", opacity=0.7))
    fig.add_trace(go.Histogram(x=np.rad2deg(ate_result.pitch), name="pitch", opacity=0.7))
    fig.add_trace(go.Histogram(x=np.rad2deg(ate_result.yaw), name="yaw", opacity=0.7))

    fig.update_layout(
        title="Rotation Deviations",
        xaxis=dict(title="Absolute Rotation Error [°]"),
        yaxis=dict(title="Count"),
        barmode="overlay",
        bargap=0.1,
    )

    return plot(fig, output_type="div")
