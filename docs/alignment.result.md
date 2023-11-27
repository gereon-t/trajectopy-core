<!-- markdownlint-disable -->

<a href="..\trajectopy_core\alignment\result.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `alignment.result`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\alignment\result.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AlignmentResult`
AlignmentResult(name: str = 'Alignment Result', position_parameters: trajectopy_core.alignment.parameters.AlignmentParameters = <factory>, rotation_parameters: trajectopy_core.alignment.parameters.SensorRotationParameters = <factory>, estimation_of: trajectopy_core.settings.alignment.AlignmentEstimationSettings = <factory>, converged: bool = True) 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    name: str = 'Alignment Result',
    position_parameters: AlignmentParameters = <factory>,
    rotation_parameters: SensorRotationParameters = <factory>,
    estimation_of: AlignmentEstimationSettings = <factory>,
    converged: bool = True
) → None
```








---

<a href="..\trajectopy_core\alignment\result.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str) → AlignmentResult
```

Load the result from a file. 



**Args:**
 
 - <b>`filename`</b> (str):  Path to the file. 



**Returns:**
 
 - <b>`AlignmentResult`</b>:  The loaded result. 

---

<a href="..\trajectopy_core\alignment\result.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```

Save the result to a file. 



**Args:**
 
 - <b>`filename`</b> (str):  Path to the file. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
