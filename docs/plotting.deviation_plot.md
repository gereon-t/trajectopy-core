<!-- markdownlint-disable -->

<a href="..\trajectopy_core\plotting\deviation_plot.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `plotting.deviation_plot`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **XLABEL_DICT**
- **UNIT_DICT**

---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_combined_devs`

```python
plot_combined_devs(
    devs: AbsoluteTrajectoryDeviations,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Figure
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_raw_rotation_devs`

```python
plot_raw_rotation_devs(
    devs: AbsoluteTrajectoryDeviations,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Figure
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_raw_position_devs`

```python
plot_raw_position_devs(
    devs: AbsoluteTrajectoryDeviations,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Figure
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_dof_dev`

```python
plot_dof_dev(
    devs: AbsoluteTrajectoryDeviations,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Figure
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L129"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_position_dof`

```python
plot_position_dof(
    devs: AbsoluteTrajectoryDeviations,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
)
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L175"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_rot_dof`

```python
plot_rot_dof(
    devs: AbsoluteTrajectoryDeviations,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → None
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_compact_deviations`

```python
plot_compact_deviations(
    devs: AbsoluteTrajectoryDeviations,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Optional[Figure]
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L254"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_compact_hist`

```python
plot_compact_hist(
    devs: AbsoluteTrajectoryDeviations,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Figure
```

Plot compact histograms of cross-track and rpy deviations 


---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L271"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_rotation_hist`

```python
plot_rotation_hist(
    devs: AbsoluteTrajectoryDeviations,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → None
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L289"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_position_hist`

```python
plot_position_hist(
    devs: AbsoluteTrajectoryDeviations,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
)
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L315"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_edf`

```python
plot_edf(
    deviation: Union[AbsoluteTrajectoryDeviations, List[AbsoluteTrajectoryDeviations]],
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Figure
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L329"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_position_edf`

```python
plot_position_edf(
    deviation_list: List[AbsoluteTrajectoryDeviations],
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → None
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L343"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_rotation_edf`

```python
plot_rotation_edf(deviation_list: List[AbsoluteTrajectoryDeviations]) → None
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L360"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_bars`

```python
plot_bars(
    deviation_list: List[AbsoluteTrajectoryDeviations],
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True),
    mode: str = 'positions'
) → Figure
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L410"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_rms_heatmap`

```python
plot_rms_heatmap(
    deviation_collection: DeviationCollection,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Tuple[Figure, Optional[Figure]]
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L420"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_rotation_rms_heatmap`

```python
plot_rotation_rms_heatmap(
    deviation_collection: DeviationCollection
) → Optional[Figure]
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L439"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_position_rms_heatmap`

```python
plot_position_rms_heatmap(
    deviation_collection: DeviationCollection,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Figure
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L463"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_bias_heatmap`

```python
plot_bias_heatmap(
    deviation_collection: DeviationCollection,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Tuple[Figure, Optional[Figure]]
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L474"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_rotation_bias_heatmap`

```python
plot_rotation_bias_heatmap(
    deviation_collection: DeviationCollection
) → Optional[Figure]
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L495"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_position_bias_heatmap`

```python
plot_position_bias_heatmap(
    deviation_collection: DeviationCollection,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Figure
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L520"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `derive_xlabel_from_sortings`

```python
derive_xlabel_from_sortings(sorting_list: List[Sorting]) → str
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L531"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_multiple_comb_deviations`

```python
plot_multiple_comb_deviations(
    deviation: Union[AbsoluteTrajectoryDeviations, List[AbsoluteTrajectoryDeviations]],
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Figure
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L583"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_multiple_deviations`

```python
plot_multiple_deviations(
    deviation_collection: DeviationCollection,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
) → Tuple[Figure, Optional[Figure]]
```






---

<a href="..\trajectopy_core\plotting\deviation_plot.py#L635"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_rpe`

```python
plot_rpe(devs: List[RelativeTrajectoryDeviations]) → Tuple[Figure, Figure]
```

Plots metric and time RPE for each Deviation given in devs 



**Args:**
 
 - <b>`devs`</b> (list[RelativeTrajectoryDeviations]):  list of RelativeTrajectoryDeviations 



**Returns:**
 
 - <b>`Tuple[Figure, Figure]`</b>:  metric and time RPE plots 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
