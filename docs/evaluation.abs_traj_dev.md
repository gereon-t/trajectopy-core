<!-- markdownlint-disable -->

<a href="..\trajectopy_core\evaluation\abs_traj_dev.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `evaluation.abs_traj_dev`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\evaluation\abs_traj_dev.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AbsoluteTrajectoryDeviations`
This class represents a set of absolute trajectory deviations 

Absolute trajectory deviations describe absolute pose deviations between two trajectories. The deviations are calculated by comparing pairs of positions and orientations in the test and reference trajectory. 

<a href="..\trajectopy_core\evaluation\abs_traj_dev.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(trajectory: Trajectory, ate_result: ATEResult, name: str = '') → None
```






---

#### <kbd>property</kbd> along

Returns deviations of along track deviations 

---

#### <kbd>property</kbd> bias_along

Returns along track bias 

---

#### <kbd>property</kbd> bias_cross_h

Returns horizontal cross track bias 

---

#### <kbd>property</kbd> bias_cross_v

Returns vertical cross track bias 

---

#### <kbd>property</kbd> bias_pitch

Returns pitch bias 

---

#### <kbd>property</kbd> bias_roll

Returns roll bias 

---

#### <kbd>property</kbd> bias_x

Returns x bias 

---

#### <kbd>property</kbd> bias_y

Returns y bias 

---

#### <kbd>property</kbd> bias_yaw

Returns yaw bias 

---

#### <kbd>property</kbd> bias_z

Returns z bias 

---

#### <kbd>property</kbd> comb_pos_devs

Returns position deviations combined using the L2 norm 

---

#### <kbd>property</kbd> comb_rot_devs

Returns rotation deviations as single rotation angles 

---

#### <kbd>property</kbd> cross

Returns deviations of horizontal and vertical cross track deviations 

---

#### <kbd>property</kbd> cross_h

Returns deviations of horizontal cross track deviations 

---

#### <kbd>property</kbd> cross_v

Returns deviations of vertical cross track deviations 

---

#### <kbd>property</kbd> has_orientation

Returns True if orientation is available 

---

#### <kbd>property</kbd> max_pos

Returns max of 3d position deviations 

---

#### <kbd>property</kbd> max_rot

Returns max of rotations 

---

#### <kbd>property</kbd> mean_pos

Returns mean of 3d position deviations 

---

#### <kbd>property</kbd> mean_rot

Returns mean of rotations 

---

#### <kbd>property</kbd> median_pos

Returns min of 3d position deviations 

---

#### <kbd>property</kbd> median_rot

Returns median of rotations 

---

#### <kbd>property</kbd> min_pos

Returns min of 3d position deviations 

---

#### <kbd>property</kbd> min_rot

Returns min of rotations 

---

#### <kbd>property</kbd> numeric_property_dict





---

#### <kbd>property</kbd> pos_dev_close_to_zero





---

#### <kbd>property</kbd> property_dict





---

#### <kbd>property</kbd> rms_along

Returns RMS of along track deviations 

---

#### <kbd>property</kbd> rms_cross_h

Returns RMS of horizontal cross track deviations 

---

#### <kbd>property</kbd> rms_cross_v

Returns RMS of vertical cross track deviations 

---

#### <kbd>property</kbd> rms_pitch

Returns RMS of pitch deviations 

---

#### <kbd>property</kbd> rms_pos

Returns RMS of 3d positions 

---

#### <kbd>property</kbd> rms_roll

Returns RMS of roll deviations 

---

#### <kbd>property</kbd> rms_rot

Returns RMS of rotations 

---

#### <kbd>property</kbd> rms_x

Returns RMS of x deviations 

---

#### <kbd>property</kbd> rms_y

Returns RMS of y deviations 

---

#### <kbd>property</kbd> rms_yaw

Returns RMS of yaw deviations 

---

#### <kbd>property</kbd> rms_z

Returns RMS of z deviations 

---

#### <kbd>property</kbd> rpy_dev_close_to_zero





---

#### <kbd>property</kbd> std_pos

Returns std of 3d position deviations 

---

#### <kbd>property</kbd> std_rot

Returns STD of rotations 

---

#### <kbd>property</kbd> x

Returns x deviations 

---

#### <kbd>property</kbd> y

Returns y deviations 

---

#### <kbd>property</kbd> z

Returns z deviations 



---

<a href="..\trajectopy_core\evaluation\abs_traj_dev.py#L150"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `apply_index`

```python
apply_index(
    index: Union[list, ndarray],
    inplace: bool = True
) → AbsoluteTrajectoryDeviations
```





---

<a href="..\trajectopy_core\evaluation\abs_traj_dev.py#L160"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `divide_into_laps`

```python
divide_into_laps() → Optional[List[ForwardRef('AbsoluteTrajectoryDeviations')]]
```

Divides the trajectory into laps and returns a list of deviations for each lap. 

---

<a href="..\trajectopy_core\evaluation\abs_traj_dev.py#L498"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_csv`

```python
from_csv(filename: str) → DataFrame
```

Init DataCollection from csv 

---

<a href="..\trajectopy_core\evaluation\abs_traj_dev.py#L467"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str)
```





---

<a href="..\trajectopy_core\evaluation\abs_traj_dev.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_sorting`

```python
set_sorting(sorting: Sorting, inplace: bool = True)
```





---

<a href="..\trajectopy_core\evaluation\abs_traj_dev.py#L536"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dataframe`

```python
to_dataframe() → DataFrame
```

Exports results as pandas dataframe 


---

<a href="..\trajectopy_core\evaluation\abs_traj_dev.py#L593"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `DeviationCollection`
This class is used to store deviations of multiple trajectories e.g. for plotting 

<a href="..\trajectopy_core\evaluation\abs_traj_dev.py#L599"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(deviations: List[AbsoluteTrajectoryDeviations]) → None
```






---

#### <kbd>property</kbd> all_sorted










---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
