<!-- markdownlint-disable -->

<a href="..\trajectopy_core\io\header.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `io.header`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 

**Global Variables**
---------------
- **GPS_WEEK_ZERO**
- **TIME_FORMAT_DICT**
- **HEADER_KEYS**
- **HANDLER_MAPPING**

---

<a href="..\trajectopy_core\io\header.py#L42"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `default_line_handler`

```python
default_line_handler(line: str) → str
```






---

<a href="..\trajectopy_core\io\header.py#L46"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `integer_line_handler`

```python
integer_line_handler(line: str) → int
```






---

<a href="..\trajectopy_core\io\header.py#L50"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `float_line_handler`

```python
float_line_handler(line: str) → float
```






---

<a href="..\trajectopy_core\io\header.py#L54"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `delimiter_line_handler`

```python
delimiter_line_handler(line: str) → str
```

This function extracts the delimiter from the file header. All characters between the first and the last quotation mark are returned. 


---

<a href="..\trajectopy_core\io\header.py#L73"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `HeaderData`
Class to store the header data of a trajectopy file. 

<a href="..\<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__(data: Dict[str, Union[str, int, float]]) → None
```






---

#### <kbd>property</kbd> comparison_method





---

#### <kbd>property</kbd> datetime_format





---

#### <kbd>property</kbd> datetime_timezone





---

#### <kbd>property</kbd> delimiter





---

#### <kbd>property</kbd> epsg





---

#### <kbd>property</kbd> fields





---

#### <kbd>property</kbd> gps_week





---

#### <kbd>property</kbd> id





---

#### <kbd>property</kbd> name





---

#### <kbd>property</kbd> nframe





---

#### <kbd>property</kbd> num_pairs





---

#### <kbd>property</kbd> relative_dist_unit





---

#### <kbd>property</kbd> rot_unit





---

#### <kbd>property</kbd> time_format





---

#### <kbd>property</kbd> time_offset





---

#### <kbd>property</kbd> type







---

<a href="..\trajectopy_core\io\header.py#L154"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(filename: str) → HeaderData
```

Reads the header of a trajectory file. 



**Args:**
 
 - <b>`filename`</b> (str):  The path to the file. 



**Returns:**
 
 - <b>`HeaderData`</b>:  The header data. 

---

<a href="..\trajectopy_core\io\header.py#L172"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_string`

```python
from_string(input_str: str) → HeaderData
```

Reads the header of an input string. 



**Args:**
 
 - <b>`input_str`</b> (str):  The header string. 



**Returns:**
 
 - <b>`HeaderData`</b>:  The header data. 

---

<a href="..\trajectopy_core\io\header.py#L143"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `handle_line`

```python
handle_line(metadata: Dict[str, Union[str, int, float]], line: str) → None
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
