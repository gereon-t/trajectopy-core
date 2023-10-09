<!-- markdownlint-disable -->

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `alignment.functional_model.equations`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L12"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `functional_relationship_x`

```python
functional_relationship_x(
    x_from: Union[float, ndarray] = 0.0,
    y_from: Union[float, ndarray] = 0.0,
    z_from: Union[float, ndarray] = 0.0,
    x_to: Union[float, ndarray] = 0.0,
    euler_x: Union[float, ndarray] = 0.0,
    euler_y: Union[float, ndarray] = 0.0,
    euler_z: Union[float, ndarray] = 0.0,
    speed_x: Union[float, ndarray] = 0.0,
    speed_y: Union[float, ndarray] = 0.0,
    speed_z: Union[float, ndarray] = 0.0,
    sim_trans_x: Union[float, ndarray] = 0.0,
    sim_rot_x: Union[float, ndarray] = 0.0,
    sim_rot_y: Union[float, ndarray] = 0.0,
    sim_rot_z: Union[float, ndarray] = 0.0,
    sim_scale: Union[float, ndarray] = 1.0,
    time_shift: Union[float, ndarray] = 0.0,
    lever_x: Union[float, ndarray] = 0.0,
    lever_y: Union[float, ndarray] = 0.0,
    lever_z: Union[float, ndarray] = 0.0
) → Union[float, ndarray]
```

Evaluates the observation equations of the Gauß-Helmert-Model 

This method puts together the individual building blocks of the Helmert transform, lever arm estimation, and synchronization to obtain the corresponding functional relationship. 





**Returns:**
 
 - <b>`np.ndarray`</b>:  Result of the functional relationship 


---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L65"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `functional_relationship_y`

```python
functional_relationship_y(
    x_from: Union[float, ndarray] = 0.0,
    y_from: Union[float, ndarray] = 0.0,
    z_from: Union[float, ndarray] = 0.0,
    y_to: Union[float, ndarray] = 0.0,
    euler_x: Union[float, ndarray] = 0.0,
    euler_y: Union[float, ndarray] = 0.0,
    euler_z: Union[float, ndarray] = 0.0,
    speed_x: Union[float, ndarray] = 0.0,
    speed_y: Union[float, ndarray] = 0.0,
    speed_z: Union[float, ndarray] = 0.0,
    sim_trans_y: Union[float, ndarray] = 0.0,
    sim_rot_x: Union[float, ndarray] = 0.0,
    sim_rot_y: Union[float, ndarray] = 0.0,
    sim_rot_z: Union[float, ndarray] = 0.0,
    sim_scale: Union[float, ndarray] = 1.0,
    time_shift: Union[float, ndarray] = 0.0,
    lever_x: Union[float, ndarray] = 0.0,
    lever_y: Union[float, ndarray] = 0.0,
    lever_z: Union[float, ndarray] = 0.0
) → Union[float, ndarray]
```

Evaluates the observation equations of the Gauß-Helmert-Model 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Result of the functional relationship 


---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L113"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `functional_relationship_z`

```python
functional_relationship_z(
    x_from: Union[float, ndarray] = 0.0,
    y_from: Union[float, ndarray] = 0.0,
    z_from: Union[float, ndarray] = 0.0,
    z_to: Union[float, ndarray] = 0.0,
    euler_x: Union[float, ndarray] = 0.0,
    euler_y: Union[float, ndarray] = 0.0,
    euler_z: Union[float, ndarray] = 0.0,
    speed_x: Union[float, ndarray] = 0.0,
    speed_y: Union[float, ndarray] = 0.0,
    speed_z: Union[float, ndarray] = 0.0,
    sim_trans_z: Union[float, ndarray] = 0.0,
    sim_rot_x: Union[float, ndarray] = 0.0,
    sim_rot_y: Union[float, ndarray] = 0.0,
    sim_scale: Union[float, ndarray] = 1.0,
    time_shift: Union[float, ndarray] = 0.0,
    lever_x: Union[float, ndarray] = 0.0,
    lever_y: Union[float, ndarray] = 0.0,
    lever_z: Union[float, ndarray] = 0.0
) → Union[float, ndarray]
```

Evaluates the observation equations of the Gauß-Helmert-Model 



**Returns:**
 
 - <b>`np.ndarray`</b>:  Result of the functional relationship 


---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L159"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `leverarm_time_component`

```python
leverarm_time_component(
    euler_x: Union[float, ndarray] = 0.0,
    euler_y: Union[float, ndarray] = 0.0,
    euler_z: Union[float, ndarray] = 0.0,
    speed_x: Union[float, ndarray] = 0.0,
    speed_y: Union[float, ndarray] = 0.0,
    speed_z: Union[float, ndarray] = 0.0,
    time_shift: Union[float, ndarray] = 0.0,
    lever_x: Union[float, ndarray] = 0.0,
    lever_y: Union[float, ndarray] = 0.0,
    lever_z: Union[float, ndarray] = 0.0
) → Tuple[Union[float, ndarray], Union[float, ndarray], Union[float, ndarray]]
```






---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L204"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `transformed_x_from`

```python
transformed_x_from(
    x_from: Union[float, ndarray] = 0.0,
    y_from: Union[float, ndarray] = 0.0,
    z_from: Union[float, ndarray] = 0.0,
    euler_x: Union[float, ndarray] = 0.0,
    euler_y: Union[float, ndarray] = 0.0,
    euler_z: Union[float, ndarray] = 0.0,
    speed_x: Union[float, ndarray] = 0.0,
    speed_y: Union[float, ndarray] = 0.0,
    speed_z: Union[float, ndarray] = 0.0,
    sim_trans_x: Union[float, ndarray] = 0.0,
    sim_rot_x: Union[float, ndarray] = 0.0,
    sim_rot_y: Union[float, ndarray] = 0.0,
    sim_rot_z: Union[float, ndarray] = 0.0,
    sim_scale: Union[float, ndarray] = 1.0,
    time_shift: Union[float, ndarray] = 0.0,
    lever_x: Union[float, ndarray] = 0.0,
    lever_y: Union[float, ndarray] = 0.0,
    lever_z: Union[float, ndarray] = 0.0
) → Union[float, ndarray]
```






---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L248"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `transformed_y_from`

```python
transformed_y_from(
    x_from: Union[float, ndarray] = 0.0,
    y_from: Union[float, ndarray] = 0.0,
    z_from: Union[float, ndarray] = 0.0,
    euler_x: Union[float, ndarray] = 0.0,
    euler_y: Union[float, ndarray] = 0.0,
    euler_z: Union[float, ndarray] = 0.0,
    speed_x: Union[float, ndarray] = 0.0,
    speed_y: Union[float, ndarray] = 0.0,
    speed_z: Union[float, ndarray] = 0.0,
    sim_trans_y: Union[float, ndarray] = 0.0,
    sim_rot_x: Union[float, ndarray] = 0.0,
    sim_rot_y: Union[float, ndarray] = 0.0,
    sim_rot_z: Union[float, ndarray] = 0.0,
    sim_scale: Union[float, ndarray] = 1.0,
    time_shift: Union[float, ndarray] = 0.0,
    lever_x: Union[float, ndarray] = 0.0,
    lever_y: Union[float, ndarray] = 0.0,
    lever_z: Union[float, ndarray] = 0.0
) → Union[float, ndarray]
```






---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L292"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `transformed_z_from`

```python
transformed_z_from(
    x_from: Union[float, ndarray] = 0.0,
    y_from: Union[float, ndarray] = 0.0,
    z_from: Union[float, ndarray] = 0.0,
    euler_x: Union[float, ndarray] = 0.0,
    euler_y: Union[float, ndarray] = 0.0,
    euler_z: Union[float, ndarray] = 0.0,
    speed_x: Union[float, ndarray] = 0.0,
    speed_y: Union[float, ndarray] = 0.0,
    speed_z: Union[float, ndarray] = 0.0,
    sim_trans_z: Union[float, ndarray] = 0.0,
    sim_rot_x: Union[float, ndarray] = 0.0,
    sim_rot_y: Union[float, ndarray] = 0.0,
    sim_scale: Union[float, ndarray] = 1.0,
    time_shift: Union[float, ndarray] = 0.0,
    lever_x: Union[float, ndarray] = 0.0,
    lever_y: Union[float, ndarray] = 0.0,
    lever_z: Union[float, ndarray] = 0.0
) → Union[float, ndarray]
```






---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L334"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `functional_helmert_component_x`

```python
functional_helmert_component_x(
    x_from: Union[float, ndarray],
    y_from: Union[float, ndarray],
    z_from: Union[float, ndarray],
    sim_trans_x: Union[float, ndarray],
    sim_rot_x: Union[float, ndarray],
    sim_rot_y: Union[float, ndarray],
    sim_rot_z: Union[float, ndarray],
    sim_scale: Union[float, ndarray]
) → Union[float, ndarray]
```

Helper function returning the helmert component of the functional relationship 



**Returns:**
 
 - <b>`np.ndarray`</b>:  helmert component 


---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L357"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `functional_helmert_component_y`

```python
functional_helmert_component_y(
    x_from: Union[float, ndarray],
    y_from: Union[float, ndarray],
    z_from: Union[float, ndarray],
    sim_trans_y: Union[float, ndarray],
    sim_rot_x: Union[float, ndarray],
    sim_rot_y: Union[float, ndarray],
    sim_rot_z: Union[float, ndarray],
    sim_scale: Union[float, ndarray]
) → Union[float, ndarray]
```

Helper function returning the helmert component of the functional relationship 



**Returns:**
 
 - <b>`np.ndarray`</b>:  helmert component 


---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L379"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `functional_helmert_component_z`

```python
functional_helmert_component_z(
    x_from: Union[float, ndarray],
    y_from: Union[float, ndarray],
    z_from: Union[float, ndarray],
    sim_trans_z: Union[float, ndarray],
    sim_rot_x: Union[float, ndarray],
    sim_rot_y: Union[float, ndarray],
    sim_scale: Union[float, ndarray]
) → Union[float, ndarray]
```

Helper function returning the helmert component of the functional relationship 



**Returns:**
 
 - <b>`np.ndarray`</b>:  helmert component 


---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L400"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `functional_leverarm_time_component_x`

```python
functional_leverarm_time_component_x(
    euler_x: Union[float, ndarray],
    euler_y: Union[float, ndarray],
    euler_z: Union[float, ndarray],
    lever_x: Union[float, ndarray],
    lever_y: Union[float, ndarray],
    lever_z: Union[float, ndarray],
    time_shift: Union[float, ndarray],
    speed_x: Union[float, ndarray]
) → Union[float, ndarray]
```

Helper function returning the helmert component of the functional relationship 



**Returns:**
 
 - <b>`np.ndarray`</b>:  helmert component 


---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L422"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `functional_leverarm_time_component_y`

```python
functional_leverarm_time_component_y(
    euler_x: Union[float, ndarray],
    euler_y: Union[float, ndarray],
    euler_z: Union[float, ndarray],
    lever_x: Union[float, ndarray],
    lever_y: Union[float, ndarray],
    lever_z: Union[float, ndarray],
    time_shift: Union[float, ndarray],
    speed_y: Union[float, ndarray]
) → Union[float, ndarray]
```

Helper function returning the helmert component of the functional relationship 



**Returns:**
 
 - <b>`np.ndarray`</b>:  helmert component 


---

<a href="..\trajectopy_core\alignment\functional_model\equations.py#L444"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `functional_leverarm_time_component_z`

```python
functional_leverarm_time_component_z(
    euler_x: Union[float, ndarray],
    euler_y: Union[float, ndarray],
    lever_x: Union[float, ndarray],
    lever_y: Union[float, ndarray],
    lever_z: Union[float, ndarray],
    time_shift: Union[float, ndarray],
    speed_z: Union[float, ndarray]
) → Union[float, ndarray]
```

Helper function returning the helmert component of the functional relationship 



**Returns:**
 
 - <b>`np.ndarray`</b>:  helmert component 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
