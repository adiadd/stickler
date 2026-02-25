"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.evaluation.bulk instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.structured_object_evaluator.evaluation.bulk instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from .evaluation.bulk import BulkStructuredModelEvaluator, aggregate_from_comparisons

__all__ = ["BulkStructuredModelEvaluator", "aggregate_from_comparisons"]
