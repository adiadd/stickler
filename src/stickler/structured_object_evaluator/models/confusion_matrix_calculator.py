"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.metrics.confusion_matrix_calculator instead."""

from ..metrics.confusion_matrix_calculator import ConfusionMatrixCalculator

__all__ = ["ConfusionMatrixCalculator"]
