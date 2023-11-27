<!-- markdownlint-disable -->

<a href="..\trajectopy_core\alignment\actions.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `alignment.actions`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\alignment\actions.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `apply_alignment`

```python
apply_alignment(
    trajectory: Trajectory,
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

<a href="..\trajectopy_core\alignment\actions.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `adopt_first_pose`

```python
adopt_first_pose(traj_from: Trajectory, traj_to: Trajectory) → Trajectory
```

Transform trajectory so that the first pose is identical in both 



**Args:**
 
 - <b>`traj_from`</b> (Trajectory):  Trajectory to be transformed 
 - <b>`traj_to`</b> (Trajectory):  Target Trajectory 



**Returns:**
 
 - <b>`Trajectory`</b>:  Transformed trajectory 


---

<a href="..\trajectopy_core\alignment\actions.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `adopt_first_position`

```python
adopt_first_position(traj_from: Trajectory, traj_to: Trajectory) → Trajectory
```

Transform trajectory so that the first position is identical in both 



**Args:**
 
 - <b>`traj_from`</b> (Trajectory):  Trajectory to be transformed 
 - <b>`traj_to`</b> (Trajectory):  Target Trajectory 



**Returns:**
 
 - <b>`Trajectory`</b>:  Transformed trajectory 


---

<a href="..\trajectopy_core\alignment\actions.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `adopt_first_orientation`

```python
adopt_first_orientation(traj_from: Trajectory, traj_to: Trajectory) → Trajectory
```

Transform trajectory so that the first orientation is identical in both 



**Args:**
 
 - <b>`traj_from`</b> (Trajectory):  Trajectory to be transformed 
 - <b>`traj_to`</b> (Trajectory):  Target Trajectory 



**Returns:**
 
 - <b>`Trajectory`</b>:  Transformed trajectory 


---

<a href="..\trajectopy_core\alignment\actions.py#L152"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `align_trajectories`

```python
align_trajectories(
    traj_from: Trajectory,
    traj_to: Trajectory,
    alignment_settings: AlignmentSettings = AlignmentSettings(preprocessing=AlignmentPreprocessing(min_speed=0.0, time_start=0.0, time_end=0.0), estimation_of=AlignmentEstimationSettings(trans_x=True, trans_y=True, trans_z=True, rot_x=True, rot_y=True, rot_z=True, scale=False, time_shift=False, use_x_speed=True, use_y_speed=True, use_z_speed=True, lever_x=False, lever_y=False, lever_z=False, sensor_rotation=False, auto_update=False), stochastics=AlignmentStochastics(std_xy_from=1.0, std_z_from=1.0, std_xy_to=1.0, std_z_to=1.0, std_roll_pitch=0.017453292519943295, std_yaw=0.017453292519943295, std_speed=1.0, error_probability=0.05, variance_component_estimation=False, variance_component_estimation_subset_size=200), metric_threshold=0.0001, time_threshold=0.0001),
    matching_settings: MatchingSettings = MatchingSettings(method=<MatchingMethod.INTERPOLATION: 3>, max_time_diff=0.01, max_distance=0.0, k_nearest=10)
) → AlignmentResult
```

Aligns two trajectories 

Performs a 
- Helmert 
- Leverarm 
- Time shift 

estimation depending on the configuration. After this, the estimated parameters are applied to the 'traj_from' trajectory. 



**Args:**
  traj_from (Trajectory)  traj_to (Trajectory) 
 - <b>`alignment_config`</b> (AlignmentConfig):  Configuration holding all  relevant settings for aligning  the trajectories. 



**Returns:**
 
 - <b>`Tuple[Trajectory, Trajectory]`</b>:  Aligned trajectories 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
