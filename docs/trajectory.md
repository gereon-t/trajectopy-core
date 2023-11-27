<!-- markdownlint-disable -->

<a href="..\trajectopy_core\trajectory.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `trajectory`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\trajectory.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TrajectoryError`








---

<a href="..\trajectopy_core\trajectory.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Trajectory`
Class representing a trajectory, i.e. position and orientation of a plattform over time 

Position-Computations are always done in a local frame Time stamps are always in UTC time Rotations are always defined in a East-North-Up frame 

<a href="..\trajectopy_core\trajectory.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    pos: PointSet,
    rot: Optional[RotationSet] = None,
    tstamps: Optional[ndarray] = None,
    name: str = '',
    arc_lengths: Optional[ndarray] = None,
    speed_3d: Optional[ndarray] = None,
    sort_by: str = 'time'
) → None
```






---

#### <kbd>property</kbd> data_rate

Returns data rate 

---

#### <kbd>property</kbd> function_of

Returns the function of the trajectory 

---

#### <kbd>property</kbd> function_of_label

Returns the label of the function of the trajectory 

---

#### <kbd>property</kbd> function_of_unit

Returns the unit of the function of the trajectory 

---

#### <kbd>property</kbd> has_orientation

Returns True if orientation is available 

---

#### <kbd>property</kbd> quat

Returns the quaternion of the trajectory 

---

#### <kbd>property</kbd> rpy

Returns the roll, pitch, yaw of the trajectory 

---

#### <kbd>property</kbd> se3

Returns SE3 pose list 

---

#### <kbd>property</kbd> speed

Returns trajectory speeds calculated using consecutive point distances 

---

#### <kbd>property</kbd> speed_3d

Returns computed speeds or custom speeds 

---

#### <kbd>property</kbd> total_length

Return the total trajectory arc_length. 

---

#### <kbd>property</kbd> xyz

Returns the xyz coordinates of the trajectory 



---

<a href="..\trajectopy_core\trajectory.py#L616"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `append`

```python
append(
    trajectory: 'Trajectory',
    inplace: bool = True
) → Optional[ForwardRef('Trajectory')]
```





---

<a href="..\trajectopy_core\trajectory.py#L564"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\trajectory.py#L601"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\trajectory.py#L127"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `copy`

```python
copy() → Trajectory
```

Deep copy of itself 

---

<a href="..\trajectopy_core\trajectory.py#L374"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\trajectory.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str, io_stream: bool = False) → Trajectory
```

Create trajectory from file 

The file must be a csv file containing columns for at least the timestamp, x, y and z coordinates of the trajectory. Those fields must be named "t", "px", "py" and "pz" in the header using the #fields tag. However, by default a trajectory with "t,px,py,pz,qx,qy,qz,qw" fields is assumed. Additional fields include the arc length, specified by "l", and the speed, specified by "vx", "vy" and "vz". The delimiter can be specified using the #delimiter tag. The default delimiter is a comma. 



**Args:**
 
 - <b>`filename`</b> (str):  path to file 
 - <b>`io_stream`</b> (bool, optional):  If true, the file is read from a stream. 



**Returns:**
 
 - <b>`Trajectory`</b>:  trajectory object 

---

<a href="..\trajectopy_core\trajectory.py#L296"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\trajectory.py#L124"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `init_arc_lengths`

```python
init_arc_lengths()
```





---

<a href="..\trajectopy_core\trajectory.py#L399"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\trajectory.py#L488"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\trajectory.py#L473"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\trajectory.py#L535"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\trajectory.py#L225"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dataframe`

```python
to_dataframe(sort_by: str = '') → DataFrame
```

Returns a pandas dataframe containing tstamps, xyz, quat 



**Args:**
 
 - <b>`sort_by`</b> (str, optional):  Column to sort by. This  overrides the current sort_by  attribute. 



**Returns:**
 
 - <b>`pd.DataFrame`</b>:  Trajectory as dataframe 

---

<a href="..\trajectopy_core\trajectory.py#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
