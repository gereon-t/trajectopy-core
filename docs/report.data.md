<!-- markdownlint-disable -->

<a href="..\trajectopy_core\report\data.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `report.data`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\report\data.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ReportData`
Class to store all data needed to render the report. 



**Args:**
 
 - <b>`ate_result`</b>:  The ATE result to be rendered. 
 - <b>`rpe_result`</b>:  The RPE result to be rendered. 
 - <b>`settings`</b>:  The report settings. 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    ate_result: ATEResult,
    rpe_result: Optional[RPEResult] = None,
    settings: ReportSettings = <factory>
) → None
```






---

#### <kbd>property</kbd> ate_unit





---

#### <kbd>property</kbd> function_of_label





---

#### <kbd>property</kbd> has_ate_rot





---

#### <kbd>property</kbd> has_rpe





---

#### <kbd>property</kbd> pos_dev_x_name





---

#### <kbd>property</kbd> pos_dev_y_name





---

#### <kbd>property</kbd> pos_dev_z_name





---

#### <kbd>property</kbd> short_name








---

<a href="..\trajectopy_core\report\data.py#L167"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ReportDataCollection`
Class to store multiple ReportData objects in a list 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(items: List[ReportData]) → None
```






---

#### <kbd>property</kbd> has_ate_rot





---

#### <kbd>property</kbd> has_rpe





---

#### <kbd>property</kbd> has_rpe_rot







---

<a href="..\trajectopy_core\report\data.py#L191"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_ate_results`

```python
get_ate_results(rot_required: bool = False) → list[ATEResult]
```





---

<a href="..\trajectopy_core\report\data.py#L194"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `get_rpe_results`

```python
get_rpe_results(rot_required: bool = False) → list[RPEResult]
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
