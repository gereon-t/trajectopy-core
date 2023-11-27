<!-- markdownlint-disable -->

<a href="..\trajectopy_core\settings\report.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `settings.report`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\settings\report.py#L11"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ExportSettings`
ExportSettings(format: str = 'png', height: int = 500, width: int = 800, scale: int = 6) 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    format: str = 'png',
    height: int = 500,
    width: int = 800,
    scale: int = 6
) → None
```








---

<a href="..\trajectopy_core\settings\report.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_config`

```python
to_config() → dict
```






---

<a href="..\trajectopy_core\settings\report.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ReportSettings`
ReportSettings(downsample_size: int = 2000, scatter_max_std: float = 4.0, ate_unit_is_mm: bool = False, directed_ate: bool = True, histogram_opacity: float = 0.7, histogram_bargap: float = 0.1, histogram_barmode: str = 'overlay', histogram_yaxis_title: str = 'Count', plot_mode: str = 'lines+markers', scatter_mode: str = 'markers', scatter_colorscale: str = 'RdYlBu_r', scatter_axis_order: str = 'xy', scatter_marker_size: int = 5, pos_x_name: str = 'x', pos_y_name: str = 'y', pos_z_name: str = 'z', pos_x_unit: str = 'm', pos_y_unit: str = 'm', pos_z_unit: str = 'm', rot_x_name: str = 'roll', rot_y_name: str = 'pitch', rot_z_name: str = 'yaw', rot_unit: str = '°', single_plot_export: settings.report.ExportSettings = <factory>, two_subplots_export: settings.report.ExportSettings = <factory>, three_subplots_export: settings.report.ExportSettings = <factory>, single_plot_height: int = 450, two_subplots_height: int = 540, three_subplots_height: int = 750) 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    downsample_size: int = 2000,
    scatter_max_std: float = 4.0,
    ate_unit_is_mm: bool = False,
    directed_ate: bool = True,
    histogram_opacity: float = 0.7,
    histogram_bargap: float = 0.1,
    histogram_barmode: str = 'overlay',
    histogram_yaxis_title: str = 'Count',
    plot_mode: str = 'lines+markers',
    scatter_mode: str = 'markers',
    scatter_colorscale: str = 'RdYlBu_r',
    scatter_axis_order: str = 'xy',
    scatter_marker_size: int = 5,
    pos_x_name: str = 'x',
    pos_y_name: str = 'y',
    pos_z_name: str = 'z',
    pos_x_unit: str = 'm',
    pos_y_unit: str = 'm',
    pos_z_unit: str = 'm',
    rot_x_name: str = 'roll',
    rot_y_name: str = 'pitch',
    rot_z_name: str = 'yaw',
    rot_unit: str = '°',
    single_plot_export: ExportSettings = <factory>,
    two_subplots_export: ExportSettings = <factory>,
    three_subplots_export: ExportSettings = <factory>,
    single_plot_height: int = 450,
    two_subplots_height: int = 540,
    three_subplots_height: int = 750
) → None
```











---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
