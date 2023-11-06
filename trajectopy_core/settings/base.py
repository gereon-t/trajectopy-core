from abc import ABC
from dataclasses import dataclass
import json
from typing import Any


@dataclass
class Settings(ABC):
    """Base Class for Settings"""

    @staticmethod
    def encoder(obj):
        """Encoder for json serialization of dataclasses"""
        return obj.__dict__

    @staticmethod
    def decoder(name: str, value: Any) -> Any:
        """Decoder for json deserialization of dataclasses"""
        return value

    def to_json(self):
        return json.dumps(self, default=self.encoder, indent=4)

    def to_file(self, path: str):
        with open(path, "w", encoding="utf-8") as f:
            f.write(self.to_json())

    @classmethod
    def from_file(cls, path: str) -> "Settings":
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        settings = cls()
        for attribute_name, attribute_type in cls.__annotations__.items():
            if attribute_name not in data:
                raise ValueError(f"Attribute {attribute_name} not found in {path}")

            attribute_data = data[attribute_name]
            if isinstance(attribute_data, dict) and issubclass(attribute_type, Settings):
                setattr(settings, attribute_name, attribute_type(**attribute_data))
            else:
                setattr(settings, attribute_name, settings.decoder(attribute_name, attribute_data))

        return settings
