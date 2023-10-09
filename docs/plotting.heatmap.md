<!-- markdownlint-disable -->

<a href="..\trajectopy_core\plotting\heatmap.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `plotting.heatmap`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\plotting\heatmap.py#L15"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `heatmap`

```python
heatmap(
    data,
    row_labels,
    col_labels,
    ax=None,
    cbar_kw=None,
    cbarlabel='',
    **kwargs
)
```

Create a heatmap from a numpy array and two lists of labels. 

Parameters 
---------- data  A 2D numpy array of shape (M, N). row_labels  A list or array of length M with the labels for the rows. col_labels  A list or array of length N with the labels for the columns. ax  A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If  not provided, use current axes or create a new one.  Optional. cbar_kw  A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional. cbarlabel  The label for the colorbar.  Optional. **kwargs  All other arguments are forwarded to `imshow`. 


---

<a href="..\trajectopy_core\plotting\heatmap.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `annotate_heatmap`

```python
annotate_heatmap(
    im,
    data=None,
    valfmt='{x:.2f}',
    textcolors=('black', 'white'),
    threshold=None,
    **textkw
)
```

A function to annotate a heatmap. 

Parameters 
---------- im  The AxesImage to be labeled. data  Data used to annotate.  If None, the image's data is used.  Optional. valfmt  The format of the annotations inside the heatmap.  This should either  use the string format method, e.g. "$ {x:.2f}", or be a  `matplotlib.ticker.Formatter`.  Optional. textcolors  A pair of colors.  The first is used for values below a threshold,  the second for those above.  Optional. threshold  Value in data units according to which the colors from textcolors are  applied.  If None (the default) uses the middle of the colormap as  separation.  Optional. **kwargs  All other arguments are forwarded to each call to `text` used to create  the text labels. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
