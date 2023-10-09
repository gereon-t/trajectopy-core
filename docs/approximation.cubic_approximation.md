<!-- markdownlint-disable -->

<a href="..\trajectopy_core\approximation\cubic_approximation.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `approximation.cubic_approximation`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\approximation\cubic_approximation.py#L220"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `piecewise_cubic`

```python
piecewise_cubic(
    function_of: ndarray,
    values: ndarray,
    int_size: float = 0.15,
    min_obs: int = 25,
    return_approx_objects: bool = False
) → Union[Tuple[ndarray, List[CubicApproximation]], ndarray]
```

Approximates a piecewise cubic function for a given set of input values. 



**Args:**
 
 - <b>`function_of`</b> (np.ndarray):  The input values to approximate the function for. 
 - <b>`values`</b> (np.ndarray):  The output values corresponding to the input values. 
 - <b>`int_size`</b> (float, optional):  The interval size for the approximation. Defaults to 0.15. 
 - <b>`min_obs`</b> (int, optional):  The minimum number of observations required for the approximation. Defaults to 25. 
 - <b>`return_approx_objects`</b> (bool, optional):  Whether to return the list of CubicApproximation objects along with the approximated values. Defaults to False. 



**Returns:**
 
 - <b>`Union[np.ndarray, Tuple[list[CubicApproximation], np.ndarray]]`</b>:  The approximated values. If `return_approx_objects` is True, returns a tuple containing the approximated values and the list of CubicApproximation objects. 


---

<a href="..\trajectopy_core\approximation\cubic_approximation.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `CubicApproximation`
Class for piecewise cubic approximation 

<a href="..\trajectopy_core\approximation\cubic_approximation.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(
    function_of: ndarray,
    values: ndarray,
    int_size: float,
    min_obs: int
) → None
```

Inititalization of a new CubicApproximation class object 




---

<a href="..\trajectopy_core\approximation\cubic_approximation.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `eval`

```python
eval(locations: ndarray) → ndarray
```

Evaluate the cubic approximation at specified locations 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
