<!-- markdownlint-disable -->

<a href="../trajectopy_core/alignment/parameters.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `alignment.parameters`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **UNIT_FORMAT_RULES**


---

<a href="../trajectopy_core/alignment/parameters.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AlignmentParametersError`








---

<a href="../trajectopy_core/alignment/parameters.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Parameter`
Class representing a Parameter 

A parameter holds a stochastic value with some variance. It can be enabled and disabled. 

If a parameter is disabled, its value value is equal to the default value. The default value of a parameter should be chosen in a way so that the parameter has no effect on computations. For example, a default scale value of 1 will not affect any computations this scale parameter is involved in. The same holds true for a rotation or translation of 0. The disabling of parameters is meant to be used to exclude parameter from being estimated during least-squares adjustment. 

<a href="../trajectopy_core/alignment/parameters.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    value: float,
    variance: float = 0.0,
    default: float = 0.0,
    enabled: bool = True,
    name: str = '',
    unit: Unit = <Unit.NONE: 6>
) → None
```






---

#### <kbd>property</kbd> value





---

#### <kbd>property</kbd> variance







---

<a href="../trajectopy_core/alignment/parameters.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable() → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L110"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `enable`

```python
enable() → None
```






---

<a href="../trajectopy_core/alignment/parameters.py#L117"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ParameterSet`
Abstract class representing a set of parameters 

This class groups related parameters. For example, 3 parameters for a 3d translation. 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(enabled: bool = True, covariance_matrix: ndarray = <factory>) → None
```






---

#### <kbd>property</kbd> any_enabled





---

#### <kbd>property</kbd> enabled_bool_list





---

#### <kbd>property</kbd> enabled_indices





---

#### <kbd>property</kbd> num_enabled





---

#### <kbd>property</kbd> values





---

#### <kbd>property</kbd> values_enabled





---

#### <kbd>property</kbd> variances





---

#### <kbd>property</kbd> variances_enabled







---

<a href="../trajectopy_core/alignment/parameters.py#L195"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable() → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L190"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `enable`

```python
enable() → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L156"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_covariance_matrix`

```python
get_covariance_matrix(enabled_only: bool = True) → ndarray
```





---

<a href="../trajectopy_core/alignment/parameters.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_covariance_matrix`

```python
set_covariance_matrix(cov_matrix: ndarray) → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict(enabled_only: bool = True) → Dict[str, List[float]]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L216"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_name_list`

```python
to_name_list(enabled_only: bool = True, lower_case: bool = True) → List[str]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_string_list`

```python
to_string_list(enabled_only: bool = True) → List[str]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L166"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `validate_covariance`

```python
validate_covariance()
```

Checks dimensions of covariance matrix and sets variances accordingly 


---

<a href="../trajectopy_core/alignment/parameters.py#L314"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `HelmertTransformation`
Parameter set for a similarity transformation 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    enabled: bool = True,
    covariance_matrix: ndarray = <factory>,
    trans_x: Parameter = <factory>,
    trans_y: Parameter = <factory>,
    trans_z: Parameter = <factory>,
    rot_x: Parameter = <factory>,
    rot_y: Parameter = <factory>,
    rot_z: Parameter = <factory>,
    scale: Parameter = <factory>
) → None
```






---

#### <kbd>property</kbd> any_enabled





---

#### <kbd>property</kbd> enabled_bool_list





---

#### <kbd>property</kbd> enabled_indices





---

#### <kbd>property</kbd> num_enabled





---

#### <kbd>property</kbd> rotation





---

#### <kbd>property</kbd> rotation_matrix





---

#### <kbd>property</kbd> rotation_set





---

#### <kbd>property</kbd> translation





---

#### <kbd>property</kbd> values





---

#### <kbd>property</kbd> values_enabled





---

#### <kbd>property</kbd> variances





---

#### <kbd>property</kbd> variances_enabled







---

<a href="../trajectopy_core/alignment/parameters.py#L354"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `apply_to`

```python
apply_to(xyz: ndarray) → ndarray
```





---

<a href="../trajectopy_core/alignment/parameters.py#L195"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable() → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L190"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `enable`

```python
enable() → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L156"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_covariance_matrix`

```python
get_covariance_matrix(enabled_only: bool = True) → ndarray
```





---

<a href="../trajectopy_core/alignment/parameters.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_covariance_matrix`

```python
set_covariance_matrix(cov_matrix: ndarray) → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict(enabled_only: bool = True) → Dict[str, List[float]]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L216"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_name_list`

```python
to_name_list(enabled_only: bool = True, lower_case: bool = True) → List[str]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_string_list`

```python
to_string_list(enabled_only: bool = True) → List[str]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L166"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `validate_covariance`

```python
validate_covariance()
```

Checks dimensions of covariance matrix and sets variances accordingly 


---

<a href="../trajectopy_core/alignment/parameters.py#L358"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Leverarm`
Parameter set for a leverarm 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    enabled: bool = True,
    covariance_matrix: ndarray = <factory>,
    x: Parameter = <factory>,
    y: Parameter = <factory>,
    z: Parameter = <factory>
) → None
```






---

#### <kbd>property</kbd> any_enabled





---

#### <kbd>property</kbd> enabled_bool_list





---

#### <kbd>property</kbd> enabled_indices





---

#### <kbd>property</kbd> num_enabled





---

#### <kbd>property</kbd> values





---

#### <kbd>property</kbd> values_enabled





---

#### <kbd>property</kbd> variances





---

#### <kbd>property</kbd> variances_enabled







---

<a href="../trajectopy_core/alignment/parameters.py#L372"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `apply_to`

```python
apply_to(xyz: ndarray, quat_body: ndarray) → ndarray
```

Applies the leverarm to a set of positions using orientations 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  Positions 
 - <b>`quat_body`</b> (np.ndarray):  Orientations 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Leverarm applied positions 

---

<a href="../trajectopy_core/alignment/parameters.py#L195"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable() → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L190"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `enable`

```python
enable() → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L156"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_covariance_matrix`

```python
get_covariance_matrix(enabled_only: bool = True) → ndarray
```





---

<a href="../trajectopy_core/alignment/parameters.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_covariance_matrix`

```python
set_covariance_matrix(cov_matrix: ndarray) → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict(enabled_only: bool = True) → Dict[str, List[float]]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L216"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_name_list`

```python
to_name_list(enabled_only: bool = True, lower_case: bool = True) → List[str]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_string_list`

```python
to_string_list(enabled_only: bool = True) → List[str]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L166"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `validate_covariance`

```python
validate_covariance()
```

Checks dimensions of covariance matrix and sets variances accordingly 


---

<a href="../trajectopy_core/alignment/parameters.py#L395"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AlignmentParameters`
Parameter set for spatio-temporal alignment 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    enabled: bool = True,
    covariance_matrix: ndarray = <factory>,
    sim_trans_x: Parameter = <factory>,
    sim_trans_y: Parameter = <factory>,
    sim_trans_z: Parameter = <factory>,
    sim_rot_x: Parameter = <factory>,
    sim_rot_y: Parameter = <factory>,
    sim_rot_z: Parameter = <factory>,
    sim_scale: Parameter = <factory>,
    time_shift: Parameter = <factory>,
    lever_x: Parameter = <factory>,
    lever_y: Parameter = <factory>,
    lever_z: Parameter = <factory>
) → None
```






---

#### <kbd>property</kbd> any_enabled





---

#### <kbd>property</kbd> enabled_bool_list





---

#### <kbd>property</kbd> enabled_indices





---

#### <kbd>property</kbd> helmert





---

#### <kbd>property</kbd> leverarm





---

#### <kbd>property</kbd> num_enabled





---

#### <kbd>property</kbd> sim3_matrix





---

#### <kbd>property</kbd> values





---

#### <kbd>property</kbd> values_enabled





---

#### <kbd>property</kbd> variances





---

#### <kbd>property</kbd> variances_enabled







---

<a href="../trajectopy_core/alignment/parameters.py#L469"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `apply_settings`

```python
apply_settings(settings: AlignmentEstimationSettings) → None
```

Applies the estimation settings to the parameters by enabling or disabling them 

---

<a href="../trajectopy_core/alignment/parameters.py#L195"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable() → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L190"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `enable`

```python
enable() → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L532"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str) → AlignmentParameters
```

Reads the alignment parameters from a file 



**Args:**
 
 - <b>`filename`</b> (str):  Path to the file 



**Returns:**
 
 - <b>`AlignmentParameters`</b>:  AlignmentParameters instance 

---

<a href="../trajectopy_core/alignment/parameters.py#L453"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_settings`

```python
from_settings(settings: AlignmentEstimationSettings) → AlignmentParameters
```





---

<a href="../trajectopy_core/alignment/parameters.py#L156"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_covariance_matrix`

```python
get_covariance_matrix(enabled_only: bool = True) → ndarray
```





---

<a href="../trajectopy_core/alignment/parameters.py#L439"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `params_labels`

```python
params_labels(enabled_only: bool = True, lower_case: bool = True) → List[str]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_covariance_matrix`

```python
set_covariance_matrix(cov_matrix: ndarray) → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L529"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dataframe`

```python
to_dataframe() → DataFrame
```





---

<a href="../trajectopy_core/alignment/parameters.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict(enabled_only: bool = True) → Dict[str, List[float]]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L501"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```

Writes the alignment parameters to a file 

All parameters are written to the file no matter if they are enabled or not. If they are not enabled, the default value is written. Enabled parameters are marked with a 1, disabled with a 0. The order of the parameters is: 


- Translation x 
- Translation y 
- Translation z 
- Rotation x 
- Rotation y 
- Rotation z 
- Scale 
- Time Shift 
- Leverarm x 
- Leverarm y 
- Leverarm z 

Besides the parameters, the covariance matrix is written to the file. The covariance matrix is written row by row next to the parameters. 



**Args:**
 
 - <b>`filename`</b> (str):  Path to the file 

---

<a href="../trajectopy_core/alignment/parameters.py#L216"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_name_list`

```python
to_name_list(enabled_only: bool = True, lower_case: bool = True) → List[str]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_string_list`

```python
to_string_list(enabled_only: bool = True) → List[str]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L166"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `validate_covariance`

```python
validate_covariance()
```

Checks dimensions of covariance matrix and sets variances accordingly 


---

<a href="../trajectopy_core/alignment/parameters.py#L550"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SensorRotationParameters`
Parameter set for sensor b-frame rotation 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    enabled: bool = True,
    covariance_matrix: ndarray = <factory>,
    sensor_rot_x: Parameter = <factory>,
    sensor_rot_y: Parameter = <factory>,
    sensor_rot_z: Parameter = <factory>
) → None
```






---

#### <kbd>property</kbd> any_enabled





---

#### <kbd>property</kbd> enabled_bool_list





---

#### <kbd>property</kbd> enabled_indices





---

#### <kbd>property</kbd> num_enabled





---

#### <kbd>property</kbd> rotation





---

#### <kbd>property</kbd> rotation_matrix





---

#### <kbd>property</kbd> rotation_set





---

#### <kbd>property</kbd> values





---

#### <kbd>property</kbd> values_enabled





---

#### <kbd>property</kbd> variances





---

#### <kbd>property</kbd> variances_enabled







---

<a href="../trajectopy_core/alignment/parameters.py#L195"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `disable`

```python
disable() → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L190"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `enable`

```python
enable() → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L596"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str) → SensorRotationParameters
```





---

<a href="../trajectopy_core/alignment/parameters.py#L156"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_covariance_matrix`

```python
get_covariance_matrix(enabled_only: bool = True) → ndarray
```





---

<a href="../trajectopy_core/alignment/parameters.py#L162"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_covariance_matrix`

```python
set_covariance_matrix(cov_matrix: ndarray) → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L223"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict(enabled_only: bool = True) → Dict[str, List[float]]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L608"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```





---

<a href="../trajectopy_core/alignment/parameters.py#L216"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_name_list`

```python
to_name_list(enabled_only: bool = True, lower_case: bool = True) → List[str]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L213"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_string_list`

```python
to_string_list(enabled_only: bool = True) → List[str]
```





---

<a href="../trajectopy_core/alignment/parameters.py#L166"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `validate_covariance`

```python
validate_covariance()
```

Checks dimensions of covariance matrix and sets variances accordingly 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
