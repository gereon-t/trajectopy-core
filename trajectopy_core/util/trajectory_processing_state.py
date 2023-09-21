"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
from dataclasses import dataclass


@dataclass
class TrajectoryProcessingState:
    """
    Class to store the processing state of a trajectory.
    For example, if a trajectory is interpolated, the attribute
    interpolated is set to True.
    """

    approximated: bool = False
    interpolated: bool = False
    intersected: bool = False
    aligned: bool = False
    matched: bool = False
    sorting_known: bool = False

    def __str__(self) -> str:
        return ", ".join([str(key) for key, value in self.__dict__.items() if value])

    @classmethod
    def from_string(cls, input_string: str) -> "TrajectoryProcessingState":
        return cls(
            approximated="approximated" in input_string,
            interpolated="interpolated" in input_string,
            intersected="intersected" in input_string,
            aligned="aligned" in input_string,
            matched="matched" in input_string,
            sorting_known="sorting_known" in input_string,
        )
