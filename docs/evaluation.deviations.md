<!-- markdownlint-disable -->

<a href="..\trajectopy_core\evaluation\deviations.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `evaluation.deviations`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\evaluation\deviations.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RelativeTrajectoryDeviations`
RelativeTrajectoryDeviations(pos_dev: Dict[float, List[float]], rot_dev: Dict[float, List[float]], pair_distance: Dict[float, List[float]], pair_distance_unit: trajectopy_core.definitions.Unit = <Unit.METER: 3>) 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    pos_dev: Dict[float, List[float]],
    rot_dev: Dict[float, List[float]],
    pair_distance: Dict[float, List[float]],
    pair_distance_unit: Unit = <Unit.METER: 3>
) → None
```






---

#### <kbd>property</kbd> num_pairs








---

<a href="..\trajectopy_core\evaluation\deviations.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AbsoluteTrajectoryDeviations`
AbsoluteTrajectoryDeviations(pos_dev: numpy.ndarray, directed_pos_dev: numpy.ndarray, rot_dev: Optional[trajectopy_core.rotationset.RotationSet] = None, rotations_used: bool = False) 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    pos_dev: ndarray,
    directed_pos_dev: ndarray,
    rot_dev: Optional[RotationSet] = None,
    rotations_used: bool = False
) → None
```











---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
