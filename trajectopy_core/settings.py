from dataclasses import dataclass
import json


@dataclass
class GeneralSettings:
    option1: str
    option2: int


@dataclass
class ComputationSettings:
    param1: float
    param2: bool


@dataclass
class ExportSettings:
    format: str
    path: str


@dataclass
class ProjectConfig:
    general: GeneralSettings
    computation: ComputationSettings
    export: ExportSettings

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
