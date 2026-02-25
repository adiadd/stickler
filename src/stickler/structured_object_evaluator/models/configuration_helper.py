"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.model_def.configuration instead."""

import warnings as _warnings
_warnings.warn(
    "Import from stickler.structured_object_evaluator.model_def.configuration instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..model_def.configuration import (
    ConfigurationHelper,
)

__all__ = ["ConfigurationHelper"]
