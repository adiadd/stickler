"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.core.non_match instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.structured_object_evaluator.core.non_match instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..core.non_match import NonMatchField, NonMatchType

__all__ = ["NonMatchField", "NonMatchType"]
