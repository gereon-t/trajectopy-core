<!-- markdownlint-disable -->

<a href="..\trajectopy_core\settings\comparison.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `settings.comparison`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\settings\comparison.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `comparison_method_from_string`

```python
comparison_method_from_string(string: str) → <enum 'ComparisonMethod'>
```






---

<a href="..\trajectopy_core\settings\comparison.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ComparisonMethod`








---

<a href="..\trajectopy_core\settings\comparison.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RelativeComparisonSettings`
A class representing the settings for relative trajectory comparison. 



**Attributes:**
 
 - <b>`relative_pair_min_distance`</b> (float):  The minimum distance between two poses in a relative pair. 
 - <b>`relative_pair_max_distance`</b> (float):  The maximum distance between two poses in a relative pair. 
 - <b>`relative_pair_distance_step`</b> (float):  The step size for the distance between two poses in a relative pair. 
 - <b>`relative_pair_distance_unit`</b> (Unit):  The unit of measurement for the distance between two poses in a relative pair. 
 - <b>`use_all_pose_pairs`</b> (bool):  Whether to use all possible pose pairs for relative comparison. 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    pair_min_distance: float = 100.0,
    pair_max_distance: float = 800.0,
    pair_distance_step: float = 100.0,
    pair_distance_unit: Unit = <Unit.METER: 3>,
    use_all_pose_pairs: bool = True
) → None
```








---

<a href="..\trajectopy_core\settings\comparison.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `decoder`

```python
decoder(name: str, value: Any) → Any
```





---

<a href="..\trajectopy_core\settings\comparison.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `encoder`

```python
encoder(name: str, value: Any) → Any
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
