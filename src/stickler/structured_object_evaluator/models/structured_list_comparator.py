"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.comparison.structured_list_handler instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.structured_object_evaluator.comparison.structured_list_handler instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..comparison.structured_list_handler import StructuredListComparator

__all__ = ["StructuredListComparator"]
