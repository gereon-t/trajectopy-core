<!-- markdownlint-disable -->

<a href="../trajectopy_core/settings/core.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `settings.core`
Trajectopy - Trajectory Evaluation in Python 

Gereon Tombrink, 2023 mail@gtombrink.de 


---

<a href="../trajectopy_core/settings/core.py#L22"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `yaml2dict`

```python
yaml2dict(file: str) → Dict
```






---

<a href="../trajectopy_core/settings/core.py#L60"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `field_extractor`

```python
field_extractor(
    config_class: Any,
    config_dict: dict,
    fill_missing_with: Dict[str, Any],
    field_handler: Optional[Dict[str, Callable[[Any], Any]]] = None
) → Settings
```

Populates the class variables using the config file dict 

This method will lookup the class variables of a given class in a dictionary holding the configuration for that class. 

If the key / variable name is not specified in the configuration dictionary, the class variable is set to the default value given in the 'fill_missing_with' dict. Inside this dict, it is also possible to define exceptional cases, where the value should be different from the default value. 



**Args:**
 
 - <b>`config_class`</b> (Config):  Config class to fill 
 - <b>`config_dict`</b> (dict):  Dictionary holding values for some or all  of the class variables. The keys must be  identical to the class variable names. 
 - <b>`fill_missing_with`</b> (dict):  Dictionary holding values that should  be used whenever no distinct value was  provided inside 'config_dict'.  It must at least include a value for  the 'default' key. Any additional keys  must match the variable names of  config_class. 
 - <b>`field_handler`</b> (dict):  Dictionary holding functions that should  be applied to the values of the  'config_dict' before they are assigned  to the class variables. The keys must  match the variable names of config_class. 



**Returns:**
 
 - <b>`Config`</b>:  Class with variables set according to config_dict and  fill_missing_with. 


---

<a href="../trajectopy_core/settings/core.py#L36"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>class</kbd> `Settings`
Abstract class defining the interface for all settings classes 

<a href="../<string>"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `__init__`

```python
__init__() → None
```








---

<a href="../trajectopy_core/settings/core.py#L56"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `copy`

```python
copy() → Settings
```





---

<a href="../trajectopy_core/settings/core.py#L40"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_config_dict`

```python
from_config_dict(config_dict: Dict) → Settings
```





---

<a href="../trajectopy_core/settings/core.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>classmethod</kbd> `from_file`

```python
from_file(file: str) → Settings
```





---

<a href="../trajectopy_core/settings/core.py#L45"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_dict`

```python
to_dict() → Dict[str, Any]
```





---

<a href="../trajectopy_core/settings/core.py#L48"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

### <kbd>method</kbd> `to_file`

```python
to_file(filename: str) → None
```








---

_This file was automatically generated via [lazydocs](https://github.com/ml-tooling/lazydocs)._
