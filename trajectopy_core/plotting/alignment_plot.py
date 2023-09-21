"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.figure import Figure

from trajectopy_core.alignment.parameters import AlignmentParameters
from trajectopy_core.plotting.heatmap import annotate_heatmap, heatmap


def plot_correlation_heatmap(estimated_parameters: AlignmentParameters, enabled_only: bool = True) -> Figure:
    """Plots the correlation heatmap of a covariance matrix.

    Args:
        covariance (np.ndarray): Covariance matrix.

    Returns:
        plt.Figure: Correlation heatmap figure.
    """
    covariance_matrix = estimated_parameters.get_covariance_matrix(enabled_only=enabled_only)
    std_devs = np.sqrt(np.diag(covariance_matrix))
    correlation_matrix = covariance_matrix / np.outer(std_devs, std_devs)
    np.fill_diagonal(correlation_matrix, np.nan)
    fig, ax = plt.subplots()
    ax.grid(False)
    im, _ = heatmap(
        correlation_matrix,
        estimated_parameters.params_labels(enabled_only=enabled_only, lower_case=True),
        estimated_parameters.params_labels(enabled_only=enabled_only, lower_case=True),
        ax=ax,
        cmap="coolwarm",
        cbarlabel="Correlation",
        cbar_kw={"format": "%.2f"},
    )
    annotate_heatmap(im, valfmt="{x:.2f}")
    ax.set_aspect("auto")

    plt.tight_layout()
    return fig


def plot_covariance_heatmap(estimated_parameters: AlignmentParameters, enabled_only: bool = True) -> Figure:
    """Plots the covariance heatmap of a covariance matrix.

    Args:
        covariance (np.ndarray): Covariance matrix.

    Returns:
        plt.Figure: Covariance heatmap figure.
    """
    covariance_matrix = estimated_parameters.get_covariance_matrix(enabled_only=enabled_only)
    fig, ax = plt.subplots()
    ax.grid(False)
    im, _ = heatmap(
        covariance_matrix,
        estimated_parameters.params_labels(enabled_only=enabled_only, lower_case=True),
        estimated_parameters.params_labels(enabled_only=enabled_only, lower_case=True),
        ax=ax,
        cmap="coolwarm",
        cbarlabel="Covariance",
        cbar_kw={"format": "%.2f"},
    )
    annotate_heatmap(im, valfmt="{x:.3f}")
    ax.set_aspect("auto")
    plt.tight_layout()
    return fig
