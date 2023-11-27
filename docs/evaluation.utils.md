<!-- markdownlint-disable -->

<a href="..\trajectopy_core\evaluation\utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `evaluation.utils`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\evaluation\utils.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rms`

```python
rms(x: Union[ndarray, float]) → float
```

Calculates the root mean square of an array. 



**Args:**
 
 - <b>`x`</b> (np.ndarray):  The input array. 



**Returns:**
 
 - <b>`float`</b>:  The root mean square of the input array. 


---

<a href="..\trajectopy_core\evaluation\utils.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `nearest_point`

```python
nearest_point(p: ndarray, line_pts: list) → Tuple[ndarray, float]
```

Finds the nearest point on a 3D line to a given point. 



**Args:**
 
 - <b>`p`</b> (np.ndarray):  The point to find the nearest point to. 
 - <b>`line_pts`</b> (list):  A list of two points that define the 3D line. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  The nearest point on the 3D line to the given point. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
