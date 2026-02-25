"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.evaluation.field_comparison_helper instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.evaluation.field_comparison_helper instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..evaluation.field_comparison_helper import FieldComparisonHelper

__all__ = ["FieldComparisonHelper"]
