<!-- markdownlint-disable -->

<a href="..\trajectopy_core\alignment\actions.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `alignment.actions`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\alignment\actions.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\alignment\actions.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\alignment\actions.py#L53"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\alignment\actions.py#L72"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `align_trajectories`

```python
align_trajectories(
    traj_from: Trajectory,
    traj_to: Trajectory,
    alignment_settings: AlignmentSettings,
    matching_settings: MatchingSettings
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
