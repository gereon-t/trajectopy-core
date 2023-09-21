<!-- markdownlint-disable -->

<a href="../trajectopy_core/approximation/rot_approximation.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `approximation.rot_approximation`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="../trajectopy_core/approximation/rot_approximation.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rot_average_slerp`

```python
rot_average_slerp(
    function_of: ndarray,
    quat: ndarray,
    sort_switching_index: ndarray
) → ndarray
```

Rotation averaging using multiple laps 

This function will detect multiple laps of a repeated closed-loop trajectory and will average the rotations of those laps to a mean rotation. For this, the rotations of individual laps are first interpolated onto common arc lengths using spherical linear interpolation (SLERP). Then, the rotations of the laps are averaged for each arc length using the chordal L2 mean. 



**Args:**
 
 - <b>`function_of`</b> (np.ndarray):  Sorted arc lengths describing the  "location" of the given rotations  in trajectory length (meters). 
 - <b>`quat`</b> (np.ndarray):  Sorted quaternions at those arc lengths 
 - <b>`sort_switching_index`</b> (np.ndarray):  Index that reverts the sorted input  data back to chronological order. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Averaged quaternions for each arc length 


---

<a href="../trajectopy_core/approximation/rot_approximation.py#L93"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `rot_average_window`

```python
rot_average_window(
    function_of: ndarray,
    quat: ndarray,
    win_size: float = 0.15
) → ndarray
```

Function that averages rotations for a given window size using quaternion averaging. 

For each rotation, all rotations within a window centered at the current rotation are averaged for the compuation of the mean rotation. For this, the chordal L2 mean is used. 

The average rotation for the first and last rotations are computed using smaller window sizes (minimum half of the window size) 



**Args:**
 
 - <b>`function_of`</b> (np.ndarray):  The time / arc lengths describing the  "location" of the given rotations either  in time or in trajectory length. 
 - <b>`quat`</b> (np.ndarray):  _description_ 
 - <b>`win_size`</b> (float, optional):  Window size used for rotation averaging  in meters. Defaults to 0.15. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Averaged quaternions. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
