<!-- markdownlint-disable -->

<a href="../trajectopy_core/util/rotationset.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `util.rotationset`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="../trajectopy_core/util/rotationset.py#L13"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `RotationSet`
Class representing rotations 

This class is essentially just a wrapper around the parent scipy.spatial.transform.Rotation class. It extends its functionality by introducing + / - operators as well as the ability to create a deepcopy and to output rotation angles. 

Furthermore, it ensures that the naming is consistent with the pointset class. 


---

#### <kbd>property</kbd> rotangle

Returns minimum rotation angle(s) 



---

<a href="../trajectopy_core/util/rotationset.py#L39"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `copy`

```python
copy() → RotationSet
```





---

<a href="../trajectopy_core/util/rotationset.py#L25"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_euler`

```python
from_euler(seq: str, angles: ndarray, degrees: bool = False) → RotationSet
```





---

<a href="../trajectopy_core/util/rotationset.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_quat`

```python
from_quat(quat: ndarray) → RotationSet
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
