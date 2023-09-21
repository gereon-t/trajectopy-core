<!-- markdownlint-disable -->

<a href="../trajectopy_core/approximation/util.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `approximation.util`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="../trajectopy_core/approximation/util.py#L19"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `fit_line_3d`

```python
fit_line_3d(xyz: ndarray) → ndarray
```

Fits a 3D line using least-squares 



**Parameters:**
 xyz (np.ndarray): A numpy array of shape (n, 3) containing the 3D points 



**Returns:**
 np.ndarray: A numpy array of shape (3,) containing the direction of the line 


---

<a href="../trajectopy_core/approximation/util.py#L33"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `fit_line_2d`

```python
fit_line_2d(
    x: ndarray,
    y: ndarray,
    weights: ndarray = array([], dtype=float64)
) → Tuple[ndarray, ndarray, ndarray]
```

Fits a 2D line using least-squares 



**Parameters:**
 x (np.ndarray): A numpy array of shape (n,) containing the x-coordinates of the 2D points y (np.ndarray): A numpy array of shape (n,) containing the y-coordinates of the 2D points weights (np.ndarray): A numpy array of shape (n,) containing the weights of the points (default is an array of ones) 



**Returns:**
 Tuple[np.ndarray, np.ndarray, np.ndarray]: A tuple containing the slope, intercept, and residuals of the fitted line 


---

<a href="../trajectopy_core/approximation/util.py#L61"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `sparse_least_squares`

```python
sparse_least_squares(
    design_matrix: csr_matrix,
    observations: ndarray
) → Tuple[ndarray, ndarray, ndarray]
```

Solves a least squares problem with a sparse matrix A and a dense vector l. 



**Parameters:**
 design_matrix (csr_matrix): A sparse matrix of shape (m, n) representing the design matrix. l (np.ndarray): A numpy array of shape (m,) containing the observations. 



**Returns:**
 Tuple[np.ndarray, np.ndarray, np.ndarray]: A tuple containing the solution vector x_s, the approximated observations l_s, and the residuals v. 


---

<a href="../trajectopy_core/approximation/util.py#L86"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `least_squares`

```python
least_squares(
    design_matrix: ndarray,
    observations: ndarray,
    sigma_ll: ndarray = array([], dtype=float64)
) → Tuple[ndarray, ndarray, ndarray]
```

Solves a least squares problem with a dense matrix A and a dense vector l. 



**Parameters:**
 design_matrix (np.ndarray): A numpy array of shape (m, n) representing the design matrix. observations (np.ndarray): A numpy array of shape (m,) containing the observations. sigma_ll (np.ndarray): A numpy array of shape (m, m) containing the weights of the observations (default is an identity matrix). 



**Returns:**
 Tuple[np.ndarray, np.ndarray, np.ndarray]: A tuple containing the solution vector x_s, the approximated observations l_s, and the residuals v. 


---

<a href="../trajectopy_core/approximation/util.py#L122"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `skew_symmetric_matrix`

```python
skew_symmetric_matrix(vector: ndarray) → ndarray
```

Returns the skew-symmetric matrix of a 3D vector. 



**Parameters:**
 vector (np.ndarray): A numpy array of shape (3,) containing the 3D vector. 



**Returns:**
 np.ndarray: A numpy array of shape (3, 3) containing the skew-symmetric matrix. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
