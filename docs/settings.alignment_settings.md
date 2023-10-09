<!-- markdownlint-disable -->

<a href="..\trajectopy_core\settings\alignment_settings.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `settings.alignment_settings`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **METRIC_THRESHOLD**
- **TIME_THRESHOLD**


---

<a href="..\trajectopy_core\settings\alignment_settings.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\settings\alignment_settings.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_config_dict`

```python
from_config_dict(config_dict: Dict)
```





---

<a href="..\trajectopy_core\settings\alignment_settings.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict() → Dict[str, Any]
```






---

<a href="..\trajectopy_core\settings\alignment_settings.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AlignmentEstimationSettings`
Dataclass defining which parameters to estimate during the alignment process 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    helmert: bool = True,
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
    leverarm: bool = False,
    lever_x: bool = True,
    lever_y: bool = True,
    lever_z: bool = True,
    sensor_rotation: bool = False
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

<a href="..\trajectopy_core\settings\alignment_settings.py#L87"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_bool_list`

```python
from_bool_list(bool_list: List[bool]) → AlignmentEstimationSettings
```





---

<a href="..\trajectopy_core\settings\alignment_settings.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_config_dict`

```python
from_config_dict(config_dict: Dict)
```






---

<a href="..\trajectopy_core\settings\alignment_settings.py#L210"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AlignmentStochastics`
Dataclass defining alignment stochastics configuration 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    var_xy_from: float = 1.0,
    var_z_from: float = 1.0,
    var_xy_to: float = 1.0,
    var_z_to: float = 1.0,
    var_roll_pitch: float = 0.00030461741978670857,
    var_yaw: float = 0.00030461741978670857,
    var_speed_to: float = 1.0,
    error_probability: float = 0.05
) → None
```








---

<a href="..\trajectopy_core\settings\alignment_settings.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_config_dict`

```python
from_config_dict(config_dict: Dict)
```






---

<a href="..\trajectopy_core\settings\alignment_settings.py#L235"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\settings\alignment_settings.py#L272"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_config_dict`

```python
from_config_dict(config_dict: dict)
```





---

<a href="..\trajectopy_core\settings\alignment_settings.py#L265"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict() → Dict[str, Any]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
