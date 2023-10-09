<!-- markdownlint-disable -->

<a href="..\trajectopy_core\alignment\ghm_estimation.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `alignment.ghm_estimation`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\alignment\ghm_estimation.py#L828"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `print_summary`

```python
print_summary(alignment: Alignment) → None
```






---

<a href="..\trajectopy_core\alignment\ghm_estimation.py#L833"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `settings_str`

```python
settings_str(alignment: Alignment) → str
```






---

<a href="..\trajectopy_core\alignment\ghm_estimation.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Alignment`
Class representing the alignment of two trajectories 

This class will align two trajectories using a combination of a 3d Helmert-transformation, a leverarm estimation and a time-shift estimation. 

It can fully align two trajectories their separation can be described by: 
- a translational shift 
- a rotation of the positions 
- a rotation of the orientations (rotation of the n-frame) 
- a scale factor 
- a time shift 
- a leverarm (e.g. mounted at different locations on the platform) 

<a href="..\trajectopy_core\alignment\ghm_estimation.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(alignment_data: AlignmentData) → None
```

Constructor 

This method prepares the data and performs an trajectory alignment 



**Args:**
 
 - <b>`alignment_data`</b> (AlignmentData):  Stores all data required for the alignment 
 - <b>`mode`</b> (AlignmentMode, optional):  Indicates the desired mode, i.e. whether a 
                                    - helmert transformation 
                                    - scale estimation 
                                    - leverarm estimation 
                                    - time shift estimation  should be performed 
 - <b>`error_probability`</b> (float, optional):  Used for the stochastic global test.  Defaults to 0.05. 


---

#### <kbd>property</kbd> est_params





---

#### <kbd>property</kbd> has_results





---

#### <kbd>property</kbd> redundancy





---

#### <kbd>property</kbd> settings





---

#### <kbd>property</kbd> variance_factor







---

<a href="..\trajectopy_core\alignment\ghm_estimation.py#L368"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `auto_design_matrix`

```python
auto_design_matrix() → csc_matrix
```





---

<a href="..\trajectopy_core\alignment\ghm_estimation.py#L79"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `estimate`

```python
estimate() → AlignmentParameters
```

Handles the estimation of the parameters 

Calls either robust reweighting or variance estimation methods. 

---

<a href="..\trajectopy_core\alignment\ghm_estimation.py#L115"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `init_parameters`

```python
init_parameters() → AlignmentParameters
```

This method computes initial parameters for the iterative adjustment 

For this, the helmert transformation and the leverarm estimation are done separatetly using methods that do not require inital parameters. 



**Returns:**
 
 - <b>`AlignmentParameters`</b>:  Hold the estimates parameters.  14 = 7 (helmert+scale) 3 (leverarm) 1 (time) 3 (orientation) 

---

<a href="..\trajectopy_core\alignment\ghm_estimation.py#L204"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `variance_component_estimation`

```python
variance_component_estimation() → Dict[str, bool]
```

Performs an estimation of the variances for different observation groups 

The observations groups are: 
    - x and y components of xyz_from 
    - z component of xyz_from 
    - x and y components of xyz_to 
    - z component of xyz_to 
    - roll / pitch components of rpy_body 
    - yaw component of rpy_body 
    - speed (at target positions) 

---

<a href="..\trajectopy_core\alignment\ghm_estimation.py#L264"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `variance_estimation`

```python
variance_estimation(at_least_once: bool = False) → None
```

Tests the consistency of the functional and stochastic model and adjusts the variance vector if necessary. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
