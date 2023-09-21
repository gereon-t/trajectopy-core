"""
Trajectopy - Trajectory Evaluation in Python

Gereon Tombrink, 2023
mail@gtombrink.de
"""
from dataclasses import dataclass, field

import numpy as np

from trajectopy_core.alignment.parameters import AlignmentParameters, SensorRotationParameters
from trajectopy_core.settings.alignment_settings import AlignmentEstimationSettings


@dataclass
class AlignmentResult:
    name: str = "Alignment Result"
    position_parameters: AlignmentParameters = field(default_factory=AlignmentParameters)
    rotation_parameters: SensorRotationParameters = field(default_factory=SensorRotationParameters)
    estimation_of: AlignmentEstimationSettings = field(default_factory=AlignmentEstimationSettings)

    def __eq__(self, other) -> bool:
        if not isinstance(other, AlignmentResult):
            return False

        assert np.allclose(self.position_parameters.values, other.position_parameters.values)
        assert np.allclose(
            self.position_parameters.covariance_matrix,
            other.position_parameters.covariance_matrix,
        )
        assert np.allclose(self.rotation_parameters.values, other.rotation_parameters.values)
        assert self.estimation_of == other.estimation_of

        return True
