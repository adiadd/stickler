"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.evaluation.non_match_collector instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.evaluation.non_match_collector instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..evaluation.non_match_collector import NonMatchCollector

__all__ = ["NonMatchCollector"]
