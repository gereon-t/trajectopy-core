<!-- markdownlint-disable -->

<a href="..\trajectopy_core\settings\plot_settings.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `settings.plot_settings`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\settings\plot_settings.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PlotSettings`
Dataclass defining plot configuration 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    rms_window_width: float = 1.0,
    grid_mp: float = 4.0,
    always_show_zero: bool = True,
    c_bar_step_divisor: int = 4,
    scatter_no_axis: bool = True,
    scatter_sigma_factor: float = 3.0,
    scatter_rotate: bool = False,
    unit_is_mm: bool = False,
    hist_as_stairs: bool = False,
    smoothing_window_size: float = 1.0,
    show_mean_line: bool = True,
    heatmap_spacing: float = 1.0,
    show_directed_devs: bool = True
) → None
```






---

#### <kbd>property</kbd> unit_multiplier





---

#### <kbd>property</kbd> unit_str







---

<a href="..\trajectopy_core\settings\plot_settings.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_config_dict`

```python
from_config_dict(config_dict: dict)
```





---

<a href="..\trajectopy_core\settings\plot_settings.py#L55"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(file: str)
```





---

<a href="..\trajectopy_core\settings\plot_settings.py#L59"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reset`

```python
reset()
```





---

<a href="..\trajectopy_core\settings\plot_settings.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
