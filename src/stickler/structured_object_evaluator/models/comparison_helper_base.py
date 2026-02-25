"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.comparison.helpers_base instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.structured_object_evaluator.comparison.helpers_base instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..comparison.helpers_base import (
    DEFAULT_MATCH_THRESHOLD,
    ComparisonHelperBase,
)

__all__ = ["ComparisonHelperBase", "DEFAULT_MATCH_THRESHOLD"]
