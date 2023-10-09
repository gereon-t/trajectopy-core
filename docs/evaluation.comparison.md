<!-- markdownlint-disable -->

<a href="..\trajectopy_core\evaluation\comparison.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `evaluation.comparison`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `compare_trajectories_absolute`

```python
compare_trajectories_absolute(
    traj_test: Trajectory,
    traj_ref: Trajectory
) → AbsoluteTrajectoryDeviations
```

Compares two trajectories in absolute terms, returning the deviations between them. 



**Args:**
 
 - <b>`traj_test`</b> (Trajectory):  The trajectory to be tested. 
 - <b>`traj_ref`</b> (Trajectory):  The reference trajectory. 



**Returns:**
 
 - <b>`AbsoluteTrajectoryDeviations`</b>:  An object containing the absolute deviations between the two trajectories. 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L63"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `compare_trajectories_relative`

```python
compare_trajectories_relative(
    traj_test: Trajectory,
    traj_ref: Trajectory,
    settings: RelativeComparisonSettings
) → RelativeTrajectoryDeviations
```

This function compares two trajectories using the relative comparison method. 





**Args:**
 
 - <b>`traj_test`</b> (Trajectory):  Test trajectory. 
 - <b>`traj_ref`</b> (Trajectory):  Reference trajectory. 
 - <b>`settings`</b> (ComparisonSettings):  Comparison settings. 



**Returns:**
 
 - <b>`RelativeTrajectoryDeviations`</b>:  Relative trajectory deviations. 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `pairwise_comparison`

```python
pairwise_comparison(
    traj_test: Trajectory,
    traj_ref: Trajectory,
    settings: RelativeComparisonSettings
) → RelativeTrajectoryDeviations
```

This function compares two trajectories using the relative comparison method. 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L198"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `se3_inv`

```python
se3_inv(pose: ndarray) → ndarray
```

Invert SE3 pose 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rotation_error`

```python
rotation_error(pose_error: ndarray) → float
```

KITTI metric port 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L218"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `translation_error`

```python
translation_error(pose_error: ndarray) → float
```

KITTI metric port 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L226"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_directed_deviations`

```python
get_directed_deviations(
    xyz_ref: ndarray,
    xyz_test: ndarray,
    rot: Optional[RotationSet] = None
) → ndarray
```






---

<a href="..\trajectopy_core\evaluation\comparison.py#L235"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `derive_dev_directions_no_rot`

```python
derive_dev_directions_no_rot(xyz_ref: ndarray, xyz_test: ndarray) → ndarray
```

Function that computes along-track and cross-track deviations between two synchronized trajectories. 

By constructing a 3D line between the corresponding point in xyz_ref and its successor (predecessor for the last point) one can determine the cross- and along-track deviations for each point in xyz_test 


---

<a href="..\trajectopy_core\evaluation\comparison.py#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
