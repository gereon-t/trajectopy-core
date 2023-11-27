<!-- markdownlint-disable -->

<a href="..\trajectopy_core\evaluation\rpe_result.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `evaluation.rpe_result`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\evaluation\rpe_result.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RPEResult`
This class represents a set of relative trajectory deviations 

Relative trajectory deviations describe relative pose deviations between two trajectories. The deviations are calculated by comparing pairs of positions and orientations in the test and reference trajectory. 

<a href="..\trajectopy_core\evaluation\rpe_result.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(rpe_dev: RelativeTrajectoryDeviations, name: str) → None
```






---

#### <kbd>property</kbd> all_pair_distances





---

#### <kbd>property</kbd> all_rot_devs





---

#### <kbd>property</kbd> columns





---

#### <kbd>property</kbd> drift_factor





---

#### <kbd>property</kbd> dynamic_pos_dict





---

#### <kbd>property</kbd> dynamic_rot_dict





---

#### <kbd>property</kbd> has_rot_dev





---

#### <kbd>property</kbd> mean_pair_distances





---

#### <kbd>property</kbd> num_pairs





---

#### <kbd>property</kbd> pair_distance_unit





---

#### <kbd>property</kbd> pos_dev_all





---

#### <kbd>property</kbd> pos_dev_max





---

#### <kbd>property</kbd> pos_dev_mean





---

#### <kbd>property</kbd> pos_dev_median





---

#### <kbd>property</kbd> pos_dev_min





---

#### <kbd>property</kbd> pos_drift_unit





---

#### <kbd>property</kbd> pos_rpe





---

#### <kbd>property</kbd> pos_std





---

#### <kbd>property</kbd> property_dict

Returns a dictionary containing the properties of the deviation set relevant for time based comparisons. This is the case when pose-pairs are defined by a time difference. 

---

#### <kbd>property</kbd> rot_dev_max





---

#### <kbd>property</kbd> rot_dev_mean





---

#### <kbd>property</kbd> rot_dev_median





---

#### <kbd>property</kbd> rot_dev_min





---

#### <kbd>property</kbd> rot_drift_unit





---

#### <kbd>property</kbd> rot_rpe

Returns the average rotation drift in radians per 100 meters. 

---

#### <kbd>property</kbd> rot_std





---

#### <kbd>property</kbd> step







---

<a href="..\trajectopy_core\evaluation\rpe_result.py#L68"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `compute_metric`

```python
compute_metric(
    key: str,
    func: Callable[[Any], float],
    factor: float = 1.0
) → List[float]
```





---

<a href="..\trajectopy_core\evaluation\rpe_result.py#L246"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str)
```

Reads a set of relative trajectory deviations from a file. 

---

<a href="..\trajectopy_core\evaluation\rpe_result.py#L143"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_all`

```python
get_all(key: str) → List[float]
```





---

<a href="..\trajectopy_core\evaluation\rpe_result.py#L229"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dataframe`

```python
to_dataframe() → DataFrame
```





---

<a href="..\trajectopy_core\evaluation\rpe_result.py#L237"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
