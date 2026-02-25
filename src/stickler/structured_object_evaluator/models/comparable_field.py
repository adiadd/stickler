"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.model_def.comparable_field instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.structured_object_evaluator.model_def.comparable_field instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..model_def.comparable_field import (
    ComparableField,
    _reconstruct_comparator_from_type,
    add_comparison_schema,
)

__all__ = [
    "ComparableField",
    "_reconstruct_comparator_from_type",
    "add_comparison_schema",
]
