"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.core.threshold_helper instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.core.threshold_helper instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..core.threshold_helper import ThresholdHelper

__all__ = ["ThresholdHelper"]
