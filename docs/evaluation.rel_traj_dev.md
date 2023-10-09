<!-- markdownlint-disable -->

<a href="..\trajectopy_core\evaluation\rel_traj_dev.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `evaluation.rel_traj_dev`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\evaluation\rel_traj_dev.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RelativeTrajectoryDeviations`
This class represents a set of relative trajectory deviations 

Relative trajectory deviations describe relative pose deviations between two trajectories. The deviations are calculated by comparing pairs of positions and orientations in the test and reference trajectory. 

<a href="..\trajectopy_core\evaluation\rel_traj_dev.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(rpe_result: RPEResult, name: str) → None
```






---

#### <kbd>property</kbd> all_distances





---

#### <kbd>property</kbd> all_pos_devs





---

#### <kbd>property</kbd> all_rot_devs





---

#### <kbd>property</kbd> drift_factor





---

#### <kbd>property</kbd> dynamic_pos_dict





---

#### <kbd>property</kbd> dynamic_rot_dict





---

#### <kbd>property</kbd> has_rot_dev





---

#### <kbd>property</kbd> max_pos_devs





---

#### <kbd>property</kbd> max_rot_devs





---

#### <kbd>property</kbd> mean_distances





---

#### <kbd>property</kbd> mean_pos_devs





---

#### <kbd>property</kbd> mean_rot_devs





---

#### <kbd>property</kbd> median_pos_devs





---

#### <kbd>property</kbd> median_rot_devs





---

#### <kbd>property</kbd> min_pos_devs





---

#### <kbd>property</kbd> min_rot_devs





---

#### <kbd>property</kbd> num_pairs





---

#### <kbd>property</kbd> pos_drift_unit





---

#### <kbd>property</kbd> pose_distance_unit





---

#### <kbd>property</kbd> property_dict

Returns a dictionary containing the properties of the deviation set relevant for time based comparisons. This is the case when pose-pairs are defined by a time difference. 

---

#### <kbd>property</kbd> rot_drift_unit





---

#### <kbd>property</kbd> step







---

<a href="..\trajectopy_core\evaluation\rel_traj_dev.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `compute_metric`

```python
compute_metric(
    key: str,
    func: Callable[[Any], float],
    factor: float = 1.0
) → List[float]
```





---

<a href="..\trajectopy_core\evaluation\rel_traj_dev.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str)
```

Reads a set of relative trajectory deviations from a file. 

---

<a href="..\trajectopy_core\evaluation\rel_traj_dev.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(key: str) → List[float]
```





---

<a href="..\trajectopy_core\evaluation\rel_traj_dev.py#L202"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dataframe`

```python
to_dataframe() → DataFrame
```





---

<a href="..\trajectopy_core\evaluation\rel_traj_dev.py#L214"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
