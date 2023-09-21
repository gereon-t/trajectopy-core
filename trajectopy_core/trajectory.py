"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import copy
import logging
from typing import List, Tuple, Union

import numpy as np
import pandas as pd
from pointset import PointSet
from scipy.spatial.transform import Slerp

import trajectopy_core.io.trajectory_io as trajectory_io
import trajectopy_core.util.datahandling as datahandling
from trajectopy_core.alignment.functional_model.equations import leverarm_time_component
from trajectopy_core.alignment.parameters import AlignmentParameters
from trajectopy_core.alignment.result import AlignmentResult
from trajectopy_core.util.rotationset import RotationSet
from trajectopy_core.util.spatialsorter import Sorting, SpatialSorter, detect_laps_by_length, infer_sort_index
from trajectopy_core.util.trajectory_processing_state import TrajectoryProcessingState

# logger configuration
logger = logging.getLogger("root")


class TrajectoryError(Exception):
    pass


class Trajectory:
    """Class representing a trajectory, i.e. position and orientation of a plattform over time

    Position-Computations are always done in a local frame
    Time stamps are always in UTC time
    Rotations are always defined in a East-North-Up frame
    """

    _counter = 1

    def __init__(
        self,
        pos: PointSet,
        rot: Union[RotationSet, None] = None,
        tstamps: Union[np.ndarray, None] = None,
        name: str = "",
        sorting: Union[Sorting, None] = None,
        sort_index: Union[np.ndarray, None] = None,
        arc_lengths: Union[np.ndarray, None] = None,
        speed_3d: Union[np.ndarray, None] = None,
        state: Union[TrajectoryProcessingState, None] = None,
    ) -> None:
        if rot and len(rot) != len(pos):
            raise ValueError("Dimension mismatch between positions and orientations.")

        # pose
        self.pos = pos
        self.rot = rot
        self.tstamps = np.arange(0, len(pos)) if tstamps is None else tstamps

        if speed_3d is not None and len(speed_3d) == len(self.pos):
            self._speed_3d = speed_3d
        else:
            self._speed_3d = datahandling.gradient_3d(xyz=self.pos.to_local(inplace=False).xyz, tstamps=self.tstamps)
            logger.info("Speeds were not provided or had wrong dimensions. Speeds were computed instead.")

        if arc_lengths is not None and len(arc_lengths) == len(self.pos):
            self.arc_lengths = arc_lengths
        else:
            self.arc_lengths = self.init_arc_lengths()
            logger.info("Arc lengths were not provided or had wrong dimensions. Arc lengths were computed instead.")

        if sort_index is not None and len(sort_index) == len(self.pos):
            self._sort_index = np.array(sort_index, dtype=int)
        else:
            self._sort_index = np.arange(0, len(self.pos), dtype=int)
            logger.info("Sort index was not provided or had wrong dimensions. Sort index was derived instead.")

        self.name = name or f"Trajectory {Trajectory._counter}"
        self._sorting = sorting or (Sorting.SPATIAL if tstamps is None else Sorting.CHRONO)
        self.state = state or TrajectoryProcessingState(sorting_known=sorting == Sorting.SPATIAL)

        Trajectory._counter += 1

    def __str__(self) -> str:
        """
        Returns string describing trajectory
        """
        width = 24
        return (
            f"\n _______________________________________________________\n"
            f"| ------------------ Trajectory Info ------------------ |\n"
            f"| Name:                         {self.name:<{width}}|\n"
            f"| Number of poses:              {len(self):<{width}}|\n"
            f"| Orientation available:        {'yes' if self.has_orientation else 'no':<{width}}|\n"
            f"| EPSG:                         {self.pos.epsg:<{width}}|\n"
            f"| Length [m]:                   {self.arc_length:<{width}.3f}|\n"
            f"| Data rate [Hz]:               {self.data_rate:<{width}.3f}|\n"
            f"| Sorting:                      {str(self._sorting):<{width}}|\n"
            f"| Approximated:                 {'yes' if self.state.approximated else 'no':<{width}}|\n"
            f"| Has valid sorting index:      {'yes' if self.state.sorting_known else 'no':<{width}}|\n"
            f"|_______________________________________________________|\n"
        )

    @property
    def has_orientation(self) -> bool:
        """
        Returns True if orientation is available
        """
        return self.rot is not None and len(self.rot) > 0

    def __repr__(self) -> str:
        return str(self)

    def __len__(self) -> int:
        """
        Return number of poses
        """
        return len(self.pos.xyz)

    def __eq__(self, other) -> bool:
        if self.rot is not None and other.rot is not None:
            rot_equal = np.allclose(self.rot.as_quat(), other.rot.as_quat())
        elif self.rot is None and other.rot is None:
            rot_equal = True
        else:
            rot_equal = False

        return (
            np.allclose(self.pos.xyz, other.pos.xyz)
            and rot_equal
            and np.allclose(self.tstamps, other.tstamps)
            and np.allclose(self.arc_lengths, other.arc_lengths)
            and np.allclose(self._speed_3d, other._speed_3d)
            and self.name == other.name
        )

    @property
    def fields(self) -> str:
        return "t,l,px,py,pz,vx,vy,vz" if self.rot is None else "t,l,px,py,pz,qx,qy,qz,qw,vx,vy,vz"

    @property
    def sorting(self) -> Sorting:
        return self._sorting

    @sorting.setter
    def sorting(self, sorting: Sorting) -> None:
        self._sorting = sorting

    def init_arc_lengths(self):
        return datahandling.lengths_from_xyz(self.pos.to_local(inplace=False).xyz)

    def copy(self) -> "Trajectory":
        """
        Deep copy of itself
        """
        return copy.deepcopy(self)

    @classmethod
    def from_file(cls, filename: str) -> "Trajectory":
        """Create trajectory from file

        The file must be a csv file containing columns for at least
        the timestamp, x, y and z coordinates of the trajectory. Those
        fields must be named "t", "px", "py" and "pz" in the header using
        the #fields tag. However, by default a trajectory with
        "t,px,py,pz,qx,qy,qz,qw" fields is assumed. Additional fields
        include the arc length, specified by "l", and the speed, specified
        by "vx", "vy" and "vz".
        The delimiter can be specified using the #delimiter
        tag. The default delimiter is a comma.

        Args:
            filename (str): path to file

        Returns:
            Trajectory: trajectory object
        """
        header_data, trajectory_data = trajectory_io.read_data(filename, dtype=object)

        tstamps = trajectory_io.extract_trajectory_timestamps(header_data=header_data, trajectory_data=trajectory_data)
        pos = trajectory_io.extract_trajectory_pointset(header_data=header_data, trajectory_data=trajectory_data)
        arc_lengths = trajectory_io.extract_trajectory_arc_lengths(
            header_data=header_data, trajectory_data=trajectory_data
        )
        speed_3d = trajectory_io.extract_trajectory_speed(header_data=header_data, trajectory_data=trajectory_data)
        sort_index = infer_sort_index(sorting=header_data.sorting, tstamps=tstamps)
        rot = trajectory_io.extract_trajectory_rotations(header_data=header_data, trajectory_data=trajectory_data)

        trajectory = Trajectory(
            tstamps=tstamps,
            pos=pos,
            rot=rot,
            name=header_data.name,
            sorting=header_data.sorting,
            sort_index=sort_index,
            arc_lengths=arc_lengths,
            speed_3d=speed_3d,
            state=header_data.state,
        )

        if trajectory.sorting == Sorting.CHRONO:
            tstamp_index = np.unique(trajectory.tstamps, return_index=True)[1]
            trajectory.apply_index(tstamp_index)

        return trajectory

    def to_dataframe(self) -> pd.DataFrame:
        """
        Returns a pandas dataframe containing tstamps, xyz, quat
        """

        if self.rot:
            return pd.DataFrame(
                np.c_[self.tstamps, self.function_of, self.pos.xyz, self.rot.as_quat()],
                columns=[
                    "time",
                    "function_of",
                    "pos_x",
                    "pos_y",
                    "pos_z",
                    "rot_x",
                    "rot_y",
                    "rot_z",
                    "rot_w",
                ],
            )

        return pd.DataFrame(
            np.c_[self.tstamps, self.function_of, self.pos.xyz],
            columns=[
                "time",
                "function_of",
                "pos_x",
                "pos_y",
                "pos_z",
            ],
        )

    def to_file(self, filename: str, mode: str = "w") -> None:
        """Writes trajectory to ascii file

        The first line will always be the epsg information.
        After that, the trajectory data is written.

        Args:
            filename (str): Output filename
        """
        if self.rot is None:
            trajectory_data = np.c_[self.tstamps, self.arc_lengths, self.pos.xyz, self.speed_3d]
        else:
            trajectory_data = np.c_[
                self.tstamps,
                self.arc_lengths,
                self.pos.xyz,
                self.rot.as_quat(),
                self.speed_3d,
            ]

        self._write_header(filename, mode=mode)

        pd.DataFrame(trajectory_data).to_csv(filename, header=False, index=False, mode="a", float_format="%.9f")

    def _write_header(self, filename: str, mode: str = "w") -> None:
        with open(filename, mode=mode, newline="\n", encoding="utf-8") as file:
            file.write(f"#epsg {self.pos.epsg}\n")
            file.write(f"#name {self.name}\n")
            file.write(f"#sorting {str(self.sorting)}\n")
            file.write(f"#state {str(self.state)}\n")
            file.write("#nframe enu\n")
            file.write(f"#fields {self.fields}\n")

    @classmethod
    def from_numpy(cls, xyz: np.ndarray, quat: np.ndarray, tstamps: np.ndarray, epsg: int = 0) -> "Trajectory":
        """
        Initialize trajectory using numpy arrays
        """
        pos = PointSet(xyz=xyz, epsg=epsg)
        rot = RotationSet.from_quat(quat)
        return Trajectory(pos=pos, rot=rot, tstamps=tstamps)

    @property
    def function_of(self) -> np.ndarray:
        """Returns the current parameterization of the trajectory


        Raises:
            ValueError: If Sorting is unknown

        Returns:
            np.ndarray: Either arclengths (spatial sorting) or
                        timestamps (chronological sorting)
        """
        if self._sorting == Sorting.CHRONO:
            return self.tstamps

        if self._sorting == Sorting.SPATIAL:
            return self.arc_lengths

        raise ValueError(f"Unknown Sorting {self._sorting}")

    @property
    def all(self) -> np.ndarray:
        """
        Return position and orientation as an nx7 matrix
        """
        if self.rot is None:
            quat = np.zeros((len(self), 4))
            quat[:, -1] = 1
        else:
            quat = self.rot.as_quat()
        return np.c_[self.tstamps, self.pos.xyz, quat]

    @property
    def se3(self) -> List[np.ndarray]:
        """
        Returns SE3 pose list
        """
        se3_list: List[np.ndarray] = []
        xyz = self.pos.xyz

        if len(xyz) == 0:
            return se3_list

        matrices = [np.eye(3)] * len(xyz) if self.rot is None else self.rot.as_matrix()
        for t, r in zip(xyz, matrices):
            se3 = np.eye(4)
            se3[:3, 3] = t
            se3[:3, :3] = r
            se3_list.append(se3)
        return se3_list

    @se3.setter
    def se3(self, se3_list: List[np.ndarray]) -> None:
        """
        Sets position and rotation from se3 list
        """
        xyz = np.zeros((len(se3_list), 3))
        matrices = np.zeros((len(se3_list), 3, 3))

        for i, pose in enumerate(se3_list):
            xyz[i, :] = pose[:3, 3]
            matrices[i, :, :] = pose[:3, :3]

        self.pos.xyz = xyz
        self.rot = RotationSet.from_matrix(matrices)

    @property
    def data_rate(self) -> float:
        """
        Returns data rate
        """
        return 1 / np.mean(np.diff(np.sort(self.tstamps)))

    @property
    def arc_length(self) -> float:
        """
        Return the total trajectory arc_length.
        """
        return 0.0 if len(self.arc_lengths) == 0 else self.arc_lengths[-1]

    @property
    def speed_3d(self) -> np.ndarray:
        """Returns computed speeds or custom speeds"""
        if self._speed_3d is not None:
            return self._speed_3d

        return datahandling.gradient_3d(xyz=self.pos.to_local(inplace=False).xyz, tstamps=self.tstamps)

    @speed_3d.setter
    def speed_3d(self, speed_3d: np.ndarray) -> None:
        """Sets custom speeds"""
        self._speed_3d = speed_3d

    @property
    def speed(self) -> np.ndarray:
        """
        Returns trajectory speeds
        calculated using consecutive point distances
        """
        return np.linalg.norm(self.speed_3d, axis=1)

    @property
    def idx_chrono(self) -> np.ndarray:
        """
        Returns index that represents the chronolgical order
        """
        return np.argsort(self.tstamps)

    @property
    def lap_indices(self) -> Union[None, np.ndarray]:
        """Returns start indices of laps

        This only makes sense if

        a) The trajectory was repeated, i.e. there
           are multiple laps.
        b) The spatial sorting is known.

        if any of those two prerequisits is not
        met, this function will return None.

        Returns:
            None | np.ndarray: lap indices or None
        """
        if not self.state.sorting_known:
            return None

        orig_sorting = copy.deepcopy(self.sorting)
        self.set_sorting(Sorting.CHRONO)
        lap_indices = detect_laps_by_length(self.arc_lengths)
        self.set_sorting(orig_sorting)
        return lap_indices

    @property
    def sort_index(self) -> np.ndarray:
        """
        Returns index that represents the current sorting that may
        be different than the chronological one
        """
        return self._sort_index

    @sort_index.setter
    def sort_index(self, sort_index: np.ndarray) -> None:
        """
        Sets the sort index
        """
        self._sort_index = sort_index

    @property
    def sort_switching_index(self) -> np.ndarray:
        """
        Returns index that, when applied to a trajectory, will
        switch its sorting (i.e. from spatial to chrono and vice versa)
        """
        return np.argsort(self._sort_index)

    def divide_into_laps(self) -> Union[None, list]:
        """Divides Trajectory into sub-trajectories for each lap.

        Only possible if there are lap_indices that can be computed
        by spatially sorting the trajectory and applying the spatial
        sorter object to the trajectory.
        """
        lap_indices = self.lap_indices
        if lap_indices is None:
            return None

        lap_list = []
        chrono_tstamps = np.sort(self.tstamps)
        for i in range(len(lap_indices) - 1):
            lap_trajectory = self.crop(
                t_start=chrono_tstamps[lap_indices[i]],
                t_end=chrono_tstamps[lap_indices[i + 1] - 1],
                inplace=False,
            ).set_sorting(Sorting.SPATIAL)
            lap_trajectory.name += f" Lap {i+1}"
            lap_list.append(lap_trajectory)
        return lap_list

    def crop(self, t_start: float, t_end: float, inverse: bool = False, inplace: bool = True) -> "Trajectory":
        """Crops trajectory to timespan defined by t_start and t_end

        Args:
            t_start (float): Start timestamp of desired time span
            t_end (float): End timestamp of desired time span
            inverse (bool, optional): If true, 'crop' turns
                                      into 'cut', i.e. everthing
                                      outside of t_start and t_end
                                      will be removed.
                                      Defaults to False.
            inplace (bool, optional): Perform crop in-place.
                                      Defaults to True.

        Returns:
            Trajectory: Cropped trajectory
        """
        # filter to t_start and t_end
        if inverse:
            filt = [not t_start <= tstamps <= t_end for tstamps in self.tstamps]
        else:
            filt = [t_start <= tstamps <= t_end for tstamps in self.tstamps]

        return self.apply_index(index=filt, inplace=inplace)

    def interpolate(self, tstamps: Union[list, np.ndarray], inplace: bool = True) -> "Trajectory":
        """Interpolates a trajectory to specified timestamps

        This method removes timestamps from tstamps if they lie
        outside of the timestamp range of the trajectory (self).
        Since providing values for those timestamps would require
        an extrapolation and not an interpolation, this behaviour
        is consistent with the definition of this method.

        Args:
            tstamps (list): Interpolation timestamps
            inplace (bool, optional): Perform in-place interpolation.
                                      Defaults to True.

        Returns:
            Trajectory: Interpolated trajectory
        """
        tstamps = np.sort(tstamps)
        traj_self = self if inplace else self.copy()
        traj_self.set_sorting(Sorting.CHRONO)
        tstamps_cropped = np.array([tstamp for tstamp in tstamps if self.tstamps[0] <= tstamp <= self.tstamps[-1]])

        traj_self.interpolate_positions(tstamps_cropped)
        traj_self.interpolate_rotations(tstamps_cropped)
        traj_self.speed_3d = datahandling.gradient_3d(xyz=traj_self.pos.xyz, tstamps=tstamps_cropped)
        traj_self.arc_lengths = np.interp(tstamps_cropped, traj_self.tstamps, traj_self.arc_lengths)
        traj_self.tstamps = tstamps_cropped

        # rebuild index
        traj_self.sort_index = np.arange(0, len(traj_self.pos), dtype=int)
        traj_self.state.sorting_known = False
        traj_self.state.interpolated = True

        logger.info("Interpolated %s", traj_self.name)

        return traj_self

    def interpolate_rotations(self, tstamps: Union[list, np.ndarray], inplace: bool = True) -> "Trajectory":
        """Function for rotation interpolation of a trajectory

        This method uses Spherical-Linear-Interpolation
        for rotation interpolation.

        Args:
            tstamps (np.ndarray): Interpolation timestamps
            inplace (bool, optional): Perform in-place interpolation.

        Returns:
            RotationSet: Interpolated Rotationset
        """
        traj_self = self if inplace else self.copy()

        if not self.rot or len(tstamps) == 0:
            return traj_self

        # spherical linear orientation interpolation
        # Slerp interpolation, as geodetic curve on unit sphere
        slerp = Slerp(traj_self.tstamps, traj_self.rot)
        r_i = slerp(tstamps)
        traj_self.rot = RotationSet.from_quat(r_i.as_quat())
        return traj_self

    def interpolate_positions(self, tstamps: np.ndarray, inplace: bool = True) -> "Trajectory":
        """Function for position interpolation of a trajectory

        Args:
            tstamps (np.ndarray): Interpolation timestamps
            inplace (bool, optional): Perform in-place interpolation.

        Returns:
            np.ndarray: Interpolated positions
        """
        traj_self = self if inplace else self.copy()

        x_i = np.interp(tstamps, traj_self.tstamps, traj_self.pos.x)
        y_i = np.interp(tstamps, traj_self.tstamps, traj_self.pos.y)
        z_i = np.interp(tstamps, traj_self.tstamps, traj_self.pos.z)
        traj_self.pos.xyz = np.c_[x_i, y_i, z_i]
        return traj_self

    def match_timestamps(self, tstamps: np.ndarray, inplace: bool = True) -> "Trajectory":
        """Truncates trajectory to only those poses where the timestamps exactly match "tstamps"

        Args:
            tstamps (np.ndarray): Input timestamps
            inplace (bool, optional): Perform matching in-place. Defaults to True.

        Returns:
            Trajectory: Trajectory with matched timestamps
        """
        traj_self = self if inplace else self.copy()
        _, idx_self, _ = np.intersect1d(traj_self.tstamps, tstamps, return_indices=True)
        traj_self.apply_index(idx_self)
        traj_self.state.matched = True
        return traj_self

    def intersect(self, tstamps: np.ndarray, max_gap_size: float = 2.0, inplace: bool = True) -> "Trajectory":
        """Intersects trajectory with a given timestamp vector

        After intersection, the trajectory covers the same
        timespan as 'tstamps'. Further, gaps larger than
        'max_gap_size' are removed. If two consecutive
        timespans in tstamps have a difference of more than
        'max_gap_size' seconds, they are considered as the
        limits of a gap. All timestamps of the trajectory
        that lie within this gap will be removed.

        Args:
            tstamps (np.ndarray): Intersection timespans
            max_gap_size (float, optional): Maximum allowed gap between timespans.
                                            If Defaults to 0.5.
            inplace (bool, optional): Perform intersection in-place.
                                      Defaults to True.

        Raises:
            ValueError: If timespans do not overlap.

        Returns:
            Trajectory: Intersected trajectory
        """
        traj_self = self if inplace else self.copy()
        time_span = datahandling.common_time_span(tstamps1=tstamps, tstamps2=traj_self.tstamps)

        if time_span is None:
            raise ValueError("intersect_both: Timespans do not overlap!")

        traj_self.crop(t_start=time_span[0], t_end=time_span[1])

        tstamps_sorted = np.sort(tstamps)
        lower_neighbor_list = np.searchsorted(tstamps_sorted, traj_self.tstamps, side="right") - 1

        filter_index = [
            idx
            for idx, (tstamp, lower_neighbor) in enumerate(zip(traj_self.tstamps, lower_neighbor_list))
            if (
                tstamps_sorted[lower_neighbor] == tstamp
                or (tstamps_sorted[lower_neighbor + 1] - tstamps_sorted[lower_neighbor]) <= max_gap_size
            )
        ]
        traj_self.apply_index(np.array(filter_index, dtype=int))
        traj_self.state.intersected = True

        return traj_self

    def same_sampling(self, other: "Trajectory", inplace: bool = True) -> Tuple["Trajectory", "Trajectory"]:
        """Ensures that both trajectories are sampled in the same way

        This method will intersect both trajectories with each other
        and then approximate the trajectory with the higher data rate
        onto the other trajectory. The sorting and the arc lengths of
        both trajectories are identical after the call of this method.

        Args:
            other (Trajectory)
            inplace (bool, optional): Defaults to True.

        Returns:
            Tuple[Trajectory, Trajectory]: Both trajectories with the
                                           same sampling. The instance
                                           which called this method is
                                           the first returned trajectory.
        """
        traj_self = self if inplace else self.copy()
        traj_other = other if inplace else other.copy()

        orig_sorting_self = traj_self.sorting
        orig_sorting_other = traj_other.sorting

        traj_self.set_sorting(Sorting.CHRONO)
        traj_other.set_sorting(Sorting.CHRONO)

        traj_self.intersect(traj_other.tstamps)
        traj_other.intersect(traj_self.tstamps)

        traj_self.adopt_sampling_and_sorting(traj_other)

        traj_self.set_sorting(orig_sorting_self)
        traj_other.set_sorting(orig_sorting_other)

        return traj_self, traj_other

    def adopt_sampling_and_sorting(self, traj_other: "Trajectory", inplace: bool = True) -> "Trajectory":
        """Adopt sampling and sorting from another trajectory

        Interpolates trajectory_1 onto trajectory_2 and
        copies the sorting of trajectory_2.

        Args:
            trajectory_1 (Trajectory): Trajectory to be
                                       interpolated.
            trajectory_2 (Trajectory): Target trajectory.
            inplace (bool, optional): Perform in-place.
        """
        traj_self = self if inplace else self.copy()
        traj_self.interpolate(traj_other.tstamps)
        traj_self.arc_lengths = copy.deepcopy(traj_other.arc_lengths)
        traj_self.sort_index = copy.deepcopy(traj_other.sort_index)
        traj_self.sorting = traj_other.sorting
        traj_self.state.sorting_known = traj_other.state.sorting_known
        return traj_self

    def apply_index(self, index: Union[list, np.ndarray], inplace: bool = True) -> "Trajectory":
        """Applies index to the trajectory

        This will be done either in-place or using a new
        instance of a trajectory. The index can be used to
        filter and / or sort the components of the trajectory.

        Those components are:
        - timestamps (tstamps)
        - positions (xyz)
        - rotations (rot)
        - arc lengths (arc_lengths)
        - sorting index (_sort_index)

        Args:
            index (Union[list, np.ndarray]): index that should be applied
            inplace (bool, optional): Perform in-place. Defaults to True.

        Returns:
            Trajectory: Trajectory with index applied.
        """
        traj_self = self if inplace else self.copy()

        traj_self.tstamps = traj_self.tstamps[index]
        traj_self.pos.xyz = traj_self.pos.xyz[index, :]

        if traj_self.rot:
            quat_filtered = traj_self.rot.as_quat()[index, :]
            traj_self.rot = RotationSet.from_quat(quat_filtered)

        traj_self.arc_lengths = traj_self.arc_lengths[index]
        traj_self.sort_index = traj_self.sort_index[index]

        if traj_self.speed_3d is not None:
            traj_self.speed_3d = traj_self.speed_3d[index]

        return traj_self

    def apply_transformation(self, transformation: np.ndarray, inplace: bool = True) -> "Trajectory":
        """Applies transformation to trajectory

        Args:
            transformation (np.ndarray): 4x4 Transformation matrix
            inplace (bool, optional): Perform in-place. Defaults to True.

        Returns:
            Trajectory: Transformed trajectory

        """
        traj_self = self if inplace else self.copy()
        traj_self.se3 = [np.dot(transformation, p) for p in traj_self.se3]
        return traj_self

    def apply_alignment(self, alignment_result: AlignmentResult, inplace: bool = True) -> "Trajectory":
        """Transforms trajectory using alignment parameters.

        After computing the alignment parameters needed to align
        two trajectories, they can be applied to arbitrary trajectories.

        Args:
            alignment_result (AlignmentResult)
            inplace (bool, optional): Perform in-place. Defaults to True.

        Returns:
            Trajectory: Aligned trajectory
        """
        traj_self = self if inplace else self.copy()

        # leverarm and time
        (
            euler_x,
            euler_y,
            euler_z,
            lever_x,
            lever_y,
            lever_z,
        ) = self._prepare_alignment_application(alignment_result.position_parameters, traj_self)

        speed_3d = traj_self.speed_3d
        speed_x, speed_y, speed_z = speed_3d[:, 0], speed_3d[:, 1], speed_3d[:, 2]

        trafo_x, trafo_y, trafo_z = leverarm_time_component(
            euler_x=euler_x,
            euler_y=euler_y,
            euler_z=euler_z,
            lever_x=lever_x,
            lever_y=lever_y,
            lever_z=lever_z,
            time_shift=alignment_result.position_parameters.time_shift.value,
            speed_x=speed_x,
            speed_y=speed_y,
            speed_z=speed_z,
        )
        traj_self.pos.xyz += np.c_[trafo_x, trafo_y, trafo_z]

        # similiarity transformation
        traj_self.apply_transformation(alignment_result.position_parameters.sim3_matrix)

        logger.info("Applied alignment parameters to positions.")

        # sensor orientation
        if traj_self.rot is not None:
            traj_self.rot = alignment_result.rotation_parameters.rotation_set * traj_self.rot
            logger.info("Applied alignment parameters to orientations.")

        traj_self.state.aligned = True
        return traj_self

    def _prepare_alignment_application(self, alignment_parameters: AlignmentParameters, traj_self: "Trajectory"):
        if traj_self.rot is not None:
            rpy = traj_self.rot.as_euler("xyz", degrees=False)
            euler_x, euler_y, euler_z = rpy[:, 0], rpy[:, 1], rpy[:, 2]
            lever_x, lever_y, lever_z = (
                alignment_parameters.lever_x.value,
                alignment_parameters.lever_y.value,
                alignment_parameters.lever_z.value,
            )
        else:
            logger.error("Trajectory has no orientations. Cannot apply leverarm.")
            euler_x, euler_y, euler_z = 0, 0, 0
            lever_x, lever_y, lever_z = 0, 0, 0

        return euler_x, euler_y, euler_z, lever_x, lever_y, lever_z

    def append(self, trajectory: "Trajectory", inplace: bool = True) -> Union["Trajectory", None]:
        if trajectory.has_orientation != self.has_orientation:
            logger.error("Cannot append trajectories with different orientation states")
            return None

        traj_self = self if inplace else self.copy()

        traj_self.tstamps = np.concatenate((traj_self.tstamps, trajectory.tstamps), axis=None)
        traj_self.pos.xyz = np.concatenate((traj_self.pos.xyz, trajectory.pos.xyz), axis=0)
        traj_self.speed_3d = np.concatenate((traj_self.speed_3d, trajectory.speed_3d), axis=0)

        if traj_self.rot is not None and trajectory.rot is not None:
            merged_quat = np.concatenate((traj_self.rot.as_quat(), trajectory.rot.as_quat()), axis=0)
            traj_self.rot = RotationSet.from_quat(merged_quat)

        traj_self.arc_lengths = traj_self.init_arc_lengths()
        traj_self.sort_index = np.arange(0, len(traj_self.pos), dtype=int)
        traj_self.apply_index(index=np.argsort(traj_self.tstamps))
        traj_self.sorting = Sorting.CHRONO

        return traj_self

    def apply_sorter(self, sorter: SpatialSorter, inplace: bool = True) -> "Trajectory":
        """Apply the sorting information of the trajectory

        Unless not interpolated, this sorting information remains
        valid.

        Args:
            sorter (SpatialSorter): Holds the sorting information
            inplace (bool, optional): Perform this. Defaults to True.

        Returns:
            Trajectory: Trajectory with sorter applied
        """
        traj_self = self if inplace else self.copy()

        # sort
        traj_self.apply_index(index=sorter.idx_sort)
        traj_self.sort_index = np.array(sorter.idx_sort, dtype=int)
        traj_self.arc_lengths = sorter.function_of

        traj_self.sorting = Sorting.SPATIAL
        traj_self.state.sorting_known = True

        return traj_self

    def set_sorting(self, sorting: Sorting, inplace: bool = True) -> "Trajectory":
        """Sets the sorting of the trajectory

        Args:
            sorting (Sorting): Either spatial or chronological
            inplace (bool, optional): Perform sorting in-place.
                                      Defaults to True.
        """

        traj_self = self if inplace else self.copy()

        if traj_self.sorting == sorting:
            return traj_self

        if traj_self.sorting == Sorting.CHRONO and sorting == Sorting.SPATIAL and not traj_self.state.sorting_known:
            raise TrajectoryError(
                (
                    f"Could not change sorting from {traj_self.sorting} to {sorting}"
                    ", because there are no valid sorting indices available. "
                    "Reasons for this might be, that you never applied a sorter to"
                    " the trajectory or that the sorter got invalid due to interpolation."
                ),
            )
        traj_self.switch_sorting()
        traj_self.sorting = sorting

        return traj_self

    def switch_sorting(self) -> None:
        """Switch sorting to previous state

        Method that switches the sorting
        in-place.

        Since there are only two states
        - Spatial
        - Chrono
        it is suffienct to switch to the last state that
        is different than the current one
        """
        idx_order = self.sort_switching_index
        self.apply_index(idx_order)
        self._sort_index = np.array(idx_order, dtype=int)
