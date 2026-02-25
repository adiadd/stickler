"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.metrics.confusion_matrix_builder instead."""

from ..metrics.confusion_matrix_builder import ConfusionMatrixBuilder

__all__ = ["ConfusionMatrixBuilder"]
