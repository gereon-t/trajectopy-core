<!-- markdownlint-disable -->

<a href="..\trajectopy_core\plotting\util.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `plotting.util`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\plotting\util.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `vertical_subplots`

```python
vertical_subplots(
    x_list: list,
    y_list: list,
    xlabel: str,
    ylabels: list,
    sharex: bool = True,
    sharey: bool = False,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
)
```

Creates a vertical array of subplots containing data provided in vals 


---

<a href="..\trajectopy_core\plotting\util.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `scatter_plotter`

```python
scatter_plotter(
    xyz: list,
    data: list,
    titles: list,
    c_labels: list,
    nrows: int = 0,
    ncols: int = 0,
    separate: bool = False,
    xlabels: Optional[list] = None,
    ylabels: Optional[list] = None,
    figure: bool = True,
    plot_settings: PlotSettings = PlotSettings(rms_window_width=1.0, grid_mp=4.0, always_show_zero=True, c_bar_step_divisor=4, scatter_no_axis=True, scatter_sigma_factor=3.0, scatter_rotate=False, unit_is_mm=False, hist_as_stairs=False, smoothing_window_size=1.0, show_mean_line=True, heatmap_spacing=1.0, show_directed_devs=True)
)
```

Scatter plotter function that plots 2d data with data mapped onto it using colors 


---

<a href="..\trajectopy_core\plotting\util.py#L175"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `norm_hist`

```python
norm_hist(l, mm: bool = False, alpha: float = 0.5, norm: bool = True) → None
```

Plots a histogram 


---

<a href="..\trajectopy_core\plotting\util.py#L188"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `stair_hist`

```python
stair_hist(l, mm: bool = False, linewidth: float = 1.5) → None
```

Plots a stair histogram 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
