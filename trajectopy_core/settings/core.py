"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
import copy
import logging
import os
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Callable, Dict, Union

import yaml

from trajectopy_core.util.printing import dict2table

# logger configuration
logger = logging.getLogger("root")


def yaml2dict(file: str) -> Dict:
    with open(os.path.abspath(file), encoding="utf-8") as f:
        return yaml.safe_load(f)


@dataclass
class _PrintableClass(ABC):
    def __str__(self) -> str:
        return dict2table(self.__dict__, title=self.__class__.__name__)

    def __repr__(self) -> str:
        return self.__str__()


@dataclass
class Settings(_PrintableClass, ABC):
    """Abstract class defining the interface for all settings classes"""

    @classmethod
    @abstractmethod
    def from_config_dict(cls, config_dict: Dict) -> "Settings":
        pass

    def to_dict(self) -> Dict[str, Any]:
        return self.__dict__

    def to_file(self, filename: str) -> None:
        with open(filename, "w", encoding="utf-8") as file:
            yaml.dump(self.to_dict(), file)

    @classmethod
    def from_file(cls, file: str) -> "Settings":
        return cls.from_config_dict(config_dict=yaml2dict(file))

    def copy(self) -> "Settings":
        return copy.deepcopy(self)


def field_extractor(
    config_class: Any,
    config_dict: dict,
    fill_missing_with: Dict[str, Any],
    field_handler: Union[None, Dict[str, Callable[[Any], Any]]] = None,
) -> Settings:
    """Populates the class variables using the config file dict

    This method will lookup the class variables of a given class in
    a dictionary holding the configuration for that class.

    If the key / variable name is not specified in the configuration
    dictionary, the class variable is set to the default value given
    in the 'fill_missing_with' dict. Inside this dict, it is also
    possible to define exceptional cases, where the value should be
    different from the default value.

    Args:
        config_class (Config): Config class to fill
        config_dict (dict): Dictionary holding values for some or all
                            of the class variables. The keys must be
                            identical to the class variable names.
        fill_missing_with (dict): Dictionary holding values that should
                                  be used whenever no distinct value was
                                  provided inside 'config_dict'.
                                  It must at least include a value for
                                  the 'default' key. Any additional keys
                                  must match the variable names of
                                  config_class.
        field_handler (dict): Dictionary holding functions that should
                                be applied to the values of the
                                'config_dict' before they are assigned
                                to the class variables. The keys must
                                match the variable names of config_class.

    Returns:
        Config: Class with variables set according to config_dict and
                fill_missing_with.
    """

    def default_handler(x):
        return x

    if field_handler is None:
        field_handler = {}

    for field in config_class.__dataclass_fields__:
        value = field_handler.get(field, default_handler)(
            config_dict.get(field, fill_missing_with.get(field, fill_missing_with["default"])),
        )
        setattr(config_class, field, value)
    return config_class
