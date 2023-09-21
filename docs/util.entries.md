<!-- markdownlint-disable -->

<a href="../trajectopy_core/util/entries.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `util.entries`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="../trajectopy_core/util/entries.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `bool_to_str`

```python
bool_to_str(input_bool: bool) → str
```






---

<a href="../trajectopy_core/util/entries.py#L35"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `generate_id`

```python
generate_id() → str
```






---

<a href="../trajectopy_core/util/entries.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Entry`
Abstract base class for all entries in their respective model. 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__() → None
```






---

#### <kbd>property</kbd> property_dict





---

#### <kbd>property</kbd> type







---

<a href="../trajectopy_core/util/entries.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `renew_id`

```python
renew_id() → None
```





---

<a href="../trajectopy_core/util/entries.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_id`

```python
set_id(entry_id: str) → None
```





---

<a href="../trajectopy_core/util/entries.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```






---

<a href="../trajectopy_core/util/entries.py#L70"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `TrajectoryEntry`
Class representing a trajectory entry in the trajectory model. 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    full_filename: str,
    trajectory: Trajectory,
    set_as_reference: bool = False,
    settings: ProcessingSettings = <factory>,
    group_id: str = <factory>
) → None
```






---

#### <kbd>property</kbd> column





---

#### <kbd>property</kbd> filename





---

#### <kbd>property</kbd> has_orientations





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> property_dict

Shows a new window with trajectory properties 

---

#### <kbd>property</kbd> type







---

<a href="../trajectopy_core/util/entries.py#L84"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(trajectory_filename: Path, settings_filename: Path) → TrajectoryEntry
```

Creates a new TrajectoryEntry from a trajectory file and a settings file. 

---

<a href="../trajectopy_core/util/entries.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `renew_id`

```python
renew_id() → None
```





---

<a href="../trajectopy_core/util/entries.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_id`

```python
set_id(entry_id: str) → None
```





---

<a href="../trajectopy_core/util/entries.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```






---

<a href="../trajectopy_core/util/entries.py#L168"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `ResultEntry`
Abstract base class for result entries in the result model. 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__() → None
```






---

#### <kbd>property</kbd> column





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> property_dict





---

#### <kbd>property</kbd> type







---

<a href="../trajectopy_core/util/entries.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `renew_id`

```python
renew_id() → None
```





---

<a href="../trajectopy_core/util/entries.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_id`

```python
set_id(entry_id: str) → None
```





---

<a href="../trajectopy_core/util/entries.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```






---

<a href="../trajectopy_core/util/entries.py#L187"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `DeviationsEntry`
Abstract base class for deviation entries in the result model. 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    deviations: Union[AbsoluteTrajectoryDeviations, RelativeTrajectoryDeviations]
) → None
```






---

#### <kbd>property</kbd> column





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> property_dict





---

#### <kbd>property</kbd> type







---

<a href="../trajectopy_core/util/entries.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `renew_id`

```python
renew_id() → None
```





---

<a href="../trajectopy_core/util/entries.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_id`

```python
set_id(entry_id: str) → None
```





---

<a href="../trajectopy_core/util/entries.py#L64"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```






---

<a href="../trajectopy_core/util/entries.py#L206"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AbsoluteDeviationEntry`
Class representing a absolute deviation entry in the result model. 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(deviations: AbsoluteTrajectoryDeviations) → None
```






---

#### <kbd>property</kbd> column





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> property_dict





---

#### <kbd>property</kbd> type







---

<a href="../trajectopy_core/util/entries.py#L219"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str) → AbsoluteDeviationEntry
```





---

<a href="../trajectopy_core/util/entries.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `renew_id`

```python
renew_id() → None
```





---

<a href="../trajectopy_core/util/entries.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_id`

```python
set_id(entry_id: str) → None
```





---

<a href="../trajectopy_core/util/entries.py#L212"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```






---

<a href="../trajectopy_core/util/entries.py#L227"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RelativeDeviationEntry`
Class representing a relative deviation entry in the result model. 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(deviations: RelativeTrajectoryDeviations) → None
```






---

#### <kbd>property</kbd> column





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> property_dict





---

#### <kbd>property</kbd> type







---

<a href="../trajectopy_core/util/entries.py#L239"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str) → RelativeDeviationEntry
```





---

<a href="../trajectopy_core/util/entries.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `renew_id`

```python
renew_id() → None
```





---

<a href="../trajectopy_core/util/entries.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_id`

```python
set_id(entry_id: str) → None
```





---

<a href="../trajectopy_core/util/entries.py#L233"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```






---

<a href="../trajectopy_core/util/entries.py#L247"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `AlignmentEntry`
Entry storing alignment results. 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(alignment_result: AlignmentResult = <factory>) → None
```






---

#### <kbd>property</kbd> column





---

#### <kbd>property</kbd> estimated_parameters





---

#### <kbd>property</kbd> estimation_of





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> property_dict





---

#### <kbd>property</kbd> type







---

<a href="../trajectopy_core/util/entries.py#L305"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str) → AlignmentEntry
```

Creates a new AlignmentEntry from a file. 

---

<a href="../trajectopy_core/util/entries.py#L49"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `renew_id`

```python
renew_id() → None
```





---

<a href="../trajectopy_core/util/entries.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `set_id`

```python
set_id(entry_id: str) → None
```





---

<a href="../trajectopy_core/util/entries.py#L291"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```






---

<a href="../trajectopy_core/util/entries.py#L325"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `PropertyEntry`
PropertyEntry(name: str, values: Tuple[str, ...]) 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(name: str, values: Tuple[str, ]) → None
```






---

#### <kbd>property</kbd> column










---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
