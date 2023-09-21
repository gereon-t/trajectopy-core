<!-- markdownlint-disable -->

<a href="../trajectopy_core/plotting/trajectory_plot.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `plotting.trajectory_plot`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="../trajectopy_core/plotting/trajectory_plot.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_trajectories`

```python
plot_trajectories(
    trajectories: List[Trajectory],
    dim: int = 2
) → Tuple[Figure, Figure, Optional[Figure]]
```

Plots Trajectories 


---

<a href="../trajectopy_core/plotting/trajectory_plot.py#L27"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_pos`

```python
plot_pos(trajectories: List[Trajectory], dim: int = 2) → Figure
```

Plots xy(z) coordinates of trajectories as 2d or 3d plot 


---

<a href="../trajectopy_core/plotting/trajectory_plot.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_xyz`

```python
plot_xyz(trajectories: List[Trajectory]) → Figure
```

Plots xyz coordinates of trajectories as subplots 


---

<a href="../trajectopy_core/plotting/trajectory_plot.py#L83"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_axis_label`

```python
get_axis_label(trajectories: List[Trajectory]) → Tuple[str, str, str]
```

Returns the unit of the axis 


---

<a href="../trajectopy_core/plotting/trajectory_plot.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_rpy`

```python
plot_rpy(trajectories: List[Trajectory]) → Optional[Figure]
```

Plots rpy coordinates of trajectories as subplots 


---

<a href="../trajectopy_core/plotting/trajectory_plot.py#L138"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `set_aspect_equal_3d`

```python
set_aspect_equal_3d(ax)
```

https://stackoverflow.com/a/35126679 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
