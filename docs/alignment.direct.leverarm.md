<!-- markdownlint-disable -->

<a href="..\trajectopy_core\alignment\direct\leverarm.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `alignment.direct.leverarm`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\alignment\direct\leverarm.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `direct_leverarm`

```python
direct_leverarm(
    xyz_to: ndarray,
    xyz_from: ndarray,
    rpy_body: ndarray,
    weights: Optional[ndarray] = None,
    speed: Optional[ndarray] = None
) → Tuple[Leverarm, Parameter, ndarray]
```

Leverarm (+time) estimation 

Estimates the leverarm and the time offset between two trajectories using a gauß-markov model. 

The observations are the difference between the target and the source positions. The parameters are: 
    - time (if gradients / speeds are provided) 
    - leverarm (dx, dy, dz) 



**Args:**
 
 - <b>`xyz_to`</b> (np.ndarray):  Source positions 
 - <b>`xyz_from`</b> (np.ndarray):  target positions 
 - <b>`rpy_body`</b> (np.ndarray):  platform orientations 
 - <b>`weights`</b> (np.ndarray, optional):  observation weights.  Defaults to None. 
 - <b>`speed`</b> (np.ndarray, optional):  speed of the platform.  Defaults to None. 



**Returns:**
 
 - <b>`Tuple[np.ndarray, np.ndarray]`</b>:  Tuple containing the estimated  parameters and the residuals of  the adjustment. 


---

<a href="..\trajectopy_core\alignment\direct\leverarm.py#L102"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `design_matrix`

```python
design_matrix(rpy: ndarray, speed: Optional[ndarray] = None) → ndarray
```

Builds design matrix for leverarm (+ time) estimation 

Contains the derivation of the observation equations with respect to the parameters 



**Args:**
 
 - <b>`rpy`</b> (np.ndarray):  platform orientations 
 - <b>`speed`</b> (np.ndarray, optional):  Gradients / speeds at the  positions. Defaults to None.  If no gradients are provided  the adjustment will fall back  to a leverarm only estimation. 



**Returns:**
 
 - <b>`np.ndarray`</b>:  design matrix 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
