<!-- markdownlint-disable -->

<a href="..\trajectopy_core\utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `utils`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\utils.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `lengths_from_xyz`

```python
lengths_from_xyz(xyz: ndarray) → ndarray
```

Computes the cumulative distance along a path defined by a sequence of 3D points. 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  An array of shape (n, 3) containing the x, y, and z  coordinates of the path. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  An array of shape (n,) containing the cumulative distance  along the path. 


---

<a href="..\trajectopy_core\utils.py#L99"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `gradient_3d`

```python
gradient_3d(xyz: ndarray, tstamps: ndarray) → ndarray
```

Computes the gradient of a 3D trajectory. 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  Positions of the trajectory [nx3]. 
 - <b>`tstamps`</b> (np.ndarray):  Timestamps of the trajectory [nx1]. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Gradient of the trajectory [nx3]. 


---

<a href="..\trajectopy_core\utils.py#L118"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `common_time_span`

```python
common_time_span(
    tstamps1: ndarray,
    tstamps2: ndarray
) → Optional[Tuple[float, float]]
```

Computes the common time span between two arrays of timestamps. 



**Args:**
 
 - <b>`tstamps1`</b> (np.ndarray):  First array of timestamps. 
 - <b>`tstamps2`</b> (np.ndarray):  Second array of timestamps. 



**Returns:**
 
 - <b>`Union[Tuple[float, float], None]`</b>:  A tuple containing the start and end times of the common time span, or None if there is no overlap between the two arrays. 


---

<a href="..\trajectopy_core\utils.py#L17"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Line3D`
A 3D line defined by a mean point and a direction vector. 



**Attributes:**
 
 - <b>`mean`</b> (np.ndarray):  The mean point of the line. 
 - <b>`direction`</b> (np.ndarray):  The direction vector of the line. 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(mean: ndarray, direction: ndarray) → None
```








---

<a href="..\trajectopy_core\utils.py#L53"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `evaluate_at`

```python
evaluate_at(location: ndarray) → List[float]
```

Evaluates the 3D line at a given location. 

This method calculates the projection of the input location onto the 3D line and returns the resulting point. 



**Args:**
 
 - <b>`location`</b> (np.ndarray):  The input location. 



**Returns:**
 
 - <b>`list[float]`</b>:  The resulting point on the 3D line. 

---

<a href="..\trajectopy_core\utils.py#L30"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_points`

```python
from_points(points: ndarray) → Line3D
```

Create a 3D line from a set of points. 

This method calculates the direction vector of the line from the eigenvector corresponding to the largest eigenvalue of the covariance matrix of the input points. The mean of the points is used as the mean point of the line. 



**Args:**
 
 - <b>`cls`</b> (Line3D):  The class object. 
 - <b>`points`</b> (np.ndarray):  The input points. 



**Returns:**
 
 - <b>`Line3D`</b>:  A 3D line defined by a mean point and a direction vector. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
