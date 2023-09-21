"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import logging
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Tuple, Union
import uuid

import numpy as np

from trajectopy_core.alignment.parameters import AlignmentParameters, SensorRotationParameters
from trajectopy_core.alignment.result import AlignmentResult
from trajectopy_core.evaluation.abs_traj_dev import AbsoluteTrajectoryDeviations
from trajectopy_core.evaluation.rel_traj_dev import RelativeTrajectoryDeviations
from trajectopy_core.io.header import HeaderData
from trajectopy_core.settings.alignment_settings import AlignmentEstimationSettings
from trajectopy_core.settings.processing_settings import ProcessingSettings
from trajectopy_core.trajectory import Trajectory
from trajectopy_core.util.spatialsorter import Sorting

logger = logging.getLogger("root")


def bool_to_str(input_bool: bool) -> str:
    return "yes" if input_bool else "no"


def generate_id() -> str:
    return str(uuid.uuid4())

@dataclass
class Entry(ABC):
    """Abstract base class for all entries in their respective model."""

    entry_id: str = field(init=False, default_factory=generate_id)
    time: str = field(init=False, default_factory=lambda: str(datetime.now()))

    def __post_init__(self) -> None:
        logger.debug("Created new %s with id: %s", self.type, self.entry_id)

    def renew_id(self) -> None:
        self.entry_id = generate_id()

    def set_id(self, entry_id: str) -> None:
        self.entry_id = entry_id

    @property
    def type(self) -> str:
        return self.__class__.__name__

    @property
    @abstractmethod
    def property_dict(self) -> Dict[str, str]:
        pass

    def to_file(self, filename: str) -> None:
        with open(filename, "w", newline="\n", encoding="utf-8") as file:
            file.write(f"#id {self.entry_id}\n")
            file.write(f"#type {self.type}\n")


@dataclass
class TrajectoryEntry(Entry):
    """Class representing a trajectory entry in the trajectory model."""

    full_filename: str
    trajectory: Trajectory
    set_as_reference: bool = False
    settings: ProcessingSettings = field(default_factory=ProcessingSettings)
    group_id: str = field(default_factory=generate_id)

    def to_file(self, filename: str) -> None:
        super().to_file(filename)
        self.trajectory.to_file(filename=filename, mode="a")

    @classmethod
    def from_file(cls, trajectory_filename: Path, settings_filename: Path) -> "TrajectoryEntry":
        """Creates a new TrajectoryEntry from a trajectory file and a settings file."""
        header_data = HeaderData.from_file(str(trajectory_filename))
        trajectory = Trajectory.from_file(str(trajectory_filename))
        if settings_filename.is_file():
            logger.info("Using existing settings file: %s", settings_filename)
            traj_settings = ProcessingSettings.from_file(str(settings_filename))
        else:
            logger.info(
                "No settings file found. Settings can be provided by storing a yaml file with the same name in the same directory."
            )
            traj_settings = ProcessingSettings()

        if trajectory is None:
            raise ValueError(
                "This file does not seem to have correct trajectory information (Time, X, Y, Z, qx, qy, qz, qw)!"
            )

        traj_entry = TrajectoryEntry(
            full_filename=str(trajectory_filename),
            trajectory=trajectory,
            settings=traj_settings,
        )
        if header_data.id:
            traj_entry.set_id(entry_id=header_data.id)
        return traj_entry

    @property
    def name(self) -> str:
        return self.trajectory.name

    @name.setter
    def name(self, name: str) -> None:
        self.trajectory.name = name

    @property
    def column(self) -> Tuple[str, str, str, int, str, str]:
        return (
            self.name,
            bool_to_str(self.set_as_reference),
            str(self.trajectory.sorting),
            self.trajectory.pos.epsg,
            str(self.trajectory.state),
            self.full_filename,
        )

    @property
    def has_orientations(self) -> str:
        return bool_to_str(self.trajectory.rot is not None)

    @property
    def filename(self) -> str:
        return os.path.basename(self.full_filename)

    @property
    def property_dict(self) -> Dict[str, str]:
        """Shows a new window with trajectory properties"""
        return {
            "Name": self.trajectory.name,
            "Date": f"{datetime.fromtimestamp(self.trajectory.tstamps[0]).strftime('%Y-%m-%d %H:%M:%S')} UTC - "
            f"{datetime.fromtimestamp(self.trajectory.tstamps[-1]).strftime('%Y-%m-%d %H:%M:%S')} UTC",
            "Duration": f"{timedelta(seconds=float(self.trajectory.tstamps[-1] - self.trajectory.tstamps[0]))}",
            "EPSG": f"{self.trajectory.pos.crs}, {self.trajectory.pos.crs.name}"
            if self.trajectory.pos.crs is not None
            else "local / unknown",
            "Orientation available": "yes" if self.trajectory.rot is not None else "no",
            "Number of Poses": str(len(self.trajectory)),
            "Sorting": f"{'Spatial' if self.trajectory.sorting == Sorting.SPATIAL else 'Chronological'}",
            "Length [m]": f"{self.trajectory.arc_length:.3f}",
            "Data Rate [Hz]": f"{self.trajectory.data_rate:.3f}",
            "Minimum Speed [m/s]": f"{np.min(self.trajectory.speed):.3f}",
            "Maximum Speed [m/s]": f"{np.max(self.trajectory.speed):.3f}",
            "Average Speed [m/s]": f"{np.mean(self.trajectory.speed):.3f}",
            "Sorting known": "yes" if self.trajectory.state.sorting_known else "no",
            "Approximated": "yes" if self.trajectory.state.approximated else "no",
            "Intersected": "yes" if self.trajectory.state.intersected else "no",
            "Interpolated": "yes" if self.trajectory.state.interpolated else "no",
            "Matched Timestamps": "yes" if self.trajectory.state.matched else "no",
            "Filename": self.full_filename,
            "UUID": self.entry_id,
        }


@dataclass
class ResultEntry(Entry, ABC):
    """Abstract base class for result entries in the result model."""

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @name.setter
    @abstractmethod
    def name(self, name: str) -> None:
        pass

    @property
    def column(self) -> Tuple[str, str, str, str]:
        return self.name, self.type, self.time, self.entry_id


@dataclass
class DeviationsEntry(ResultEntry, ABC):
    """Abstract base class for deviation entries in the result model."""

    deviations: Union[AbsoluteTrajectoryDeviations, RelativeTrajectoryDeviations]

    @property
    def name(self) -> str:
        return self.deviations.name

    @name.setter
    def name(self, name: str) -> None:
        self.deviations.name = name

    @property
    def property_dict(self) -> Dict[str, str]:
        return self.deviations.property_dict


@dataclass
class AbsoluteDeviationEntry(DeviationsEntry):
    """Class representing a absolute deviation entry in the result model."""

    deviations: AbsoluteTrajectoryDeviations

    def to_file(self, filename: str) -> None:
        super().to_file(filename=filename)
        with open(filename, "a", newline="\n", encoding="utf-8") as file:
            file.write(f"#name {self.name}\n")
            file.write(f"#sorting {str(self.deviations.trajectory.sorting)}\n")
        self.deviations.to_dataframe().to_csv(filename, header=False, index=False, mode="a", float_format="%.12f")

    @classmethod
    def from_file(cls, filename: str) -> "AbsoluteDeviationEntry":
        deviations = AbsoluteTrajectoryDeviations.from_file(filename)
        abs_dev_entry = cls(deviations=deviations)
        abs_dev_entry.set_id(entry_id=HeaderData.from_file(filename).id)
        return abs_dev_entry


@dataclass
class RelativeDeviationEntry(DeviationsEntry):
    """Class representing a relative deviation entry in the result model."""

    deviations: RelativeTrajectoryDeviations

    def to_file(self, filename: str) -> None:
        super().to_file(filename=filename)
        with open(filename, "a", newline="\n", encoding="utf-8") as file:
            file.write(f"#name {self.name}\n")
        self.deviations.to_file(filename)

    @classmethod
    def from_file(cls, filename: str) -> "RelativeDeviationEntry":
        deviations = RelativeTrajectoryDeviations.from_file(filename)
        rel_dev_entry = cls(deviations=deviations)
        rel_dev_entry.set_id(entry_id=HeaderData.from_file(filename).id)
        return rel_dev_entry


@dataclass
class AlignmentEntry(ResultEntry):
    """Entry storing alignment results."""

    alignment_result: AlignmentResult = field(default_factory=AlignmentResult)

    @property
    def estimated_parameters(self) -> AlignmentParameters:
        return self.alignment_result.position_parameters

    @property
    def estimation_of(self) -> AlignmentEstimationSettings:
        return self.alignment_result.estimation_of

    @property
    def name(self) -> str:
        return self.alignment_result.name

    @name.setter
    def name(self, name: str) -> None:
        self.alignment_result.name = name

    @property
    def property_dict(self) -> Dict[str, str]:
        if self.alignment_result.position_parameters is None:
            return {}

        return {
            "Translation x [m]": f"{self.alignment_result.position_parameters.helmert.trans_x.value:<10.4f} s-dev.: {np.sqrt(self.alignment_result.position_parameters.helmert.trans_x.variance):<10.4f}",
            "Translation y [m]": f"{self.alignment_result.position_parameters.helmert.trans_y.value:<10.4f} s-dev.: {np.sqrt(self.alignment_result.position_parameters.helmert.trans_y.variance):<10.4f}",
            "Translation z [m]": f"{self.alignment_result.position_parameters.helmert.trans_z.value:<10.4f} s-dev.: {np.sqrt(self.alignment_result.position_parameters.helmert.trans_z.variance):<10.4f}",
            "Rotation x [°]": f"{np.rad2deg(self.alignment_result.position_parameters.helmert.rot_x.value):<10.4f} s-dev.: {np.rad2deg(np.sqrt(self.alignment_result.position_parameters.helmert.rot_x.variance)):<10.4f}",
            "Rotation y [°]": f"{np.rad2deg(self.alignment_result.position_parameters.helmert.rot_y.value):<10.4f} s-dev.: {np.rad2deg(np.sqrt(self.alignment_result.position_parameters.helmert.rot_y.variance)):<10.4f}",
            "Rotation z [°]": f"{np.rad2deg(self.alignment_result.position_parameters.helmert.rot_z.value):<10.4f} s-dev.: {np.rad2deg(np.sqrt(self.alignment_result.position_parameters.helmert.rot_z.variance)):<10.4f}",
            "Scale [-]": f"{self.alignment_result.position_parameters.helmert.scale.value:<10.4f} s-dev.: {np.sqrt(self.alignment_result.position_parameters.helmert.scale.variance)*1e6:<10.4f} ppm",
            "Time Shift [s]": f"{self.alignment_result.position_parameters.time_shift.value:<10.4f} s-dev.: {np.sqrt(self.alignment_result.position_parameters.time_shift.variance):<10.4f}",
            "Leverarm x [m]": f"{self.alignment_result.position_parameters.leverarm.x.value:<10.4f} s-dev.: {np.sqrt(self.alignment_result.position_parameters.leverarm.x.variance):<10.4f}",
            "Leverarm y [m]": f"{self.alignment_result.position_parameters.leverarm.y.value:<10.4f} s-dev.: {np.sqrt(self.alignment_result.position_parameters.leverarm.y.variance):<10.4f}",
            "Leverarm z [m]": f"{self.alignment_result.position_parameters.leverarm.z.value:<10.4f} s-dev.: {np.sqrt(self.alignment_result.position_parameters.leverarm.z.variance):<10.4f}",
            "Sensor Rotation x [°]": f"{np.rad2deg(self.alignment_result.rotation_parameters.sensor_rot_x.value):<10.4f}",
            "Sensor Rotation y [°]": f"{np.rad2deg(self.alignment_result.rotation_parameters.sensor_rot_y.value):<10.4f}",
            "Sensor Rotation z [°]": f"{np.rad2deg(self.alignment_result.rotation_parameters.sensor_rot_z.value):<10.4f}",
        }

    def to_file(self, filename: str) -> None:
        if self.alignment_result.position_parameters is None:
            raise ValueError("No estimated parameters available!")

        super().to_file(filename=filename)

        with open(filename, "a", newline="\n", encoding="utf-8") as file:
            file.write(f"#name {self.name}\n")

        self.alignment_result.position_parameters.to_dataframe().to_csv(
            filename, header=False, index=False, mode="a", float_format="%.15f"
        )
        self.alignment_result.rotation_parameters.to_file(filename=filename)

    @classmethod
    def from_file(cls, filename: str) -> "AlignmentEntry":
        """Creates a new AlignmentEntry from a file."""
        header_data = HeaderData.from_file(filename)
        estimated_parameters = AlignmentParameters.from_file(filename)
        sensor_rot_parameters = SensorRotationParameters.from_file(filename)
        alignment_entry = cls(
            alignment_result=AlignmentResult(
                name=str(header_data.data.get("name", "Alignment")),
                position_parameters=estimated_parameters,
                estimation_of=AlignmentEstimationSettings.from_bool_list(
                    estimated_parameters.enabled_bool_list + sensor_rot_parameters.enabled_bool_list
                ),
                rotation_parameters=sensor_rot_parameters,
            ),
        )
        alignment_entry.set_id(entry_id=header_data.id)
        return alignment_entry


@dataclass
class PropertyEntry:
    name: str
    values: Tuple[str, ...]

    @property
    def column(self) -> Tuple[str, ...]:
        return (self.name, *self.values)
