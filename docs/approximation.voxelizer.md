<!-- markdownlint-disable -->

<a href="..\trajectopy_core\approximation\voxelizer.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `approximation.voxelizer`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\approximation\voxelizer.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Voxel`
A class representing a voxel. 



**Attributes:**
 
 - <b>`id`</b> (int):  The unique identifier of the voxel. 
 - <b>`size`</b> (float):  The size of the voxel. 
 - <b>`points`</b> (list):  A list of points contained within the voxel. 

Properties: 
 - <b>`mean_point`</b> (np.ndarray):  The mean point of the voxel. 
 - <b>`num_points`</b> (int):  The number of points contained within the voxel. 
 - <b>`to_numpy`</b> (np.ndarray):  The points contained within the voxel as a numpy array. 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(id: str, size: float, points: list) → None
```






---

#### <kbd>property</kbd> mean_point





---

#### <kbd>property</kbd> num_points





---

#### <kbd>property</kbd> to_numpy








---

<a href="..\trajectopy_core\approximation\voxelizer.py#L47"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Voxelizer`
A class for voxelizing point clouds. 



**Attributes:**
 
 - <b>`voxels`</b> (dict[str, Voxel]):  A dictionary containing voxels, each with a unique id. 
 - <b>`kd_tree`</b> (scipy.spatial.KDTree):  A KDTree containing the mean points of each voxel. 

Methods: 
 - <b>`ball_query(xyz`</b>:  np.ndarray, r: float) -> list[frozenset[str]]: Performs a kd-ball-query within the voxels. 
 - <b>`index_to_id(index`</b>:  int) -> int: Returns the id of the voxel at the given index. 

<a href="..\trajectopy_core\approximation\voxelizer.py#L59"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(xyz: ndarray, voxel_size: float = 0.05) → None
```






---

#### <kbd>property</kbd> mean_points







---

<a href="..\trajectopy_core\approximation\voxelizer.py#L101"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `ball_query`

```python
ball_query(xyz: ndarray, r: float) → List[FrozenSet[str]]
```

Performs a kd-ball-query within the voxels 

Returns a list of frozensets containing the voxel ids vor neighboring voxels. 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  query positions 
 - <b>`r`</b> (float):  radius in [m] 



**Returns:**
 
 - <b>`list[frozenset[str]]`</b>:  list of frozensets containing voxel ids. 

---

<a href="..\trajectopy_core\approximation\voxelizer.py#L98"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `index_to_id`

```python
index_to_id(index: int) → str
```





---

<a href="..\trajectopy_core\approximation\voxelizer.py#L117"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `k_nearest_query`

```python
k_nearest_query(xyz: ndarray, k_nearest: int) → List[FrozenSet[str]]
```

Performs a k-nearest-query within the voxels 

Returns a list of frozensets containing the voxel ids vor neighboring voxels. 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  query positions 
 - <b>`k_nearest`</b> (int):  k-nearest neighbors 



**Returns:**
 
 - <b>`list[frozenset[str]]`</b>:  list of frozensets containing voxel ids. 

---

<a href="..\trajectopy_core\approximation\voxelizer.py#L133"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `points_from_voxel_set`

```python
points_from_voxel_set(voxel_set: FrozenSet[str]) → ndarray
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
