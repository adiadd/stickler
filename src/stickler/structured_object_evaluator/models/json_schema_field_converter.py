"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.model_def.json_schema_converter instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.structured_object_evaluator.model_def.json_schema_converter instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..model_def.json_schema_converter import (
    JsonSchemaFieldConverter,
)

__all__ = ["JsonSchemaFieldConverter"]
