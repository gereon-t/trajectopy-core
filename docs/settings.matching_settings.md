<!-- markdownlint-disable -->

<a href="..\trajectopy_core\settings\matching_settings.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `settings.matching_settings`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\settings\matching_settings.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `matching_method_from_string`

```python
matching_method_from_string(string: str) → <enum 'MatchingMethod'>
```






---

<a href="..\trajectopy_core\settings\matching_settings.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `matching_settings_from_dict`

```python
matching_settings_from_dict(config_dict: Dict)
```






---

<a href="..\trajectopy_core\settings\matching_settings.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MatchingMethod`








---

<a href="..\trajectopy_core\settings\matching_settings.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `MatchingSettings`
Dataclass defining matching configuration 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    method: MatchingMethod = <MatchingMethod.INTERPOLATION: 3>,
    max_time_diff: float = 0.01,
    max_distance: float = 0.01
) → None
```








---

<a href="..\trajectopy_core\settings\matching_settings.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_config_dict`

```python
from_config_dict(config_dict: Dict)
```





---

<a href="..\trajectopy_core\settings\matching_settings.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict() → Dict[str, Any]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
