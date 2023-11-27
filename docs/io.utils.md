<!-- markdownlint-disable -->

<a href="..\trajectopy_core\io\utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `io.utils`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\io\utils.py#L14"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_rot_matrix`

```python
get_rot_matrix(nframe: str) → ndarray
```

Returns rotation matrix to transform rotations to ENU 



**Args:**
 
 - <b>`nframe`</b> (str):  String defining the current nframe definition.  e.g. "ned". This string must contain "e", "n",  and either "d" OR "u" 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Rotation Matrix 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
