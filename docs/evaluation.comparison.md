<!-- markdownlint-disable -->

<a href="..\trajectopy_core\evaluation\comparison.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `evaluation.comparison`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `compare_trajectories_absolute`

```python
compare_trajectories_absolute(
    traj_test: Trajectory,
    traj_ref: Trajectory
) → ATEResult
```

Compares two trajectories in absolute terms, returning the deviations between them. 



**Args:**
 
 - <b>`traj_test`</b> (Trajectory):  The trajectory to be tested. 
 - <b>`traj_ref`</b> (Trajectory):  The reference trajectory. 



**Returns:**
 
 - <b>`ATEResult`</b>:  An object containing the absolute deviations between the two trajectories. 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L94"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `compare_trajectories_relative`

```python
compare_trajectories_relative(
    traj_test: Trajectory,
    traj_ref: Trajectory,
    settings: RelativeComparisonSettings = RelativeComparisonSettings(pair_min_distance=100.0, pair_max_distance=800.0, pair_distance_step=100.0, pair_distance_unit=<Unit.METER: 3>, use_all_pose_pairs=True)
) → RPEResult
```

This function compares two trajectories using the relative comparison method. 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L174"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `se3_inv`

```python
se3_inv(pose: ndarray) → ndarray
```

Invert SE3 pose 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L185"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rotation_error`

```python
rotation_error(pose_error: ndarray) → float
```

KITTI metric port 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L194"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `translation_error`

```python
translation_error(pose_error: ndarray) → float
```

KITTI metric port 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L202"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_directed_deviations`

```python
get_directed_deviations(
    xyz_ref: ndarray,
    xyz_test: ndarray,
    rot: Optional[RotationSet] = None
) → ndarray
```






---

<a href="..\trajectopy_core\evaluation\comparison.py#L211"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `derive_dev_directions_no_rot`

```python
derive_dev_directions_no_rot(xyz_ref: ndarray, xyz_test: ndarray) → ndarray
```

Function that computes along-track and cross-track deviations between two synchronized trajectories. 

By constructing a 3D line between the corresponding point in xyz_ref and its successor (predecessor for the last point) one can determine the cross- and along-track deviations for each point in xyz_test 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L240"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `derive_dev_directions_with_rot`

```python
derive_dev_directions_with_rot(
    xyz_ref: ndarray,
    xyz_test: ndarray,
    rot: RotationSet
) → ndarray
```

Function that computes the deviation between ref and single with respect to coordinate axes defined by rpy 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
