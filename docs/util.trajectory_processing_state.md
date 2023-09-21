<!-- markdownlint-disable -->

<a href="../trajectopy_core/util/trajectory_processing_state.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `util.trajectory_processing_state`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="../trajectopy_core/util/trajectory_processing_state.py#L10"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TrajectoryProcessingState`
Class to store the processing state of a trajectory. For example, if a trajectory is interpolated, the attribute interpolated is set to True. 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    approximated: bool = False,
    interpolated: bool = False,
    intersected: bool = False,
    aligned: bool = False,
    matched: bool = False,
    sorting_known: bool = False
) → None
```








---

<a href="../trajectopy_core/util/trajectory_processing_state.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_string`

```python
from_string(input_string: str) → TrajectoryProcessingState
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
