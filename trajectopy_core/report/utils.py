"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import base64
import logging
import os
import sys
import uuid
import webbrowser

# import webbrowser
from typing import Tuple

import numpy as np

# logger configuration
logger = logging.getLogger("root")

try:
    BASE_PATH = os.path.join(sys._MEIPASS, "trajectopy")
except Exception:
    BASE_PATH = os.path.dirname(__file__)
TEMPLATES_PATH = os.path.join(BASE_PATH, "templates")


def number_to_string(number: float) -> str:
    return f"{number:.3f}"


def image_to_base64(image_path: str) -> str:
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string


def convert_images_to_base64() -> Tuple[str, str, str]:
    igg_path = os.path.join(os.path.join(BASE_PATH), "assets", "igg.png")
    uni_bonn_path = os.path.join(os.path.join(BASE_PATH), "assets", "uni_bonn.png")
    icon_path = os.path.join(os.path.join(BASE_PATH), "assets", "icon.png")

    igg_base64 = image_to_base64(igg_path)
    uni_bonn_base64 = image_to_base64(uni_bonn_path)
    icon_base64 = image_to_base64(icon_path)

    return igg_base64, uni_bonn_base64, icon_base64


def shrink_data(data: np.ndarray, max_size: int = 1000) -> np.ndarray:
    """
    Shrink the given data to the given max_size by taking
    the moving average of the data.

    Args:
        data (np.ndarray): The data to shrink
        max_size (int): The maximum size of the data

    Returns:
        np.ndarray: The shrunk data
    """
    if max_size < 0:
        return data

    if len(data) <= max_size:
        return data

    data = data.astype(float)
    array_size = (-len(data) % max_size) + len(data)
    padded_data = np.pad(data, (0, array_size - len(data)))
    padded_data[padded_data == 0] = np.nan

    reshaped_data = np.array(
        [row for row in padded_data.reshape(-1, len(padded_data) // max_size) if not np.all(np.isnan(row))]
    )

    return np.nanmean(reshaped_data, 1)


def write_report(*, output_file: str, report_text: str) -> None:
    """
    Writes a report to the given output file.

    Args:

        output_file (str): The output file path

    """
    logger.info("Writing report to %s", output_file)
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(report_text)


def show_report(report_text: str, filepath: str = "") -> None:
    """
    Shows a report in the browser.

    Args:

        report_text (str): The report string

    """
    dirname = os.path.dirname(filepath)
    if not os.path.exists(dirname):
        os.mkdir(dirname)

    random_string = uuid.uuid4().hex

    file = filepath or os.path.join(dirname, f"{random_string}.html")

    with open(file, "w", encoding="utf-8") as f:
        f.write(report_text)
        url = "file://" + os.path.realpath(f.name)
        webbrowser.open(url)
