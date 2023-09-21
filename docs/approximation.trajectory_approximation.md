<!-- markdownlint-disable -->

<a href="../trajectopy_core/approximation/trajectory_approximation.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `approximation.trajectory_approximation`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="../trajectopy_core/approximation/trajectory_approximation.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TrajectoryApproximation`
Class representing an approximation 

<a href="../trajectopy_core/approximation/trajectory_approximation.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
    settings: Optional[ApproximationSettings] = None,
    state: Optional[TrajectoryProcessingState] = None
) → None
```

Create new Approximation Trajectory 

During initialization, deep copies of the input trajectory field are made. 



**Args:**
 
 - <b>`traj`</b> (Trajectory):  Trajectory that should be approximated 
 - <b>`config`</b> (ApproximationConfig, optional):  Contains approximation settings.  Defaults to ApproximationConfig(). 



**Raises:**
 
 - <b>`ValueError`</b>:  _description_ 


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

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
