<!-- markdownlint-disable -->

<a href="..\trajectopy_core\pipelines.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `pipelines`
Trajectopy - Trajectory Evaluation in Python 

High-level API for trajectory evaluation in Python. 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\pipelines.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `ate`

```python
ate(
    trajectory_gt: Trajectory,
    trajectory_est: Trajectory,
    settings: ProcessingSettings = ProcessingSettings(alignment=AlignmentSettings(preprocessing=AlignmentPreprocessing(min_speed=0.0, time_start=0.0, time_end=0.0), estimation_of=AlignmentEstimationSettings(trans_x=True, trans_y=True, trans_z=True, rot_x=True, rot_y=True, rot_z=True, scale=False, time_shift=False, use_x_speed=True, use_y_speed=True, use_z_speed=True, lever_x=False, lever_y=False, lever_z=False, sensor_rotation=False, auto_update=False), stochastics=AlignmentStochastics(std_xy_from=1.0, std_z_from=1.0, std_xy_to=1.0, std_z_to=1.0, std_roll_pitch=0.017453292519943295, std_yaw=0.017453292519943295, std_speed=1.0, error_probability=0.05, variance_component_estimation=False, variance_component_estimation_subset_size=200), metric_threshold=0.0001, time_threshold=0.0001), matching=MatchingSettings(method=<MatchingMethod.INTERPOLATION: 3>, max_time_diff=0.01, max_distance=0.0, k_nearest=10), relative_comparison=RelativeComparisonSettings(pair_min_distance=100.0, pair_max_distance=800.0, pair_distance_step=100.0, pair_distance_unit=<Unit.METER: 3>, use_all_pose_pairs=True), report=ReportSettings(downsample_size=2000, scatter_max_std=4.0, ate_unit_is_mm=False, directed_ate=True, histogram_opacity=0.7, histogram_bargap=0.1, histogram_barmode='overlay', histogram_yaxis_title='Count', plot_mode='lines+markers', scatter_mode='markers', scatter_colorscale='RdYlBu_r', scatter_axis_order='xy', scatter_marker_size=5, pos_x_name='x', pos_y_name='y', pos_z_name='z', pos_x_unit='m', pos_y_unit='m', pos_z_unit='m', rot_x_name='roll', rot_y_name='pitch', rot_z_name='yaw', rot_unit='°', single_plot_export=ExportSettings(format='png', height=450, width=800, scale=6), two_subplots_export=ExportSettings(format='png', height=540, width=800, scale=6), three_subplots_export=ExportSettings(format='png', height=750, width=800, scale=6), single_plot_height=450, two_subplots_height=540, three_subplots_height=750))
) → ATEResult
```

Computes the absolute trajectory error (ATE) between two trajectories. 



**Args:**
 
 - <b>`trajectory_gt`</b> (Trajectory):  Ground truth trajectory. 
 - <b>`trajectory_est`</b> (Trajectory):  Estimated trajectory. 
 - <b>`settings`</b> (ProcessingSettings, optional):  Processing settings. 



**Returns:**
 
 - <b>`ATEResult`</b>:  Result of the ATE computation. 


---

<a href="..\trajectopy_core\pipelines.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rpe`

```python
rpe(
    trajectory_gt: Trajectory,
    trajectory_est: Trajectory,
    settings: ProcessingSettings = ProcessingSettings(alignment=AlignmentSettings(preprocessing=AlignmentPreprocessing(min_speed=0.0, time_start=0.0, time_end=0.0), estimation_of=AlignmentEstimationSettings(trans_x=True, trans_y=True, trans_z=True, rot_x=True, rot_y=True, rot_z=True, scale=False, time_shift=False, use_x_speed=True, use_y_speed=True, use_z_speed=True, lever_x=False, lever_y=False, lever_z=False, sensor_rotation=False, auto_update=False), stochastics=AlignmentStochastics(std_xy_from=1.0, std_z_from=1.0, std_xy_to=1.0, std_z_to=1.0, std_roll_pitch=0.017453292519943295, std_yaw=0.017453292519943295, std_speed=1.0, error_probability=0.05, variance_component_estimation=False, variance_component_estimation_subset_size=200), metric_threshold=0.0001, time_threshold=0.0001), matching=MatchingSettings(method=<MatchingMethod.INTERPOLATION: 3>, max_time_diff=0.01, max_distance=0.0, k_nearest=10), relative_comparison=RelativeComparisonSettings(pair_min_distance=100.0, pair_max_distance=800.0, pair_distance_step=100.0, pair_distance_unit=<Unit.METER: 3>, use_all_pose_pairs=True), report=ReportSettings(downsample_size=2000, scatter_max_std=4.0, ate_unit_is_mm=False, directed_ate=True, histogram_opacity=0.7, histogram_bargap=0.1, histogram_barmode='overlay', histogram_yaxis_title='Count', plot_mode='lines+markers', scatter_mode='markers', scatter_colorscale='RdYlBu_r', scatter_axis_order='xy', scatter_marker_size=5, pos_x_name='x', pos_y_name='y', pos_z_name='z', pos_x_unit='m', pos_y_unit='m', pos_z_unit='m', rot_x_name='roll', rot_y_name='pitch', rot_z_name='yaw', rot_unit='°', single_plot_export=ExportSettings(format='png', height=450, width=800, scale=6), two_subplots_export=ExportSettings(format='png', height=540, width=800, scale=6), three_subplots_export=ExportSettings(format='png', height=750, width=800, scale=6), single_plot_height=450, two_subplots_height=540, three_subplots_height=750))
) → RPEResult
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
