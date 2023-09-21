<!-- markdownlint-disable -->

<a href="../trajectopy_core/alignment/direct_timeshift.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `alignment.direct_timeshift`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="../trajectopy_core/alignment/direct_timeshift.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `direct_timeshift`

```python
direct_timeshift(
    xyz_to: ndarray,
    xyz_from: ndarray,
    speed: ndarray,
    weights: ndarray = array([], dtype=float64)
) → Tuple[Parameter, ndarray]
```

Time shift estimation 

Estimates the time offset between two trajectories using a gauß-markov model. 

The observations are the difference between the target and the source positions. The parameters are: 
    - time 



**Args:**
 
 - <b>`xyz_to`</b> (np.ndarray):  Source positions 
 - <b>`xyz_from`</b> (np.ndarray):  target positions 
 - <b>`speed`</b> (np.ndarray):  speed of the platform. 
 - <b>`weights`</b> (np.ndarray, optional):  observation weights.  Defaults to None. 





**Returns:**
 
 - <b>`Tuple[np.ndarray, np.ndarray]`</b>:  Tuple containing the estimated  parameters and the residuals of  the adjustment. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
