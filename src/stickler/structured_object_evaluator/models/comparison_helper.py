"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.comparison.helpers instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.comparison.helpers instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..comparison.helpers import ComparisonHelper

__all__ = ["ComparisonHelper"]
