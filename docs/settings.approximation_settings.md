<!-- markdownlint-disable -->

<a href="../trajectopy_core/settings/approximation_settings.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `settings.approximation_settings`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **ROT_APPROX**


---

<a href="../trajectopy_core/settings/approximation_settings.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ApproximationSettings`
Dataclass defining approximation configuration 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    fe_int_size: float = 0.15,
    fe_min_obs: int = 25,
    rot_approx_technique: RotApprox = <RotApprox.WINDOW: 0>,
    rot_approx_win_size: float = 0.15
) → None
```








---

<a href="../trajectopy_core/settings/approximation_settings.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_config_dict`

```python
from_config_dict(config_dict: Dict)
```





---

<a href="../trajectopy_core/settings/approximation_settings.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict() → Dict[str, Any]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
