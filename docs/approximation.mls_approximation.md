<!-- markdownlint-disable -->

<a href="..\trajectopy_core\approximation\mls_approximation.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `approximation.mls_approximation`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\approximation\mls_approximation.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `mls_iterative`

```python
mls_iterative(
    xyz: ndarray,
    voxel_size: float = 0.05,
    k_nearest: int = 4,
    movement_threshold: float = 0.005
) → ndarray
```

Performs the mls approximation iteratively 

This method approximates the neighborhood of a point using a 3d line. Neighborhoods are defined using voxels. The mls approximation is repeatetly applied to the result from the previous iteration until the average point movement falls below a user defined threshold (movement_threshold). 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  Input points that should be approximated 
 - <b>`voxel_size`</b> (float):  length of one voxel side 
 - <b>`k_nearest`</b> (int):  number of voxels that define a neighborhood 
 - <b>`movement_threshold`</b> (float, optional):  Threshold that defines  when to stop iterating.  When the average point  movement is below of the  pointsDefaults to 0.005. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Approximated positions 


---

<a href="..\trajectopy_core\approximation\mls_approximation.py#L114"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `mls_single`

```python
mls_single(
    xyz: ndarray,
    voxel_size: float,
    k_nearest: int
) → Tuple[ndarray, float]
```

Performs the mls approximation iteratively 

This method approximates the neighborhood of a point using a 3d line. Neighborhoods are defined using voxels. 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  Input points that should be approximated 
 - <b>`voxel_size`</b> (float):  length of one voxel side 
 - <b>`k_nearest`</b> (int):  number of voxels that define a neighborhood 



**Returns:**
 
 - <b>`Tuple[np.ndarray, float]`</b>:  Approximated positions, average point movement 


---

<a href="..\trajectopy_core\approximation\mls_approximation.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\approximation\mls_approximation.py#L57"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\approximation\mls_approximation.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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
