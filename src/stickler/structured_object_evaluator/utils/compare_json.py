"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.evaluation.single instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.evaluation.single instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..evaluation.single import compare_json

__all__ = ["compare_json"]
