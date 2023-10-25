"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
import os
import sys

logger = logging.getLogger("root")


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


TEMPLATES_PATH = resource_path("trajectopy_core/pdf_report/templates")


def mplstyle_file_path() -> str:
    custom_path = os.path.join("./custom.mplstyle")
    if os.path.isfile(custom_path):
        logger.info("Using custom matplotlib style from %s", custom_path)
        return custom_path

    logger.info(
        "Using default settings for matplotlib style. You can use custom styles by creating a 'custom.mplstyle' file in the current directory."
    )
    return resource_path("trajectopy_core/plotting/default.mplstyle")
