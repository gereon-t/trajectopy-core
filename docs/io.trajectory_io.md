<!-- markdownlint-disable -->

<a href="..\trajectopy_core\io\trajectory_io.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `io.trajectory_io`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **GPS_LEAP_SECONDS**
- **GPS_WEEK_ZERO**

---

<a href="..\trajectopy_core\io\trajectory_io.py#L23"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_data`

```python
read_data(filename: str, dtype=<class 'float'>) → Tuple[HeaderData, ndarray]
```

Reads the header and the data from a file 

By default, the trajectory data is read using pandas. If this fails, numpy is used instead. 



**Args:**
 
 - <b>`filename`</b> (str):  File to read 



**Returns:**
 
 - <b>`Tuple[HeaderData, np.ndarray]`</b>:  Header data and data 


---

<a href="..\trajectopy_core\io\trajectory_io.py#L51"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_string`

```python
read_string(input_str: str, dtype=<class 'float'>) → Tuple[HeaderData, ndarray]
```

Reads the header and the data from a string 

By default, the trajectory data is read using pandas. If this fails, numpy is used instead. 



**Args:**
 
 - <b>`input_str`</b> (str):  String to read 



**Returns:**
 
 - <b>`Tuple[HeaderData, np.ndarray]`</b>:  Header data and data 


---

<a href="..\trajectopy_core\io\trajectory_io.py#L80"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `extract_trajectory_rotations`

```python
extract_trajectory_rotations(
    header_data: HeaderData,
    trajectory_data: ndarray
) → Optional[RotationSet]
```

Extracts rotations from trajectory data and returns them as RotationSet 

Loaded rotations are converted to refer to the ENU navigation frame. For this, the actual navigation frame must be specified in the header of the trajectory file using the #nframe tag. Otherwise, the default ENU frame is assumed. 



**Args:**
 
 - <b>`header_data`</b> (HeaderData):  Holds information about the header of the trajectory file 
 - <b>`trajectory_data`</b> (np.ndarray):  Holds the trajectory data 



**Returns:**
 
 - <b>`RotationSet`</b>:  Rotations read from the trajectory file 


---

<a href="..\trajectopy_core\io\trajectory_io.py#L108"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `extract_quaternions`

```python
extract_quaternions(
    header_data: HeaderData,
    trajectory_data: ndarray
) → RotationSet
```

Extracts quaternions from trajectory data and returns them as RotationSet 



**Args:**
 
 - <b>`header_data`</b> (HeaderData):  Holds information about the header of the trajectory file 
 - <b>`trajectory_data`</b> (np.ndarray):  Holds the trajectory data 



**Returns:**
 
 - <b>`RotationSet`</b>:  Rotations read from the trajectory file 


---

<a href="..\trajectopy_core\io\trajectory_io.py#L131"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `extract_euler_angles`

```python
extract_euler_angles(
    header_data: HeaderData,
    trajectory_data: ndarray
) → RotationSet
```

Extracts euler angles from trajectory data and returns them as RotationSet 



**Args:**
 
 - <b>`header_data`</b> (HeaderData):  Holds information about the header of the trajectory file 
 - <b>`trajectory_data`</b> (np.ndarray):  Holds the trajectory data 



**Returns:**
 
 - <b>`RotationSet`</b>:  Rotations read from the trajectory file 


---

<a href="..\trajectopy_core\io\trajectory_io.py#L155"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `extract_trajectory_timestamps`

```python
extract_trajectory_timestamps(
    header_data: HeaderData,
    trajectory_data: ndarray
) → ndarray
```

Extracts timestamps from trajectory data and returns them as numpy array 



**Args:**
 
 - <b>`header_data`</b> (HeaderData):  Holds information about the header of the trajectory file 
 - <b>`trajectory_data`</b> (np.ndarray):  Holds the trajectory data 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Timestamps read from the trajectory file 


---

<a href="..\trajectopy_core\io\trajectory_io.py#L195"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `parse_datetime`

```python
parse_datetime(
    trajectory_data: ndarray,
    time_columns: List[int],
    header_data: HeaderData
) → ndarray
```

Parses datetime strings to timestamps 



**Args:**
 
 - <b>`trajectory_data`</b> (np.ndarray):  Holds the trajectory data 
 - <b>`time_columns`</b> (list[int]):  Indices of the column containing the datetime strings 
 - <b>`header_data`</b> (HeaderData):  Holds information about the header of the trajectory file 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Timestamps read from the trajectory file 


---

<a href="..\trajectopy_core\io\trajectory_io.py#L227"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `parse_gps_sow`

```python
parse_gps_sow(
    trajectory_data: ndarray,
    time_columns: List[int],
    header_data: HeaderData
) → ndarray
```

Parses GPS seconds of week to timestamps 



**Args:**
 
 - <b>`trajectory_data`</b> (np.ndarray):  Holds the trajectory data 
 - <b>`time_columns`</b> (list[int]):  Indices of the column containing the GPS seconds of week 
 - <b>`header_data`</b> (HeaderData):  Holds information about the header of the trajectory file 



**Returns:**
 
 - <b>`np.ndarray`</b>:  GPS seconds of week (SOW) read from the trajectory file 


---

<a href="..\trajectopy_core\io\trajectory_io.py#L246"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `extract_trajectory_speed`

```python
extract_trajectory_speed(
    header_data: HeaderData,
    trajectory_data: ndarray
) → Optional[ndarray]
```

Extracts speed from trajectory data and returns them as numpy array 



**Args:**
 
 - <b>`header_data`</b> (HeaderData):  Holds information about the header of the trajectory file 
 - <b>`trajectory_data`</b> (np.ndarray):  Holds the trajectory data 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Speeds read from the trajectory file 


---

<a href="..\trajectopy_core\io\trajectory_io.py#L270"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `extract_trajectory_arc_lengths`

```python
extract_trajectory_arc_lengths(
    header_data: HeaderData,
    trajectory_data: ndarray
) → Optional[ndarray]
```

Extracts arc lengths from trajectory data and returns them as numpy array 



**Args:**
 
 - <b>`header_data`</b> (HeaderData):  Holds information about the header of the trajectory file 
 - <b>`trajectory_data`</b> (np.ndarray):  Holds the trajectory data 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Arc lengths read from the trajectory file 


---

<a href="..\trajectopy_core\io\trajectory_io.py#L283"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `extract_trajectory_pointset`

```python
extract_trajectory_pointset(
    header_data: HeaderData,
    trajectory_data: ndarray
) → PointSet
```

Extracts positions from pandas DataFrame and returns a PointSet 

The positions of 'px', 'py', 'pz' are used as indices to access the DataFrame. 



**Args:**
 
 - <b>`header_data`</b> (HeaderData):  Holds information about the header of the trajectory file 
 - <b>`trajectory_data`</b> (np.ndarray):  Holds the trajectory data 



**Returns:**
 
 - <b>`PointSet`</b>:  PointSet object containing the parsed positions. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
