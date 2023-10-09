<!-- markdownlint-disable -->

<a href="..\trajectopy_core\io\result_io.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `io.result_io`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\io\result_io.py#L16"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `read_result_file`

```python
read_result_file(
    filename: str
) → Union[AbsoluteDeviationEntry, RelativeDeviationEntry, AlignmentEntry]
```

Reads a result file and returns an object of the appropriate type based on the file's header data. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the result file to read. 



**Returns:**
 
 - <b>`Union[AbsoluteDeviationEntry, RelativeDeviationEntry, AlignmentEntry]`</b>:  An object of the appropriate type based on the file's header data. 



**Raises:**
 
 - <b>`ValueError`</b>:  If the result file type is not supported. 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
