"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.metrics.confusion_matrix_calculator instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.structured_object_evaluator.metrics.confusion_matrix_calculator instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..metrics.confusion_matrix_calculator import ConfusionMatrixCalculator

__all__ = ["ConfusionMatrixCalculator"]
