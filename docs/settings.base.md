<!-- markdownlint-disable -->

<a href="..\trajectopy_core\settings\base.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `settings.base`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\settings\base.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Settings`
Base Class for Settings 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__() → None
```








---

<a href="..\trajectopy_core\settings\base.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `decoder`

```python
decoder(name: str, value: Any) → Any
```

Decoder for json deserialization of dataclasses 

---

<a href="..\trajectopy_core\settings\base.py#L28"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `encoder`

```python
encoder(name: str, value: Any) → Any
```

Encoder for json serialization of dataclasses 

---

<a href="..\trajectopy_core\settings\base.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_dict`

```python
from_dict(dct: dict) → Settings
```





---

<a href="..\trajectopy_core\settings\base.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(path: str) → Settings
```





---

<a href="..\trajectopy_core\settings\base.py#L18"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict() → dict
```





---

<a href="..\trajectopy_core\settings\base.py#L41"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(path: str)
```





---

<a href="..\trajectopy_core\settings\base.py#L38"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_json`

```python
to_json()
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
