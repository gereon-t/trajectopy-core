<!-- markdownlint-disable -->

<a href="..\trajectopy_core\io\rosbag.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `io.rosbag`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **ROS_MESSAGE_HANDLERS**

---

<a href="..\trajectopy_core\io\rosbag.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `trajectories_from_rosbag`

```python
trajectories_from_rosbag(filename: str) → List[Trajectory]
```

Creates a trajectory from a ROS bag file 



**Args:**
 
 - <b>`filename`</b> (str):  File to read 



**Returns:**
 
 - <b>`Trajectory`</b>:  Trajectory created from the ROS bag file 


---

<a href="..\trajectopy_core\io\rosbag.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_ros_bag`

```python
read_ros_bag(filename: str) → Dict[str, Dict[str, List[Any]]]
```

Reads a ROS bag file and returns the header and the data 



**Args:**
 
 - <b>`filename`</b> (str):  File to read 



**Returns:**
 
 - <b>`Tuple[HeaderData, np.ndarray]`</b>:  Header data and data 


---

<a href="..\trajectopy_core\io\rosbag.py#L79"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `add_to_dict`

```python
add_to_dict(
    data: Dict[str, Dict[str, List[Any]]],
    key: str,
    sub_key: str,
    value: Any
) → None
```

Adds a value to a dictionary 



**Args:**
 
 - <b>`data`</b> (dict):  Dictionary to add the value to 
 - <b>`key`</b> (str):  Key to add the value to 
 - <b>`value`</b> (Any):  Value to add 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
