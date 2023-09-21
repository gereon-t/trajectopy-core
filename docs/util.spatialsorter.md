<!-- markdownlint-disable -->

<a href="../trajectopy_core/util/spatialsorter.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `util.spatialsorter`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **SORTING_DICT**

---

<a href="../trajectopy_core/util/spatialsorter.py#L251"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `reconstruct_spatial_sorting`

```python
reconstruct_spatial_sorting(xyz: ndarray) → Tuple[list, list]
```

Reconstruct the spatial sorting 

Given a set of points inside a numpy array, this method reconstruct the spatial sorting of those points using a minimum-spanning-tree. The minimum-spanning-tree is a cycle-free graph that connects all points while minimizing its edge lengths. 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  Input points that should be sorted 



**Returns:**
 
 - <b>`Tuple[list, list]`</b>:  Index that establishes a spatial sorting  as well as a list containing the indices  of missing points. This can be the case  if the delaunay triangulation necessary  for the minimum-spanning-tree computation  discards some points if they are almost  identical. If no points are missing, the  list will be empty. 


---

<a href="../trajectopy_core/util/spatialsorter.py#L308"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `begin_with`

```python
begin_with(idx: list, begin: int) → list
```

Reorganizes list so that 'begin' is the first value in the list 



**Args:**
 
 - <b>`idx`</b> (list):  index that should be reorganized 
 - <b>`begin`</b> (int):  value of the new first element 



**Returns:**
 
 - <b>`list`</b>:  reorganized list whose first value is now  'begin' 


---

<a href="../trajectopy_core/util/spatialsorter.py#L326"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `compute_mst`

```python
compute_mst(xyz: ndarray) → Tuple[Graph, list]
```

Function that computes a Minimum-Spanning-Tree using the matplotlib implementation. This implementation may skip some (nearly) colinear points. 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  2d / 3d positions used for mst computation 



**Returns:**
 
 - <b>`Tuple[nx.Graph, list]`</b>:  networkx.Graph object of the mst and  list of missing point indices if any  points are missing due to colinearity 


---

<a href="../trajectopy_core/util/spatialsorter.py#L401"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `detect_laps_by_length`

```python
detect_laps_by_length(lengths: ndarray) → ndarray
```

Detect laps by detecting jumps in unsorted trajectory lengths 


---

<a href="../trajectopy_core/util/spatialsorter.py#L416"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `complete_lap_dist`

```python
complete_lap_dist(xyz, dist_th: float = 0.5) → bool_
```

Function to determine if lap is complete A lap is considered as complete, if the distance between the starting point and the end point is below a specified distance 


---

<a href="../trajectopy_core/util/spatialsorter.py#L433"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `infer_sort_index`

```python
infer_sort_index(sorting: Sorting, tstamps: ndarray)
```

Infers the sort index from the sorting and timestamps 


---

<a href="../trajectopy_core/util/spatialsorter.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Sorting`
An enumeration. 





---

<a href="../trajectopy_core/util/spatialsorter.py#L34"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `SpatialSorter`
Class representing a spatial sorter. 

This class sorts position spatially by computing the moving-least-squares approximation and the minimum-spanning-tree of the point set. 

Spatially in the context of a trajectory means, that after sorting, the trajectory is a function of its arc length and not a function of time. Spatially sorting a trajectory only makes sense if the trajectory was repeated multiple times. 

A sorter object should sort input data and provide at least the following interface: 
- idx_sort: Index to establish the sorting starting from unordered raw data 
- function_of: Parameterization of the sorted data 

<a href="../trajectopy_core/util/spatialsorter.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(xyz: ndarray, discard_missing: bool = True) → None
```

Initialization of the SpatialSorter 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  Input points for sorting 
 - <b>`mls_dist`</b> (float, optional):  Neighborhood distance for  moving-least-squares  approximation in meters.  It describes the radius of a  kd-tree ball-query.  Defaults to 0.05. 
 - <b>`mls_it_th`</b> (float, optional):  Threshold when to stop  performing the iterative  moving-least-squares  approximation in meters.  It describes the average point  movement after an mls iteration.  Defaults to 0.01. 
 - <b>`discard_missing`</b> (bool, optional):  If set to True, points  dicarded during delaunay  triangulation are also  discarded during sorting.  Alternatively, missing  points can be inserted  'manually' after the  actual sorting.  Defaults to True. 


---

#### <kbd>property</kbd> direction

Detect lap directions 

---

#### <kbd>property</kbd> function_of

How should the points be parameterized AFTER sorting? 

---

#### <kbd>property</kbd> idx_sort

How can unsorted arrays be sorted? 

---

#### <kbd>property</kbd> lap_indices

Returns the indices of each lap 

The lap indices are indicating at which index a new lap begins 

---

#### <kbd>property</kbd> mls_arc_lengths

Returns trajectory lengths from mls positions 

---

#### <kbd>property</kbd> mls_unsorted

Returns (unsorted) mls positions used for sorting 

---

#### <kbd>property</kbd> num_laps

Returns the number of laps 



---

<a href="../trajectopy_core/util/spatialsorter.py#L137"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `reconstruct`

```python
reconstruct() → list
```

Reconstructs the spatial sorting of the given points 

Spatially sorts the positions by constructing the minimum-spanning-tree of the positions. Finally, by performing up to 3 breadth-first-searched within the mst, the spatial sorting can be reconstructed 

This method also takes care of inserting missing points or assuring that the direction of travel is kept during sorting. 



**Returns:**
 
 - <b>`list`</b>:  Sort index 

---

<a href="../trajectopy_core/util/spatialsorter.py#L176"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `sort`

```python
sort(array: ndarray, inverse: bool = False) → ndarray
```

Function that applies the sorting index to an array / list 



**Args:**
 
 - <b>`array`</b> (np.ndarray]):  array that needs to get sorted 
 - <b>`inverse`</b> (bool, optional):  Specifies whether the sorting  should be inverted. If set to  'True', already sorted data can  be 'unsorted'.  Defaults to False. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Sorted array 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
