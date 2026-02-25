"""Backward-compatibility shim. Import from stickler.structured_object_evaluator.model_def.json_schema_validator instead."""

import warnings as _warnings

_warnings.warn(
    "Import from stickler.structured_object_evaluator.model_def.json_schema_validator instead. This shim will be removed in v0.3.0.",
    DeprecationWarning,
    stacklevel=2,
)

from ..model_def.json_schema_validator import (
    validate_instance_against_schema,
    validate_json_schema,
)

__all__ = ["validate_json_schema", "validate_instance_against_schema"]
