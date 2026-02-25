"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.metrics.derived instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.metrics.derived instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..metrics.derived import DerivedMetricsCalculator

__all__ = ["DerivedMetricsCalculator"]
