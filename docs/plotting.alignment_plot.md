<!-- markdownlint-disable -->

<a href="../trajectopy_core/plotting/alignment_plot.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `plotting.alignment_plot`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="../trajectopy_core/plotting/alignment_plot.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_correlation_heatmap`

```python
plot_correlation_heatmap(
    estimated_parameters: AlignmentParameters,
    enabled_only: bool = True
) → Figure
```

Plots the correlation heatmap of a covariance matrix. 



**Args:**
 
 - <b>`covariance`</b> (np.ndarray):  Covariance matrix. 



**Returns:**
 
 - <b>`plt.Figure`</b>:  Correlation heatmap figure. 


---

<a href="../trajectopy_core/plotting/alignment_plot.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `plot_covariance_heatmap`

```python
plot_covariance_heatmap(
    estimated_parameters: AlignmentParameters,
    enabled_only: bool = True
) → Figure
```

Plots the covariance heatmap of a covariance matrix. 



**Args:**
 
 - <b>`covariance`</b> (np.ndarray):  Covariance matrix. 



**Returns:**
 
 - <b>`plt.Figure`</b>:  Covariance heatmap figure. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
