<!-- markdownlint-disable -->

<a href="..\trajectopy_core\report\single.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `report.single`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **base_path**
- **TEMPLATES_PATH**

---

<a href="..\trajectopy_core\report\single.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `convert_images_to_base64`

```python
convert_images_to_base64() → Tuple[str, str, str]
```






---

<a href="..\trajectopy_core\report\single.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `render_side_by_side_plots`

```python
render_side_by_side_plots(report_data: ReportData) → List[str]
```






---

<a href="..\trajectopy_core\report\single.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `render_one_line_plots`

```python
render_one_line_plots(report_data: ReportData) → List[str]
```






---

<a href="..\trajectopy_core\report\single.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `render_single_report`

```python
render_single_report(
    ate_result: ATEResult,
    rpe_result: Optional[RPEResult] = None,
    report_settings: ReportSettings = ReportSettings(downsample_size=2000, scatter_max_std=4.0, ate_unit_is_mm=False, directed_ate=True, histogram_opacity=0.7, histogram_bargap=0.1, histogram_barmode='overlay', histogram_yaxis_title='Count', plot_mode='lines+markers', scatter_mode='markers', scatter_colorscale='RdYlBu_r', scatter_axis_order='xy', scatter_marker_size=5, pos_x_name='x', pos_y_name='y', pos_z_name='z', pos_x_unit='m', pos_y_unit='m', pos_z_unit='m', rot_x_name='roll', rot_y_name='pitch', rot_z_name='yaw', rot_unit='°', single_plot_export=ExportSettings(format='png', height=450, width=800, scale=6), two_subplots_export=ExportSettings(format='png', height=540, width=800, scale=6), three_subplots_export=ExportSettings(format='png', height=750, width=800, scale=6), single_plot_height=450, two_subplots_height=540, three_subplots_height=750)
) → str
```

Renders a html report string of a single trajectory comparison. 



**Args:**
 
 - <b>`ate_result`</b> (ATEResult):  The absolute trajectory error result 
 - <b>`rpe_result`</b> (Optional[RPEResult]):  The relative pose error result 
 - <b>`max_std`</b> (float):  The upper bound of scatter plot colorbars is set to max_std * std of the data 
 - <b>`report_settings`</b> (ReportSettings):  The report settings 



**Returns:**
 
 - <b>`str`</b>:  The html report string 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
