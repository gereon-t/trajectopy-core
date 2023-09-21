"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
from typing import Union

from trajectopy_core.util.entries import AbsoluteDeviationEntry, AlignmentEntry, RelativeDeviationEntry
from trajectopy_core.io.header import HeaderData

logger = logging.getLogger("root")


def read_result_file(
    filename: str,
) -> Union[AbsoluteDeviationEntry, RelativeDeviationEntry, AlignmentEntry]:
    """
    Reads a result file and returns an object of the appropriate type based on the file's header data.

    Args:
        filename (str): The path to the result file to read.

    Returns:
        Union[AbsoluteDeviationEntry, RelativeDeviationEntry, AlignmentEntry]: An object of the appropriate type based on the file's header data.

    Raises:
        ValueError: If the result file type is not supported.
    """
    header_data = HeaderData.from_file(filename)

    if header_data.type == AbsoluteDeviationEntry.__name__.lower():
        logger.info("Detected Absolute Deviations file.")
        return AbsoluteDeviationEntry.from_file(filename)

    if header_data.type == RelativeDeviationEntry.__name__.lower():
        logger.info("Detected Relative Deviations file.")
        return RelativeDeviationEntry.from_file(filename)

    if header_data.type == "alignmententry":
        logger.info("Detected Alignment file.")
        return AlignmentEntry.from_file(filename)

    raise ValueError(f"No supported result type '{header_data.type}'")
