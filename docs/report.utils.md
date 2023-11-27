<!-- markdownlint-disable -->

<a href="..\trajectopy_core\report\utils.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `report.utils`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **BASE_PATH**
- **TEMPLATES_PATH**

---

<a href="..\trajectopy_core\report\utils.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `number_to_string`

```python
number_to_string(number: float) → str
```






---

<a href="..\trajectopy_core\report\utils.py#L26"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `image_to_base64`

```python
image_to_base64(image_path: str) → str
```






---

<a href="..\trajectopy_core\report\utils.py#L32"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `convert_images_to_base64`

```python
convert_images_to_base64() → Tuple[str, str, str]
```






---

<a href="..\trajectopy_core\report\utils.py#L44"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `shrink_data`

```python
shrink_data(data: ndarray, max_size: int = 1000) → ndarray
```

Shrink the given data to the given max_size by taking the moving average of the data. 



**Args:**
 
 - <b>`data`</b> (np.ndarray):  The data to shrink 
 - <b>`max_size`</b> (int):  The maximum size of the data 



**Returns:**
 
 - <b>`np.ndarray`</b>:  The shrunk data 


---

<a href="..\trajectopy_core\report\utils.py#L74"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `write_report`

```python
write_report(output_file: str, report_text: str) → None
```

Writes a report to the given output file. 



**Args:**
 


 - <b>`output_file`</b> (str):  The output file path 


---

<a href="..\trajectopy_core\report\utils.py#L88"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `show_report`

```python
show_report(report_text: str) → None
```

Shows a report in the browser. 



**Args:**
 


 - <b>`report_text`</b> (str):  The report string 




---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
