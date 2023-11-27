<!-- markdownlint-disable -->

<a href="..\trajectopy_core\evaluation\ate_result.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `evaluation.ate_result`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\evaluation\ate_result.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ATEResult`
This class represents a set of absolute trajectory deviations 

Absolute trajectory deviations describe absolute pose deviations between two trajectories. The deviations are calculated by comparing pairs of positions and orientations in the test and reference trajectory. 

<a href="..\trajectopy_core\evaluation\ate_result.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    trajectory: Trajectory,
    abs_dev: AbsoluteTrajectoryDeviations,
    name: str = ''
) → None
```






---

#### <kbd>property</kbd> columns

Returns the column names of the dataframe 

---

#### <kbd>property</kbd> has_orientation

Returns True if orientation is available 

---

#### <kbd>property</kbd> pos_ate

Returns mean of 3d position deviations 

---

#### <kbd>property</kbd> pos_bias_along

Returns along track bias 

---

#### <kbd>property</kbd> pos_bias_cross_h

Returns horizontal cross track bias 

---

#### <kbd>property</kbd> pos_bias_cross_v

Returns vertical cross track bias 

---

#### <kbd>property</kbd> pos_bias_x

Returns x bias 

---

#### <kbd>property</kbd> pos_bias_y

Returns y bias 

---

#### <kbd>property</kbd> pos_bias_z

Returns z bias 

---

#### <kbd>property</kbd> pos_dev_along

Returns deviations of along track deviations 

---

#### <kbd>property</kbd> pos_dev_comb

Returns position deviations combined using the L2 norm 

---

#### <kbd>property</kbd> pos_dev_cross_h

Returns deviations of horizontal cross track deviations 

---

#### <kbd>property</kbd> pos_dev_cross_v

Returns deviations of vertical cross track deviations 

---

#### <kbd>property</kbd> pos_dev_max

Returns max of 3d position deviations 

---

#### <kbd>property</kbd> pos_dev_median

Returns min of 3d position deviations 

---

#### <kbd>property</kbd> pos_dev_min

Returns min of 3d position deviations 

---

#### <kbd>property</kbd> pos_dev_rms

Returns RMS of 3d positions 

---

#### <kbd>property</kbd> pos_dev_std

Returns std of 3d position deviations 

---

#### <kbd>property</kbd> pos_dev_x

Returns x deviations 

---

#### <kbd>property</kbd> pos_dev_y

Returns y deviations 

---

#### <kbd>property</kbd> pos_dev_z

Returns z deviations 

---

#### <kbd>property</kbd> pos_rms_along

Returns RMS of along track deviations 

---

#### <kbd>property</kbd> pos_rms_cross_h

Returns RMS of horizontal cross track deviations 

---

#### <kbd>property</kbd> pos_rms_cross_v

Returns RMS of vertical cross track deviations 

---

#### <kbd>property</kbd> pos_rms_x

Returns RMS of x deviations 

---

#### <kbd>property</kbd> pos_rms_y

Returns RMS of y deviations 

---

#### <kbd>property</kbd> pos_rms_z

Returns RMS of z deviations 

---

#### <kbd>property</kbd> property_dict





---

#### <kbd>property</kbd> rot_ate

Returns mean of rotation deviations 

---

#### <kbd>property</kbd> rot_bias_x

Returns roll bias 

---

#### <kbd>property</kbd> rot_bias_y

Returns pitch bias 

---

#### <kbd>property</kbd> rot_bias_z

Returns yaw bias 

---

#### <kbd>property</kbd> rot_dev_comb

Returns rotation deviations as single rotation angles 

---

#### <kbd>property</kbd> rot_dev_max

Returns max of rotations 

---

#### <kbd>property</kbd> rot_dev_median

Returns median of rotations 

---

#### <kbd>property</kbd> rot_dev_min

Returns min of rotations 

---

#### <kbd>property</kbd> rot_dev_rms

Returns RMS of rotations 

---

#### <kbd>property</kbd> rot_dev_std

Returns STD of rotations 

---

#### <kbd>property</kbd> rot_dev_x

Returns roll deviations 

---

#### <kbd>property</kbd> rot_dev_y

Returns pitch deviations 

---

#### <kbd>property</kbd> rot_dev_z

Returns yaw deviations 

---

#### <kbd>property</kbd> rot_rms_x

Returns RMS of roll deviations 

---

#### <kbd>property</kbd> rot_rms_y

Returns RMS of pitch deviations 

---

#### <kbd>property</kbd> rot_rms_z

Returns RMS of yaw deviations 



---

<a href="..\trajectopy_core\evaluation\ate_result.py#L398"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str)
```





---

<a href="..\trajectopy_core\evaluation\ate_result.py#L434"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dataframe`

```python
to_dataframe() → DataFrame
```

Exports results as pandas dataframe 

---

<a href="..\trajectopy_core\evaluation\ate_result.py#L456"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```

Exports results as csv 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
