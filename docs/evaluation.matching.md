<!-- markdownlint-disable -->

<a href="../trajectopy_core/evaluation/matching.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `evaluation.matching`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="../trajectopy_core/evaluation/matching.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `match_trajectories`

```python
match_trajectories(
    traj_test: Trajectory,
    traj_ref: Trajectory,
    settings: MatchingSettings,
    inplace: bool = True
) → Tuple[Trajectory, Trajectory]
```

Matches two trajectories using the specified method 

Supported methods: 
    - MatchingMethod.INTERPOLATION 
    - MatchingMethod.NEAREST_TEMPORAL 
    - MatchingMethod.NEAREST_SPATIAL 


---

<a href="../trajectopy_core/evaluation/matching.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `match_trajectories_temporal`

```python
match_trajectories_temporal(
    traj_test: Trajectory,
    traj_ref: Trajectory,
    max_distance: float = 0.01
) → Tuple[Trajectory, Trajectory]
```

This method matches both trajectories temporally 

After this operation, both trajectories will have the length of the test trajectory. This means, that the reference trajectory may be modified. 



**Args:**
 
 - <b>`traj_test`</b> (Trajectory):  Test trajectory 
 - <b>`traj_ref`</b> (Trajectory):  Reference trajectory 
 - <b>`max_distance`</b> (float, optional):  Maximum distance between two timestamps.  Defaults to 0.1. 



**Returns:**
 
 - <b>`Tuple[Trajectory, Trajectory]`</b>:  Matched trajectories 


---

<a href="../trajectopy_core/evaluation/matching.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `match_trajectories_spatial`

```python
match_trajectories_spatial(
    traj_test: Trajectory,
    traj_ref: Trajectory,
    max_distance: float = 0.0
) → Tuple[Trajectory, Trajectory]
```

This method matches both trajectories spatially 

After this operation, both trajectories will have the length of the test trajectory. This means, that the reference trajectory may be modified. 



**Args:**
 
 - <b>`traj_from`</b> (Trajectory):  Test trajectory 
 - <b>`traj_to`</b> (Trajectory):  Reference trajectory 
 - <b>`max_distance`</b> (float, optional):  Maximum distance between two poses.  Defaults to None. This means all  matches are accepted. 



**Returns:**
 
 - <b>`Tuple[Trajectory, Trajectory]`</b>:  Matched trajectories 


---

<a href="../trajectopy_core/evaluation/matching.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `kd_matcher`

```python
kd_matcher(
    ref: ndarray,
    test: ndarray,
    max_distance: float = 0.0
) → Tuple[ndarray, ndarray]
```

This method matches data using a KDTree 



**Args:**
 
 - <b>`ref`</b> (np.ndarray):  Reference data 
 - <b>`test`</b> (np.ndarray):  Test data 
 - <b>`max_distance`</b> (float):  Maximum distance for a match 



**Returns:**
 
 - <b>`Tuple[np.ndarray, np.ndarray]`</b>:  Matched indices 


---

<a href="../trajectopy_core/evaluation/matching.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rough_timestamp_matching`

```python
rough_timestamp_matching(
    traj_ref: Trajectory,
    traj_test: Trajectory,
    max_distance: float = 0.0
) → float
```

This method roughly matches two trajectories temporally 

**Args:**
 
 - <b>`traj_from`</b> (Trajectory):  Test trajectory 
 - <b>`traj_to`</b> (Trajectory):  Reference trajectory 



**Returns:**
 
 - <b>`float`</b>:  Mean time offset 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
