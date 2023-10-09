<!-- markdownlint-disable -->

<a href="..\trajectopy_core\util\datahandling.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `util.datahandling`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\util\datahandling.py#L62"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\util\datahandling.py#L75"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `merge_dicts`

```python
merge_dicts(dicts: Tuple[Dict[str, str], ])
```

Merges multiple dictionaries into a single dictionary, where each key in the merged dictionary corresponds to a list of values from each input dictionary. 



**Args:**
 
 - <b>`dicts`</b> (Tuple[dict]):  A tuple of dictionaries to be merged. 



**Returns:**
 
 - <b>`dict`</b>:  A dictionary containing the merged key-value pairs. 


---

<a href="..\trajectopy_core\util\datahandling.py#L95"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\util\datahandling.py#L123"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `moving`

```python
moving(
    x: ndarray,
    win_size: int,
    function: Callable[[ndarray], float]
) → ndarray
```

Computes values with a given window size and function. For example, if function=np.std this method computes the moving standard deviation. 



**Args:**
 
 - <b>`x`</b> (np.ndarray):  The input array. 
 - <b>`win_size`</b> (int):  The size of the window. 
 - <b>`function`</b> (Callable[[np.ndarray], float]):  The function to apply to the window. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  An array containing the computed values. 


---

<a href="..\trajectopy_core\util\datahandling.py#L154"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `moving_width`

```python
moving_width(
    t: ndarray,
    data: ndarray,
    width: float,
    function: Callable[[ndarray], float]
) → ndarray
```

Computes values with a given width and function. For example, if function=np.std this method computes the moving standard deviation. 



**Args:**
 
 - <b>`t`</b> (np.ndarray):  The time array. 
 - <b>`data`</b> (np.ndarray):  The input array. 
 - <b>`width`</b> (float):  The width of the window. 
 - <b>`function`</b> (Callable[[np.ndarray], float]):  The function to apply to the window. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  An array containing the computed values. 


---

<a href="..\trajectopy_core\util\datahandling.py#L182"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `round_to_precision`

```python
round_to_precision(
    function_of: ndarray,
    data: ndarray,
    resolution: float,
    filter_size: int = 100
) → Tuple[ndarray, ndarray]
```

Reduces the amount of deviations using smoothing and rounding 

It will first smooth the data using a convolution with a filter of size filter_size. Then, the data is rounded to the specified resolution and duplicate values that can result from this operation are deleted. 



**Args:**
 
 - <b>`function_of`</b> (np.ndarray):  nxm array that contains for example  time stamps, arc lengths or positions  corresponding to the data. 
 - <b>`data`</b> (np.ndarray):  nx1 array that contains the data that should  be smoothed. 
 - <b>`precision`</b> (float):  Desired resolution 
 - <b>`filter_size`</b> (int):  Window / filter size for smoothing 



**Returns:**
 downsampled function_of and data 


---

<a href="..\trajectopy_core\util\datahandling.py#L215"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rndodd`

```python
rndodd(s: float) → int
```

Rounds a float to the nearest odd integer. 



**Args:**
 
 - <b>`s`</b> (float):  The float to round. 



**Returns:**
 
 - <b>`int`</b>:  The rounded odd integer. 


---

<a href="..\trajectopy_core\util\datahandling.py#L233"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\util\datahandling.py#L259"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\util\datahandling.py#L291"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `remove_nan_vals`

```python
remove_nan_vals(a: ndarray) → ndarray
```

Removes NaN values from a numpy array. 



**Args:**
 
 - <b>`a`</b> (np.ndarray):  The numpy array to remove NaN values from. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  The numpy array with NaN values removed. 


---

<a href="..\trajectopy_core\util\datahandling.py#L307"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rotate_to_main_axis`

```python
rotate_to_main_axis(xyz: ndarray) → ndarray
```

Rotates a point cloud to align with its main axis. 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  An array of shape (n, 3) containing the x, y, and z  coordinates of the point cloud. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  An array of shape (n, 3) containing the rotated point cloud. 


---

<a href="..\trajectopy_core\util\datahandling.py#L324"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `main_axis`

```python
main_axis(xyz: ndarray) → ndarray
```

Computes the main axis of a point cloud. 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  An array of shape (n, 3) containing the x, y, and z  coordinates of the point cloud. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  An array of shape (3,) containing the direction cosines of  the main axis. 


---

<a href="..\trajectopy_core\util\datahandling.py#L340"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `line_angle`

```python
line_angle(line: ndarray) → float
```

Calculates the angle between a 2D line and the x-axis. 



**Args:**
 
 - <b>`line`</b> (np.ndarray):  A 2D line represented as a numpy array of shape (2,). 



**Returns:**
 
 - <b>`float`</b>:  The angle between the line and the x-axis in radians. 


---

<a href="..\trajectopy_core\util\datahandling.py#L353"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rot_from_vec`

```python
rot_from_vec(vec_a: ndarray, vec_b: ndarray) → ndarray
```

Computes the rotation matrix that rotates vector a to vector b. 



**Args:**
 
 - <b>`vec_a`</b> (np.ndarray):  The vector to rotate. 
 - <b>`vec_b`</b> (np.ndarray):  The target vector. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  The rotation matrix that rotates vector a to vector b. 


---

<a href="..\trajectopy_core\util\datahandling.py#L375"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `cart2pol`

```python
cart2pol(x, y)
```

Converts Cartesian coordinates to polar coordinates. 



**Args:**
 
 - <b>`x`</b> (float):  The x-coordinate. 
 - <b>`y`</b> (float):  The y-coordinate. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  An array of shape (1, 2) containing the polar coordinates  (rho and phi) of the input Cartesian coordinates. 


---

<a href="..\trajectopy_core\util\datahandling.py#L392"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `pol2cart`

```python
pol2cart(rho, phi)
```

Converts polar coordinates to Cartesian coordinates. 



**Args:**
 
 - <b>`rho`</b> (float):  The radial distance from the origin to the point. 
 - <b>`phi`</b> (float):  The angle between the x-axis and the line connecting the  origin to the point, in radians. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  An array of shape (1, 2) containing the Cartesian  coordinates (x and y) of the input polar coordinates. 


---

<a href="..\trajectopy_core\util\datahandling.py#L410"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `get_tau`

```python
get_tau(ts_pos: ndarray, ts_target: ndarray) → float
```

Calculates the angle between a position and a target point. 



**Args:**
 
 - <b>`ts_pos`</b> (np.array):  A numpy array of shape (2,) representing the position. 
 - <b>`ts_target`</b> (np.array):  A numpy array of shape (2,) representing the target point. 



**Returns:**
 
 - <b>`float`</b>:  The angle between the position and the target point in radians. 


---

<a href="..\trajectopy_core\util\datahandling.py#L424"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rot_z`

```python
rot_z(gamma: float, dim: int = 3) → ndarray
```

Computes the rotation matrix around the z-axis. 



**Args:**
 
 - <b>`gamma`</b> (float):  The rotation angle in radians. 
 - <b>`dim`</b> (int, optional):  The dimension of the rotation matrix. Defaults to 3. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  The rotation matrix around the z-axis. 


---

<a href="..\trajectopy_core\util\datahandling.py#L454"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `filter_from_limits`

```python
filter_from_limits(tstamps: ndarray, gap_limits: ndarray) → ndarray
```

Creates a boolean filter which filters tstamps according to limits defined in gap_limits 



**Args:**
 
 - <b>`tstamps`</b> (np.ndarray):  Timestamps that should be filtered 
 - <b>`gap_limits`</b> (np.ndarray):  [nx2] array containing the time  limits of n gaps 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Boolean filter which filter tstamps so that  all gaps are removed. 


---

<a href="..\trajectopy_core\util\datahandling.py#L479"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `detect_time_gaps`

```python
detect_time_gaps(tstamps: ndarray, max_gap_size: float) → ndarray
```

Function that detect gaps within a timespan 

As soon as two timestamps have a difference greater than 'max_gap_size' they are considered as start and end points of a time gap. This methods returns those timestamps as a [nx2] array. 



**Args:**
 
 - <b>`tstamps`</b> (np.ndarray):  Timestamps in which gaps  should be detected 
 - <b>`max_gap_size`</b> (float):  Maximum tolerated gap size  in seconds. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  [nx2] array containing time limits  of all detected gaps 


---

<a href="..\trajectopy_core\util\datahandling.py#L508"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\util\datahandling.py#L539"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

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

<a href="..\trajectopy_core\util\datahandling.py#L558"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `togrid`

```python
togrid(xyz: ndarray, data: ndarray, grid_mp: float = 1.0) → Grid
```

Discretizes data into a grid of size grid_mp 



**Args:**
 
 - <b>`xyz`</b> (np.ndarray):  Positions of data values [nx2] / [nx3] 
 - <b>`data`</b> (np.ndarray):  data values [nx1] 
 - <b>`grid_mp`</b> (float, optional):  Number of grid bins in megapixels.  Defaults to 1.0. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  grid with averaged values 


---

<a href="..\trajectopy_core\util\datahandling.py#L20"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Grid`
A class representing a 2D grid of values, with methods for accessing and manipulating the grid. 



**Attributes:**
 
 - <b>`full_grid`</b> (np.ndarray):  The full 2D grid of values. 
 - <b>`x_bin_locations`</b> (list[int]):  The x-coordinates of the grid cells. 
 - <b>`y_bin_locations`</b> (list[int]):  The y-coordinates of the grid cells. 
 - <b>`pixel_size`</b> (float):  The size of each pixel in the grid. 

Methods: values() -> np.ndarray:  Returns the values of the grid cells. populated_grid_cells() -> np.ndarray:  Returns the x and y coordinates and values of the populated grid cells. scaled_grid_cells() -> np.ndarray:  Returns the x and y coordinates and values of the populated grid cells, scaled by the pixel size. 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    full_grid: ndarray,
    x_bin_locations: ndarray,
    y_bin_locations: ndarray,
    pixel_size: float
) → None
```






---

#### <kbd>property</kbd> populated_grid_cells





---

#### <kbd>property</kbd> scaled_grid_cells





---

#### <kbd>property</kbd> values










---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
