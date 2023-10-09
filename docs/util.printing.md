<!-- markdownlint-disable -->

<a href="..\trajectopy_core\util\printing.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `util.printing`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="..\trajectopy_core\util\printing.py#L9"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `dict2table`

```python
dict2table(
    input_dict: dict,
    title: str,
    key_width: int = 16,
    value_width: int = 8,
    key_value_filler: str = ' : ',
    decimal_places: int = 3
) → str
```

 Converts a dictionary to a formatted table string. 



**Args:**
 
     - <b>`input`</b> (dict):  The dictionary to be converted to a table. 
     - <b>`title`</b> (str):  The title of the table. 
     - <b>`key_width`</b> (int, optional):  The width of the key column. Defaults to 16. 
     - <b>`value_width`</b> (int, optional):  The width of the value column. Defaults to 8. 
     - <b>`key_value_filler`</b> (str, optional):  The string used to separate the key and value columns. Defaults to " : ". 
     - <b>`decimal_places`</b> (int, optional):  The number of decimal places to display for float values. Defaults to 3. 



**Returns:**
 
     - <b>`str`</b>:  The formatted table string. 



**Example:**
 ``` my_dict = {"key1": 123.456, "key2": "value2"}```
        >>> dict2table(my_dict, "My Table")
        '
 ______________________
| ------ My Table ------ |
| key1            : 123.456 |  
| key2            : value2  |  
|________________________|
'
    



---

<a href="..\trajectopy_core\util\printing.py#L77"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `list2box`

```python
list2box(
    input_list: list,
    title: str = '',
    upper_boundary: bool = True,
    lower_boundary: bool = True,
    field_length: int = 0
) → str
```

 Converts a list to a formatted box string. 



**Args:**
 
     - <b>`input_list`</b> (list):  The list to be converted to a box. 
     - <b>`title`</b> (str, optional):  The title of the box. Defaults to "". 
     - <b>`upper_boundary`</b> (bool, optional):  Whether to include an upper boundary. Defaults to True. 
     - <b>`lower_boundary`</b> (bool, optional):  Whether to include a lower boundary. Defaults to True. 
     - <b>`field_length`</b> (int, optional):  The width of each field in the box. Default to 0 (auto). 



**Returns:**
 
     - <b>`str`</b>:  The formatted box string. 



**Example:**
 ``` my_list = ["item1", "item2", "item3"]```
        >>> list2box(my_list, "My Box")
        '┌─────────── My Box ───────────┐
│ item1                       │
│ item2                       │
│ item3                       │
└─────────────────────────────┘
'
    





---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
