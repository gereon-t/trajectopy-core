<!-- markdownlint-disable -->

<a href="..\trajectopy_core\settings\processing_settings.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `settings.processing_settings`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\settings\processing_settings.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ProcessingSettings`
This class stores all processing settings 

It can be initialized by either providing separate configurationsets for 


- sorting 
- approximation 
- alignment 

or by using the 'from_file' method together with a yaml configuration file 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    sorting: SortingSettings = <factory>,
    approximation: ApproximationSettings = <factory>,
    alignment: AlignmentSettings = <factory>,
    rel_comparison: RelativeComparisonSettings = <factory>,
    matching: MatchingSettings = <factory>
) → None
```








---

<a href="..\trajectopy_core\settings\processing_settings.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_config_dict`

```python
from_config_dict(config_dict: Dict)
```





---

<a href="..\trajectopy_core\settings\processing_settings.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(file: str)
```





---

<a href="..\trajectopy_core\settings\processing_settings.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict() → Dict[str, Any]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
