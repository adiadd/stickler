"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.comparison.field_handler instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.comparison.field_handler instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..comparison.field_handler import FieldComparator

__all__ = ["FieldComparator"]
