<!-- markdownlint-disable -->

<a href="../trajectopy_core/trajectory.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `trajectory`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="../trajectopy_core/trajectory.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TrajectoryError`








---

<a href="../trajectopy_core/trajectory.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Trajectory`
Class representing a trajectory, i.e. position and orientation of a plattform over time 

Position-Computations are always done in a local frame Time stamps are always in UTC time Rotations are always defined in a East-North-Up frame 

<a href="../trajectopy_core/trajectory.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    pos: PointSet,
    rot: Optional[RotationSet] = None,
    tstamps: Optional[ndarray] = None,
    name: str = '',
    sorting: Optional[Sorting] = None,
    sort_index: Optional[ndarray] = None,
    arc_lengths: Optional[ndarray] = None,
    speed_3d: Optional[ndarray] = None,
    state: Optional[TrajectoryProcessingState] = None
) → None
```






---

#### <kbd>property</kbd> all

Return position and orientation as an nx7 matrix 

---

#### <kbd>property</kbd> arc_length

Return the total trajectory arc_length. 

---

#### <kbd>property</kbd> data_rate

Returns data rate 

---

#### <kbd>property</kbd> fields





---

#### <kbd>property</kbd> function_of

Returns the current parameterization of the trajectory 





**Raises:**
 
 - <b>`ValueError`</b>:  If Sorting is unknown 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Either arclengths (spatial sorting) or  timestamps (chronological sorting) 

---

#### <kbd>property</kbd> has_orientation

Returns True if orientation is available 

---

#### <kbd>property</kbd> idx_chrono

Returns index that represents the chronolgical order 

---

#### <kbd>property</kbd> lap_indices

Returns start indices of laps 

This only makes sense if 

a) The trajectory was repeated, i.e. there  are multiple laps. b) The spatial sorting is known. 

if any of those two prerequisits is not met, this function will return None. 



**Returns:**
 
 - <b>`None | np.ndarray`</b>:  lap indices or None 

---

#### <kbd>property</kbd> se3

Returns SE3 pose list 

---

#### <kbd>property</kbd> sort_index

Returns index that represents the current sorting that may be different than the chronological one 

---

#### <kbd>property</kbd> sort_switching_index

Returns index that, when applied to a trajectory, will switch its sorting (i.e. from spatial to chrono and vice versa) 

---

#### <kbd>property</kbd> sorting





---

#### <kbd>property</kbd> speed

Returns trajectory speeds calculated using consecutive point distances 

---

#### <kbd>property</kbd> speed_3d

Returns computed speeds or custom speeds 



---

<a href="../trajectopy_core/trajectory.py#L669"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `adopt_sampling_and_sorting`

```python
adopt_sampling_and_sorting(
    traj_other: 'Trajectory',
    inplace: bool = True
) → Trajectory
```

Adopt sampling and sorting from another trajectory 

Interpolates trajectory_1 onto trajectory_2 and copies the sorting of trajectory_2. 



**Args:**
 
 - <b>`trajectory_1`</b> (Trajectory):  Trajectory to be  interpolated. 
 - <b>`trajectory_2`</b> (Trajectory):  Target trajectory. 
 - <b>`inplace`</b> (bool, optional):  Perform in-place. 

---

<a href="../trajectopy_core/trajectory.py#L813"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `append`

```python
append(
    trajectory: 'Trajectory',
    inplace: bool = True
) → Optional[ForwardRef('Trajectory')]
```





---

<a href="../trajectopy_core/trajectory.py#L742"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `apply_alignment`

```python
apply_alignment(
    alignment_result: AlignmentResult,
    inplace: bool = True
) → Trajectory
```

Transforms trajectory using alignment parameters. 

After computing the alignment parameters needed to align two trajectories, they can be applied to arbitrary trajectories. 



**Args:**
  alignment_result (AlignmentResult) 
 - <b>`inplace`</b> (bool, optional):  Perform in-place. Defaults to True. 



**Returns:**
 
 - <b>`Trajectory`</b>:  Aligned trajectory 

---

<a href="../trajectopy_core/trajectory.py#L689"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `apply_index`

```python
apply_index(index: Union[list, ndarray], inplace: bool = True) → Trajectory
```

Applies index to the trajectory 

This will be done either in-place or using a new instance of a trajectory. The index can be used to filter and / or sort the components of the trajectory. 

Those components are: 
- timestamps (tstamps) 
- positions (xyz) 
- rotations (rot) 
- arc lengths (arc_lengths) 
- sorting index (_sort_index) 



**Args:**
 
 - <b>`index`</b> (Union[list, np.ndarray]):  index that should be applied 
 - <b>`inplace`</b> (bool, optional):  Perform in-place. Defaults to True. 



**Returns:**
 
 - <b>`Trajectory`</b>:  Trajectory with index applied. 

---

<a href="../trajectopy_core/trajectory.py#L835"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `apply_sorter`

```python
apply_sorter(sorter: SpatialSorter, inplace: bool = True) → Trajectory
```

Apply the sorting information of the trajectory 

Unless not interpolated, this sorting information remains valid. 



**Args:**
 
 - <b>`sorter`</b> (SpatialSorter):  Holds the sorting information 
 - <b>`inplace`</b> (bool, optional):  Perform this. Defaults to True. 



**Returns:**
 
 - <b>`Trajectory`</b>:  Trajectory with sorter applied 

---

<a href="../trajectopy_core/trajectory.py#L727"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `apply_transformation`

```python
apply_transformation(transformation: ndarray, inplace: bool = True) → Trajectory
```

Applies transformation to trajectory 



**Args:**
 
 - <b>`transformation`</b> (np.ndarray):  4x4 Transformation matrix 
 - <b>`inplace`</b> (bool, optional):  Perform in-place. Defaults to True. 



**Returns:**
 
 - <b>`Trajectory`</b>:  Transformed trajectory 

---

<a href="../trajectopy_core/trajectory.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `copy`

```python
copy() → Trajectory
```

Deep copy of itself 

---

<a href="../trajectopy_core/trajectory.py#L463"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `crop`

```python
crop(
    t_start: float,
    t_end: float,
    inverse: bool = False,
    inplace: bool = True
) → Trajectory
```

Crops trajectory to timespan defined by t_start and t_end 



**Args:**
 
 - <b>`t_start`</b> (float):  Start timestamp of desired time span 
 - <b>`t_end`</b> (float):  End timestamp of desired time span 
 - <b>`inverse`</b> (bool, optional):  If true, 'crop' turns  into 'cut', i.e. everthing  outside of t_start and t_end  will be removed.  Defaults to False. 
 - <b>`inplace`</b> (bool, optional):  Perform crop in-place.  Defaults to True. 



**Returns:**
 
 - <b>`Trajectory`</b>:  Cropped trajectory 

---

<a href="../trajectopy_core/trajectory.py#L440"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `divide_into_laps`

```python
divide_into_laps() → Optional[list]
```

Divides Trajectory into sub-trajectories for each lap. 

Only possible if there are lap_indices that can be computed by spatially sorting the trajectory and applying the spatial sorter object to the trajectory. 

---

<a href="../trajectopy_core/trajectory.py#L161"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str) → Trajectory
```

Create trajectory from file 

The file must be a csv file containing columns for at least the timestamp, x, y and z coordinates of the trajectory. Those fields must be named "t", "px", "py" and "pz" in the header using the #fields tag. However, by default a trajectory with "t,px,py,pz,qx,qy,qz,qw" fields is assumed. Additional fields include the arc length, specified by "l", and the speed, specified by "vx", "vy" and "vz". The delimiter can be specified using the #delimiter tag. The default delimiter is a comma. 



**Args:**
 
 - <b>`filename`</b> (str):  path to file 



**Returns:**
 
 - <b>`Trajectory`</b>:  trajectory object 

---

<a href="../trajectopy_core/trajectory.py#L275"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_numpy`

```python
from_numpy(
    xyz: ndarray,
    quat: ndarray,
    tstamps: ndarray,
    epsg: int = 0
) → Trajectory
```

Initialize trajectory using numpy arrays 

---

<a href="../trajectopy_core/trajectory.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `init_arc_lengths`

```python
init_arc_lengths()
```





---

<a href="../trajectopy_core/trajectory.py#L488"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `interpolate`

```python
interpolate(tstamps: Union[list, ndarray], inplace: bool = True) → Trajectory
```

Interpolates a trajectory to specified timestamps 

This method removes timestamps from tstamps if they lie outside of the timestamp range of the trajectory (self). Since providing values for those timestamps would require an extrapolation and not an interpolation, this behaviour is consistent with the definition of this method. 



**Args:**
 
 - <b>`tstamps`</b> (list):  Interpolation timestamps 
 - <b>`inplace`</b> (bool, optional):  Perform in-place interpolation.  Defaults to True. 



**Returns:**
 
 - <b>`Trajectory`</b>:  Interpolated trajectory 

---

<a href="../trajectopy_core/trajectory.py#L550"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `interpolate_positions`

```python
interpolate_positions(tstamps: ndarray, inplace: bool = True) → Trajectory
```

Function for position interpolation of a trajectory 



**Args:**
 
 - <b>`tstamps`</b> (np.ndarray):  Interpolation timestamps 
 - <b>`inplace`</b> (bool, optional):  Perform in-place interpolation. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Interpolated positions 

---

<a href="../trajectopy_core/trajectory.py#L525"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `interpolate_rotations`

```python
interpolate_rotations(
    tstamps: Union[list, ndarray],
    inplace: bool = True
) → Trajectory
```

Function for rotation interpolation of a trajectory 

This method uses Spherical-Linear-Interpolation for rotation interpolation. 



**Args:**
 
 - <b>`tstamps`</b> (np.ndarray):  Interpolation timestamps 
 - <b>`inplace`</b> (bool, optional):  Perform in-place interpolation. 



**Returns:**
 
 - <b>`RotationSet`</b>:  Interpolated Rotationset 

---

<a href="../trajectopy_core/trajectory.py#L584"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `intersect`

```python
intersect(
    tstamps: ndarray,
    max_gap_size: float = 2.0,
    inplace: bool = True
) → Trajectory
```

Intersects trajectory with a given timestamp vector 

After intersection, the trajectory covers the same timespan as 'tstamps'. Further, gaps larger than 'max_gap_size' are removed. If two consecutive timespans in tstamps have a difference of more than 'max_gap_size' seconds, they are considered as the limits of a gap. All timestamps of the trajectory that lie within this gap will be removed. 



**Args:**
 
 - <b>`tstamps`</b> (np.ndarray):  Intersection timespans 
 - <b>`max_gap_size`</b> (float, optional):  Maximum allowed gap between timespans.  If Defaults to 0.5. 
 - <b>`inplace`</b> (bool, optional):  Perform intersection in-place.  Defaults to True. 



**Raises:**
 
 - <b>`ValueError`</b>:  If timespans do not overlap. 



**Returns:**
 
 - <b>`Trajectory`</b>:  Intersected trajectory 

---

<a href="../trajectopy_core/trajectory.py#L568"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `match_timestamps`

```python
match_timestamps(tstamps: ndarray, inplace: bool = True) → Trajectory
```

Truncates trajectory to only those poses where the timestamps exactly match "tstamps" 



**Args:**
 
 - <b>`tstamps`</b> (np.ndarray):  Input timestamps 
 - <b>`inplace`</b> (bool, optional):  Perform matching in-place. Defaults to True. 



**Returns:**
 
 - <b>`Trajectory`</b>:  Trajectory with matched timestamps 

---

<a href="../trajectopy_core/trajectory.py#L632"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `same_sampling`

```python
same_sampling(
    other: 'Trajectory',
    inplace: bool = True
) → Tuple[ForwardRef('Trajectory'), ForwardRef('Trajectory')]
```

Ensures that both trajectories are sampled in the same way 

This method will intersect both trajectories with each other and then approximate the trajectory with the higher data rate onto the other trajectory. The sorting and the arc lengths of both trajectories are identical after the call of this method. 



**Args:**
  other (Trajectory) 
 - <b>`inplace`</b> (bool, optional):  Defaults to True. 



**Returns:**
 
 - <b>`Tuple[Trajectory, Trajectory]`</b>:  Both trajectories with the  same sampling. The instance  which called this method is  the first returned trajectory. 

---

<a href="../trajectopy_core/trajectory.py#L860"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_sorting`

```python
set_sorting(sorting: Sorting, inplace: bool = True) → Trajectory
```

Sets the sorting of the trajectory 



**Args:**
 
 - <b>`sorting`</b> (Sorting):  Either spatial or chronological 
 - <b>`inplace`</b> (bool, optional):  Perform sorting in-place.  Defaults to True. 

---

<a href="../trajectopy_core/trajectory.py#L888"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `switch_sorting`

```python
switch_sorting() → None
```

Switch sorting to previous state 

Method that switches the sorting in-place. 

Since there are only two states 
- Spatial 
- Chrono it is suffienct to switch to the last state that is different than the current one 

---

<a href="../trajectopy_core/trajectory.py#L210"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dataframe`

```python
to_dataframe() → DataFrame
```

Returns a pandas dataframe containing tstamps, xyz, quat 

---

<a href="../trajectopy_core/trajectory.py#L242"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str, mode: str = 'w') → None
```

Writes trajectory to ascii file 

The first line will always be the epsg information. After that, the trajectory data is written. 



**Args:**
 
 - <b>`filename`</b> (str):  Output filename 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
