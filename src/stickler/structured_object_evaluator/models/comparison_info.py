"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.core.field instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.structured_object_evaluator.core.field instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..core.field import (
    ComparableFieldConfig,
    ComparisonInfo,
    add_comparison_schema,
)

__all__ = ["ComparisonInfo", "ComparableFieldConfig", "add_comparison_schema"]
