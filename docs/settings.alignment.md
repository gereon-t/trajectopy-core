<!-- markdownlint-disable -->

<a href="..\trajectopy_core\settings\alignment.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `settings.alignment`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **METRIC_THRESHOLD**
- **TIME_THRESHOLD**


---

<a href="..\trajectopy_core\settings\alignment.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AlignmentPreprocessing`
Dataclass defining alignment preprocessing configuration 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    min_speed: float = 0.0,
    time_start: float = 0.0,
    time_end: float = 0.0
) → None
```









---

<a href="..\trajectopy_core\settings\alignment.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AlignmentEstimationSettings`
Dataclass defining which parameters to estimate during the alignment process 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    trans_x: bool = True,
    trans_y: bool = True,
    trans_z: bool = True,
    rot_x: bool = True,
    rot_y: bool = True,
    rot_z: bool = True,
    scale: bool = False,
    time_shift: bool = False,
    use_x_speed: bool = True,
    use_y_speed: bool = True,
    use_z_speed: bool = True,
    lever_x: bool = False,
    lever_y: bool = False,
    lever_z: bool = False,
    sensor_rotation: bool = False,
    auto_update: bool = False
) → None
```






---

#### <kbd>property</kbd> all_disabled





---

#### <kbd>property</kbd> all_lq_disabled

Returns True if all parameters estimated with Least-Squares are disabled 

---

#### <kbd>property</kbd> enabled_lq_parameter_filter

Returns a list of bools indicating which parameters estimated within LQ are enabled 

---

#### <kbd>property</kbd> helmert_enabled





---

#### <kbd>property</kbd> helmert_filter





---

#### <kbd>property</kbd> leverarm_enabled





---

#### <kbd>property</kbd> leverarm_filter





---

#### <kbd>property</kbd> lq_parameter_filter





---

#### <kbd>property</kbd> short_mode_str

Returns a short string describing the enabled parameters 

---

#### <kbd>property</kbd> time_shift_enabled





---

#### <kbd>property</kbd> time_shift_filter







---

<a href="..\trajectopy_core\settings\alignment.py#L85"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `all`

```python
all(
    sensor_rotation: bool = True,
    auto_update: bool = False
) → AlignmentEstimationSettings
```





---

<a href="..\trajectopy_core\settings\alignment.py#L106"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_bool_list`

```python
from_bool_list(bool_list: List[bool]) → AlignmentEstimationSettings
```





---

<a href="..\trajectopy_core\settings\alignment.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_components`

```python
from_components(
    similarity: bool = False,
    time_shift: bool = False,
    leverarm: bool = False,
    sensor_rotation: bool = False,
    auto_update: bool = False
) → AlignmentEstimationSettings
```






---

<a href="..\trajectopy_core\settings\alignment.py#L217"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AlignmentStochastics`
Dataclass defining alignment stochastics configuration 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    std_xy_from: float = 1.0,
    std_z_from: float = 1.0,
    std_xy_to: float = 1.0,
    std_z_to: float = 1.0,
    std_roll_pitch: float = 0.017453292519943295,
    std_yaw: float = 0.017453292519943295,
    std_speed: float = 1.0,
    error_probability: float = 0.05,
    variance_component_estimation: bool = False,
    variance_component_estimation_subset_size: int = 200
) → None
```






---

#### <kbd>property</kbd> var_roll_pitch





---

#### <kbd>property</kbd> var_speed_to





---

#### <kbd>property</kbd> var_xy_from





---

#### <kbd>property</kbd> var_xy_to





---

#### <kbd>property</kbd> var_yaw





---

#### <kbd>property</kbd> var_z_from





---

#### <kbd>property</kbd> var_z_to








---

<a href="..\trajectopy_core\settings\alignment.py#L261"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AlignmentSettings`
Dataclass defining alignment configuration 



**Args:**
 


    - mode (str): Mode of the H(elmert)-L(everarm)-T(ime) transformation  Depending on the presence of the letters "h", "l", "t"  inside this string, the alignment will estimate the  corresponding parameters 
    - std_xx (float): Standard deviations in their corresponding unit  of the supported observation_groups: 
        - xy_from (source positions) 
        - z_from 
        - xy_to (target positions) 
        - z_to 
        - roll_pitch (platform orientations) 
        - yaw 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    preprocessing: AlignmentPreprocessing = <factory>,
    estimation_of: AlignmentEstimationSettings = <factory>,
    stochastics: AlignmentStochastics = <factory>,
    metric_threshold: float = 0.0001,
    time_threshold: float = 0.0001
) → None
```











---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
