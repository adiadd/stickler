"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.comparison.dispatcher instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.comparison.dispatcher instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..comparison.dispatcher import ComparisonDispatcher

__all__ = ["ComparisonDispatcher"]
