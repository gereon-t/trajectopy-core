<!-- markdownlint-disable -->

<a href="..\trajectopy_core\report\multi.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `report.multi`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **TEMPLATES_PATH**

---

<a href="..\trajectopy_core\report\multi.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `render_one_line_plots`

```python
render_one_line_plots(report_data_collection: ReportDataCollection) → List[str]
```






---

<a href="..\trajectopy_core\report\multi.py#L43"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `render_multi_report`

```python
render_multi_report(
    ate_results: List[ATEResult],
    rpe_results: Optional[List[RPEResult]] = None,
    report_settings: ReportSettings = ReportSettings(downsample_size=2000, scatter_max_std=4.0, ate_unit_is_mm=False, directed_ate=True, histogram_opacity=0.7, histogram_bargap=0.1, histogram_barmode='overlay', histogram_yaxis_title='Count', plot_mode='lines+markers', scatter_mode='markers', scatter_colorscale='RdYlBu_r', scatter_axis_order='xy', scatter_marker_size=5, pos_x_name='x', pos_y_name='y', pos_z_name='z', pos_x_unit='m', pos_y_unit='m', pos_z_unit='m', rot_x_name='roll', rot_y_name='pitch', rot_z_name='yaw', rot_unit='°', single_plot_export=ExportSettings(format='png', height=450, width=800, scale=6), two_subplots_export=ExportSettings(format='png', height=540, width=800, scale=6), three_subplots_export=ExportSettings(format='png', height=750, width=800, scale=6), single_plot_height=450, two_subplots_height=540, three_subplots_height=750)
) → str
```

Renders a html report string of multiple trajectory comparisons 



**Args:**
 
 - <b>`ate_results`</b> (list[ATEResult]):  A list of absolute trajectory error results 
 - <b>`rpe_results`</b> (Optional[list[RPEResult]]):  A list of relative pose error results 
 - <b>`report_settings`</b> (ReportSettings):  The report settings 



**Returns:**
 
 - <b>`str`</b>:  The html report string 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
