"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.evaluation.format_helper instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.evaluation.format_helper instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..evaluation.format_helper import EvaluatorFormatHelper

__all__ = ["EvaluatorFormatHelper"]
