"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.metrics.confidence instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.metrics.confidence instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..metrics.confidence import ConfidenceCalculator

__all__ = ["ConfidenceCalculator"]
