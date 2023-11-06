from dataclasses import field, dataclass
from enum import Enum
from typing import Any
import unittest
from pathlib import Path

from trajectopy_core.settings.base import Settings


class SettingsEnum(Enum):
    SETTING_1 = 1
    SETTING_2 = 2
    SETTING_3 = 3


@dataclass
class DeeplyNestedSettings(Settings):
    setting_1: bool = True
    setting_2: float = 4.56
    setting_3: int = 23
    setting_4: str = "Some Text"
    setting_5: SettingsEnum = SettingsEnum.SETTING_1

    @staticmethod
    def encoder(name: str, value: Any) -> Any:
        if name == "setting_5":
            return value.value
        return value

    @staticmethod
    def decoder(name: str, value: Any) -> Any:
        if name == "setting_5":
            return SettingsEnum(value)
        return value


@dataclass
class NestedSettings(Settings):
    setting_1: bool = False
    setting_2: float = 1.23
    setting_3: int = 42
    setting_4: str = "Hello World"
    setting_5: DeeplyNestedSettings = field(default_factory=DeeplyNestedSettings)


@dataclass
class AllSettings(Settings):
    nested_settings: NestedSettings = field(default_factory=NestedSettings)
    setting_1: bool = True
    setting_2: float = 4.56
    setting_3: DeeplyNestedSettings = field(default_factory=DeeplyNestedSettings)
    setting_4: str = "Some Text"
    setting_5: SettingsEnum = SettingsEnum.SETTING_1

    @staticmethod
    def encoder(name: str, value: Any) -> Any:
        if name == "setting_5":
            return value.value
        return value

    @staticmethod
    def decoder(name: str, value: Any) -> Any:
        if name == "setting_5":
            return SettingsEnum(value)
        return value


class TestSettings(unittest.TestCase):
    _file = 0

    def setUp(self) -> None:
        super().setUp()
        Path("./test/tmp").mkdir(parents=True, exist_ok=True)

    def settings_io(self) -> None:
        settings = AllSettings()
        settings.to_file("./test/tmp/test.json")
        imported_settings = AllSettings.from_file("./test/tmp/test.json")

        assert settings == imported_settings


if __name__ == "__main__":
    TestSettings().setUp()
    TestSettings().settings_io()
