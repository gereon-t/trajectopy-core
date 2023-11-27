<!-- markdownlint-disable -->

<a href="..\trajectopy_core\alignment\ghm\data.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `alignment.ghm.data`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **POSITION_VARIANCE_GROUPS**
- **ORIENTATION_VARIANCE_GROUPS**
- **SPEED_VARIANCE_GROUP**


---

<a href="..\trajectopy_core\alignment\ghm\data.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AlignmentData`
Class holding the observation data required for Alignment 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    traj_from: Trajectory,
    traj_to: Trajectory,
    alignment_settings: AlignmentSettings,
    matching_settings: MatchingSettings
) → None
```






---

#### <kbd>property</kbd> est_euler_x





---

#### <kbd>property</kbd> est_euler_y





---

#### <kbd>property</kbd> est_euler_z





---

#### <kbd>property</kbd> est_obs_vector





---

#### <kbd>property</kbd> est_rpy_from





---

#### <kbd>property</kbd> est_speed





---

#### <kbd>property</kbd> est_speed_x





---

#### <kbd>property</kbd> est_speed_y





---

#### <kbd>property</kbd> est_speed_z





---

#### <kbd>property</kbd> est_x_from





---

#### <kbd>property</kbd> est_x_to





---

#### <kbd>property</kbd> est_xyz_from





---

#### <kbd>property</kbd> est_xyz_to





---

#### <kbd>property</kbd> est_y_from





---

#### <kbd>property</kbd> est_y_to





---

#### <kbd>property</kbd> est_z_from





---

#### <kbd>property</kbd> est_z_to





---

#### <kbd>property</kbd> euler_x





---

#### <kbd>property</kbd> euler_y





---

#### <kbd>property</kbd> euler_z





---

#### <kbd>property</kbd> group_stds

Returns the mean standard deviation for each group 

---

#### <kbd>property</kbd> num_obs_per_epoch

Returns the number of observations per epoch depending on the enabled estimation modes. 

---

#### <kbd>property</kbd> number_of_epochs





---

#### <kbd>property</kbd> obs_vector





---

#### <kbd>property</kbd> res_vector





---

#### <kbd>property</kbd> rpy_from





---

#### <kbd>property</kbd> sigma_ll





---

#### <kbd>property</kbd> speed





---

#### <kbd>property</kbd> speed_x





---

#### <kbd>property</kbd> speed_y





---

#### <kbd>property</kbd> speed_z





---

#### <kbd>property</kbd> tstamps





---

#### <kbd>property</kbd> var_vector





---

#### <kbd>property</kbd> x_from





---

#### <kbd>property</kbd> x_to





---

#### <kbd>property</kbd> xyz_from





---

#### <kbd>property</kbd> xyz_to





---

#### <kbd>property</kbd> y_from





---

#### <kbd>property</kbd> y_to





---

#### <kbd>property</kbd> z_from





---

#### <kbd>property</kbd> z_to







---

<a href="..\trajectopy_core\alignment\ghm\data.py#L212"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `build_obs_vector`

```python
build_obs_vector(
    xyz_from: ndarray,
    xyz_to: ndarray,
    rot_from: Optional[RotationSet],
    speed: Optional[ndarray]
) → ndarray
```

Creates the observation vector required for the alignment adjustment. 



**Args:**
 
 - <b>`xyz_from`</b> (np.ndarray):  Positions to be aligned. 
 - <b>`xyz_to`</b> (np.ndarray):  Target Positions. 
 - <b>`rpy_from`</b> (np.ndarray):  The roll, pitch, and yaw angles of the platform.  Those angles should describe the rotation of the  body-fixed coordinate system with respect to the  inertial coordinate system. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  The observation vector required for the alignment adjustment. 

---

<a href="..\trajectopy_core\alignment\ghm\data.py#L294"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `build_res_vector`

```python
build_res_vector() → ndarray
```





---

<a href="..\trajectopy_core\alignment\ghm\data.py#L256"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `build_var_vector`

```python
build_var_vector() → ndarray
```

Sets up the variance vector 

Its size depends on whether the leverarm should be estimated or not. In this case, not only the source and the target positions are relevant but also the platform orientations. Also, when estimating the time shift, the platform speed is also considered. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  variance vector 

---

<a href="..\trajectopy_core\alignment\ghm\data.py#L300"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_est_obs_group`

```python
get_est_obs_group(key: str) → Tuple[ndarray, ]
```





---

<a href="..\trajectopy_core\alignment\ghm\data.py#L297"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_obs_group`

```python
get_obs_group(key: str) → Tuple[ndarray, ]
```





---

<a href="..\trajectopy_core\alignment\ghm\data.py#L312"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_res_group`

```python
get_res_group(key: str) → Tuple[ndarray, ]
```





---

<a href="..\trajectopy_core\alignment\ghm\data.py#L306"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_var_group`

```python
get_var_group(key: str) → Tuple[ndarray, ]
```





---

<a href="..\trajectopy_core\alignment\ghm\data.py#L508"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_variance_estimation_subset`

```python
get_variance_estimation_subset(num_obs: int = 200) → AlignmentData
```





---

<a href="..\trajectopy_core\alignment\ghm\data.py#L303"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_obs_group`

```python
set_obs_group(key: str, values: ndarray) → None
```





---

<a href="..\trajectopy_core\alignment\ghm\data.py#L315"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_res_group`

```python
set_res_group(key: str, values: ndarray) → None
```





---

<a href="..\trajectopy_core\alignment\ghm\data.py#L309"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_var_group`

```python
set_var_group(key: str, values: ndarray) → None
```





---

<a href="..\trajectopy_core\alignment\ghm\data.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `setup`

```python
setup() → None
```

Prepare two trajectories for alignment. 

This method will filter the trajectories by speed and resample both trajectories to the same sampling. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
