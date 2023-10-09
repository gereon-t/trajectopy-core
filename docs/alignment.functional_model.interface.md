<!-- markdownlint-disable -->

<a href="..\trajectopy_core\alignment\functional_model\interface.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `alignment.functional_model.interface`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 



---

<a href="..\trajectopy_core\alignment\functional_model\interface.py#L21"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `FunctionalRelationship`
Class for the functional relationship between the observations and the parameters. 

<a href="..\trajectopy_core\alignment\functional_model\interface.py#L24"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__() → None
```








---

<a href="..\trajectopy_core\alignment\functional_model\interface.py#L91"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `eval`

```python
eval(
    func: Callable,
    observations: AlignmentData,
    parameters: AlignmentParameters
)
```

Evaluates the functional relationship for the given observations and parameters. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
